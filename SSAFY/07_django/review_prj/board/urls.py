from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path("index/", views.index, name="index"),
    path("greeting/<str:name>/<str:c>", views.greeting, name="greeting"),
    path("articles/", views.article_list, name="list"),
    path("articles/new/", views.article_new, name="new"),
    path("articles/<int:id>/", views.article_detail, name="detail"),
    path("articles/<int:id>/edit", views.article_edit, name="edit"),
    path("articles/<int:id>/delete", views.article_delete, name="delete"),
]