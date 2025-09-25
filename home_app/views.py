from django.shortcuts import render
from blog.models import Article , New
# Create your views here.
def home(request):
    articles = Article.objects.filter(status =True)
   
    return render(request ,"home_app/index.html", {'articles': articles} )