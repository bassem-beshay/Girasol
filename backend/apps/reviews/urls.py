"""
Review URL routes.
"""
from django.urls import path
from . import views

app_name = 'reviews'

urlpatterns = [
    path('', views.ReviewListView.as_view(), name='list'),
    path('create/', views.ReviewCreateView.as_view(), name='create'),
    path('featured/', views.FeaturedReviewsView.as_view(), name='featured'),
    path('tour/<slug:tour_slug>/', views.TourReviewsView.as_view(), name='tour-reviews'),
    path('testimonials/', views.TestimonialListView.as_view(), name='testimonials'),
]
