from django.shortcuts import render

from django.template import RequestContext, loader
from django.http import HttpResponse

from .models import Game


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

