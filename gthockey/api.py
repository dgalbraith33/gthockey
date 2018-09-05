from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView

from .forms import ContactForm, ProspectForm, EmailListForm, OrderForm
from .models import Game, Season, Player, NewsStory, Board, Coach, Email, ShopItem
from .serializers import PlayerSerializer, GameSerializer, GameMinSerializer, ArticleSerializer, \
    BoardSerializer, CoachSerializer, ShopItemListSerializer, ShopItemSerializer, SeasonSerializer


class PlayerList(APIView):
    def get(self, request):
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


class CurrentSeason(APIView):
    def get(self, request):
        season = Season.get_current()
        serializer = SeasonSerializer(season)
        return JsonResponse(serializer.data, safe=False)


class ArticleList(APIView):
    def get(self, request):
        articles = NewsStory.objects.order_by('-date')
        serializer = ArticleSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)


class ArticleDetail(APIView):
    def get(self, request, id):
        article = NewsStory.objects.get(pk=id)
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data, safe=False)


class BoardList(APIView):
    def get(self, request):
        board = Board.objects.all().order_by('priority')
        serializer = BoardSerializer(board, many=True)
        return JsonResponse(serializer.data, safe=False)


class CoachList(APIView):
    def get(self, request):
        coaches = Coach.objects.all().order_by('priority')
        serializer = CoachSerializer(coaches, many=True)
        return JsonResponse(serializer.data, safe=False)


class ShopList(APIView):
    def get(self, request):
        items = ShopItem.objects.all().filter(visible=True)
        serializer = ShopItemListSerializer(items, many=True)
        return JsonResponse(serializer.data, safe=False)


class ShopDetail(APIView):
    def get(self, request, id):
        try:
            item = ShopItem.objects.get(pk=id, visible=True)
            serializer = ShopItemSerializer(item)
            return JsonResponse(serializer.data, safe=False)
        except ObjectDoesNotExist:
            return JsonResponse({"errors": "Object Does Not Exist"}, status=404)


class ContactFormView(APIView):
    @csrf_exempt
    def post(self, request):
        form = ContactForm(request.data)
        if form.is_valid():
            subject = form.get_subject()
            sender = "GT Hockey"
            message = form.get_message()
            recipients = [e.email for e in Email.objects.all() if e.active]
            send_mail(subject, message, sender, recipients)
            return JsonResponse({}, status=200)
        return JsonResponse({"errors": form.errors}, status=400)

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(ContactFormView, self).dispatch(*args, **kwargs)


class ProspectFormView(APIView):
    @csrf_exempt
    def post(self, request):
        form = ProspectForm(request.data)
        if form.is_valid():
            subject = form.get_subject()
            sender = "GT Hockey"
            message = form.get_message()
            recipients = [e.email for e in Email.objects.all() if e.active]
            send_mail(subject, message, sender, recipients)
            return JsonResponse({}, status=200)
        return JsonResponse({"errors": form.errors}, status=400)

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(ProspectFormView, self).dispatch(*args, **kwargs)


class InvolvementFormView(APIView):
    @csrf_exempt
    def post(self, request):
        form = EmailListForm(request.data)
        if form.is_valid():
            subject = form.get_subject()
            sender = "GT Hockey"
            message = form.get_message()
            recipients = [e.email for e in Email.objects.all()]
            send_mail(subject, message, sender, recipients)
            return JsonResponse({}, status=200)
        return JsonResponse({"errors": form.errors}, status=400)

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(InvolvementFormView, self).dispatch(*args, **kwargs)


class OrderFormView(APIView):
    @csrf_exempt
    def post(self, request):
        form = OrderForm(request.data)
        if form.is_valid():
            subject = form.get_subject()
            sender = "GT Hockey"
            message = form.get_message()
            recipients = [e.email for e in Email.objects.all()]
            send_mail(subject, message, sender, recipients)

            # Customer Email
            subject = form.get_customer_subject()
            sender = "GT Hockey"
            message = form.get_customer_message()
            recipients = [form.cleaned_data['email']]
            send_mail(subject, message, sender, recipients)
            return JsonResponse({}, status=200)
        return JsonResponse({"errors": form.errors}, status=400)

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(OrderFormView, self).dispatch(*args, **kwargs)


def handler404(request, exception):
    return JsonResponse({'message': 'API method does not exist'}, status=404)
