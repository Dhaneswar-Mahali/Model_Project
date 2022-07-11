'''
1. import the  models module

2. create  userdefined model class   by using predefind  model class

3. create required userdefined model fields with required field datatypes.

'''
#Model created by Dhaneswar
from django.db import models
class Employee(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=30)
    salary = models.FloatField()






