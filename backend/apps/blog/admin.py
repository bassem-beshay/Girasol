from django.contrib import admin
from .models import Category, Tag, Post, Comment


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'post_count', 'is_active']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['is_active']
    fieldsets = (
        ('Basic', {'fields': ('name', 'slug', 'image', 'is_active')}),
        ('Description', {'fields': ('description', 'description_es', 'description_pt')}),
        ('Translations', {'fields': ('name_es', 'name_pt'), 'classes': ('collapse',)}),
    )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic', {'fields': ('name', 'slug')}),
        ('Translations', {'fields': ('name_es', 'name_pt'), 'classes': ('collapse',)}),
    )


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ['created_at']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'title', 'category', 'author', 'is_published',
        'is_featured', 'view_count', 'published_at'
    ]
    list_filter = ['is_published', 'is_featured', 'category', 'created_at']
    search_fields = ['title', 'excerpt', 'content']
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ['tags', 'related_tours', 'related_destinations']
    date_hierarchy = 'created_at'
    list_editable = ['is_published', 'is_featured']

    fieldsets = (
        ('Content', {
            'fields': ('title', 'title_es', 'title_pt', 'slug', 'excerpt', 'excerpt_es', 'excerpt_pt', 'content', 'content_es', 'content_pt')
        }),
        ('Media', {
            'fields': ('featured_image', 'featured_image_alt', 'featured_image_alt_es', 'featured_image_alt_pt')
        }),
        ('Classification', {
            'fields': ('category', 'tags')
        }),
        ('Author', {
            'fields': ('author', 'author_name')
        }),
        ('Related Content', {
            'fields': ('related_tours', 'related_destinations'),
            'classes': ('collapse',)
        }),
        ('Publishing', {
            'fields': ('is_published', 'published_at', 'is_featured', 'allow_comments')
        }),
        ('SEO', {
            'fields': ('meta_title', 'meta_description', 'meta_keywords'),
            'classes': ('collapse',)
        }),
        ('Stats', {
            'fields': ('view_count', 'reading_time'),
            'classes': ('collapse',)
        }),
    )

    inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'get_author', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'created_at']
    search_fields = ['content', 'name', 'user__email']
    list_editable = ['is_approved']

    def get_author(self, obj):
        return obj.user.email if obj.user else obj.name
    get_author.short_description = 'Author'
