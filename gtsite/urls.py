"""gtsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import include, path, re_path
from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('gthockey.urls')),
    re_path(r'^(?!/?static/)(?!/?media/)(?P<path>.*\..*)$',
            RedirectView.as_view(url='/static/%(path)s', permanent=False)),
    path('', serve, kwargs={'path': 'index.html'}),
    path('roster/', serve, kwargs={'path': 'index.html'}),
    path('schedule/', serve, kwargs={'path': 'index.html'}),
]
