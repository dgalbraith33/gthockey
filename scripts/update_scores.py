from bs4 import BeautifulSoup
import requests
from datetime import datetime as dt

URL_BASE = "http://achahockey.org/stats/schedule/team/508789"
SEASON_ID = "16169"
YEAR = 2016

GT_NAME = 'M3 Georgia Institute of Technology'


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
    if row['home'] == GT_NAME:
        cd['score_gt'] = row['home_score']
        cd['opp'] = row['away'][3:]
        cd['score_opp'] = row['away_score']
    else:
        cd['score_gt'] = row['away_score']
        cd['opp'] = row['home'][3:]
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
    row['away'] = strip(tds[1].a.string)
    row['away_score'] = strip(tds[2].string)
    row['home'] = strip(tds[3].a.string)
    row['home_score'] = strip(tds[4].string)
    row['date'] = strip(tds[6].string)
    return clean_dict(row, year)


def build_result_table(page_bs, year):
    return [parse_row_dict(tr, year) for tr in page_bs.find('tbody').find_all('tr')]


def main():
    resp = get_stats_page(SEASON_ID)
    soup = BeautifulSoup(resp.text, 'html.parser')
    result_table = build_result_table(soup, YEAR)
    for result in result_table:
        print(result)


if __name__ == "__main__":
    main()