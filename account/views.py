from django.shortcuts import render
from django.contrib.auth import aauthenticate , login
# Create your views here.
def login(request):
    if request.method == "POST":
       username =  request.POST.get('username')
       password = request.POST.get('password')


    return render(request , 'account/login.html' ,{})