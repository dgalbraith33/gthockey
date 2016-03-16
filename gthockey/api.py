from django.http import JsonResponse

from datetime import date

from .models import Game

def nextgame(request):
    games = Game.objects.order_by('date')
    ind = 0
    d = date.today()
    while ind < len(games) and games[ind].date < d:
        ind += 1

    game = games[ind]
    resp = {
        "date": game.date,
        "time": game.time,
        "team": game.opponent.school_name,
        "location": game.location.rink_name,
        "logo": game.opponent.logo.url
    }
    return JsonResponse(resp)
