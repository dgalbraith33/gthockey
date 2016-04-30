from django.http import JsonResponse

from datetime import date

from .models import Game

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
            "logo": "//placehold.it/80x80"
        }

        if game.opponent.logo is not None:
            resp["logo"] = game.opponent.logo.url

    return JsonResponse(resp)
