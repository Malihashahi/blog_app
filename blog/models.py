from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=608)
    image = models.ImageField(upload_to="image/article")
    created = models.DateField(auto_now_add=True)