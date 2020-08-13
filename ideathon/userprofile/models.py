from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class rectify_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    school = models.CharField(max_length=10)
    contact = models.CharField(max_length=10)
    introduce = models.TextField(max_length=500)


