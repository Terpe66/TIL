from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("accounts:index")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


def signout(request):
    logout(request)
    return redirect("accounts:index")


def index(request):
    return render(request, "accounts/index.html")


def signin(request):
    # 사용자가 로그인 한 상태에서 또 들어올 경우
    if request.user.is_authenticated:
        return redirect("accounts:index")

    # 로그인 안 한 상태에서 POST 형식으로 들어올 때 => 가입 절차로
    if request.method == "POST":
        # 로그인하는 창의 폼
        form = AuthenticationForm(request, request.POST)
        # 로그인 검증 성공
        if form.is_valid():
            # 로그인
            login(request, form.get_user())
            # 로그인 전에 있던 페이지가 있다면
            if request.GET.get("next"):
                # 그 페이지로 보내고
                return redirect(request.GET.get("next"))
            # 없다면 index 페이지로 보낸다
            return redirect("accounts:index")
    # 로그인 안 한 상태에서 GET 형식으로 들어올 때 => 가입 페이지로
    else:
        form = AuthenticationForm()
    return render(request, "accounts/signin.html", {"form": form})

