from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Account(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    is_fresher = models.BooleanField(default=True)
    resume = models.FileField(blank=True)


    def __str__(self):
        return self.user.username
