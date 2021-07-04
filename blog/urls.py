from django.contrib import admin
from django.urls import path
#import this( . means current directory)
from . import views
#how to use class based views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserPostListView

urlpatterns = [
    # path('', views.home,name='blog-home'),
    path('about/', views.about,name='blog-about'),
    # class based view
    path('', PostListView.as_view(),name='blog-home'),
    # url with variables
    path('post/<int:pk>/', PostDetailView.as_view(),name='post-detail'),
    # post create view
    path('post/new/', PostCreateView.as_view(),name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),name='post-delete'),
    path('user/<str:username>/', UserPostListView.as_view(),name='user-posts'),

]