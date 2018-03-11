from django.urls import path
from . import api

urlpatterns = [
    path('api/players/', api.PlayerList.as_view()),
    path('api/games/', api.GameList.as_view()),
    path('api/games/<int:id>/', api.GameDetail.as_view()),
    path('api/articles/', api.ArticleList.as_view()),
    path('api/articles/<int:id>/', api.ArticleDetail.as_view()),
    path('api/board/', api.BoardList.as_view()),
    path('api/coaches/', api.CoachList.as_view()),
    path('api/forms/contact/', api.ContactFormView.as_view()),
    path('api/forms/prospect/', api.ProspectFormView.as_view()),
    path('api/forms/involvement/', api.InvolvementFormView.as_view()),
]
