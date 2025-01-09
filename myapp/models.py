from django.db import models
from django.contrib.auth.models import AbstractUser

class Custom_user(AbstractUser):
    USER=[
        ('creator','Creator'),
        ('viewer','Viewer')
    ]

    user_type=models.CharField(choices=USER,max_length=100,null=True)
    Image=models.ImageField(upload_to='Media/user_Pic',null=True)


    def  __str__(self):
        return f"{self.username}-{self.user_type}"
    

class photograph(models.Model):
    title = models. CharField (max_length=200)
    description=models.TextField(max_length=1000)
    pic=models.ImageField(upload_to="media/pictures")
    tags=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class sports(models.Model):
    title = models. CharField (max_length=200)
    description=models.TextField(max_length=1000)
    pic=models.ImageField(upload_to="media/pictures")
    tags=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class food(models.Model):
    title = models. CharField (max_length=200)
    description=models.TextField(max_length=1000)
    pic=models.ImageField(upload_to="media/pictures")
    tags=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"

class work(models.Model):
    title = models. CharField (max_length=200)
    description=models.TextField(max_length=1000)
    pic=models.ImageField(upload_to="media/pictures")
    tags=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title}"
