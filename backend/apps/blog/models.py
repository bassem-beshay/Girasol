"""
Blog models for Girasol Tours.
"""
from django.db import models
from django.conf import settings
from apps.core.models import TimeStampedModel, SluggedModel, SEOModel, PublishableModel


class Category(TimeStampedModel, SluggedModel):
    """Blog category."""

    name = models.CharField(max_length=100)
    name_es = models.CharField('Name (Spanish)', max_length=100, blank=True)
    name_pt = models.CharField('Name (Portuguese)', max_length=100, blank=True)
    description = models.TextField(blank=True)
    description_es = models.TextField('Description (Spanish)', blank=True)
    description_pt = models.TextField('Description (Portuguese)', blank=True)
    image = models.ImageField(upload_to='blog/categories/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_slug_source(self):
        return self.name

    @property
    def post_count(self):
        return self.posts.filter(is_published=True).count()


class Tag(TimeStampedModel, SluggedModel):
    """Blog tag."""

    name = models.CharField(max_length=50)
    name_es = models.CharField('Name (Spanish)', max_length=50, blank=True)
    name_pt = models.CharField('Name (Portuguese)', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_slug_source(self):
        return self.name


class Post(TimeStampedModel, SluggedModel, SEOModel, PublishableModel):
    """Blog post."""

    # Content
    title = models.CharField(max_length=200)
    title_es = models.CharField('Title (Spanish)', max_length=200, blank=True)
    title_pt = models.CharField('Title (Portuguese)', max_length=200, blank=True)
    excerpt = models.TextField(max_length=300)
    excerpt_es = models.TextField('Excerpt (Spanish)', max_length=300, blank=True)
    excerpt_pt = models.TextField('Excerpt (Portuguese)', max_length=300, blank=True)
    content = models.TextField()
    content_es = models.TextField('Content (Spanish)', blank=True)
    content_pt = models.TextField('Content (Portuguese)', blank=True)

    # Media
    featured_image = models.ImageField(upload_to='blog/posts/')
    featured_image_alt = models.CharField(max_length=200, blank=True)
    featured_image_alt_es = models.CharField('Alt Text (Spanish)', max_length=200, blank=True)
    featured_image_alt_pt = models.CharField('Alt Text (Portuguese)', max_length=200, blank=True)

    # Classification
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True, related_name='posts'
    )
    tags = models.ManyToManyField(Tag, blank=True, related_name='posts')

    # Author
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, related_name='blog_posts'
    )
    author_name = models.CharField(max_length=100, blank=True)

    # Related
    related_tours = models.ManyToManyField(
        'tours.Tour', blank=True, related_name='blog_posts'
    )
    related_destinations = models.ManyToManyField(
        'destinations.Destination', blank=True, related_name='blog_posts'
    )

    # Stats
    view_count = models.PositiveIntegerField(default=0)
    reading_time = models.PositiveIntegerField(
        default=5, help_text='Estimated reading time in minutes'
    )

    # Features
    is_featured = models.BooleanField(default=False)
    allow_comments = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published_at', '-created_at']

    def __str__(self):
        return self.title

    def get_slug_source(self):
        return self.title

    def increment_views(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])


class Comment(TimeStampedModel):
    """Blog post comment."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='blog_comments'
    )

    # For non-logged in users
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True)

    content = models.TextField()
    is_approved = models.BooleanField(default=False)

    # Reply
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies'
    )

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ['-created_at']

    def __str__(self):
        author = self.user.email if self.user else self.name
        return f"Comment by {author} on {self.post.title}"
