'use client';

import { useMemo } from 'react';
import { useQuery } from '@tanstack/react-query';
import { blogApi } from '@/lib/api';
import { useParams } from 'next/navigation';
import Link from 'next/link';
import Image from 'next/image';
import { motion } from 'framer-motion';
import DOMPurify from 'dompurify';
import {
  Calendar,
  Clock,
  User,
  Tag,
  ArrowLeft,
  Share2,
  Facebook,
  Twitter,
  Linkedin,
  BookOpen,
  ChevronRight,
  Eye,
} from 'lucide-react';

interface BlogCategory {
  id: number;
  name: string;
  slug: string;
}

interface BlogTag {
  id: number;
  name: string;
  slug: string;
}

interface BlogPost {
  id: number;
  title: string;
  slug: string;
  excerpt: string;
  content: string;
  featured_image: string | null;
  category: BlogCategory | null;
  author_name: string;
  published_date: string;
  reading_time: number;
  is_featured: boolean;
  view_count: number;
  tags: BlogTag[];
}

interface RelatedPostsResponse {
  results: BlogPost[];
}

export default function BlogPostPage() {
  const params = useParams();
  const slug = params.slug as string;

  const { data: post, isLoading, error } = useQuery<BlogPost>({
    queryKey: ['blog-post', slug],
    queryFn: async () => {
      const response = await blogApi.getPost(slug);
      return response.data;
    },
    enabled: !!slug,
  });

  // Fetch related posts (latest posts for now)
  const { data: relatedData } = useQuery<RelatedPostsResponse>({
    queryKey: ['blog-latest'],
    queryFn: async () => {
      const response = await blogApi.getLatest();
      return response.data;
    },
  });

  const relatedPosts = relatedData?.results?.filter(p => p.slug !== slug).slice(0, 3) || [];

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });
  };

  const shareUrl = typeof window !== 'undefined' ? window.location.href : '';

  // Sanitize HTML content to prevent XSS attacks
  const sanitizedContent = useMemo(() => {
    if (!post?.content || typeof window === 'undefined') return '';
    return DOMPurify.sanitize(post.content, {
      ALLOWED_TAGS: [
        'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
        'p', 'br', 'hr',
        'ul', 'ol', 'li',
        'strong', 'em', 'b', 'i', 'u', 's',
        'a', 'img',
        'blockquote', 'pre', 'code',
        'table', 'thead', 'tbody', 'tr', 'th', 'td',
        'div', 'span',
        'figure', 'figcaption',
      ],
      ALLOWED_ATTR: [
        'href', 'src', 'alt', 'title', 'class', 'id',
        'target', 'rel', 'width', 'height',
      ],
      ALLOW_DATA_ATTR: false,
      ADD_ATTR: ['target'],
      FORBID_TAGS: ['script', 'style', 'iframe', 'form', 'input', 'button'],
      FORBID_ATTR: ['onerror', 'onload', 'onclick', 'onmouseover'],
    });
  }, [post?.content]);

  if (isLoading) {
    return (
      <div className="min-h-screen pt-32 pb-16">
        <div className="container-custom">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500 mx-auto"></div>
            <p className="mt-4 text-gray-600">Loading article...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error || !post) {
    return (
      <div className="min-h-screen pt-32 pb-16">
        <div className="container-custom">
          <div className="text-center">
            <BookOpen className="w-16 h-16 text-gray-300 mx-auto mb-4" />
            <h1 className="text-2xl font-bold text-gray-900 mb-4">Article Not Found</h1>
            <p className="text-gray-600 mb-8">The article you&apos;re looking for doesn&apos;t exist.</p>
            <Link href="/blog" className="btn btn-primary btn-md">
              Back to Blog
            </Link>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[60vh] min-h-[500px]">
        <div className="absolute inset-0 bg-black/50 z-10" />
        {post.featured_image ? (
          <Image
            src={post.featured_image}
            alt={post.title}
            fill
            className="object-cover"
            priority
          />
        ) : (
          <div className="w-full h-full bg-gradient-to-br from-primary-500 to-primary-700" />
        )}

        <div className="absolute inset-0 z-20 flex items-end">
          <div className="container-custom pb-12">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
              className="max-w-4xl"
            >
              {/* Back Link */}
              <Link
                href="/blog"
                className="inline-flex items-center gap-2 text-white/80 hover:text-white mb-6 transition-colors"
              >
                <ArrowLeft className="w-4 h-4" />
                Back to Blog
              </Link>

              {/* Category */}
              {post.category && (
                <Link
                  href={`/blog?category=${post.category.slug}`}
                  className="inline-block bg-primary-500 text-white px-4 py-1 rounded-full text-sm font-medium mb-4 hover:bg-primary-600 transition-colors"
                >
                  {post.category.name}
                </Link>
              )}

              <h1 className="text-4xl md:text-5xl font-display font-bold text-white mb-6">
                {post.title}
              </h1>

              <div className="flex flex-wrap items-center gap-6 text-white/90">
                <div className="flex items-center gap-2">
                  <User className="w-5 h-5" />
                  <span>{post.author_name}</span>
                </div>
                <div className="flex items-center gap-2">
                  <Calendar className="w-5 h-5" />
                  <span>{formatDate(post.published_date)}</span>
                </div>
                <div className="flex items-center gap-2">
                  <Clock className="w-5 h-5" />
                  <span>{post.reading_time} min read</span>
                </div>
                <div className="flex items-center gap-2">
                  <Eye className="w-5 h-5" />
                  <span>{post.view_count} views</span>
                </div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Main Content */}
      <section className="py-12">
        <div className="container-custom">
          <div className="grid lg:grid-cols-4 gap-8">
            {/* Article Content */}
            <article className="lg:col-span-3">
              <div className="bg-white rounded-2xl p-8 shadow-md">
                {/* Excerpt */}
                <p className="text-xl text-gray-600 leading-relaxed mb-8 pb-8 border-b">
                  {post.excerpt}
                </p>

                {/* Content - Sanitized to prevent XSS */}
                <div
                  className="prose prose-lg max-w-none prose-headings:font-display prose-headings:text-gray-900 prose-p:text-gray-600 prose-a:text-primary-600 prose-a:no-underline hover:prose-a:underline prose-img:rounded-xl"
                  dangerouslySetInnerHTML={{ __html: sanitizedContent }}
                />

                {/* Tags */}
                {post.tags && post.tags.length > 0 && (
                  <div className="mt-8 pt-8 border-t">
                    <div className="flex items-center gap-3 flex-wrap">
                      <Tag className="w-5 h-5 text-gray-400" />
                      {post.tags.map((tag) => (
                        <Link
                          key={tag.id}
                          href={`/blog?tag=${tag.slug}`}
                          className="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-sm hover:bg-primary-100 hover:text-primary-700 transition-colors"
                        >
                          {tag.name}
                        </Link>
                      ))}
                    </div>
                  </div>
                )}

                {/* Share */}
                <div className="mt-8 pt-8 border-t">
                  <div className="flex items-center gap-4">
                    <span className="text-gray-600 font-medium flex items-center gap-2">
                      <Share2 className="w-5 h-5" />
                      Share this article:
                    </span>
                    <div className="flex gap-2">
                      <a
                        href={`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(shareUrl)}`}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="w-10 h-10 rounded-full bg-blue-600 text-white flex items-center justify-center hover:bg-blue-700 transition-colors"
                      >
                        <Facebook className="w-5 h-5" />
                      </a>
                      <a
                        href={`https://twitter.com/intent/tweet?url=${encodeURIComponent(shareUrl)}&text=${encodeURIComponent(post.title)}`}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="w-10 h-10 rounded-full bg-sky-500 text-white flex items-center justify-center hover:bg-sky-600 transition-colors"
                      >
                        <Twitter className="w-5 h-5" />
                      </a>
                      <a
                        href={`https://www.linkedin.com/shareArticle?mini=true&url=${encodeURIComponent(shareUrl)}&title=${encodeURIComponent(post.title)}`}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="w-10 h-10 rounded-full bg-blue-700 text-white flex items-center justify-center hover:bg-blue-800 transition-colors"
                      >
                        <Linkedin className="w-5 h-5" />
                      </a>
                    </div>
                  </div>
                </div>
              </div>
            </article>

            {/* Sidebar */}
            <aside className="lg:col-span-1 space-y-8">
              {/* Author Card */}
              <div className="bg-white rounded-2xl p-6 shadow-md text-center">
                <div className="w-20 h-20 rounded-full bg-gradient-to-br from-primary-400 to-primary-600 mx-auto mb-4 flex items-center justify-center text-white text-2xl font-bold">
                  {post.author_name?.charAt(0) || 'A'}
                </div>
                <h3 className="text-lg font-bold text-gray-900 mb-1">{post.author_name || 'Anonymous'}</h3>
                <p className="text-gray-500 text-sm mb-4">Travel Writer</p>
                <p className="text-gray-600 text-sm">
                  Sharing stories and tips about Egypt&apos;s amazing destinations.
                </p>
              </div>

              {/* Related Posts */}
              {relatedPosts.length > 0 && (
                <div className="bg-white rounded-2xl p-6 shadow-md">
                  <h3 className="text-lg font-bold text-gray-900 mb-4">Related Articles</h3>
                  <div className="space-y-4">
                    {relatedPosts.map((relatedPost) => (
                      <Link
                        key={relatedPost.id}
                        href={`/blog/${relatedPost.slug}`}
                        className="flex gap-4 group"
                      >
                        <div className="w-20 h-20 rounded-lg bg-primary-100 flex items-center justify-center flex-shrink-0 overflow-hidden">
                          {relatedPost.featured_image ? (
                            <Image
                              src={relatedPost.featured_image}
                              alt={relatedPost.title}
                              width={80}
                              height={80}
                              className="w-full h-full object-cover"
                            />
                          ) : (
                            <BookOpen className="w-8 h-8 text-primary-400" />
                          )}
                        </div>
                        <div className="flex-1">
                          <h4 className="text-sm font-semibold text-gray-900 line-clamp-2 group-hover:text-primary-600 transition-colors">
                            {relatedPost.title}
                          </h4>
                          <p className="text-xs text-gray-500 mt-1">
                            {formatDate(relatedPost.published_date)}
                          </p>
                        </div>
                      </Link>
                    ))}
                  </div>
                </div>
              )}

              {/* CTA */}
              <div className="bg-gradient-to-br from-primary-500 to-primary-600 rounded-2xl p-6 text-white">
                <h3 className="text-lg font-bold mb-2">Plan Your Trip</h3>
                <p className="text-white/80 text-sm mb-4">
                  Ready to experience Egypt? Browse our tours and start your adventure.
                </p>
                <Link
                  href="/tours"
                  className="block w-full py-3 bg-white text-primary-600 rounded-xl font-semibold text-center hover:bg-gray-100 transition-colors"
                >
                  Explore Tours
                </Link>
              </div>
            </aside>
          </div>
        </div>
      </section>

      {/* More Articles */}
      {relatedPosts.length > 0 && (
        <section className="py-16 bg-gray-50">
          <div className="container-custom">
            <div className="flex items-center justify-between mb-8">
              <h2 className="text-2xl font-display font-bold text-gray-900">More Articles</h2>
              <Link
                href="/blog"
                className="text-primary-600 font-medium flex items-center gap-1 hover:gap-2 transition-all"
              >
                View All
                <ChevronRight className="w-4 h-4" />
              </Link>
            </div>

            <div className="grid md:grid-cols-3 gap-8">
              {relatedPosts.map((relatedPost, index) => (
                <motion.article
                  key={relatedPost.id}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  className="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition-shadow group"
                >
                  <Link href={`/blog/${relatedPost.slug}`}>
                    <div className="relative h-48">
                      {relatedPost.featured_image ? (
                        <Image
                          src={relatedPost.featured_image}
                          alt={relatedPost.title}
                          fill
                          className="object-cover group-hover:scale-105 transition-transform duration-300"
                        />
                      ) : (
                        <div className="w-full h-full bg-primary-500 flex items-center justify-center">
                          <BookOpen className="w-12 h-12 text-white/30" />
                        </div>
                      )}
                      {relatedPost.category && (
                        <div className="absolute top-4 left-4">
                          <span className="bg-white/90 backdrop-blur-sm text-primary-600 px-3 py-1 rounded-full text-sm font-medium">
                            {relatedPost.category.name}
                          </span>
                        </div>
                      )}
                    </div>
                    <div className="p-6">
                      <div className="flex items-center gap-4 text-sm text-gray-500 mb-3">
                        <span className="flex items-center gap-1">
                          <Calendar className="w-4 h-4" />
                          {formatDate(relatedPost.published_date)}
                        </span>
                        <span className="flex items-center gap-1">
                          <Clock className="w-4 h-4" />
                          {relatedPost.reading_time} min
                        </span>
                      </div>
                      <h3 className="text-lg font-bold text-gray-900 group-hover:text-primary-600 transition-colors line-clamp-2">
                        {relatedPost.title}
                      </h3>
                    </div>
                  </Link>
                </motion.article>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-r from-primary-600 to-secondary-500">
        <div className="container-custom text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-4xl font-display font-bold text-white mb-6">
              Ready to Experience Egypt?
            </h2>
            <p className="text-xl text-white/90 mb-8 max-w-2xl mx-auto">
              Turn your travel dreams into reality. Browse our tours and start planning your
              unforgettable Egyptian adventure today.
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <Link href="/tours" className="btn bg-white text-primary-600 hover:bg-gray-100 btn-lg">
                Explore Tours
              </Link>
              <Link href="/contact" className="btn btn-outline border-white text-white hover:bg-white/10 btn-lg">
                Contact Us
              </Link>
            </div>
          </motion.div>
        </div>
      </section>
    </div>
  );
}
