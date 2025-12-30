'use client';

import { useQuery } from '@tanstack/react-query';
import { toursApi, fixImageUrl } from '@/lib/api';
import { motion } from 'framer-motion';
import Link from 'next/link';
import Image from 'next/image';
import { ChevronRight, Star, MapPin, Clock, Loader2, Sparkles } from 'lucide-react';
import { formatCurrency } from '@/lib/utils';
import { useInView } from '@/hooks/useInView';

interface Tour {
  id: number;
  name: string;
  slug: string;
  short_description: string;
  featured_image: string | null;
  destination_names: string[];
  days: number;
  nights: number;
  duration_display: string;
  price: string;
  discounted_price: string;
  has_discount: boolean;
  discount_percentage: number | null;
  average_rating: string;
  review_count: number;
  is_best_seller: boolean;
  is_new: boolean;
  is_featured: boolean;
  highlights: string[];
  // Early Booking fields
  is_early_booking: boolean;
  early_booking_discount: number | null;
  early_booking_price: number | null;
  early_booking_badge: string | null;
}

interface ToursResponse {
  count: number;
  results: Tour[];
}

export function PopularTours() {
  const [ref, isInView] = useInView<HTMLElement>({ rootMargin: '200px' });

  const { data, isLoading, error } = useQuery<ToursResponse>({
    queryKey: ['popular-tours'],
    queryFn: async () => {
      const response = await toursApi.getPopular();
      return response.data;
    },
    enabled: isInView, // Only fetch when section is in view
    staleTime: 5 * 60 * 1000, // Cache for 5 minutes
  });

  const tours = data?.results?.slice(0, 4) || [];

  return (
    <section ref={ref} className="section-padding">
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
              Popular Tours
            </motion.span>
            <motion.h2
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.1 }}
              className="heading-2 text-gray-900"
            >
              Most Loved Tour Packages
            </motion.h2>
          </div>
          <motion.div
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
          >
            <Link
              href="/tours"
              className="inline-flex items-center text-primary-600 font-medium hover:text-primary-700"
            >
              View All Tours
              <ChevronRight className="w-5 h-5 ml-1" />
            </Link>
          </motion.div>
        </div>

        {/* Loading state */}
        {isLoading && (
          <div className="flex items-center justify-center py-16">
            <Loader2 className="w-8 h-8 animate-spin text-primary-500" />
            <span className="ml-3 text-gray-600">Loading tours...</span>
          </div>
        )}

        {/* Error state */}
        {error && (
          <div className="text-center py-16">
            <p className="text-gray-500">Unable to load tours. Please try again later.</p>
          </div>
        )}

        {/* Tours grid */}
        {!isLoading && !error && tours.length > 0 && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            {tours.map((tour, index) => (
              <motion.div
                key={tour.id}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                className="h-full"
              >
                <Link href={`/tours/${tour.slug}`} className="card card-hover block group h-full flex flex-col">
                  {/* Image */}
                  <div className="relative aspect-tour-card overflow-hidden flex-shrink-0">
                    {tour.featured_image ? (
                      <Image
                        src={fixImageUrl(tour.featured_image) || ''}
                        alt={tour.name}
                        fill
                        className="object-cover transition-transform duration-500 group-hover:scale-110"
                      />
                    ) : (
                      <div className="w-full h-full bg-gradient-to-br from-primary-100 to-primary-200 flex items-center justify-center">
                        <MapPin className="w-12 h-12 text-primary-400" />
                      </div>
                    )}
                    <div className="gradient-overlay-light" />

                    {/* Badges */}
                    <div className="absolute top-4 left-4 flex flex-col gap-2">
                      {tour.is_early_booking && (
                        <span className="badge bg-gradient-to-r from-orange-500 to-amber-500 text-white flex items-center gap-1">
                          <Sparkles className="w-3 h-3" />
                          {tour.early_booking_badge || 'Early Bird'}
                        </span>
                      )}
                      {tour.is_best_seller && (
                        <span className="badge bg-primary-500 text-white">Best Seller</span>
                      )}
                      {tour.is_new && (
                        <span className="badge bg-green-500 text-white">New</span>
                      )}
                      {tour.has_discount && tour.discount_percentage && (
                        <span className="badge bg-red-500 text-white">
                          {tour.discount_percentage}% OFF
                        </span>
                      )}
                    </div>

                    {/* Duration badge */}
                    <div className="absolute bottom-4 left-4">
                      <span className="inline-flex items-center gap-1 px-3 py-1 rounded-full bg-white/90 text-gray-900 text-sm font-medium">
                        <Clock className="w-4 h-4" />
                        {tour.duration_display || `${tour.days}D/${tour.nights}N`}
                      </span>
                    </div>
                  </div>

                  {/* Content */}
                  <div className="p-5 flex flex-col flex-grow">
                    {/* Title - Fixed height for 2 lines */}
                    <h3 className="text-lg font-semibold text-gray-900 mb-2 group-hover:text-primary-600 transition-colors line-clamp-2 min-h-[3rem]">
                      {tour.name}
                    </h3>

                    {/* Destinations - Fixed height */}
                    <div className="flex items-center text-gray-600 text-sm mb-3 h-5">
                      <MapPin className="w-4 h-4 mr-1 text-primary-500 flex-shrink-0" />
                      <span className="line-clamp-1">{tour.destination_names?.join(', ') || 'Egypt'}</span>
                    </div>

                    {/* Rating - Now aligned across all cards */}
                    <div className="flex items-center gap-2 mb-3">
                      <div className="flex items-center">
                        <Star className="w-4 h-4 text-gold-400 fill-current" />
                        <span className="ml-1 text-sm font-medium">{tour.average_rating || '5.0'}</span>
                      </div>
                      <span className="text-gray-400 text-sm">({tour.review_count || 0} reviews)</span>
                    </div>

                    {/* Price - Always at bottom */}
                    <div className="flex items-center justify-between pt-3 border-t mt-auto">
                      <div>
                        <span className="text-gray-500 text-sm">
                          {tour.is_early_booking ? 'Early Bird' : 'From'}
                        </span>
                        <div className="flex items-center gap-2">
                          <span className={`text-xl font-bold ${tour.is_early_booking ? 'text-orange-500' : 'text-primary-600'}`}>
                            {formatCurrency(tour.early_booking_price || parseFloat(tour.discounted_price || tour.price))}
                          </span>
                          {(tour.has_discount || tour.is_early_booking) && (
                            <span className="text-sm text-gray-400 line-through">
                              {formatCurrency(parseFloat(tour.price))}
                            </span>
                          )}
                        </div>
                      </div>
                      <span className="text-primary-600 font-medium group-hover:translate-x-1 transition-transform inline-flex items-center">
                        Details
                        <ChevronRight className="w-4 h-4" />
                      </span>
                    </div>
                  </div>
                </Link>
              </motion.div>
            ))}
          </div>
        )}

        {/* Empty state */}
        {!isLoading && !error && tours.length === 0 && (
          <div className="text-center py-16">
            <MapPin className="w-16 h-16 text-gray-300 mx-auto mb-4" />
            <p className="text-gray-500">No tours available at the moment.</p>
          </div>
        )}
      </div>
    </section>
  );
}
