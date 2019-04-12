from django.db import models
import os
ENV = os.environ.get("ENVIRONMENT", "development")

if ENV == "development":
    from faker import Faker
    hide_on_bush = Faker()


class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            Post.objects.create(content=hide_on_bush.text(102))