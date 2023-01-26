from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin
# Create your models here.
class Employee(models.Model):
    employeeid = models.CharField(max_length=8,primary_key=True)
    name =models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    salary = models.IntegerField()
   
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employeeid','name','email','age','salary')