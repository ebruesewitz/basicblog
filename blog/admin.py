from django.contrib import admin
#import my blog post model in order to register it
from .models import Post
# Register your models here.

# admin will now be able to log in and manage blog posts from admin portal
admin.site.register(Post)
