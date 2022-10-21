from django.db import models
from tkinter import CASCADE
from tkinter.messagebox import QUESTION
from unicodedata import name
from datetime import datetime 
# Create your models here.


class send_mail(models.Model):
    title = models.CharField(max_length=255)
    send_date = models.DateTimeField(default=datetime.now(), blank=True)
    email = models.EmailField()
    content = models.CharField(max_length=1000)
    

class read_mail(models.Model):
    Subject = models.CharField(max_length=100)
    To = models.CharField(max_length=100)
    send_date = models.CharField(max_length=100)
    From = models.CharField(max_length=100)
    Message = models.CharField(max_length=2000)