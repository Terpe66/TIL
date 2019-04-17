from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from .models import Post, Image
from .forms import PostModelForm, ImageModelForm, CommentModelForm
from django.contrib.auth.decorators import login_required


@login_required
@require_http_methods(["GET", "POST"])
def create_post(request):
    if request.method == "POST":
        post_form = PostModelForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False) # save를 하면 나오는 값을 post에 담아둠
            # commit=False를 쓰면 가짜 save, 저장은 하는데 넘기진 않음
            post.user = request.user
            post.save()
            for image in request.FILES.getlist("file"):
                request.FILES["file"] = image
                image_form = ImageModelForm(files=request.FILES)
                if image_form.is_valid():
                    image = image_form.save(commit=False)
                    image.post = post
                    image.save()
            return redirect("posts:post_list")
    else:
        post_form = PostModelForm()
    image_form = ImageModelForm()
    return render(request, "posts/form.html", {"post_form": post_form, "image_form": image_form})


@login_required
@require_http_methods(["GET", "POST"])
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.user == request.user:
        if request.method == "POST":
            post_form = PostModelForm(request.POST, request.FILES, instance=post)
            if post_form.is_valid():
                post_form.save()
                return redirect("posts:post_list")
        else:
            post_form = PostModelForm(instance=post)
        return render(request, "posts/form.html", {"post_form": post_form})
    else:
        # 403 : Forbidden 금지!
        return redirect("posts:post_list")


@require_GET
def post_list(request):
    posts = Post.objects.all()
    comment_form = CommentModelForm()
    return render(request, "posts/list.html", {"posts": posts, "comment_form": comment_form})


@login_required
@require_POST
def create_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comment_form = CommentModelForm(data=request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.user = request.user
        comment.post = post
        comment.save()
    return redirect("posts:post_list")