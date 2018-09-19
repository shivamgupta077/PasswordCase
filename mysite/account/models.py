from django.db import models

# Create your models here.

class Profile(models.Model):
    id = models.AutoField(primary_key=True)

class Case(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    mobilenum = models.BigIntegerField()
    ans1 = models.CharField(max_length=100)
    ans2 = models.CharField(max_length=100)
    ans3 = models.CharField(max_length=100)
    ans4 = models.CharField(max_length=100)
    ans5 = models.CharField(max_length=100)
    place = models.OneToOneField(Profile, on_delete=models.CASCADE)

class Passwords(models.Model):
    website = models.CharField(max_length=20)
    uname = models.CharField(max_length=100)
    eccrypted_password = models.CharField(max_length=100)
    belongs_to = models.ForeignKey(Profile, on_delete=models.CASCADE)

class Question(models.Model):
    ques = models.CharField(max_length=100)
