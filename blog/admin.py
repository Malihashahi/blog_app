from django.contrib import admin
from .models import Article , Category  , New ,Comment
# Register your models here.

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(New)
admin.site.register(Comment)