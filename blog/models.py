from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Category(models.Model):
     title = models.CharField(max_length=100)
     created = models.DateTimeField(auto_now_add=True)


def __str__(self):
     return self.title



class Article(models.Model):
    id = models.BigAutoField()
    author = models.ForeignKey(User ,on_delete=models.SET_NULL ,null=True , blank=True)
    category = models.ManyToManyField(Category)
    title = models.CharField(max_length=30 ,  primary_key=True)
    body = models.CharField(max_length=608)
    image = models.ImageField(upload_to="image/article")
    created = models.DateTimeField(auto_now_add=True , editable=False)
    updated = models.DateTimeField(auto_now= True)
    pub_date = models.DateField(default=timezone.now())
    myfile = models.BinaryField(null=True)
    is_published = models.BooleanField()


def __str__(self):
     return  f"{self.title } - {self.body}"
 




class New(models.Model):
     title = models.CharField(max_length=34)
     des = models.TextField()

     def __str__(self):
          return self.title
