from django.contrib import admin

# Register your models here.

from .models import Post, Profile

admin.site.register(Profile)
admin.site.register(Post)
