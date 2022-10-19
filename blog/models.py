# from enum import auto
# from turtle import title
# from venv import create
# import email
# from turtle import update
# from unicodedata import name
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class book(models.Model):
    title = models.CharField(max_length=225)
    subtitle = models.CharField(max_length=225)
    author =models.CharField(max_length=225)
    isbn =  models.CharField(max_length=13)

    def __str__(self):
        return self.title
class Post(models.Model):
    STATUS_CHOICES =(
        ('draft','Draft'),
        ('published','Published')
    )
    title = models.CharField(max_length=250)
    post_image=models.ImageField(blank=True, null=True, upload_to = "posts/")
    slug =models.CharField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='blog_Post')
    body =models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    create = models.DateField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES, default='draft')
    class meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year,self.publish.month,self.publish.day,self.slug])

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='Comments')
    name  =models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created =models.DateTimeField(auto_now_add=True)
    updated =models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    class meta:
        ordering = ('created',)
    def __str__(self):
        return f'comments by{self.name}on{self.post}'