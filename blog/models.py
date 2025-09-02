from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Article(models.Model):
    author = models.ForeignKey(User ,on_delete=models.SET_NULL ,null=True , blank=True)
    title = models.CharField(max_length=30 , help_text="Enter A volid title" , unique=True , db_column="mytitle" , unique_for_date='pub_date')
    body = models.CharField(max_length=608)
    image = models.ImageField(upload_to="image/article")
    created = models.DateTimeField(auto_now_add=True , editable=False)
    updated = models.DateTimeField(auto_now= True)
    pub_date = models.DateField(default=timezone.now())




def __str__(self):
     return  f"{self.title } - {self.body}"