from pyexpat import model
from turtle import title
from django.db import models
from django.forms import IntegerField

# Create your models here.

class meetup(models.Model):
    
    title  = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField(max_length=1000)