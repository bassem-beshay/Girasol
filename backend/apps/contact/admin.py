

from django.contrib import admin
from django.utils.html import format_html
from django.urls import path, reverse
from django.shortcuts import redirect
from django.contrib import messages
from .models import Inquiry, InquiryResponse, Newsletter, NewsletterCampaign, FAQ, Office, Statistic


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
        from .emails import send_confirmation_email
        count = 0
        for subscriber in queryset.filter(is_confirmed=False):
            send_confirmation_email(subscriber)
            count += 1
        self.message_user(request, f'Confirmation emails sent to {count} subscribers.')

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
    fieldsets = (
        ('Question', {'fields': ('question', 'question_es', 'question_pt')}),
        ('Answer', {'fields': ('answer', 'answer_es', 'answer_pt')}),
        ('Settings', {'fields': ('category', 'is_active', 'sort_order')}),
    )


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'phone', 'is_headquarters', 'is_active', 'sort_order']
    list_filter = ['is_headquarters', 'is_active']
    list_editable = ['is_active', 'sort_order']
    fieldsets = (
        ('Basic', {'fields': ('name', 'name_es', 'name_pt')}),
        ('Location', {'fields': ('city', 'city_es', 'city_pt', 'address', 'address_es', 'address_pt', 'latitude', 'longitude')}),
        ('Contact', {'fields': ('phone', 'email', 'whatsapp')}),
        ('Hours', {'fields': ('working_hours', 'working_hours_es', 'working_hours_pt')}),
        ('Settings', {'fields': ('is_headquarters', 'is_active', 'sort_order')}),
    )


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
            'fields': ('value', 'label', 'icon')
        }),
        ('Description', {
            'fields': ('description', 'description_es', 'description_pt')
        }),
        ('Translations', {
            'fields': ('label_es', 'label_pt'),
            'classes': ('collapse',)
        }),
        ('Settings', {
            'fields': ('is_active', 'sort_order')
        }),
    )


@admin.register(NewsletterCampaign)
class NewsletterCampaignAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'status', 'recipients_display', 'sent_display', 'created_at', 'send_button']
    list_filter = ['status', 'created_at']
    search_fields = ['title', 'subject']
    readonly_fields = ['status', 'recipients_count', 'sent_count', 'failed_count', 'sent_at', 'created_at', 'updated_at']
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Campaign Info', {
            'fields': ('title', 'subject', 'preview_text')
        }),
        ('Content', {
            'fields': ('content',),
            'description': 'HTML content is supported. Use basic HTML for email compatibility.'
        }),
        ('Status & Stats', {
            'fields': ('status', 'scheduled_at', 'sent_at', 'recipients_count', 'sent_count', 'failed_count'),
            'classes': ('collapse',)
        }),
        ('Metadata', {
            'fields': ('created_by', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def recipients_display(self, obj):
        count = Newsletter.objects.filter(is_active=True, is_confirmed=True).count()
        return f"{count} subscribers"
    recipients_display.short_description = 'Recipients'

    def sent_display(self, obj):
        if obj.sent_count > 0:
            return format_html(
                '<span style="color: green;">{} sent</span> / <span style="color: red;">{} failed</span>',
                obj.sent_count, obj.failed_count
            )
        return '-'
    sent_display.short_description = 'Sent/Failed'

    def send_button(self, obj):
        if obj.status == 'draft':
            url = reverse('admin:contact_newslettercampaign_send', args=[obj.pk])
            return format_html(
                '<a class="button" href="{}" style="background-color: #ea580c; color: white; padding: 5px 10px; border-radius: 4px; text-decoration: none;">Send Now</a>',
                url
            )
        elif obj.status == 'sent':
            return format_html('<span style="color: green;">✓ Sent</span>')
        elif obj.status == 'sending':
            return format_html('<span style="color: orange;">⏳ Sending...</span>')
        return '-'
    send_button.short_description = 'Action'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:campaign_id>/send/', self.admin_site.admin_view(self.send_campaign), name='contact_newslettercampaign_send'),
        ]
        return custom_urls + urls

    def send_campaign(self, request, campaign_id):
        from django.core.mail import send_mail
        from django.template.loader import render_to_string
        from django.conf import settings
        from django.utils import timezone

        campaign = NewsletterCampaign.objects.get(pk=campaign_id)

        if campaign.status != 'draft':
            messages.error(request, 'This campaign has already been sent or is currently sending.')
            return redirect('admin:contact_newslettercampaign_changelist')

        # Get active subscribers
        subscribers = Newsletter.objects.filter(is_active=True, is_confirmed=True)
        campaign.recipients_count = subscribers.count()
        campaign.status = 'sending'
        campaign.save()

        sent_count = 0
        failed_count = 0

        for subscriber in subscribers:
            try:
                # Render email content
                html_content = render_to_string('emails/newsletter_campaign.html', {
                    'name': subscriber.name,
                    'content': campaign.content,
                    'subject': campaign.subject,
                    'preview_text': campaign.preview_text,
                    'unsubscribe_url': f"{settings.FRONTEND_URL}/newsletter/unsubscribe/{subscriber.unsubscribe_token}/",
                    'website_url': settings.FRONTEND_URL,
                })

                send_mail(
                    subject=campaign.subject,
                    message='',  # Plain text fallback
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[subscriber.email],
                    html_message=html_content,
                    fail_silently=False,
                )
                sent_count += 1

                # Update subscriber stats
                subscriber.emails_sent += 1
                subscriber.last_email_sent_at = timezone.now()
                subscriber.save(update_fields=['emails_sent', 'last_email_sent_at'])

            except Exception as e:
                failed_count += 1
                import logging
                logger = logging.getLogger(__name__)
                logger.error(f"Failed to send to {subscriber.email}: {e}")

        # Update campaign stats
        campaign.sent_count = sent_count
        campaign.failed_count = failed_count
        campaign.status = 'sent'
        campaign.sent_at = timezone.now()
        campaign.save()

        messages.success(request, f'Campaign sent successfully! {sent_count} emails sent, {failed_count} failed.')
        return redirect('admin:contact_newslettercampaign_changelist')

    def save_model(self, request, obj, form, change):
        if not change:  # New campaign
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
