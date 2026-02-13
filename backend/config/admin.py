from django.contrib import admin


class GirasolAdminSite(admin.AdminSite):
    def index(self, request, extra_context=None):
        from apps.tours.models import Tour
        from apps.contact.models import Inquiry, Newsletter
        from apps.blog.models import Post

        extra_context = extra_context or {}
        extra_context['dashboard_stats'] = {
            'total_tours': Tour.objects.count(),
            'total_inquiries': Inquiry.objects.count(),
            'new_inquiries': Inquiry.objects.filter(status='new').count(),
            'total_subscribers': Newsletter.objects.filter(is_confirmed=True).count(),
            'total_posts': Post.objects.count(),
        }
        return super().index(request, extra_context=extra_context)


# Replace the default admin site
admin_site = GirasolAdminSite()
admin.site.__class__ = GirasolAdminSite
