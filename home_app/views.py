from django.shortcuts import render
from blog.models import Article
# Create your views here.
def home(request):
    articles = Article.objects.all()
    article = Article.objects.get(id = 16)
    article.myfile = bytes('hello  ' ,'utf-8')
    article.save()
    return render(request ,"home_app/index.html", {'articles': articles} )