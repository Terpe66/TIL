from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST) # Form은 data, file로 돼 있나?
        if form.is_valid():
            form.save()
        return redirect("posts:post_list")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


@require_http_methods(["GET", "POST"])
def login(request):
    if request.user.is_authenticated:
        return redirect("posts:post_list")
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST) # 얘는 request, request.???로
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get("next") or "posts:post_list")
    else:
        form = AuthenticationForm(request)
    return render(request, "accounts/login.html", {"form": form})


def logout(request):
    auth_logout(request)
    return redirect("posts:post_list")