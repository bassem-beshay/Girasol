from django.contrib import admin
from .models import (
    TourCategory, TourType, Tour, TourImage, TourHighlight, TourItinerary,
    TourInclusion, TourPricing, TourDeparture, TourFAQ
)


@admin.register(TourCategory)
class TourCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'sort_order']
    list_editable = ['is_active', 'sort_order']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(TourType)
class TourTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'sort_order']
    list_editable = ['is_active', 'sort_order']
    prepopulated_fields = {'slug': ('name',)}


class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1


class TourHighlightInline(admin.TabularInline):
    model = TourHighlight
    extra = 1


class TourItineraryInline(admin.StackedInline):
    model = TourItinerary
    extra = 1


class TourInclusionInline(admin.TabularInline):
    model = TourInclusion
    extra = 2


class TourPricingInline(admin.TabularInline):
    model = TourPricing
    extra = 1


class TourDepartureInline(admin.TabularInline):
    model = TourDeparture
    extra = 1


class TourFAQInline(admin.StackedInline):
    model = TourFAQ
    extra = 0


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'category', 'tour_type', 'days', 'price',
        'is_featured', 'is_best_seller', 'is_published', 'average_rating'
    ]
    list_filter = [
        'category', 'tour_type', 'is_published', 'is_featured',
        'is_best_seller', 'has_discount', 'difficulty_level'
    ]
    search_fields = ['name', 'description', 'short_description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_featured', 'is_best_seller', 'is_published']
    filter_horizontal = ['destinations']
    date_hierarchy = 'created_at'

    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'name_es', 'name_pt', 'slug', 'short_description', 'short_description_es', 'short_description_pt', 'description', 'description_es', 'description_pt')
        }),
        ('Classification', {
            'fields': ('category', 'tour_type', 'destinations')
        }),
        ('Duration', {
            'fields': ('days', 'nights', 'departure_city')
        }),
        ('Pricing', {
            'fields': ('price', 'price_single_supplement', 'child_price', 'currency')
        }),
        ('Group Settings', {
            'fields': ('min_group_size', 'max_group_size')
        }),
        ('Media', {
            'fields': ('featured_image', 'video_url')
        }),
        ('Features', {
            'fields': (
                'is_featured', 'is_best_seller', 'is_new',
                'has_discount', 'discount_percentage',
                'discount_start_date', 'discount_end_date'
            )
        }),
        ('Additional Info', {
            'fields': ('difficulty_level', 'languages')
        }),
        ('Publishing', {
            'fields': ('is_published', 'published_at')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Stats', {
            'fields': ('average_rating', 'review_count'),
            'classes': ('collapse',)
        }),
    )

    inlines = [
        TourImageInline, TourHighlightInline, TourItineraryInline,
        TourInclusionInline, TourPricingInline, TourDepartureInline, TourFAQInline
    ]
