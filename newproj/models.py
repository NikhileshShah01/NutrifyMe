from tkinter import Widget
from unicodedata import name
from click import launch
from django.db import models
from tomlkit import date

# Create your models here.
class Register(models.Model):
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=3)
    city=models.CharField(max_length=50)
    genders=[
        ('male','Male'),('female','Female'),('others','Others'), ]
    gender = models.CharField(max_length=10, choices=genders,default='male')
    userid=models.CharField(primary_key= True,max_length=15 ,unique=True)
    password=models.CharField(max_length=25)
  
    def __str__(self):
        return self.name

# make migrations :- create changes and store it in a file
#migration :- apply the changes made by make migrations