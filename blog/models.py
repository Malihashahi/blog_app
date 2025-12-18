from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Category(models.Model):
     title = models.CharField(max_length=100)
     created = models.DateTimeField(auto_now_add=True)


def __str__(self):
     return self.title



class ArticleManager(models.Manager):
     def counter(self):
          return len(self.all)

     def publisher(self):
          return self.filter(published = True)




class Article(models.Model):
    id = models.BigAutoField()
    author = models.ForeignKey(User ,on_delete=models.SET_NULL , blank=True , related_name="articles")
    category = models.ManyToManyField(Category , related_name="articles")
    title = models.CharField(max_length=30 ,  primary_key=True)
    body = models.CharField(max_length=608)
    image = models.ImageField(upload_to="image/article")
    created = models.DateTimeField(auto_now_add=True , editable=False)
    updated = models.DateTimeField(auto_now= True)
    pub_date = models.DateField(default=timezone.now())
    myfile = models.BinaryField()
    status = models.BooleanField()
    published = models.BooleanField(default=True)
    slug = models.SlugField(null=True , unique=True)
    objects = ArticleManager()
   

    class Meta:
         ordaring =('created' , 'updated')
         
    

    def save(self, force_insert = ..., force_update = ..., using = ..., update_fields = ...):
         self.slug = self.title
         return super().save(force_insert, force_update, using, update_fields)
     



def get_absolute_url(self):
     return reversed('blog:article_detail' , args = [self.id])


def __str__(self):
     return  f"{self.title } - {self.body}"
 


class Comment(models.Model):
     article = models.ForeignKey(Article , on_delete=models.CASCADE , related_name='comments')
     User = models.ForeignKey(User ,on_delete=models.CASCADE , related_name='comments')

     parent = models.ForeignKey('self' , on_delete=models.CASCADE, null=True , related_name='replies')

     body = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)




     def __str__(self):
          return self.body[:50]

