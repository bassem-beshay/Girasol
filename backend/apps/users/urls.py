"""
User URL routes.
"""
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('me/', views.UserProfileView.as_view(), name='profile'),
    path('me/profile/', views.UserProfileUpdateView.as_view(), name='profile-update'),
    path('wishlist/', views.WishlistView.as_view(), name='wishlist'),
    path('wishlist/<int:tour_id>/', views.WishlistDeleteView.as_view(), name='wishlist-delete'),
]
