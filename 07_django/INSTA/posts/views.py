from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse, HttpResponseBadRequest
from .models import Post, Image, HashTag
from .forms import PostModelForm, ImageModelForm, CommentModelForm


@login_required
@require_http_methods(["GET", "POST"])
def create_post(request):
    posts = Post.objects.all()
    if request.method == "POST":
        post_form = PostModelForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False) # save를 하면 나오는 값을 post에 담아둠
            # commit=False를 쓰면 가짜 save, 저장은 하는데 넘기진 않음
            post.user = request.user
            if post not in posts:
                post.save()
            else:
                print("있어")

            # create hashtag => <input name="tags" /> #hi #ssafy #20층
            content = post_form.cleaned_data.get("content") #
            words = content.split(" ") # 띄어쓰기로 split
            for word in words:
                if word[0] == "#":
                    word = word[1:]
                    tag = HashTag.objects.get_or_create(content=word) # (HashTagObject, True or False)
                    post.tags.add(tag[0])
                    if tag[1]:
                        messages.add_message(request, messages.SUCCESS, f"{tag[0].content}를 처음으로 추가하셨어요!")


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
                #update hashtag
                post.tags.clear() # 포스트의 모든 tag 삭제
                content = post_form.cleaned_data.get("content")  #
                words = content.split(" ")  # 띄어쓰기로 split
                for word in words:
                    if word[0] == "#":
                        word = word[1:]
                        tag = HashTag.objects.get_or_create(content=word)  # (HashTagObject, True or False)
                        post.tags.add(tag[0])
                        if tag[1]:
                            messages.add_message(request, messages.SUCCESS, f"{tag[0].content}를 처음으로 추가하셨어요!")

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
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/insta/"))
    # TODO: else => if comment is not valid, then what?


# @login_required()
# @require_POST
# def create_like(request, post_id):
#     user = request.user
#     post = get_object_or_404(Post, id=post_id)
#     # user.like_posts.add(post) # 유저가 가진 정보를 add 하는 방법
#     post.like_users.add(user) # 포스트에 유저를 더하는 방법
#

@login_required
@require_POST
def toggle_like(request, post_id):
    if request.is_ajax():
        user = request.user
        post = get_object_or_404(Post, id=post_id)
        # if post.like_users.filter(id=user.id).exist(): # 좋아요 한 사람이 있으면 값이 나오고 없으면 빈 리스트 # exist는 좀 더 명확하게 만드는 역할
        is_active = True
        if user in post.like_users.all():
            post.like_users.remove(user)
            is_active = False
        else:
            post.like_users.add(user)
        # return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/insta/"))
        return JsonResponse({"likeCount": post.like_users.count(), "is_active": is_active})
    else:
        return HttpResponseBadRequest()


@require_GET
def tag_posts_list(request, tag_name):
    tag = get_object_or_404(HashTag, content=tag_name)
    posts = tag.posts.all()
    comment_form = CommentModelForm()
    return render(request, "posts/list.html", {"posts": posts, "comment_form": comment_form, "h1": f"#{tag}를 포함한 posts입니다."})