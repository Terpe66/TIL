from django.db import models


class User(models.Model):
    email = models.CharField(max_length=100, default="", unique=True)
    password = models.CharField(max_length=16, default="")

    def __str__(self):
        return f"{self.id} : {self.email}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    last_name = models.CharField(max_length=50, default="")
    first_name = models.CharField(max_length=50, default="")

    def __str__(self):
        return f"{self.user.email} : {self.last_name} {self.first_name}"