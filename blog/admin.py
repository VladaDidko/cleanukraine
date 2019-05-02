from django.contrib import admin
from .models import Post, Comment
from User.models import Profile


admin.site.register(Post)
admin.site.register(Comment)

# Register your models here.
