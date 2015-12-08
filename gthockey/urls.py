from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^schedule/', views.schedule, name="schedule"),
    url(r'^roster/', views.roster, name="roster"),
]

