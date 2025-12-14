'use client';

import { useQuery } from '@tanstack/react-query';
import { blogApi } from '@/lib/api';
import { motion } from 'framer-motion';
import Link from 'next/link';
import Image from 'next/image';
import { ChevronRight, Calendar, Clock, Loader2, BookOpen } from 'lucide-react';
import { formatDate } from '@/lib/utils';

interface BlogCategory {
  id: number;
  name: string;
  slug: string;
}

interface BlogPost {
  id: number;
  title: string;
  slug: string;
  excerpt: string;
  featured_image: string | null;
  category: BlogCategory | null;
  published_date: string;
  reading_time: number;
}

interface BlogResponse {
  count: number;
  results: BlogPost[];
}

export function BlogPreview() {
  const { data, isLoading, error } = useQuery<BlogResponse>({
    queryKey: ['latest-blog'],
    queryFn: async () => {
      const response = await blogApi.getLatest();
      return response.data;
    },
  });

  const blogPosts = data?.results?.slice(0, 3) || [];

  return (
    <section className="section-padding bg-gray-50">
      <div className="container-custom">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-end md:justify-between gap-4 mb-12">
          <div>
            <motion.span
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              className="text-primary-600 font-medium mb-2 block"
            >
              Travel Blog
            </motion.span>
            <motion.h2
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.1 }}
              className="heading-2 text-gray-900"
            >
              Tips, Guides & Stories
            </motion.h2>
          </div>
          <motion.div
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
          >
            <Link
              href="/blog"
              className="inline-flex items-center text-primary-600 font-medium hover:text-primary-700"
            >
              View All Articles
              <ChevronRight className="w-5 h-5 ml-1" />
            </Link>
          </motion.div>
        </div>

        {/* Loading state */}
        {isLoading && (
          <div className="flex items-center justify-center py-16">
            <Loader2 className="w-8 h-8 animate-spin text-primary-500" />
            <span className="ml-3 text-gray-600">Loading articles...</span>
          </div>
        )}

        {/* Error state */}
        {error && (
          <div className="text-center py-16">
            <p className="text-gray-500">Unable to load articles. Please try again later.</p>
          </div>
        )}

        {/* Blog posts grid */}
        {!isLoading && !error && blogPosts.length > 0 && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {blogPosts.map((post, index) => (
              <motion.article
                key={post.id}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
              >
                <Link href={`/blog/${post.slug}`} className="card card-hover block group">
                  {/* Image */}
                  <div className="relative aspect-[16/10] overflow-hidden">
                    {post.featured_image ? (
                      <Image
                        src={post.featured_image}
                        alt={post.title}
                        fill
                        className="object-cover transition-transform duration-500 group-hover:scale-110"
                      />
                    ) : (
                      <div className="w-full h-full bg-gradient-to-br from-primary-100 to-primary-200 flex items-center justify-center">
                        <BookOpen className="w-12 h-12 text-primary-400" />
                      </div>
                    )}
                    {post.category && (
                      <div className="absolute top-4 left-4">
                        <span className="badge-primary">{post.category.name}</span>
                      </div>
                    )}
                  </div>

                  {/* Content */}
                  <div className="p-6">
                    {/* Meta */}
                    <div className="flex items-center gap-4 text-sm text-gray-500 mb-3">
                      <span className="flex items-center gap-1">
                        <Calendar className="w-4 h-4" />
                        {formatDate(post.published_date)}
                      </span>
                      <span className="flex items-center gap-1">
                        <Clock className="w-4 h-4" />
                        {post.reading_time} min read
                      </span>
                    </div>

                    {/* Title */}
                    <h3 className="text-lg font-semibold text-gray-900 mb-2 group-hover:text-primary-600 transition-colors line-clamp-2">
                      {post.title}
                    </h3>

                    {/* Excerpt */}
                    <p className="text-gray-600 text-sm line-clamp-2">
                      {post.excerpt}
                    </p>

                    {/* Read more */}
                    <span className="inline-flex items-center text-primary-600 font-medium mt-4 group-hover:translate-x-1 transition-transform">
                      Read More
                      <ChevronRight className="w-4 h-4 ml-1" />
                    </span>
                  </div>
                </Link>
              </motion.article>
            ))}
          </div>
        )}

        {/* Empty state */}
        {!isLoading && !error && blogPosts.length === 0 && (
          <div className="text-center py-16">
            <BookOpen className="w-16 h-16 text-gray-300 mx-auto mb-4" />
            <p className="text-gray-500">No articles available at the moment.</p>
          </div>
        )}
      </div>
    </section>
  );
}
