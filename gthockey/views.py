from django.shortcuts import render

from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core.mail import send_mail

from .models import Game, Player, Email
from .forms import ProspectForm, ContactForm


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


def board(request):
    return HttpResponseNotFound("Board")


def coaches(request):
    return HttpResponseNotFound("Coaches")


def prospect(request):
    if request.method == 'POST':
        form = ProspectForm(request.POST)
        if form.is_valid():
            subject = form.get_subject()
            sender = "GT Hockey"
            message = form.get_message()
            recipients = [e.email for e in Email.objects.all()]

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/') # TODO create landing page
    else:
        form = ProspectForm()

    return render(request, 'prospect.html', {"form": form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.get_subject()
            sender = "GT Hockey"
            print(sender)
            message = form.get_message()
            recipients = [e.email for e in Email.objects.all()]

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/') # TODO create landing page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {"form": form})
