from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser): # User는 빈 껍데기고, AbstractUser가 거의 모든 걸 가지고 있음
    # username, password, first_name, last_name, email은 기본적으로 가지고 있음
    # settings.AUTH_USER_MODEL 부분은 "self"나 "accounts.User"를 써도 됨
    followings = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followers", blank=True)

    def __str__(self):
        return f"{self.username}"