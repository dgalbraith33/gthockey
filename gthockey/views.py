from django.shortcuts import render

from django.template import RequestContext, loader
from django.http import HttpResponse

from .models import Game, Player


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def schedule(request):
    games = Game.objects.order_by('date')
    template = loader.get_template("schedule.html")
    context = RequestContext(request, {
        'games': games,
    })
    return HttpResponse(template.render(context))

def roster(request):
    players = Player.objects.order_by('number')
    template = loader.get_template("roster.html")
    context = RequestContext(request, {
        "players": players,
    })
    return HttpResponse(template.render(context))