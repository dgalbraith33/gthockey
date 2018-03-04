from django.http import JsonResponse

from datetime import date

from .models import Game, Season, Player
from .serializers import PlayerSerializer

def nextgame(request):
    games = Game.objects.order_by('date').filter(date__gte=date.today())

    resp = {
        "exists": False
    }

    if len(games) > 0:
        game = games[0]
        resp = {
            "exists": True,
            "date": game.date,
            "time": game.time,
            "team": game.opponent.school_name,
            "location": game.location.rink_name,
            "logo": "",
        }

        if len(game.opponent.logo.name) is not 0:
            resp["logo"] = game.opponent.logo.url

    return JsonResponse(resp)

def seasonRecord(request):
    currentSeason = Season.get_current()
    games = Game.objects.filter(season=currentSeason)

    wins = 0
    losses = 0
    otl = 0
    ties = 0
    unknown = 0

    for game in games:
        if game.date < date.today() and game.score_gt_final and game.score_opp_final:
            if game.score_gt_final > game.score_opp_final:
                wins += 1
            elif game.score_gt_ot and game.score_opp_ot and game.score_opp_ot > 0:
                otl += 1
            elif game.score_gt_final < game.score_opp_final:
                losses += 1
            elif game.score_gt_final == game.score_opp_final:
                ties += 1
            else: 
                unknown += 1

    return JsonResponse({
            "season": str(currentSeason),
            "wins": wins,
            "losses": losses,
            "otl": otl,
            "ties": ties,
            "unknown": unknown
        })


# Django Rest Framework

def player_list(request):
    players = Player.objects.order_by('number')
    serializer = PlayerSerializer(players, many=True)
    return JsonResponse(serializer.data, safe=False)
