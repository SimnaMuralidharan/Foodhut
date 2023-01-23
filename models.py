from django.db import models
from django.contrib.auth.models import User

class regmodel(models.Model):
    fullname=models.CharField(max_length=30)
    username=models.CharField(max_length=30)
    email=models.EmailField()
    gender=models.CharField(max_length=20)
    phone=models.IntegerField()
    password=models.CharField(max_length=30)

class usermodel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)


class nonmodel(models.Model):
    nitem=models.CharField(max_length=25)
    nprice=models.IntegerField()
    ndes=models.CharField(max_length=100)
    nimage=models.FileField(upload_to='foodhut_app/static/non_veg')


class vegmodel(models.Model):
    vitem=models.CharField(max_length=25)
    vprice=models.IntegerField()
    vdes=models.CharField(max_length=100)
    vimage=models.FileField(upload_to='foodhut_app/static/veg')

class adddetailsmodel(models.Model):
    rimage = models.FileField(upload_to='foodhut_app/static')
    rid = models.IntegerField()
    rname = models.CharField(max_length=25)
    rno = models.IntegerField()
    rloc = models.CharField(max_length=50)
    ropen = models.TimeField()
    rclose = models.TimeField()
