from django.conf.urls import handler404
from django.urls import path
from . import views, api

urlpatterns = [
    path('nextgame/', api.nextgame),
    path('record/', api.seasonRecord),
    path('players/', api.player_list),
    path('games/', api.GameList.as_view()),
    path('games/<int:id>', api.GameDetail.as_view()),
    path('articles/', api.article_list),
]

handler404 = 'views.handler404'
