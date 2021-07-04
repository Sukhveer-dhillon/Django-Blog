from django.contrib import admin

# Register your models here.
#import
from .models import Profile

admin.site.register(Profile)

#now to interact with profile using django shell

# python manage.py shell
# from django.contrib.auth.models import User
# user=User.objects.filter(username='Sukhveer_Singh')
# user.profile
# user.profile.image
# user.profile.image.width
# user.profile.image.url
#exit()