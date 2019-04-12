from django.db import models
from faker import Faker

SKT = Faker()

class User(models.Model):
    name = models.CharField(max_length=10)


class Profile(models.Model):
    age = models.IntegerField()
    address = models.CharField(max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Client(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.id} : {self.name}"

    class Meta:
        ordering = ("name", )

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            cls.objects.create(name=SKT.name())


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    clients = models.ManyToManyField(Client)

    @classmethod
    def dummy(cls, n):
        for i in range(n):
            cls.objects.create(name=SKT.company())

#
# class Student(models.Model):
#     name = models.CharField(max_length=30)
#     major = models.CharField(max_length=50)
#     account = models.CharField(max_length=50)
#
#     def __str__(self):
#         return f"{self.id} : {self.major} {self.name}"
#
#
# class Lecture(models.Model):
#     title = models.CharField(max_length=100)
#     classroom = models.CharField(max_length=30)
#     credits = models.IntegerField()
#     lecture_time = models.IntegerField()
#     students = models.ManyToManyField(Student)
#
#     def __str__(self):
#         return f"{self.id} : {self.title} {self.classroom}"
#
#
# class Enrollment(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f"{self.id} : {self.student.name} {self.lecture.title}"