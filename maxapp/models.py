import email
from django.db import models

# Create your models here.
class usersignup(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    uname=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    city=models.CharField(max_length=20)
    ustate=models.CharField(max_length=20)
    zipcode=models.IntegerField()


class notesdata(models.Model):
    query=models.TextField()
    opt=models.CharField(max_length=50)
    fileup=models.FileField(upload_to="Notesupload")
    comments=models.TextField()


class contactdata(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phnno=models.BigIntegerField()
    msg=models.TextField()

    