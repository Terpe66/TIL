from django.db import models
from faker import Faker

hide_on_bush = Faker()

class Movie(models.Model):
    title = models.CharField(max_length=100)

    @classmethod
    def dummy(cls, n):
        for _ in range(n):
            cls.objects.create(title=hide_on_bush.catch_phrase())

    def __str__(self):
        return f"{self.id}: {self.title}"