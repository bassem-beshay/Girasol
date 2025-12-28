

from django.contrib import admin
from .models import Inquiry, InquiryResponse, Newsletter, FAQ, Office, Statistic


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
    list_display = ['email', 'name', 'is_confirmed', 'is_active', 'source', 'subscribed_at', 'confirmed_at']
    list_filter = ['is_confirmed', 'is_active', 'source', 'subscribed_at']
    search_fields = ['email', 'name']
    list_editable = ['is_active']
    readonly_fields = ['confirmation_token', 'unsubscribe_token', 'confirmed_at', 'confirmation_sent_at', 'emails_sent', 'last_email_sent_at']
    date_hierarchy = 'subscribed_at'

    fieldsets = (
        ('Subscriber Info', {
            'fields': ('email', 'name', 'interests', 'source')
        }),
        ('Status', {
            'fields': ('is_active', 'is_confirmed', 'confirmed_at', 'unsubscribed_at')
        }),
        ('Tokens (Read-only)', {
            'fields': ('confirmation_token', 'unsubscribe_token', 'confirmation_sent_at'),
            'classes': ('collapse',)
        }),
        ('Email Stats', {
            'fields': ('emails_sent', 'last_email_sent_at'),
            'classes': ('collapse',)
        }),
    )

    actions = ['resend_confirmation', 'mark_as_confirmed']

    @admin.action(description='Resend confirmation email')
    def resend_confirmation(self, request, queryset):
        from .tasks import send_confirmation_email_task
        count = 0
        for subscriber in queryset.filter(is_confirmed=False):
            send_confirmation_email_task.delay(subscriber.id)
            count += 1
        self.message_user(request, f'Confirmation emails queued for {count} subscribers.')

    @admin.action(description='Mark as confirmed (manual)')
    def mark_as_confirmed(self, request, queryset):
        from django.utils import timezone
        updated = queryset.filter(is_confirmed=False).update(
            is_confirmed=True,
            confirmed_at=timezone.now()
        )
        self.message_user(request, f'{updated} subscribers marked as confirmed.')


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


@admin.register(Statistic)
class StatisticAdmin(admin.ModelAdmin):
    list_display = ['id', 'value', 'label', 'is_active', 'sort_order']
    list_display_links = ['id']
    list_filter = ['is_active']
    list_editable = ['value', 'label', 'is_active', 'sort_order']
    search_fields = ['label', 'value']
    ordering = ['sort_order']

    fieldsets = (
        (None, {
            'fields': ('value', 'label', 'description')
        }),
        ('Translations', {
            'fields': ('label_es', 'label_pt'),
            'classes': ('collapse',)
        }),
        ('Settings', {
            'fields': ('is_active', 'sort_order')
        }),
    )
