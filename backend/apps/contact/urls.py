"""
Contact URL routes.
"""
from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('inquiry/', views.InquiryCreateView.as_view(), name='inquiry'),
    path('newsletter/subscribe/', views.NewsletterSubscribeView.as_view(), name='newsletter-subscribe'),
    path('newsletter/unsubscribe/', views.NewsletterUnsubscribeView.as_view(), name='newsletter-unsubscribe'),
    path('faq/', views.FAQListView.as_view(), name='faq'),
    path('offices/', views.OfficeListView.as_view(), name='offices'),
]
