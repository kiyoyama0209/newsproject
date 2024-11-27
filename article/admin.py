from django.contrib import admin
from .models import  Category,ArticlePost

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

class ArticlePostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')

admin.site.register(Category, CategoryAdmin)

admin.site.register(ArticlePost, ArticlePostAdmin)
# Register your models here.
