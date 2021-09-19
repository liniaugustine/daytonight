from django.db import models
from django.db.models import Q,F
from datetime import datetime
class Login(models.Model):
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=8)
    def __str__(self):
        return self.username
        
class Udetails(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=20)   
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
class Task(models.Model):
    newtask=models.CharField(max_length=500)
    date=models.DateField(null=True) 
    time=models.TimeField(null=True)
    status=models.CharField(max_length=20, default="active")
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
class Notes(models.Model):
    mynote=models.CharField(max_length=100)  
    mycolor=models.CharField(max_length=30)  
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
class Diet(models.Model):
    age=models.IntegerField()    
    height=models.IntegerField()
    weight=models.IntegerField()
    medcondition=models.CharField(max_length=20)
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
class Myfood(models.Model):
    morning=models.CharField(max_length=40)   
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE) 
class Mylunch(models.Model):
    lunch=models.CharField(max_length=40)
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
class Mydinner(models.Model):
    dinner=models.CharField(max_length=40)
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
