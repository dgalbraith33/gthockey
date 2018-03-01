from django.conf.urls import url, handler404
from django.urls import path, re_path
from . import views, api

urlpatterns = [
    path('', views.index),
    path('schedule/', views.schedule),
    path('roster/', views.roster),
    path('board/', views.board),
    path('prospect/', views.prospect),
    path('contact/', views.contact),
    path('news/<int:id>/', views.news),
    path('involvement/', views.involvement),
    # path('golf/', views.golf),
    path('api/nextgame/', api.nextgame),
    path('api/record/', api.seasonRecord),
]

handler404 = 'views.handler404'
