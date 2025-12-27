from django.urls import path
from . import views


urlpatterns = [
  path('detail/<int:pk>' , views.post_detail , name ="article_detail"),
  path('list' , views.article_list , name ="article_list"),
  path('category/<int:pk>' , name="category_detail"),
  path('search/', views.search , name "search_articles"),
]