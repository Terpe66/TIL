# django form



```html
<!-- create.html -->
{% extends "movie/base.html" %}

{% block body %}
    <form action="{% url 'movie:create' %}" method="POST">
        {% csrf_token %}
        <!-- required를 넣으면 필수 입력란으로 바뀜 -->
        제목: <input type="text" name="title" required> <br>
        영문: <input type="text" name="title_eng" required> <br>
        관객수: <input type="text" name="audience"> <br>
        개봉일: <input type="date" name="open_date"> <br>
        장르: <input type="text" name="genre"> <br>
        상영등급: <input type="text" name="watch_grade"> <br>
        점수: <input type="number" step="0.01" name="score"> <br>
        포스터 url: <input type="text" name="poster_url"> <br>
        영화소개: <textarea name="description" cols="30" rows="10"></textarea> <br>
        <input type="submit" value="등록">
    </form>
{% endblock %}
```

```python
# forms.py
from django import forms

class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    title_eng = forms.CharField(max_length=100)
    audience = forms.IntegerField()
    open_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={"type": "date"})
    )
    genre = forms.CharField(max_length=100)
    watch_grade = forms.CharField(max_length=100)
    score = forms.FloatField()
    # form엔 TextField가 없고, CharField()라고 작성하면 대체됨.
    poster_url = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())

```

```python
# views.py

def create(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get("title")
            title_eng = form.cleaned_data.get("title_eng")
            audience = form.cleaned_data.get("audience")
            open_date = form.cleaned_data.get("open_date")
            genre = form.cleaned_data.get("genre")
            watch_grade = form.cleaned_data.get("watch_grade")
            score = form.cleaned_data.get("score")
            poster_url = form.cleaned_data.get("poster_url")
            description = form.cleaned_data.get("description")

            Movie.objects.create(
                title=title,
                title_eng=title_eng,
                audience=audience,
                open_date=open_date,
                genre=genre,
                watch_grade=watch_grade,
                score=score,
                poster_url=poster_url,
                description=description
            )

            return redirect("movie:list")

    else:
        form = MovieForm()

    return render(request, "movie/create.html", { "form": form, })
```

```html
<!-- create.html -->

{% extends "movie/base.html" %}

{% block body %}
    <form action="{% url 'movie:create' %}" method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="등록">
    </form>
{% endblock %}
```





```python
# forms.py

from django import forms
from .models import Movie


class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    title_eng = forms.CharField(max_length=100)
    audience = forms.IntegerField()
    open_date = forms.DateField(
        widget=forms.widgets.DateInput(attrs={"type": "date"})
    )
    genre = forms.CharField(max_length=100)
    watch_grade = forms.CharField(max_length=100)
    score = forms.FloatField()
    poster_url = forms.CharField()
    description = forms.CharField(widget=forms.Textarea())


class MovieModelForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = "__all__"
        widgets = {
            "open_date": forms.DateInput(attrs={"type": "date"}),
        }


```

```python
# views.py

# create 2
def create(request):
    if request.method == "POST":
        form = MovieModelForm(request.POST)
        if form.is_vaild():
            form.save()

            return redirect("movie:list")

    else:
        form = MovieModelForm()

    return render(request, "movie/create.html", { "form": form, })

# update
def update(request, id):
    movie = get_object_or_404(Movie, id=id)
    if request.method == "POST":
        form = MovieModelForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()

            return redirect("movie:detail", id)

    else:
        form = MovieModelForm(instance=movie)

    return render(request, "movie/update.html", {
        "form": form,
    })
```



```python
# settings.py

INSTALLED_APPS = [
    'django.contrib.admin',
    # 인증 관리하는 앱
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django_extensions",
    "sns",
    "movie",
    "accounts",
]
```

```python
# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
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
```

```html
<!-- signup -->

<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="가입">
</form>
```



가입 확인하기

```html
<h1>회원가입 & 로그인 테스트</h1>

<h2>
    {% if user.is_authenticated %}
    Logout - 로그아웃
    {% else %}
    Login - 로그인
    {% endif %}
</h2>
```



로그인하기

```python
# views.py

def signin(request):
    # 사용자가 로그인 한 상태에서 또 들어올 경우
    if request.user.is_authenticated:
        return redirect("accounts:index")

    # 로그인 안 한 상태에서 POST 형식으로 들어올 때 => 가입 절차로
    if request.method == "POST":
        # 로그인하는 창의 폼
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("accounts:index")
    # 로그인 안 한 상태에서 GET 형식으로 들어올 때 => 가입 페이지로
    else:
        form = AuthenticationForm()
    return render(request, "accounts/signin.html", {"form": form})
```

```html
<form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit" value="가입">
</form>
```



```python
# movie의 views.py
from django.contrib.auth.decorators import login_required

# 로그인 안 하면 못 들어감
@login_required
def create(request):
```

```python
# accounts의 views.py

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
```

