from django.db import models
from django_extensions.db.models import TimeStampedModel, TitleDescriptionModel


class MagazineArticle(TimeStampedModel, TitleDescriptionModel):
    content = models.TextField()


class TimeStamp(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Writer(TimeStamp):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.id} : {self.name}"


class Book(TimeStamp):
    author = models.ForeignKey(Writer, on_delete=models.PROTECT)
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.id}. {self.author.name} : {self.title}"


class Chapter(TitleDescriptionModel, TimeStampedModel):
    # title, description, created, modified
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}. {self.book.title}"


class Student(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} : {self.name}"


class Message(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    content = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.student.name} : {self.content}"


class Reply(models.Model):
    content = models.CharField(max_length=30)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} - {self.content}"