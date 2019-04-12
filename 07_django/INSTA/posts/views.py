from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .models import Post
from .forms import PostModelForm


@require_http_methods(["GET", "POST"])
def create_post(request):
    if request.method == "POST":
        form = PostModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("posts:post_list")
    else:
        form = PostModelForm()
    return render(request, "posts/form.html", {"form": form})


@require_http_methods(["GET", "POST"])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("posts:post_list")
    else:
        form = PostModelForm(instance=post)
    return render(request, "posts/form.html", {"form": form})



def post_list(requests):
    posts = Post.objects.all()

    return render(requests, "posts/list.html", {"posts":posts})