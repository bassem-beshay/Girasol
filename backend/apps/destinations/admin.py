from django.contrib import admin
from .models import Destination, DestinationImage, Activity


class DestinationImageInline(admin.TabularInline):
    model = DestinationImage
    extra = 1


class ActivityInline(admin.TabularInline):
    model = Activity
    extra = 0


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'region', 'is_featured', 'is_active', 'tour_count', 'sort_order']
    list_filter = ['is_featured', 'is_active', 'country']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_featured', 'is_active', 'sort_order']

    fieldsets = (
        (None, {'fields': ('name', 'name_es', 'name_pt', 'slug', 'tagline', 'tagline_es', 'tagline_pt')}),
        ('Content', {'fields': ('description', 'description_es', 'description_pt')}),
        ('Media', {'fields': ('featured_image', 'banner_image', 'video_url')}),
        ('Location', {'fields': ('country', 'region', 'latitude', 'longitude')}),
        ('Travel Info', {'fields': ('best_time_to_visit', 'getting_there', 'climate_info')}),
        ('SEO', {'fields': ('meta_title', 'meta_description', 'meta_keywords'), 'classes': ('collapse',)}),
        ('Settings', {'fields': ('is_featured', 'is_active', 'sort_order')}),
    )

    inlines = [DestinationImageInline, ActivityInline]


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'destination', 'price_from', 'duration', 'sort_order']
    list_filter = ['destination']
    search_fields = ['name', 'description']
