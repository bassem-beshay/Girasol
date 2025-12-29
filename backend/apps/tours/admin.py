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
    fieldsets = (
        ('Basic', {'fields': ('name', 'slug', 'icon', 'image', 'is_active', 'sort_order')}),
        ('Description', {'fields': ('description', 'description_es', 'description_pt')}),
        ('Translations', {'fields': ('name_es', 'name_pt'), 'classes': ('collapse',)}),
    )


@admin.register(TourType)
class TourTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'sort_order']
    list_editable = ['is_active', 'sort_order']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic', {'fields': ('name', 'slug', 'icon', 'is_active', 'sort_order')}),
        ('Description', {'fields': ('description', 'description_es', 'description_pt')}),
        ('Translations', {'fields': ('name_es', 'name_pt'), 'classes': ('collapse',)}),
    )


class TourImageInline(admin.TabularInline):
    model = TourImage
    extra = 1
    fields = ['image', 'caption', 'caption_es', 'caption_pt', 'alt_text', 'alt_text_es', 'alt_text_pt', 'sort_order']


class TourHighlightInline(admin.StackedInline):
    model = TourHighlight
    extra = 1
    fieldsets = (
        (None, {'fields': ('icon', 'sort_order')}),
        ('Title', {'fields': ('title', 'title_es', 'title_pt')}),
        ('Description', {'fields': ('description', 'description_es', 'description_pt')}),
    )


class TourItineraryInline(admin.StackedInline):
    model = TourItinerary
    extra = 1
    fieldsets = (
        ('Day', {'fields': ('day_number', 'image')}),
        ('Title', {'fields': ('title', 'title_es', 'title_pt')}),
        ('Description', {'fields': ('description', 'description_es', 'description_pt')}),
        ('Locations', {'fields': ('locations', 'locations_es', 'locations_pt')}),
        ('Meals', {'fields': ('meals_included', 'meals_included_es', 'meals_included_pt')}),
        ('Accommodation', {'fields': ('accommodation', 'accommodation_es', 'accommodation_pt')}),
    )


class TourInclusionInline(admin.TabularInline):
    model = TourInclusion
    extra = 2
    fields = ['item', 'item_es', 'item_pt', 'is_included', 'sort_order']


class TourPricingInline(admin.TabularInline):
    model = TourPricing
    extra = 1
    fields = ['season_name', 'season_name_es', 'season_name_pt', 'start_date', 'end_date', 'price_per_person', 'single_supplement']


class TourDepartureInline(admin.TabularInline):
    model = TourDeparture
    extra = 1


class TourFAQInline(admin.StackedInline):
    model = TourFAQ
    extra = 0
    fieldsets = (
        ('Question', {'fields': ('question', 'question_es', 'question_pt')}),
        ('Answer', {'fields': ('answer', 'answer_es', 'answer_pt')}),
        ('Settings', {'fields': ('sort_order',)}),
    )


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
            'fields': ('title', 'title_es', 'title_pt', 'subtitle', 'subtitle_es', 'subtitle_pt', 'description', 'description_es', 'description_pt')
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
            'fields': ('benefits', 'terms_conditions', 'terms_conditions_es', 'terms_conditions_pt', 'cancellation_policy', 'cancellation_policy_es', 'cancellation_policy_pt'),
            'classes': ('collapse',)
        }),
        ('Display Settings', {
            'fields': ('badge_text', 'badge_text_es', 'badge_text_pt', 'banner_image', 'background_color')
        }),
        ('Status', {
            'fields': ('is_active', 'is_featured', 'sort_order')
        }),
        ('Countdown Info (Read Only)', {
            'fields': ('is_currently_active', 'days_remaining', 'hours_remaining', 'minutes_remaining'),
            'classes': ('collapse',)
        }),
    )
