'use client';

import { useState } from 'react';
import { useQuery, keepPreviousData } from '@tanstack/react-query';
import { blogApi } from '@/lib/api';
import { motion } from 'framer-motion';
import Image from 'next/image';
import Link from 'next/link';
import {
  Calendar,
  Clock,
  User,
  ArrowRight,
  Search,
  Tag,
  TrendingUp,
  BookOpen,
} from 'lucide-react';
import { useLanguageStore } from '@/store/languageStore';
import { blogPageT, t } from '@/lib/translations';
import { RichText } from '@/components/ui/RichText';

interface BlogCategory {
  id: number;
  name: string;
  slug: string;
  post_count: number;
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
  tags: Array<{ id: number; name: string; slug: string }>;
}

interface BlogPostsResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: BlogPost[];
}

interface CategoriesResponse {
  count: number;
  results: BlogCategory[];
}

export default function BlogPage() {
  const { language } = useLanguageStore();
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState('');

  // Fetch blog posts
  const { data: postsData, isLoading: postsLoading, isFetching } = useQuery<BlogPostsResponse>({
    queryKey: ['blog-posts', selectedCategory],
    queryFn: async () => {
      const params: Record<string, unknown> = {};
      if (selectedCategory !== 'all') {
        params.category__slug = selectedCategory;
      }
      const response = await blogApi.getPosts(params);
      return response.data;
    },
    placeholderData: keepPreviousData,
  });

  // Fetch categories
  const { data: categoriesData } = useQuery<CategoriesResponse>({
    queryKey: ['blog-categories'],
    queryFn: async () => {
      const response = await blogApi.getCategories();
      return response.data;
    },
  });

  // Fetch featured posts
  const { data: featuredData } = useQuery<BlogPostsResponse>({
    queryKey: ['blog-featured'],
    queryFn: async () => {
      const response = await blogApi.getFeatured();
      return response.data;
    },
  });

  const posts = postsData?.results || [];
  const categories = categoriesData?.results || [];
  const featuredPosts = featuredData?.results || [];
  const totalPosts = postsData?.count || 0;

  // Filter posts by search query (client-side for simplicity)
  const filteredPosts = posts.filter((post) => {
    if (!searchQuery) return true;
    const query = searchQuery.toLowerCase();
    return (
      post.title.toLowerCase().includes(query) ||
      post.excerpt.toLowerCase().includes(query)
    );
  });

  const formatDate = (dateString: string) => {
    return new Date(dateString).toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric',
    });
  };

  if (postsLoading && !postsData) {
    return (
      <div className="min-h-screen pt-32 pb-16">
        <div className="container-custom">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500 mx-auto"></div>
            <p className="mt-4 text-gray-600">{t(blogPageT, language, 'loadingPosts')}</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[40vh] sm:h-[50vh] md:h-[70vh] lg:h-[85vh] min-h-[250px] sm:min-h-[300px] md:min-h-[450px] lg:min-h-[700px] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-primary-900/90 to-primary-800/80 z-10" />
        <div
          className="absolute inset-0 bg-cover bg-center"
          style={{ backgroundImage: "url('/images/blog-hero.jpg')" }}
        />
        <div className="relative z-20 text-center text-white max-w-4xl mx-auto px-4">
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="text-2xl sm:text-3xl md:text-5xl lg:text-6xl font-display font-bold mb-3 sm:mb-6"
          >
            {t(blogPageT, language, 'travelBlog')}
          </motion.h1>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="text-xl md:text-2xl text-white/90"
          >
            {t(blogPageT, language, 'heroSubtitle')}
          </motion.p>
        </div>
      </section>

      {/* Featured Posts */}
      {featuredPosts.length > 0 && (
        <section className="py-16 bg-white">
          <div className="container-custom">
            <div className="flex items-center gap-3 mb-8">
              <TrendingUp className="w-6 h-6 text-primary-600" />
              <h2 className="text-2xl font-display font-bold text-gray-900">{t(blogPageT, language, 'featuredArticles')}</h2>
            </div>

            <div className="grid md:grid-cols-2 gap-8">
              {featuredPosts.slice(0, 2).map((post, index) => (
                <motion.article
                  key={post.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  className="group relative bg-gray-50 rounded-2xl overflow-hidden hover:shadow-xl transition-shadow"
                >
                  <div className="relative h-64">
                    <div className="absolute inset-0 bg-gradient-to-t from-gray-900/80 via-gray-900/40 to-transparent z-10" />
                    {post.featured_image ? (
                      <Image
                        src={post.featured_image}
                        alt={post.title}
                        fill
                        sizes="(max-width: 768px) 100vw, 50vw"
                        className="object-cover"
                      />
                    ) : (
                      <div className="absolute inset-0 bg-primary-600 flex items-center justify-center">
                        <BookOpen className="w-16 h-16 text-white/30" />
                      </div>
                    )}
                    <div className="absolute top-4 left-4 z-20">
                      <span className="bg-primary-500 text-white px-3 py-1 rounded-full text-sm font-medium">
                        {t(blogPageT, language, 'featured')}
                      </span>
                    </div>
                  </div>
                  <div className="p-6">
                    <div className="flex items-center gap-4 text-sm text-gray-500 mb-3">
                      {post.category && (
                        <span className="flex items-center gap-1">
                          <Tag className="w-4 h-4" />
                          {post.category.name}
                        </span>
                      )}
                      <span className="flex items-center gap-1">
                        <Calendar className="w-4 h-4" />
                        {formatDate(post.published_date)}
                      </span>
                    </div>
                    <h3 className="text-xl font-bold text-gray-900 mb-3 group-hover:text-primary-600 transition-colors">
                      <Link href={`/blog/${post.slug}`}>{post.title}</Link>
                    </h3>
                    <RichText html={post.excerpt} className="rich-text-compact text-gray-600 mb-4 line-clamp-2" />
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2 text-sm text-gray-500">
                        <User className="w-4 h-4" />
                        {post.author_name}
                      </div>
                      <div className="flex items-center gap-2 text-sm text-gray-500">
                        <Clock className="w-4 h-4" />
                        {post.reading_time} {t(blogPageT, language, 'minRead')}
                      </div>
                    </div>
                  </div>
                </motion.article>
              ))}
            </div>
          </div>
        </section>
      )}

      {/* Main Blog Section */}
      <section className="py-16 bg-gray-50">
        <div className="container-custom">
          <div className="grid lg:grid-cols-4 gap-8">
            {/* Sidebar */}
            <aside className="lg:col-span-1 space-y-8">
              {/* Search */}
              <div className="bg-white rounded-2xl p-6 shadow-md">
                <h3 className="text-lg font-bold text-gray-900 mb-4">{t(blogPageT, language, 'search')}</h3>
                <div className="relative">
                  <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                  <input
                    type="text"
                    placeholder={t(blogPageT, language, 'searchPlaceholder')}
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="w-full pl-12 pr-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all"
                  />
                </div>
              </div>

              {/* Categories */}
              <div className="bg-white rounded-2xl p-6 shadow-md">
                <h3 className="text-lg font-bold text-gray-900 mb-4">{t(blogPageT, language, 'categories')}</h3>
                <div className="space-y-2">
                  <button
                    onClick={() => setSelectedCategory('all')}
                    className={`w-full flex items-center justify-between px-4 py-2 rounded-xl transition-colors ${
                      selectedCategory === 'all'
                        ? 'bg-primary-500 text-white'
                        : 'bg-gray-50 text-gray-700 hover:bg-gray-100'
                    }`}
                  >
                    <span>{t(blogPageT, language, 'all')}</span>
                    <span
                      className={`text-sm ${
                        selectedCategory === 'all' ? 'text-white/80' : 'text-gray-400'
                      }`}
                    >
                      ({totalPosts})
                    </span>
                  </button>
                  {categories.map((category) => (
                    <button
                      key={category.id}
                      onClick={() => setSelectedCategory(category.slug)}
                      className={`w-full flex items-center justify-between px-4 py-2 rounded-xl transition-colors ${
                        selectedCategory === category.slug
                          ? 'bg-primary-500 text-white'
                          : 'bg-gray-50 text-gray-700 hover:bg-gray-100'
                      }`}
                    >
                      <span>{category.name}</span>
                      <span
                        className={`text-sm ${
                          selectedCategory === category.slug ? 'text-white/80' : 'text-gray-400'
                        }`}
                      >
                        ({category.post_count})
                      </span>
                    </button>
                  ))}
                </div>
              </div>

              {/* Popular Posts */}
              {featuredPosts.length > 0 && (
                <div className="bg-white rounded-2xl p-6 shadow-md">
                  <h3 className="text-lg font-bold text-gray-900 mb-4">{t(blogPageT, language, 'popularPosts')}</h3>
                  <div className="space-y-4">
                    {featuredPosts.slice(0, 4).map((post) => (
                      <Link
                        key={post.id}
                        href={`/blog/${post.slug}`}
                        className="flex gap-4 group"
                      >
                        <div className="w-20 h-20 rounded-lg bg-primary-100 flex items-center justify-center flex-shrink-0 overflow-hidden">
                          {post.featured_image ? (
                            <Image
                              src={post.featured_image}
                              alt={post.title}
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
                            {post.title}
                          </h4>
                          <p className="text-xs text-gray-500 mt-1">{formatDate(post.published_date)}</p>
                        </div>
                      </Link>
                    ))}
                  </div>
                </div>
              )}

              {/* Newsletter */}
              <div className="bg-gradient-to-br from-primary-500 to-primary-600 rounded-2xl p-6 text-white">
                <h3 className="text-lg font-bold mb-2">{t(blogPageT, language, 'subscribeNewsletter')}</h3>
                <p className="text-white/80 text-sm mb-4">
                  {t(blogPageT, language, 'newsletterDesc')}
                </p>
                <input
                  type="email"
                  placeholder={t(blogPageT, language, 'yourEmail')}
                  className="w-full px-4 py-3 rounded-xl bg-white/20 border border-white/30 text-white placeholder-white/60 focus:bg-white/30 focus:outline-none transition-all mb-3"
                />
                <button className="w-full py-3 bg-white text-primary-600 rounded-xl font-semibold hover:bg-gray-100 transition-colors">
                  {t(blogPageT, language, 'subscribe')}
                </button>
              </div>
            </aside>

            {/* Blog Posts Grid */}
            <div className={`lg:col-span-3 transition-opacity duration-300 ${isFetching ? 'opacity-50' : 'opacity-100'}`}>
              {filteredPosts.length > 0 ? (
                <>
                  <div className="grid md:grid-cols-2 gap-8">
                    {filteredPosts.map((post, index) => (
                      <motion.article
                        key={post.id}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.5, delay: index * 0.1 }}
                        className="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition-shadow group"
                      >
                        <div className="relative h-48">
                          {post.featured_image ? (
                            <Image
                              src={post.featured_image}
                              alt={post.title}
                              fill
                              sizes="(max-width: 768px) 100vw, (max-width: 1024px) 50vw, 33vw"
                              className="object-cover group-hover:scale-105 transition-transform duration-300"
                            />
                          ) : (
                            <div className="absolute inset-0 bg-primary-500 flex items-center justify-center">
                              <BookOpen className="w-12 h-12 text-white/30" />
                            </div>
                          )}
                          {post.category && (
                            <div className="absolute top-4 left-4">
                              <span className="bg-white/90 backdrop-blur-sm text-primary-600 px-3 py-1 rounded-full text-sm font-medium">
                                {post.category.name}
                              </span>
                            </div>
                          )}
                        </div>
                        <div className="p-6">
                          <div className="flex items-center gap-4 text-sm text-gray-500 mb-3">
                            <span className="flex items-center gap-1">
                              <Calendar className="w-4 h-4" />
                              {formatDate(post.published_date)}
                            </span>
                            <span className="flex items-center gap-1">
                              <Clock className="w-4 h-4" />
                              {post.reading_time} {t(blogPageT, language, 'minRead')}
                            </span>
                          </div>
                          <h3 className="text-lg font-bold text-gray-900 mb-3 group-hover:text-primary-600 transition-colors">
                            <Link href={`/blog/${post.slug}`}>{post.title}</Link>
                          </h3>
                          <RichText html={post.excerpt} className="rich-text-compact text-gray-600 text-sm mb-4 line-clamp-2" />
                          <div className="flex items-center justify-between">
                            <div className="flex items-center gap-2 text-sm text-gray-500">
                              <User className="w-4 h-4" />
                              {post.author_name}
                            </div>
                            <Link
                              href={`/blog/${post.slug}`}
                              className="text-primary-600 font-medium text-sm flex items-center gap-1 hover:gap-2 transition-all"
                            >
                              {t(blogPageT, language, 'readMore')}
                              <ArrowRight className="w-4 h-4" />
                            </Link>
                          </div>
                        </div>
                      </motion.article>
                    ))}
                  </div>

                </>
              ) : (
                <div className="text-center py-16 bg-white rounded-2xl">
                  <BookOpen className="w-16 h-16 text-gray-300 mx-auto mb-4" />
                  <h3 className="text-xl font-bold text-gray-900 mb-2">{t(blogPageT, language, 'noArticles')}</h3>
                  <p className="text-gray-600 mb-6">
                    {t(blogPageT, language, 'noArticlesDesc')}
                  </p>
                  <button
                    onClick={() => {
                      setSearchQuery('');
                      setSelectedCategory('all');
                    }}
                    className="btn btn-primary btn-md"
                  >
                    {t(blogPageT, language, 'clearFilters')}
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-12 sm:py-16 md:py-20 mx-4 lg:mx-16 mb-16 bg-gradient-to-r from-gray-700 via-gray-600 to-gray-700 rounded-3xl">
        <div className="container-custom text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-4xl font-display font-bold text-white mb-6">
              {t(blogPageT, language, 'readyToExperience')}
            </h2>
            <p className="text-xl text-white/90 mb-8 max-w-2xl mx-auto">
              {t(blogPageT, language, 'readyDesc')}
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <Link href="/tours" className="btn bg-white text-primary-600 hover:bg-gray-100 btn-lg">
                {t(blogPageT, language, 'exploreTours')}
              </Link>
              <Link href="/contact" className="btn btn-outline border-white text-white hover:bg-white/10 btn-lg">
                {t(blogPageT, language, 'contactUs')}
              </Link>
            </div>
          </motion.div>
        </div>
      </section>
    </div>
  );
}
