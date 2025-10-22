from django.shortcuts import render , get_object_or_404
from blog.models import Article
from django.urls import reverse




def post_detail(request , pk):
   article = Article.objects.all()[0:30]
  
   return render(request , "blog/article_detail.html" , {'article' : article})
