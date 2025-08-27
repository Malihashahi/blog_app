from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(User ,on_delete=models.CASCADE, )
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=608)
    image = models.ImageField(upload_to="image/article")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now= True)





def __str__(self):
     return  f"{self.title } - {self.body}"