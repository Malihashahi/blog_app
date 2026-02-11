from django.shortcuts import render
from blog.models import Article , New
# Create your views here.
def home(request):
    articles = Article.objects.published()
   
    return render(request ,"home_app/index.html", {'articles': articles} )




def sidebar(request):
    context = {'name' : 'Bahar'}
    return render(request , 'includes/sidebar.html' , context)



def contactus(request):
    if request.methode == "POST":
        form = MessageFrom(data = request.GET)  
        if form.is_valid():
              form.save()