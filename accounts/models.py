from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=30, blank=True)
    Gender = models.CharField(max_length=30, blank=True)
    phonenum = models.CharField(max_length=30, blank=True)
