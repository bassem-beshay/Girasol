"""
Blog serializers for API.
"""
from rest_framework import serializers
from .models import Category, Tag, Post, Comment


class CategorySerializer(serializers.ModelSerializer):
    post_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'name_es', 'name_pt', 'slug',
            'description', 'description_es', 'description_pt',
            'image', 'post_count'
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.SerializerMethodField()
    replies = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'author_name', 'content', 'created_at', 'replies']

    def get_author_name(self, obj):
        if obj.user:
            return obj.user.full_name or obj.user.email
        return obj.name

    def get_replies(self, obj):
        if obj.parent is None:
            replies = obj.replies.filter(is_approved=True)
            return CommentSerializer(replies, many=True).data
        return []


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'content', 'parent']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            validated_data['user'] = request.user
            validated_data['is_approved'] = True  # Auto-approve for logged in users
        return super().create(validated_data)


class PostListSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    author_display = serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'title_es', 'title_pt', 'slug',
            'excerpt', 'excerpt_es', 'excerpt_pt', 'featured_image',
            'category', 'author_display', 'published_at',
            'reading_time', 'view_count', 'comment_count', 'is_featured'
        ]

    def get_author_display(self, obj):
        if obj.author_name:
            return obj.author_name
        if obj.author:
            return obj.author.full_name
        return 'Girasol Tours'

    def get_comment_count(self, obj):
        return obj.comments.filter(is_approved=True, parent=None).count()


class PostDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    author_display = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()
    related_posts = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'title_es', 'title_pt', 'slug',
            'excerpt', 'excerpt_es', 'excerpt_pt',
            'content', 'content_es', 'content_pt',
            'featured_image', 'featured_image_alt',
            'category', 'tags', 'author_display',
            'published_at', 'reading_time', 'view_count',
            'comments', 'allow_comments', 'related_posts',
            'meta_title', 'meta_description'
        ]

    def get_author_display(self, obj):
        if obj.author_name:
            return obj.author_name
        if obj.author:
            return obj.author.full_name
        return 'Girasol Tours'

    def get_comments(self, obj):
        comments = obj.comments.filter(is_approved=True, parent=None)
        return CommentSerializer(comments, many=True).data

    def get_related_posts(self, obj):
        related = Post.objects.filter(
            is_published=True,
            category=obj.category
        ).exclude(id=obj.id)[:3]
        return PostListSerializer(related, many=True).data
