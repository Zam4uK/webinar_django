from django.contrib import admin
from .models import Blog

class AdminBlog(admin.ModelAdmin):
    fields = ('name', 'text')
    list_display = ('name',)



admin.site.register(Blog,AdminBlog)