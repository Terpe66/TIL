# 190411 Django M:N DB

ex) 나의 수강신청 과목 list <-> 개별 과목에 수강신청을 한 여러 학생들



**Student**

| id   | name | major | account |
| ---- | ---- | ----- | ------- |
|      |      |       |         |



**Lecture**

| id   | title | classroom | credits | lecture time |
| ---- | ----- | --------- | ------- | ------------ |
|      |       |           |         |              |



**어떤 학생이 어떤 수업을 듣는지 저장할 때**

| id   | student_id | lecture_id |
| ---- | ---------- | ---------- |
|      |            |            |



### jointable

```python
students = models.ManyToManyField(Student)

# models.ManyToManyField(클래스명)이 아래 클래스의 역할을 대신하고, 테이블을 생성한다
class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} : {self.student.name} {self.lecture.title}"
```



```python
from django.db import models
from faker import Faker

SKT = Faker()

class Client(models.Model):
    name = models.CharField(max_length=30)

    # 이름 순으로 나오게 만드는 class
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
```

