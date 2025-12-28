from django.contrib import admin
from .models import (
    TourCategory, TourType, Tour, TourImage, TourHighlight, TourItinerary,
    TourInclusion, TourPricing, TourDeparture, TourFAQ, EarlyBookingOffer
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
        'is_featured', 'is_best_seller', 'is_multi_destination', 'is_published', 'average_rating'
    ]
    list_filter = [
        'category', 'tour_type', 'is_published', 'is_featured',
        'is_best_seller', 'is_multi_destination', 'has_discount', 'difficulty_level'
    ]
    search_fields = ['name', 'description', 'short_description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_featured', 'is_best_seller', 'is_multi_destination', 'is_published']
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
                'is_featured', 'is_best_seller', 'is_new', 'is_multi_destination',
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


@admin.register(EarlyBookingOffer)
class EarlyBookingOfferAdmin(admin.ModelAdmin):
    """
    Admin for Early Booking Offers (الحجز المبكر)
    """
    list_display = [
        'title', 'discount_percentage', 'offer_end_date',
        'is_currently_active', 'is_featured', 'is_active', 'sort_order'
    ]
    list_display_links = ['title']
    list_filter = ['is_active', 'is_featured', 'offer_start_date', 'offer_end_date']
    list_editable = ['is_featured', 'is_active', 'sort_order']
    search_fields = ['title', 'subtitle', 'description']
    filter_horizontal = ['tours']
    date_hierarchy = 'offer_start_date'
    readonly_fields = ['is_currently_active', 'days_remaining', 'hours_remaining', 'minutes_remaining']

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'title_ar', 'subtitle', 'subtitle_ar', 'description', 'description_ar')
        }),
        ('Discount Settings', {
            'fields': ('discount_percentage', 'min_days_advance')
        }),
        ('Offer Period (When customers can book)', {
            'fields': ('offer_start_date', 'offer_end_date'),
            'description': 'The period during which customers can take advantage of this early booking offer'
        }),
        ('Travel Period (When customers can travel)', {
            'fields': ('travel_start_date', 'travel_end_date'),
            'description': 'The period during which travel must occur to qualify for this offer'
        }),
        ('Tours Included', {
            'fields': ('tours',),
            'description': 'Select which tours are included in this early booking offer'
        }),
        ('Benefits & Terms', {
            'fields': ('benefits', 'terms_conditions', 'cancellation_policy'),
            'classes': ('collapse',)
        }),
        ('Display Settings', {
            'fields': ('badge_text', 'banner_image', 'background_color')
        }),
        ('Status', {
            'fields': ('is_active', 'is_featured', 'sort_order')
        }),
        ('Countdown Info (Read Only)', {
            'fields': ('is_currently_active', 'days_remaining', 'hours_remaining', 'minutes_remaining'),
            'classes': ('collapse',)
        }),
    )
