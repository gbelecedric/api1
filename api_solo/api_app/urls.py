from django.urls import path
from . import views

urlpatterns = [
    path("list", views.lists, name="list"),
    path("article", views.article, name="article"),
    path("details/<int:pk>/", views.detail, name="details"),
    path("commentaire", views.commentaire, name="com"),
    path("souscategorie", views.souscategorie, name="sous"),
]