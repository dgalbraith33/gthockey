from bs4 import BeautifulSoup
from datetime import datetime as dt
from django.core.management.base import BaseCommand
import requests

from gthockey.models import Game, Season

URL_BASE = "http://achahockey.org/stats/schedule/team/508789"
GT_NAME = 'Georgia Institute of Tech'


def strip(str_or_none):
    if str_or_none:
        return str_or_none.strip()
    return None


def get_stats_page(season_id):
    url_params = "?seasonid={season}"
    url = URL_BASE + url_params.format(season=season_id)
    resp = requests.get(url)
    assert resp.status_code == 200
    return resp


def clean_dict(row, year):
    cd = {}
    if GT_NAME in row['home']:
        cd['score_gt'] = row['home_score']
        cd['opp'] = row['away']
        cd['score_opp'] = row['away_score']
    else:
        cd['score_gt'] = row['away_score']
        cd['opp'] = row['home']
        cd['score_opp'] = row['home_score']
    datestr = row['date'][5:]

    if datestr[:3] in ['Aug', 'Sep', 'Oct', 'Nov', 'Dec']:
        datestr += " " + str(year)
    else:
        datestr += " " + str(year + 1)

    cd['date'] = dt.strptime(datestr, '%b %d %Y').date()
    return cd


def parse_row_dict(tr, year):
    row = {}
    tds = tr.find_all('td')
    if tds[8].string.strip() != "FINAL":
        return None
    row['away'] = strip(tds[1].a.string)
    row['away_score'] = strip(tds[2].string)
    row['home'] = strip(tds[3].a.string)
    row['home_score'] = strip(tds[4].string)
    row['date'] = strip(tds[6].string)
    return clean_dict(row, year)


def build_result_table(page_bs, year):
    results = [parse_row_dict(tr, year) for tr in page_bs.find('tbody').find_all('tr')]
    return filter(lambda d: d is not None, results)


def get_games_from_season(season):
    return Game.objects.filter(season=season)


def equal(game, result):
    return (game.score_opp_final == int(result['score_opp']) and
            game.score_gt_final == int(result['score_gt']))


class Command(BaseCommand):
    help = 'Pulls results from acha website'

    def _match_result_to_game(self, result, games, dry_run, overwrite):
        matched = games.filter(date=result['date'])
        if matched and len(matched) > 0:
            game = matched[0]
            message = ("Matched: " + str(result['date']) + " : " + result['opp'] + "==" +
                       str(game.opponent))
            self.stdout.write(self.style.SUCCESS(message))

            if not equal(game, result):
                if game.is_reported and not overwrite:
                    warn = "DB(gt={db_gt}, opp={db_opp}) ACHA(gt={gt}, opp={opp})"
                    warn = warn.format(db_gt=game.score_gt_final, db_opp=game.score_opp_final,
                                       gt=result['score_gt'], opp=result['score_opp'])
                    self.stdout.write(self.style.WARNING(warn))
                else:
                    if not dry_run:
                        game.score_opp_final = int(result['score_opp'])
                        game.score_gt_final = int(result['score_gt'])
                        game.save()

                    success = "----Updated(gt={gt}, opp={opp})".format(gt=result['score_gt'],
                                                                       opp=result['score_opp'])
                    self.stdout.write(self.style.SUCCESS(success))
        else:
            self.stderr.write("Couldn't Match " + str(result['date']) + " : " + result['opp'])

    def add_arguments(self, parser):
        parser.add_argument("--acha_season", type=int, required=True)
        parser.add_argument("--db_season", type=int, required=True)
        parser.add_argument("--dry_run", dest='dry_run', action='store_true', default=False)
        parser.add_argument("--overwrite", dest='overwrite', action='store_true', default=False)

    def handle(self, *args, **options):
        season = Season.objects.get(pk=options['db_season'])
        resp = get_stats_page(options['acha_season'])
        soup = BeautifulSoup(resp.text, 'html.parser')
        result_table = build_result_table(soup, season.year)
        games = get_games_from_season(season)
        for result in result_table:
            self._match_result_to_game(result, games, options['dry_run'], options['overwrite'])
