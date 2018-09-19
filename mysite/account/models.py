from django.db import models

# Create your models here.

class Case(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    mobilenum = models.BigIntegerField()
    ans1 = models.CharField(max_length=50)
    ans2 = models.CharField(max_length=50)
    ans3 = models.CharField(max_length=50)
    ans4 = models.CharField(max_length=50)
    ans5 = models.CharField(max_length=50)

class Question(models.Model):
    ques = models.CharField(max_length=100)


class Profile(models.Model):
    password = mo