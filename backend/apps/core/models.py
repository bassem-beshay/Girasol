"""
Core models - Abstract base models for the project.
"""
from django.db import models
from django.utils.text import slugify
import uuid


class TimeStampedModel(models.Model):
    """Abstract model with created and updated timestamps."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """Abstract model with UUID primary key."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class SluggedModel(models.Model):
    """Abstract model with auto-generated slug."""
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def generate_unique_slug(self):
        """Generate a unique slug from the model's name field."""
        base_slug = slugify(self.get_slug_source())
        slug = base_slug
        counter = 1
        model_class = self.__class__
        while model_class.objects.filter(slug=slug).exclude(pk=self.pk).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        return slug

    def get_slug_source(self):
        """Override this method to specify the field used for slug generation."""
        return getattr(self, 'name', str(self.pk))


class PublishableModel(models.Model):
    """Abstract model for content that can be published/unpublished."""
    is_published = models.BooleanField(default=False)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True


class SEOModel(models.Model):
    """Abstract model for SEO fields."""
    meta_title = models.CharField(max_length=70, blank=True)
    meta_title_es = models.CharField('Meta Title (Spanish)', max_length=70, blank=True)
    meta_title_pt = models.CharField('Meta Title (Portuguese)', max_length=70, blank=True)
    meta_description = models.CharField(max_length=160, blank=True)
    meta_description_es = models.CharField('Meta Description (Spanish)', max_length=160, blank=True)
    meta_description_pt = models.CharField('Meta Description (Portuguese)', max_length=160, blank=True)
    focus_keyphrase = models.CharField('Focus Key Phrase', max_length=255, blank=True,
        help_text='Main keyword to rank for. Place in H1, URL, Meta Title, first 100 words.')
    focus_keyphrase_es = models.CharField('Focus Key Phrase (Spanish)', max_length=255, blank=True)
    focus_keyphrase_pt = models.CharField('Focus Key Phrase (Portuguese)', max_length=255, blank=True)
    semantic_keywords = models.TextField('Semantic Keywords', blank=True,
        help_text='5-10 related terms, comma-separated. E.g.: Valley of the Kings, Karnak Temple, 5 star Nile cruise')
    semantic_keywords_es = models.TextField('Semantic Keywords (Spanish)', blank=True)
    semantic_keywords_pt = models.TextField('Semantic Keywords (Portuguese)', blank=True)
    lsi_keywords = models.TextField('LSI Keywords', blank=True,
        help_text='Synonyms and variations, comma-separated. E.g.: Egypt package, Nile trip, Cairo Luxor tour')
    lsi_keywords_es = models.TextField('LSI Keywords (Spanish)', blank=True)
    lsi_keywords_pt = models.TextField('LSI Keywords (Portuguese)', blank=True)
    long_tail_phrases = models.TextField('Long Tail Phrases', blank=True,
        help_text='Specific search queries, one per line. E.g.: How much does the Nile Splendor 8 day tour cost?')
    long_tail_phrases_es = models.TextField('Long Tail Phrases (Spanish)', blank=True)
    long_tail_phrases_pt = models.TextField('Long Tail Phrases (Portuguese)', blank=True)

    class Meta:
        abstract = True


class SortableModel(models.Model):
    """Abstract model for sortable items."""
    sort_order = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ['sort_order']
