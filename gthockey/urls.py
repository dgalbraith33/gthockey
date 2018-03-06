from django.conf.urls import handler404
from django.urls import path
from . import api

urlpatterns = [
    path('api/nextgame/', api.nextgame),
    path('api/record/', api.seasonRecord),
    path('api/players/', api.player_list),
    path('api/games/', api.GameList.as_view()),
    path('api/games/<int:id>/', api.GameDetail.as_view()),
    path('api/articles/', api.article_list),
    path('api/articles/<int:id>/', api.article_get),
    path('api/board/', api.board_list),
    path('api/coaches/', api.coach_list),
]

handler404 = 'views.handler404'
