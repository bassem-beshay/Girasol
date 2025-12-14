"""
Tour URL routes.
"""
from django.urls import path
from . import views

app_name = 'tours'

urlpatterns = [
    # Main listings
    path('', views.TourListView.as_view(), name='list'),
    path('featured/', views.FeaturedToursView.as_view(), name='featured'),
    path('popular/', views.PopularToursView.as_view(), name='popular'),
    path('search/', views.TourSearchView.as_view(), name='search'),

    # Categories
    path('categories/', views.TourCategoryListView.as_view(), name='categories'),
    path('category/<slug:category_slug>/', views.ToursByCategoryView.as_view(), name='by-category'),

    # By destination
    path('destination/<slug:destination_slug>/', views.ToursByDestinationView.as_view(), name='by-destination'),

    # Tour detail and related
    path('<slug:slug>/', views.TourDetailView.as_view(), name='detail'),
    path('<slug:slug>/related/', views.RelatedToursView.as_view(), name='related'),
    path('<slug:slug>/departures/', views.TourDeparturesView.as_view(), name='departures'),
]
