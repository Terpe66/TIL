from django.shortcuts import render, resolve_url, redirect, get_object_or_404
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, "board/list.html", {"articles":articles})


def article_new(request):
    if request.method == "POST":
        article = Article()
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect("board:list")

    return render(request, "board/new.html")


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "board/detail.html", {"article":article})


def article_edit(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        article.title = request.POST.get("title")
        article.content = request.POST.get("content")
        article.save()
        return redirect("board:detail")

    return render(request, "board/edit.html", {"article":article})


def article_delete(request, id):
    if request.method == "POST":
        article = get_object_or_404(Article, id=id)
        article.delete()
    return redirect("board:list")




def index(request):
    return render(request, "board/index.html")


def greeting(request, name, c):
    return render(request, "board/greeting.html", {"ireum":name, "class":c})