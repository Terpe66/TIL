from django.db import models


class Post(models.Model):
    content = models.CharField(max_length=140)
    image = models.ImageField(blank=True) # pip install pillow
    created_at = models.DateTimeField(auto_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    content = models.CharField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
