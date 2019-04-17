from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("create/", views.create_post, name="create_post"),
    path("<int:post_id>/update/", views.update_post, name="update_post"),
    path("<int:post_id>/create_comment/", views.create_comment, name="create_comment")
]