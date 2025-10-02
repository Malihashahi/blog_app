from django.shortcuts import render
from blog.models import Article





def post_detail(request , pk):
   article = Article.objects.get(id = pk)
   return render(request , "blog/article_detail.html" , {'article' : article})
