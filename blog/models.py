from django.db import models
#for data
from django.utils import timezone
#for user
from django.contrib.auth.models import User
#here user can post multiple posts
# to create posts redirect path
from django.urls import reverse

# Create your models here.
#adding data to databasess
class Post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)
    # ondelete means on deletion of user what will happen to post(here we deleted the posts by user)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title
    # to create posts(redirect path)

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})

# to upload python manage.py makemigrations
#to see sql code python manage.py sqlmigrate blog 0001
# finally python manage.py migrate

#to access data
#python manage.py shell
#from blog.models import Post
#from django.contrib.auth.models import User
#user.objects.all()
#user.objects.first()  , last()
#user.objects.filter(username='testuser1')
#user=user.objects.filter(username='testuser1').first()
#user.id  , user.pk
#user=user.object.get(id=1)
#post.objects.all()
#post_1=Post(title='Blog 1' ,content='First blog content!',author=user)
#post_1.save()
#exit()
#post=Post.objects.first()
#post.content
#data of user
#post.author.email
#user.post_set.all()
#to create post
#user.post_set.create(title='',  )