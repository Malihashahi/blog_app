from django.contrib.auth.models import User
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate , login , logout
#view 
def user_login(request):
    if request.user.is_authenticate == True:
         return redirect('/')



    if request.method == "POST":
       username =  request.POST.get('username')
       password = request.POST.get('password')
       user = authenticate(request , username=username , password = password)
       if user is not None:
           login(request , user)
           return redirect('/')

    return render(request , 'account/login.html' ,{})


def user_register(request):
    if request.user.is_authenticate == True:
        return redirect('/')
    
    if request.method =="POST":
         username = request.POST.get('username')
         email = request.POST.get('email')
         password1 = request.POST.get('password1')
         password2 = request.POST.get('password2')

    return render(request , "account/register.html" , {})




def user_logout(request):
    logout(request)
    return redirect('/')

