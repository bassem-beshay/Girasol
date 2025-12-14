"""
Destination URL routes.
"""
from django.urls import path
from . import views

app_name = 'destinations'

urlpatterns = [
    path('', views.DestinationListView.as_view(), name='list'),
    path('featured/', views.FeaturedDestinationsView.as_view(), name='featured'),
    path('<slug:slug>/', views.DestinationDetailView.as_view(), name='detail'),
]
