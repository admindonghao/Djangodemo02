from django.db import models

# Create your models here.
"""
创建新的类
"""


class Author(models.Model):
    name = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Book(models.Model):
    bookname = models.CharField(max_length=10)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    brief_info = models.CharField(max_length=200)
    writing_time = models.DateTimeField()

    def __str__(self):
        return self.bookname




