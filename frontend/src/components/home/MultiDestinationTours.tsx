'use client';

import { useQuery } from '@tanstack/react-query';
import { toursApi, fixImageUrl } from '@/lib/api';
import { motion } from 'framer-motion';
import Link from 'next/link';
import Image from 'next/image';
import { ChevronRight, Star, MapPin, Clock, Loader2, Globe2, Plane } from 'lucide-react';
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
  is_multi_destination: boolean;
}

interface ToursResponse {
  count: number;
  results: Tour[];
}

export function MultiDestinationTours() {
  const [ref, isInView] = useInView<HTMLElement>({ rootMargin: '200px' });

  const { data, isLoading, error } = useQuery<ToursResponse>({
    queryKey: ['multi-destination-tours'],
    queryFn: async () => {
      const response = await toursApi.getMultiDestination();
      return response.data;
    },
    enabled: isInView,
    staleTime: 5 * 60 * 1000,
  });

  const tours = data?.results?.slice(0, 6) || [];

  // Don't render the section if no multi-destination tours
  if (!isLoading && !error && tours.length === 0 && isInView) {
    return null;
  }

  return (
    <section ref={ref} className="section-padding bg-gradient-to-b from-blue-50/50 to-white">
      <div className="container-custom">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-end md:justify-between gap-4 mb-12">
          <div>
            <motion.span
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              className="inline-flex items-center gap-2 text-blue-600 font-medium mb-2"
            >
              <Globe2 className="w-5 h-5" />
              Multi-Destination Tours
            </motion.span>
            <motion.h2
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.1 }}
              className="heading-2 text-gray-900"
            >
              Explore Multiple Countries
            </motion.h2>
            <motion.p
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.15 }}
              className="text-gray-600 mt-2 max-w-xl"
            >
              Combine the wonders of Egypt with Jordan, Dubai, and more in one unforgettable journey
            </motion.p>
          </div>
          <motion.div
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
          >
            <Link
              href="/tours?multi_destination=true"
              className="inline-flex items-center text-blue-600 font-medium hover:text-blue-700"
            >
              View All Multi-Destination Tours
              <ChevronRight className="w-5 h-5 ml-1" />
            </Link>
          </motion.div>
        </div>

        {/* Loading state */}
        {isLoading && (
          <div className="flex items-center justify-center py-16">
            <Loader2 className="w-8 h-8 animate-spin text-blue-500" />
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
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {tours.map((tour, index) => (
              <motion.div
                key={tour.id}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                className="h-full"
              >
                <Link href={`/tours/${tour.slug}`} className="card card-hover block group h-full flex flex-col border-2 border-blue-100 hover:border-blue-200">
                  {/* Image */}
                  <div className="relative aspect-[16/10] overflow-hidden flex-shrink-0">
                    {tour.featured_image ? (
                      <Image
                        src={fixImageUrl(tour.featured_image) || ''}
                        alt={tour.name}
                        fill
                        className="object-cover transition-transform duration-500 group-hover:scale-110"
                      />
                    ) : (
                      <div className="w-full h-full bg-gradient-to-br from-blue-100 to-blue-200 flex items-center justify-center">
                        <Globe2 className="w-12 h-12 text-blue-400" />
                      </div>
                    )}
                    <div className="gradient-overlay-light" />

                    {/* Multi-Destination Badge */}
                    <div className="absolute top-4 left-4 flex flex-col gap-2">
                      <span className="badge bg-gradient-to-r from-blue-600 to-indigo-600 text-white flex items-center gap-1.5 shadow-lg">
                        <Plane className="w-3.5 h-3.5" />
                        Multi-Country
                      </span>
                      {tour.is_best_seller && (
                        <span className="badge bg-amber-500 text-white">Best Seller</span>
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
                    {/* Title */}
                    <h3 className="text-lg font-semibold text-gray-900 mb-2 group-hover:text-blue-600 transition-colors line-clamp-2 min-h-[3rem]">
                      {tour.name}
                    </h3>

                    {/* Destinations - Highlighted */}
                    <div className="flex items-start text-gray-600 text-sm mb-3">
                      <MapPin className="w-4 h-4 mr-1 text-blue-500 flex-shrink-0 mt-0.5" />
                      <span className="line-clamp-2 font-medium text-blue-700">
                        {tour.destination_names?.join(' • ') || 'Egypt'}
                      </span>
                    </div>

                    {/* Rating */}
                    <div className="flex items-center gap-2 mb-3">
                      <div className="flex items-center">
                        <Star className="w-4 h-4 text-gold-400 fill-current" />
                        <span className="ml-1 text-sm font-medium">{tour.average_rating || '5.0'}</span>
                      </div>
                      <span className="text-gray-400 text-sm">({tour.review_count || 0} reviews)</span>
                    </div>

                    {/* Price */}
                    <div className="flex items-center justify-between pt-3 border-t mt-auto">
                      <div>
                        <span className="text-gray-500 text-sm">From</span>
                        <div className="flex items-center gap-2">
                          <span className="text-xl font-bold text-blue-600">
                            {formatCurrency(parseFloat(tour.discounted_price || tour.price))}
                          </span>
                          {tour.has_discount && (
                            <span className="text-sm text-gray-400 line-through">
                              {formatCurrency(parseFloat(tour.price))}
                            </span>
                          )}
                        </div>
                      </div>
                      <span className="text-blue-600 font-medium group-hover:translate-x-1 transition-transform inline-flex items-center">
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
      </div>
    </section>
  );
}
