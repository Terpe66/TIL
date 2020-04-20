from django import forms
from .models import Post, Comment


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post()
        fields = "_all_"


class CommentModelForm(forms.ModelForm):
    class META:
        model = Comment
        fields = "_all_"

