ssh-keygen -t rsa -b 4096 -f "$env:USERPROFILE\.ssh\id_rsa" -C "you@example.com"ssh-keygen -t rsa -b 4096 -f "$env:USERPROFILE\.ssh\id_rsa" -C "you@example.com"ssh-keygen -t rsa -b 4096 -f "$env:USERPROFILE\.ssh\id_rsa" -C "you@example.com"from django.contrib import admin
from .models import Inquiry, InquiryResponse, Newsletter, FAQ, Office


class InquiryResponseInline(admin.StackedInline):
    model = InquiryResponse
    extra = 1


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'email', 'inquiry_type', 'status',
        'assigned_to', 'created_at'
    ]
    list_filter = ['inquiry_type', 'status', 'created_at']
    search_fields = ['name', 'email', 'message', 'subject']
    list_editable = ['status']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Contact Info', {
            'fields': ('name', 'email', 'phone', 'country')
        }),
        ('Inquiry', {
            'fields': ('inquiry_type', 'subject', 'message', 'tour')
        }),
        ('Travel Details', {
            'fields': ('travel_date', 'travelers', 'budget'),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('status', 'assigned_to', 'internal_notes')
        }),
        ('Source Tracking', {
            'fields': ('source', 'utm_source', 'utm_medium', 'utm_campaign'),
            'classes': ('collapse',)
        }),
    )

    inlines = [InquiryResponseInline]


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'is_active', 'source', 'subscribed_at']
    list_filter = ['is_active', 'source', 'subscribed_at']
    search_fields = ['email', 'name']
    list_editable = ['is_active']


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ['question', 'category', 'is_active', 'sort_order']
    list_filter = ['category', 'is_active']
    search_fields = ['question', 'answer']
    list_editable = ['is_active', 'sort_order']


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'phone', 'is_headquarters', 'is_active', 'sort_order']
    list_filter = ['is_headquarters', 'is_active']
    list_editable = ['is_active', 'sort_order']
