'use client';

import { useQuery } from '@tanstack/react-query';
import { toursApi } from '@/lib/api';
import { motion } from 'framer-motion';
import Link from 'next/link';
import Image from 'next/image';
import { Clock, MapPin, Tag, ArrowRight, Loader2, Percent } from 'lucide-react';
import { formatCurrency } from '@/lib/utils';

interface Tour {
  id: number;
  name: string;
  slug: string;
  short_description: string;
  featured_image: string | null;
  days: number;
  nights: number;
  duration_display: string;
  price: string;
  discounted_price: string;
  has_discount: boolean;
  discount_percentage: number | null;
  destination: {
    name: string;
    slug: string;
  } | null;
}

interface ToursResponse {
  count: number;
  results: Tour[];
}

export default function OffersPage() {
  const { data, isLoading, error } = useQuery<ToursResponse>({
    queryKey: ['discounted-tours'],
    queryFn: async () => {
      const response = await toursApi.getAll({ has_discount: true });
      return response.data;
    },
  });

  const discountedTours = data?.results?.filter(t => t.has_discount) || [];

  return (
    <main className="min-h-screen">
      {/* Hero Section */}
      <section className="relative py-24 bg-gradient-to-r from-primary-600 to-primary-700">
        <div className="absolute inset-0 bg-hero-pattern opacity-10" />
        <div className="container-custom relative z-10">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-center text-white"
          >
            <span className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/10 text-sm mb-6">
              <Percent className="w-4 h-4" />
              Limited Time Offers
            </span>
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-display font-bold mb-6">
              Special Offers & Deals
            </h1>
            <p className="text-xl text-white/80 max-w-2xl mx-auto">
              Discover amazing discounts on our most popular Egyptian tours.
              Book now and save big on your dream adventure!
            </p>
          </motion.div>
        </div>
      </section>

      {/* Offers Grid */}
      <section className="section-padding">
        <div className="container-custom">
          {isLoading ? (
            <div className="flex items-center justify-center py-16">
              <Loader2 className="w-8 h-8 animate-spin text-primary-600" />
              <span className="ml-3 text-gray-600">Loading offers...</span>
            </div>
          ) : error ? (
            <div className="text-center py-16">
              <p className="text-red-500">Failed to load offers. Please try again later.</p>
            </div>
          ) : discountedTours.length === 0 ? (
            <div className="text-center py-16">
              <div className="w-24 h-24 mx-auto mb-6 rounded-full bg-gray-100 flex items-center justify-center">
                <Tag className="w-12 h-12 text-gray-400" />
              </div>
              <h2 className="text-2xl font-bold text-gray-900 mb-4">No Active Offers</h2>
              <p className="text-gray-600 mb-8">
                Check back soon for exciting deals and discounts on our tours!
              </p>
              <Link href="/tours" className="btn btn-primary">
                Browse All Tours
              </Link>
            </div>
          ) : (
            <>
              <div className="text-center mb-12">
                <h2 className="text-3xl font-display font-bold text-gray-900 mb-4">
                  {discountedTours.length} Special {discountedTours.length === 1 ? 'Offer' : 'Offers'} Available
                </h2>
                <p className="text-gray-600">
                  Don&apos;t miss out on these exclusive deals!
                </p>
              </div>

              <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
                {discountedTours.map((tour, index) => (
                  <motion.div
                    key={tour.id}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: index * 0.1 }}
                  >
                    <Link href={`/tours/${tour.slug}`}>
                      <div className="group bg-white rounded-2xl shadow-card overflow-hidden hover:shadow-card-hover transition-all duration-300">
                        {/* Image */}
                        <div className="relative aspect-[4/3] overflow-hidden">
                          {tour.featured_image ? (
                            <Image
                              src={tour.featured_image}
                              alt={tour.name}
                              fill
                              className="object-cover group-hover:scale-110 transition-transform duration-500"
                            />
                          ) : (
                            <div className="w-full h-full bg-gradient-to-br from-primary-400 to-primary-600" />
                          )}

                          {/* Discount Badge */}
                          {tour.discount_percentage && (
                            <div className="absolute top-4 left-4 px-3 py-1 rounded-full bg-red-500 text-white text-sm font-bold">
                              {tour.discount_percentage}% OFF
                            </div>
                          )}

                          {/* Duration Badge */}
                          <div className="absolute bottom-4 left-4 flex items-center gap-2 px-3 py-1 rounded-full bg-white/90 backdrop-blur-sm text-sm">
                            <Clock className="w-4 h-4 text-primary-600" />
                            {tour.duration_display || `${tour.days} Days`}
                          </div>
                        </div>

                        {/* Content */}
                        <div className="p-6">
                          {tour.destination && (
                            <div className="flex items-center gap-1 text-sm text-gray-500 mb-2">
                              <MapPin className="w-4 h-4" />
                              {tour.destination.name}
                            </div>
                          )}

                          <h3 className="text-xl font-bold text-gray-900 mb-2 group-hover:text-primary-600 transition-colors line-clamp-2">
                            {tour.name}
                          </h3>

                          {tour.short_description && (
                            <p className="text-gray-600 text-sm mb-4 line-clamp-2">
                              {tour.short_description}
                            </p>
                          )}

                          {/* Price */}
                          <div className="flex items-center justify-between pt-4 border-t border-gray-100">
                            <div>
                              <span className="text-sm text-gray-500 line-through">
                                {formatCurrency(parseFloat(tour.price))}
                              </span>
                              <div className="text-2xl font-bold text-primary-600">
                                {formatCurrency(parseFloat(tour.discounted_price))}
                              </div>
                            </div>
                            <span className="flex items-center gap-1 text-primary-600 font-medium group-hover:gap-2 transition-all">
                              View Deal
                              <ArrowRight className="w-4 h-4" />
                            </span>
                          </div>
                        </div>
                      </div>
                    </Link>
                  </motion.div>
                ))}
              </div>
            </>
          )}
        </div>
      </section>

      {/* CTA Section */}
      <section className="section-padding bg-gray-50">
        <div className="container-custom">
          <div className="text-center max-w-2xl mx-auto">
            <h2 className="text-3xl font-display font-bold text-gray-900 mb-4">
              Can&apos;t Find What You&apos;re Looking For?
            </h2>
            <p className="text-gray-600 mb-8">
              Browse our complete collection of tours or contact us for a custom package.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link href="/tours" className="btn btn-primary btn-lg">
                View All Tours
              </Link>
              <Link href="/contact" className="btn btn-outline btn-lg">
                Contact Us
              </Link>
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}
