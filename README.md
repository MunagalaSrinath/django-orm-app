# Django ORM Web Application

## AIM
To develop a Django application to store and retrieve data from a database using Object Relational Mapping(ORM).

## Entity Relationship Diagram
![entity diagram](./images/marksinfo.png)

## DESIGN STEPS

### STEP 1:
first we have to clone the reprositry from git then we have to give a command to enter in django-orm-app we have to enter in the file called called dataproject by using command called cd dataproject  

### STEP 2:
now we have to enter in our own created file name marksinfo by using a command called python3 manage.py startapp marksinfo.

### STEP 3:
now we have to copy the theia link and add it in admin paste that in new app to get the output and enter the user name and password and the details ew created in the terminal



## PROGRAM
```
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
```




## OUTPUT

![server side output](./images/serversideoutput.png)
![client side output](./images/clientserveroutput.png)





## RESULT
