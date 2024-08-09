from django.contrib import admin # type: ignore

from blogapp.models import MyBlog

# Register your models here.
admin.site.register(MyBlog)