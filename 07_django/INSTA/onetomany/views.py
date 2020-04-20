from django.shortcuts import render, redirect
from .models import Writer, Book, Chapter
from .forms import WriterModelForm, BookModelForm, ChapterModelForm

def new(request):
    return render()



def create(request):
    if request.method == "POST":
        form = WriterModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("detail")
    else:
        form = WriterModelForm()
    return render(request, "new.html", {"form":form})


def update(request, id):
    writer = Writer.objects.get(id=id)
    if request.method == "POST":
        form = WriterModelForm(request.POST, instance=writer) # instance를 붙이면 수정 로직
        if form.is_valid():
            form.save()
            return redirect()
    else:
        form = WriterModelForm(instance=writer)
    return render(request, "edit.html", {"form":form})