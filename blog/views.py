# get object for display posts specific to user
from django.shortcuts import render,get_object_or_404
#import this
from django.http import HttpResponse
#to use data from database
from .models import Post
# create,delete and update posts(class-based views)
from django.views.generic import ListView , DetailView ,CreateView,UpdateView,DeleteView
# login required for class based views and only same author can update the post
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# to display user sprcific posts
from django.contrib.auth.models import User
# Create your views here.


#dynamic data
# posts=[
#     {
#         'author':'coreyMs',
#         'title':'Blog post 1',
#         'content':'first post content',
#         'date_posted':'August 27,2021'
#     },
#      {
#         'author':'Jane doe',
#         'title':'Blog post 2',
#         'content':'second post content',
#         'date_posted':'July 27,2021'
#     },

# ]

def home(request):
    # return HttpResponse('<h2>Blog home</h2>')
    context={
        # 'posts':posts
        #data from database
        'posts':Post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    # return HttpResponse('<h2>Blog About</h2>')
    return render(request,'blog/about.html',{'title':'About'})

# class based views
class PostListView(ListView):
    model=Post
    # blog/post_list.html (it will look for this template)
    template_name='blog/home.html'
    context_object_name='posts'
    # how it will display posts( - for newest to oldest)
    ordering=['-date_posted']   
    # pagination (to view in pages)
    paginate_by=5

# details view of posts
class PostDetailView(DetailView):
    model=Post
    # dont need other things if we follow naming convention

# create of posts by users
class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    # dont need other things if we follow naming convention
    fields=['title','content']
    # author equal to current logged in user
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    # then in models.py add redirect path

# update of posts by users
class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Post
    # dont need other things if we follow naming convention
    fields=['title','content']
    # author equal to current logged in user
    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)
    # then in models.py add redirect path

    # to update post by only that user
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

# to delete posts
class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url='/'
    # to delete post by only that user
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False
   # dont need other things if we follow naming convention

# posts related to specific user
class UserPostListView(ListView):
    model=Post
    # blog/post_list.html (it will look for this template)
    template_name='blog/user_posts.html'
    context_object_name='posts'
    
    # pagination (to view in pages)
    paginate_by=5

    def get_queryset(self):
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
