"""
Blog views for API.
"""
from rest_framework import generics, filters, permissions
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Tag, Post, Comment
from .serializers import (
    CategorySerializer, TagSerializer,
    PostListSerializer, PostDetailSerializer,
    CommentCreateSerializer
)


class CategoryListView(generics.ListAPIView):
    """List all blog categories."""
    serializer_class = CategorySerializer
    queryset = Category.objects.filter(is_active=True)


class TagListView(generics.ListAPIView):
    """List all tags."""
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class PostListView(generics.ListAPIView):
    """List published blog posts."""
    serializer_class = PostListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category__slug', 'is_featured']
    search_fields = ['title', 'excerpt', 'content']
    ordering_fields = ['published_at', 'view_count']
    ordering = ['-published_at']

    def get_queryset(self):
        queryset = Post.objects.filter(is_published=True).select_related('category')

        # Filter by tag
        tag_slug = self.request.query_params.get('tag')
        if tag_slug:
            queryset = queryset.filter(tags__slug=tag_slug)

        return queryset


class PostDetailView(generics.RetrieveAPIView):
    """Get blog post details."""
    serializer_class = PostDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related(
            'category', 'author'
        ).prefetch_related('tags', 'comments')

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        # Increment view count
        post = self.get_object()
        post.increment_views()
        return response


class FeaturedPostsView(generics.ListAPIView):
    """List featured blog posts."""
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(
            is_published=True, is_featured=True
        ).select_related('category')[:5]


class LatestPostsView(generics.ListAPIView):
    """List latest blog posts for homepage."""
    serializer_class = PostListSerializer

    def get_queryset(self):
        return Post.objects.filter(
            is_published=True
        ).select_related('category')[:3]


class CommentCreateView(generics.CreateAPIView):
    """Create a comment on a blog post."""
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.AllowAny]
