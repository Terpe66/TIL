from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .models import Post, Comment
from .forms import PostModelForm, CommentModelForm


@require_http_methods(["GET", "POST"])
def create_post(request):
    if request.method == "POST":
        post_form = PostModelForm(request.POST)
        if post_form.is_valid():
            post_form.save()
        return redirect("posts:post_list")
    else:
        post_form = PostModelForm()
    return render("posts/form.html", {"post_form": post_form, })


@require_http_methods(["GET", "POST"])
def update_post(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == "POST":
        post_form = PostModelForm(request.POST, instance=Post)
        if post_form.is_valid():
            post_form.save()
            return redirect("posts:post_list")
    else:
        post_form = PostModelForm(instance=Post)
    return render(request, "posts/form.html", {"post_form": post_form})


@require_GET
def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentModelForm()
    return render(request, "posts/list.html", {"posts": posts, "comment_form": comment_form})


@require_POST
def create_comment(request, id):
    comment_form = CommentModelForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save()
        comment.save()
    return redirect("posts:post_list")