from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    title  = models.CharField(max_length = 150)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    page_count = models.IntegerField()
    is_available = models.BooleanField()

    def __str__(self):
        return self.title