from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=240, null=True,blank=True)
    text = models.TextField(max_length=240, null=True,blank=True)
    photo = models.ImageField(upload_to='photos/',blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name