from django.urls import path
from .import views




urlpatterns =[
     path("",views.home , name="main"),
     path('sidebar' , views.sidebar , name="sidebar_partial")
]