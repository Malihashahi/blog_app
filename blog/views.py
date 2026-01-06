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
   page_number = request.GET.get('page')
   paginator = Paginator(articles , 1)
   objects_list = paginator.get_page(page_number)
   return render(request , "blog/articles_list.html", {'article': objects_list })



def category_deatial(request , pk=None):
   category = get_object_or_404(Category , id=pk)
   articles = category.article_set.all()
   return render(request , "blog/articles_list.html" ,{'article' : articles})
       


def search(request):
   q = request.GET.get('q')
   articles = Article.objects.filter(title__icontains = q)
   page_number = request.GET.get('page')
   paginator = Paginator(articles , 2)
   objects_list = paginator.get_page(page_number)
   return render(request, 'blog/articles_list.html' ,{'articles' : articles})




def contactus(request):
   if request.methond == 'POST':
      form = ContactUs(request.POST)
      if form.is_valid():
         print(form.cleaned_data['text'])
         massage = Massage.object()
         return redirect('home_app:home')
      

   form  = ContactUsForm()
   return render(request ,"blog/contact_us.html")