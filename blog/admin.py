from django.contrib import admin
from .models import BlogPost


# Core from https://djangocentral.com/building-a-blog-application-with-django/
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BlogPost, BlogPostAdmin)
