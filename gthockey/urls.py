from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from . import api

urlpatterns = [
    path('api/players/', api.PlayerList.as_view()),
    path('api/games/', api.GameList.as_view()),
    path('api/games/<int:id>/', api.GameDetail.as_view()),
    path('api/seasons/current/', api.CurrentSeason.as_view()),
    path('api/articles/', api.ArticleList.as_view()),
    path('api/articles/<int:id>/', api.ArticleDetail.as_view()),
    path('api/board/', api.BoardList.as_view()),
    path('api/coaches/', api.CoachList.as_view()),
    path('api/shop/', api.ShopList.as_view()),
    path('api/shop/<int:id>/', api.ShopDetail.as_view()),
    path('api/forms/contact/', csrf_exempt(api.ContactFormView.as_view())),
    path('api/forms/prospect/', csrf_exempt(api.ProspectFormView.as_view())),
    path('api/forms/involvement/', csrf_exempt(api.InvolvementFormView.as_view())),
    path('api/forms/order/', csrf_exempt(api.OrderFormView.as_view())),
]
