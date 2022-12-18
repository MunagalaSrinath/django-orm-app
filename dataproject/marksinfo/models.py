from django.db import models
from django.contrib import admin
class Marks(models.Model):
    studentid = models.CharField(max_length=8,primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    marks = models.IntegerField()
class MarksAdmin(admin.ModelAdmin):
    list_display = ('studentid','name','age','email','marks')

# Create your models here.
