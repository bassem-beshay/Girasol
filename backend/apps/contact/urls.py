"""
Contact URL routes.
"""
from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    # Inquiry
    path('inquiry/', views.InquiryCreateView.as_view(), name='inquiry'),

    # Newsletter - Double Opt-In
    path('newsletter/subscribe/', views.NewsletterSubscribeView.as_view(), name='newsletter-subscribe'),
    path('newsletter/confirm/<uuid:token>/', views.NewsletterConfirmView.as_view(), name='newsletter-confirm'),
    path('newsletter/unsubscribe/', views.NewsletterUnsubscribeView.as_view(), name='newsletter-unsubscribe'),
    path('newsletter/unsubscribe/<uuid:token>/', views.NewsletterUnsubscribeView.as_view(), name='newsletter-unsubscribe-token'),
    path('newsletter/status/', views.NewsletterStatusView.as_view(), name='newsletter-status'),

    # FAQ & Offices
    path('faq/', views.FAQListView.as_view(), name='faq'),
    path('offices/', views.OfficeListView.as_view(), name='offices'),

    # Statistics
    path('statistics/', views.StatisticListView.as_view(), name='statistics'),
]
