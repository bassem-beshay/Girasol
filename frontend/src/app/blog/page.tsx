'use client';

import { useState, useRef } from 'react';
import { useQuery } from '@tanstack/react-query';
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
  ChevronLeft,
  ChevronRight,
  ChevronsLeft,
  ChevronsRight,
} from 'lucide-react';

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

const POSTS_PER_PAGE = 10;

export default function BlogPage() {
  const [selectedCategory, setSelectedCategory] = useState<string>('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [currentPage, setCurrentPage] = useState(1);
  const blogSectionRef = useRef<HTMLDivElement>(null);

  // Fetch blog posts with pagination
  const { data: postsData, isLoading: postsLoading } = useQuery<BlogPostsResponse>({
    queryKey: ['blog-posts', selectedCategory, currentPage],
    placeholderData: (prev) => prev,
    queryFn: async () => {
      const params: Record<string, unknown> = {
        page: currentPage,
        page_size: POSTS_PER_PAGE,
      };
      if (selectedCategory !== 'all') {
        params.category__slug = selectedCategory;
      }
      const response = await blogApi.getPosts(params);
      return response.data;
    },
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
  const totalPages = Math.ceil(totalPosts / POSTS_PER_PAGE);

  // Filter posts by search query (client-side)
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

  const handleCategoryChange = (slug: string) => {
    setSelectedCategory(slug);
    setCurrentPage(1);
  };

  const handlePageChange = (page: number) => {
    setCurrentPage(page);
    setTimeout(() => {
      blogSectionRef.current?.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 100);
  };

  // Generate page numbers to display
  const getPageNumbers = () => {
    const pages: (number | string)[] = [];
    if (totalPages <= 7) {
      for (let i = 1; i <= totalPages; i++) pages.push(i);
    } else {
      pages.push(1);
      if (currentPage > 3) pages.push('...');
      const start = Math.max(2, currentPage - 1);
      const end = Math.min(totalPages - 1, currentPage + 1);
      for (let i = start; i <= end; i++) pages.push(i);
      if (currentPage < totalPages - 2) pages.push('...');
      pages.push(totalPages);
    }
    return pages;
  };

  if (postsLoading && currentPage === 1) {
    return (
      <div className="min-h-screen pt-32 pb-16">
        <div className="container-custom">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500 mx-auto"></div>
            <p className="mt-4 text-gray-600">Loading blog posts...</p>
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
            Travel Blog
          </motion.h1>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="text-xl md:text-2xl text-white/90"
          >
            Stories, tips, and inspiration for your Egyptian adventure
          </motion.p>
        </div>
      </section>

      {/* Featured Posts */}
      {featuredPosts.length > 0 && (
        <section className="py-16 bg-white">
          <div className="container-custom">
            <div className="flex items-center gap-3 mb-8">
              <TrendingUp className="w-6 h-6 text-primary-600" />
              <h2 className="text-2xl font-display font-bold text-gray-900">Featured Articles</h2>
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
                        className="object-cover"
                      loading="lazy" />
                    ) : (
                      <div className="absolute inset-0 bg-primary-600 flex items-center justify-center">
                        <BookOpen className="w-16 h-16 text-white/30" />
                      </div>
                    )}
                    <div className="absolute top-4 left-4 z-20">
                      <span className="bg-primary-500 text-white px-3 py-1 rounded-full text-sm font-medium">
                        Featured
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
                    <p className="text-gray-600 mb-4 line-clamp-2">{post.excerpt}</p>
                    <div className="flex items-center justify-between">
                      <div className="flex items-center gap-2 text-sm text-gray-500">
                        <User className="w-4 h-4" />
                        {post.author_name}
                      </div>
                      <div className="flex items-center gap-2 text-sm text-gray-500">
                        <Clock className="w-4 h-4" />
                        {post.reading_time} min read
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
      <section ref={blogSectionRef} className="py-16 bg-gray-50">
        <div className="container-custom">
          <div className="grid lg:grid-cols-4 gap-8">
            {/* Sidebar */}
            <aside className="lg:col-span-1 space-y-8">
              {/* Search */}
              <div className="bg-white rounded-2xl p-6 shadow-md">
                <h3 className="text-lg font-bold text-gray-900 mb-4">Search</h3>
                <div className="relative">
                  <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                  <input
                    type="text"
                    placeholder="Search articles..."
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                    className="w-full pl-12 pr-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all"
                  />
                </div>
              </div>

              {/* Categories */}
              <div className="bg-white rounded-2xl shadow-md overflow-hidden">
                <div className="bg-gradient-to-r from-primary-500 to-primary-600 px-6 py-4">
                  <h3 className="text-base font-bold text-white flex items-center gap-2">
                    <Tag className="w-4 h-4" />
                    Categories
                  </h3>
                </div>
                <div className="p-4">
                  <button
                    onClick={() => handleCategoryChange('all')}
                    className={`w-full flex items-center justify-between px-4 py-2.5 rounded-xl text-sm font-medium transition-all duration-200 mb-1 ${
                      selectedCategory === 'all'
                        ? 'bg-primary-50 text-primary-700 border border-primary-200'
                        : 'text-gray-600 hover:bg-gray-50'
                    }`}
                  >
                    <span className="flex items-center gap-2">
                      {selectedCategory === 'all' && <span className="w-1.5 h-1.5 rounded-full bg-primary-500"></span>}
                      All Articles
                    </span>
                    <span className={`text-xs font-semibold px-2 py-0.5 rounded-full ${
                      selectedCategory === 'all'
                        ? 'bg-primary-500 text-white'
                        : 'bg-gray-100 text-gray-500'
                    }`}>{totalPosts}</span>
                  </button>
                  {categories.filter(c => c.post_count > 0).map((category) => (
                    <button
                      key={category.id}
                      onClick={() => handleCategoryChange(category.slug)}
                      className={`w-full flex items-center justify-between px-4 py-2.5 rounded-xl text-sm font-medium transition-all duration-200 mb-1 ${
                        selectedCategory === category.slug
                          ? 'bg-primary-50 text-primary-700 border border-primary-200'
                          : 'text-gray-600 hover:bg-gray-50'
                      }`}
                    >
                      <span className="flex items-center gap-2">
                        {selectedCategory === category.slug && <span className="w-1.5 h-1.5 rounded-full bg-primary-500"></span>}
                        {category.name}
                      </span>
                      <span className={`text-xs font-semibold px-2 py-0.5 rounded-full ${
                        selectedCategory === category.slug
                          ? 'bg-primary-500 text-white'
                          : 'bg-gray-100 text-gray-500'
                      }`}>{category.post_count}</span>
                    </button>
                  ))}
                </div>
              </div>

              {/* Popular Posts */}
              {featuredPosts.length > 0 && (
                <div className="bg-white rounded-2xl p-6 shadow-md">
                  <div className="flex items-center gap-2 mb-5">
                    <div className="w-1 h-6 bg-primary-500 rounded-full"></div>
                    <h3 className="text-lg font-bold text-gray-900">Popular Posts</h3>
                  </div>
                  <div className="space-y-4">
                    {featuredPosts.slice(0, 4).map((post, idx) => (
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
                            loading="lazy" />
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
                <h3 className="text-lg font-bold mb-2">Subscribe to Newsletter</h3>
                <p className="text-white/80 text-sm mb-4">
                  Get the latest travel tips and inspiration delivered to your inbox.
                </p>
                <input
                  type="email"
                  placeholder="Your email address"
                  className="w-full px-4 py-3 rounded-xl bg-white/20 border border-white/30 text-white placeholder-white/60 focus:bg-white/30 focus:outline-none transition-all mb-3"
                />
                <button className="w-full py-3 bg-white text-primary-600 rounded-xl font-semibold hover:bg-gray-100 transition-colors">
                  Subscribe
                </button>
              </div>
            </aside>

            {/* Blog Posts Grid */}
            <div className="lg:col-span-3 min-h-[600px]">
              {/* Results count */}
              {totalPosts > 0 && (
                <div className="flex items-center justify-between mb-6">
                  <p className="text-sm text-gray-500">
                    Showing {((currentPage - 1) * POSTS_PER_PAGE) + 1}–{Math.min(currentPage * POSTS_PER_PAGE, totalPosts)} of {totalPosts} articles
                  </p>
                </div>
              )}

              {filteredPosts.length > 0 ? (
                <>
                  <div className="grid md:grid-cols-2 gap-8">
                    {filteredPosts.map((post, index) => (
                      <motion.article
                        key={post.id}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.5, delay: index * 0.05 }}
                        className="bg-white rounded-2xl overflow-hidden shadow-md hover:shadow-xl transition-shadow group"
                      >
                        <div className="relative h-48">
                          {post.featured_image ? (
                            <Image
                              src={post.featured_image}
                              alt={post.title}
                              fill
                              className="object-cover group-hover:scale-105 transition-transform duration-300"
                            loading="lazy" />
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
                              {post.reading_time} min read
                            </span>
                          </div>
                          <h3 className="text-lg font-bold text-gray-900 mb-3 group-hover:text-primary-600 transition-colors">
                            <Link href={`/blog/${post.slug}`}>{post.title}</Link>
                          </h3>
                          <p className="text-gray-600 text-sm mb-4 line-clamp-2">{post.excerpt}</p>
                          <div className="flex items-center justify-between">
                            <div className="flex items-center gap-2 text-sm text-gray-500">
                              <User className="w-4 h-4" />
                              {post.author_name}
                            </div>
                            <Link
                              href={`/blog/${post.slug}`}
                              className="text-primary-600 font-medium text-sm flex items-center gap-1 hover:gap-2 transition-all"
                            >
                              Read More
                              <ArrowRight className="w-4 h-4" />
                            </Link>
                          </div>
                        </div>
                      </motion.article>
                    ))}
                  </div>

                  {/* Pagination */}
                  {totalPages > 1 && (
                    <div className="mt-12 flex flex-col items-center gap-4">
                      <div className="flex items-center gap-1.5">
                        {/* First Page */}
                        <button
                          onClick={() => handlePageChange(1)}
                          disabled={currentPage === 1}
                          className="w-10 h-10 rounded-lg flex items-center justify-center text-gray-500 hover:bg-primary-50 hover:text-primary-600 disabled:opacity-30 disabled:cursor-not-allowed transition-colors"
                          title="First page"
                        >
                          <ChevronsLeft className="w-4 h-4" />
                        </button>

                        {/* Previous */}
                        <button
                          onClick={() => handlePageChange(currentPage - 1)}
                          disabled={currentPage === 1}
                          className="w-10 h-10 rounded-lg flex items-center justify-center text-gray-500 hover:bg-primary-50 hover:text-primary-600 disabled:opacity-30 disabled:cursor-not-allowed transition-colors"
                          title="Previous page"
                        >
                          <ChevronLeft className="w-4 h-4" />
                        </button>

                        {/* Page Numbers */}
                        {getPageNumbers().map((page, idx) => (
                          typeof page === 'string' ? (
                            <span key={`dots-${idx}`} className="w-10 h-10 flex items-center justify-center text-gray-400">
                              ...
                            </span>
                          ) : (
                            <button
                              key={page}
                              onClick={() => handlePageChange(page)}
                              className={`w-10 h-10 rounded-lg flex items-center justify-center text-sm font-semibold transition-all duration-200 ${
                                currentPage === page
                                  ? 'bg-primary-500 text-white shadow-md shadow-primary-500/25'
                                  : 'text-gray-600 hover:bg-primary-50 hover:text-primary-600'
                              }`}
                            >
                              {page}
                            </button>
                          )
                        ))}

                        {/* Next */}
                        <button
                          onClick={() => handlePageChange(currentPage + 1)}
                          disabled={currentPage === totalPages}
                          className="w-10 h-10 rounded-lg flex items-center justify-center text-gray-500 hover:bg-primary-50 hover:text-primary-600 disabled:opacity-30 disabled:cursor-not-allowed transition-colors"
                          title="Next page"
                        >
                          <ChevronRight className="w-4 h-4" />
                        </button>

                        {/* Last Page */}
                        <button
                          onClick={() => handlePageChange(totalPages)}
                          disabled={currentPage === totalPages}
                          className="w-10 h-10 rounded-lg flex items-center justify-center text-gray-500 hover:bg-primary-50 hover:text-primary-600 disabled:opacity-30 disabled:cursor-not-allowed transition-colors"
                          title="Last page"
                        >
                          <ChevronsRight className="w-4 h-4" />
                        </button>
                      </div>

                      <p className="text-sm text-gray-400">
                        Page {currentPage} of {totalPages}
                      </p>
                    </div>
                  )}
                </>
              ) : (
                <div className="text-center py-16 bg-white rounded-2xl">
                  <BookOpen className="w-16 h-16 text-gray-300 mx-auto mb-4" />
                  <h3 className="text-xl font-bold text-gray-900 mb-2">No articles found</h3>
                  <p className="text-gray-600 mb-6">
                    Try adjusting your search or filter to find what you're looking for.
                  </p>
                  <button
                    onClick={() => {
                      setSearchQuery('');
                      setSelectedCategory('all');
                      setCurrentPage(1);
                    }}
                    className="btn btn-primary btn-md"
                  >
                    Clear Filters
                  </button>
                </div>
              )}
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-12 sm:py-16 md:py-20 bg-white">
        <div className="container-custom px-4 sm:px-6">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="bg-gradient-to-r from-gray-700 via-gray-600 to-gray-700 rounded-3xl py-12 sm:py-16 md:py-20 px-6 sm:px-10 md:px-16 text-center relative overflow-hidden"
          >
            <div className="absolute top-0 right-0 w-64 h-64 bg-primary-500/15 rounded-full blur-3xl" />
            <div className="absolute bottom-0 left-0 w-48 h-48 bg-primary-500/10 rounded-full blur-2xl" />
            <div className="relative z-10">
              <h2 className="text-2xl sm:text-3xl md:text-4xl font-display font-bold text-white mb-4 sm:mb-6">
                Ready to Experience Egypt?
              </h2>
              <p className="text-base sm:text-lg md:text-xl text-white/80 mb-6 sm:mb-8 max-w-2xl mx-auto">
                Turn your travel dreams into reality. Browse our tours and start planning your
                unforgettable Egyptian adventure today.
              </p>
              <div className="flex flex-wrap justify-center gap-4">
                <Link href="/tours" className="btn bg-primary-500 text-white hover:bg-primary-600 btn-lg rounded-xl">
                  Explore Tours
                </Link>
                <Link href="/contact" className="btn btn-outline border-white/30 text-white hover:bg-white/10 btn-lg rounded-xl">
                  Contact Us
                </Link>
              </div>
            </div>
          </motion.div>
        </div>
      </section>
    </div>
  );
}
