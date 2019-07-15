from django.contrib import admin
from .models import Post, Comment
from .models import Post

admin.site.register(Post) #This is for making our model visible on the admin page
admin.site.register(Comment)
