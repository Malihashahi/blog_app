from django.db import models

# Create your models here.
class User(models.Model):
   fullname = models.CharField(max_length=44)