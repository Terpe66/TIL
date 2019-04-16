from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill
from django_extensions.db.models import TimeStampedModel

import os
ENV = os.environ.get("ENVIRONMENT", "development")

if ENV == "development":
    from faker import Faker
    hide_on_bush = Faker()


class Post(TimeStampedModel):
    content = models.CharField(max_length=140)
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