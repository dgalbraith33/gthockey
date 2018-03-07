from django.http import JsonResponse
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from datetime import date
from rest_framework.views import APIView

from .forms import ContactForm, ProspectForm, EmailListForm
from .models import Game, Season, Player, NewsStory, Board, Coach, Email
from .serializers import PlayerSerializer, GameSerializer, GameMinSerializer, ArticleSerializer, BoardSerializer, \
    CoachSerializer


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


class GameList(APIView):
    def get(self, request):
        params = request.query_params
        season = Season.get_current()

        min_date_str = params.get('date_from', '2000-01-01')
        max_date_str = params.get('date_to', '2099-01-01')

        limit = int(params.get('limit', 1000))

        descending = 'desc' in params
        order = '-date' if descending else 'date'

        games = Game.objects.order_by(order) \
            .filter(season=season) \
            .filter(date__gte=min_date_str) \
            .filter(date__lte=max_date_str) \
            .prefetch_related('location') \
            .prefetch_related('opponent')[:limit]

        serializer = GameMinSerializer(games, many=True)
        return JsonResponse(serializer.data, safe=False)


class GameDetail(APIView):
    def get(self, request, id):
        game = Game.objects.get(pk=id)
        serializer = GameSerializer(game)
        return JsonResponse(serializer.data, safe=False)


def article_list(request):
    articles = NewsStory.objects.order_by('-date')[:5]
    serializer = ArticleSerializer(articles, many=True)
    return JsonResponse(serializer.data, safe=False)

def article_get(request, id):
    article = NewsStory.objects.get(pk=id)
    serializer = ArticleSerializer(article)
    return JsonResponse(serializer.data, safe=False)


def board_list(request):
    board = Board.objects.all().order_by('priority')
    serializer = BoardSerializer(board, many=True)
    return JsonResponse(serializer.data, safe=False)


def coach_list(request):
    coaches = Coach.objects.all().order_by('priority')
    serializer = CoachSerializer(coaches, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def submit_contact(request):
    success = False
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.get_subject()
            sender = "GT Hockey"
            message = form.get_message()
            recipients = [e.email for e in Email.objects.all() if e.active]

            send_mail(subject, message, sender, recipients)
            success = True

    return JsonResponse({"success": success, "errors": form.errors})


@csrf_exempt
def submit_prospect(request):
    success = False
    form = ProspectForm
    if request.method == 'POST':
        form = ProspectForm(request.POST)
        if form.is_valid():
            subject = form.get_subject()
            sender = "GT Hockey"
            message = form.get_message()
            recipients = [e.email for e in Email.objects.all() if e.active]

            send_mail(subject, message, sender, recipients)
            success = True
            form = ProspectForm()

    return JsonResponse({"success": success, "errors": form.errors})

@csrf_exempt
def submit_involvement(request):
    success = False
    form = EmailListForm()
    if request.method == 'POST':
        form = EmailListForm(request.POST)
        if form.is_valid():
            subject = form.get_subject()
            sender = "GT Hockey"
            message = form.get_message()
            recipients = [e.email for e in Email.objects.all()]

            send_mail(subject, message, sender, recipients)
            success = True
            form = EmailListForm()

    return JsonResponse({"success": success, "errors": form.errors})