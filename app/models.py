from django.db import models

class Student(models.Model):
    Name = models.CharField(max_length=30)
    Roll_No = models.IntegerField()
    Location = models.CharField(max_length=50)

class Teacher(models.Model):
    t_name = models.CharField(max_length=30)
    t_id = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
