"""
Blog URL routes.
"""
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('posts/featured/', views.FeaturedPostsView.as_view(), name='featured'),
    path('posts/latest/', views.LatestPostsView.as_view(), name='latest'),
    path('posts/<slug:slug>/', views.PostDetailView.as_view(), name='post-detail'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('tags/', views.TagListView.as_view(), name='tags'),
    path('comments/', views.CommentCreateView.as_view(), name='comment-create'),
]
