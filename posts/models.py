from django.db import models
from django.contrib.auth.models import User
import datetime 

# Create your models here.

class Post(models.Model):
    """Django data model Post"""
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(blank=True, max_length=100)
    body = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return str(self.title)
