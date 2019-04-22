from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.views.decorators.http import require_GET, require_POST, require_http_methods
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User
from .forms import CustomUserAuthenticationForm, CustomUserCreateForm
# from django.contrib.auth import get_user_model 위의 코드랑 같은 내용
from posts.forms import CommentModelForm


@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = CustomUserCreateForm(data=request.POST) # Form은 data, file로 돼 있나?
        if form.is_valid():
            form.save()
        return redirect("posts:post_list")
    else:
        form = CustomUserCreateForm()
    return render(request, "accounts/signup.html", {"form": form})


@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated:
        return redirect("posts:post_list")
    if request.method == "POST":
        form = CustomUserAuthenticationForm(request, data=request.POST) # 얘는 request, request.???로
        if form.is_valid():
            user = form.get_user()
            auth_login(request, form.get_user())
            messages.add_message(request, messages.SUCCESS, f"어서오세요! {user.username}")
            messages.add_message(request, messages.INFO, f"이전 접속은 {user.last_login}입니다.")
            return redirect(request.GET.get("next") or "posts:post_list")
    else:
        form = CustomUserAuthenticationForm(request)
    return render(request, "accounts/login.html", {"form": form})

@login_required
def logout(request):
    auth_logout(request)
    messages.add_message(request, messages.SUCCESS, "다음에 또 만나요")
    return redirect("posts:post_list")


def user_detail(request, username):
    user_info = User.objects.get(username=username)
    return render(request, "accounts/user_detail.html", {"user_info": user_info, "comment_form": CommentModelForm()})


@login_required
@require_POST
def toggle_follow(request, username):
    sender = request.user
    receiver = get_object_or_404(User, username=username)

    if sender != receiver:
        if receiver in sender.followings.all():
            sender.followings.remove(receiver)
        else:
            sender.followings.add(receiver)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER", "/insta/"))


