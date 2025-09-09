from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class User(models.Model):
   fullname = models.CharField(max_length=44)



class Profile(models.Model):
   uset = models.OneToOneField()