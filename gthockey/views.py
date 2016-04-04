from django.shortcuts import render, render_to_response

from django.template import RequestContext, loader
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core.mail import send_mail

from .models import Game, Player, Email, NewsStory
from .forms import ProspectForm, ContactForm


def index(request):
    stories = NewsStory.objects.order_by("-date")[:3]
    return render(request, 'index.html', {'stories': stories})


def schedule(request):
    games = Game.objects.order_by('date')
    return render(request, 'schedule.html', {'games': games})


def roster(request):
    players = Player.objects.order_by('number')
    return render(request, 'roster.html', {'players': players})


def board(request):
    return render(request, 'board.html')


def coaches(request):
    return render(request, 'coaches.html')


def prospect(request):
    success = False
    if request.method == 'POST':
        form = ProspectForm(request.POST)
        if form.is_valid():
            subject = form.get_subject()
            sender = "GT Hockey"
            message = form.get_message()
            recipients = [e.email for e in Email.objects.all()]

            send_mail(subject, message, sender, recipients)
            success = True
            form = ProspectForm()
    else:
        form = ProspectForm()

    return render(request, 'prospect.html', {"form": form, "success": success})


def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.get_subject()
            sender = "GT Hockey"
            print(sender)
            message = form.get_message()
            recipients = [e.email for e in Email.objects.all()]

            send_mail(subject, message, sender, recipients)
            success = True
            form = ContactForm()
    else:
        form = ContactForm()

    return render(request, 'contact.html', {"form": form, "success": success})


def news(request, id):
    story = NewsStory.objects.get(id=id)
    return render(request, 'news.html', {'story': story})


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response