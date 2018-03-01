from django.conf.urls import url
from . import views, api

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^schedule/', views.schedule, name="schedule"),
    url(r'^roster/', views.roster, name="roster"),
    url(r'^board/', views.board, name="board"),
    # url(r'^coaches/', views.coaches, name="coaches"),
    url(r'^prospect/', views.prospect, name="prospect"),
    url(r'^contact/', views.contact, name="contact"),
    url(r'^api/nextgame/', api.nextgame, name="nextgame"),
    url(r'^api/record/', api.seasonRecord, name="record"),
    url(r'^news/(?P<id>[0-9]+)/', views.news, name="newsstory"),
    url(r'^involvement/', views.involvement, name="involvement"),
    # url(r'^golf/', views.golf, name="golf")
]
