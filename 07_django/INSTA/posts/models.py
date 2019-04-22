from django.db import models
from django_extensions.db.models import TimeStampedModel
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django.conf import settings

import os
ENV = os.environ.get("ENVIRONMENT", "development")

if ENV == "development":
    from faker import Faker
    hide_on_bush = Faker()


class HashTag(models.Model):
    content = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.content


class Post(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_posts")
    tags = models.ManyToManyField(HashTag, blank=True, related_name="posts")
    # image = models.ImageField(blank=True) # pip install pillow
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            Post.objects.create(content=hide_on_bush.text(102))


class Image(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = ProcessedImageField(
        processors=[ResizeToFill(600, 600)],
        upload_to="posts/images", format="JPEG", options={"quality": 90, },
        blank=True)


class Comment(TimeStampedModel):
    content = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

