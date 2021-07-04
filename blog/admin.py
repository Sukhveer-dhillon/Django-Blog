from django.contrib import admin

# Register your models here.
#here to post data from admin page to database
from .models import Post
admin.site.register(Post)
