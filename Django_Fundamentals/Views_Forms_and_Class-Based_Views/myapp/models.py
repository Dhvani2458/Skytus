
from django.db import models

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.course_name


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='students'
    )

    def __str__(self):
        return self.name
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.title


