from django.shortcuts import render , get_object_or_404
from blog.models import Article ,Category
from django.urls import reverse
from django.core.paginator import Paginator



def article_detail(request , pk):
   article = Article.objects.all().order_by('-created' , '-updated')
   recent_articles = Article.objects.all()[:3]
  
   return render(request , "blog/article_detail.html" , {'article' : article})

def article_list(request):
   articles = Article.objects.all()
   return render(request , "blog/articles_list.html", {'article': articles })



def category_deatial(request , pk=None):
   category = get_object_or_404(Category , id=pk)
   articles = category.article_set.all()
   return render(request , "blog/articles_list.html" ,{'article' : articles})
       

