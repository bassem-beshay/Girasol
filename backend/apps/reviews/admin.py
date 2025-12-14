from django.contrib import admin
from .models import Review, ReviewImage, Testimonial


class ReviewImageInline(admin.TabularInline):
    model = ReviewImage
    extra = 1


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = [
        'reviewer_name', 'tour', 'rating', 'is_verified',
        'is_approved', 'is_featured', 'created_at'
    ]
    list_filter = ['rating', 'is_verified', 'is_approved', 'is_featured', 'created_at']
    search_fields = ['reviewer_name', 'content', 'tour__name']
    list_editable = ['is_approved', 'is_featured']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Reviewer', {
            'fields': ('user', 'reviewer_name', 'reviewer_country', 'reviewer_avatar')
        }),
        ('Review', {
            'fields': ('tour', 'booking', 'rating', 'title', 'content', 'travel_date')
        }),
        ('Status', {
            'fields': ('is_verified', 'is_approved', 'is_featured')
        }),
        ('Admin Response', {
            'fields': ('admin_response', 'admin_response_at'),
            'classes': ('collapse',)
        }),
    )

    inlines = [ReviewImageInline]


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'rating', 'tour', 'is_active', 'sort_order']
    list_filter = ['is_active', 'rating']
    search_fields = ['name', 'quote']
    list_editable = ['is_active', 'sort_order']
