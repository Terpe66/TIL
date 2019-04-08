from django.shortcuts import render, resolve_url, redirect, get_object_or_404
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, "board/list.html", {"articles":articles})


def article_new(request):
    if request.method == "POST":


        pass
    return True


def article_detail(request, id):
    if request.method == "POST":
        pass
    return True


def article_edit(request, id):
    if request.method == "POST":
        pass
    return True


def article_delete(request, id):
    if request.method == "POST":
        pass
    return True




def index(request):
    return render(request, "board/index.html")


def greeting(request, name, c):
    return render(request, "board/greeting.html", {"ireum":name, "class":c})