'use client';

import { useQuery } from '@tanstack/react-query';
import { destinationsApi, fixImageUrl } from '@/lib/api';
import { motion } from 'framer-motion';
import Link from 'next/link';
import Image from 'next/image';
import { ChevronRight, MapPin, Loader2 } from 'lucide-react';

interface Destination {
  id: number;
  name: string;
  slug: string;
  tagline: string;
  description: string;
  featured_image: string | null;
  tour_count: number;
  is_featured: boolean;
}

interface DestinationsResponse {
  count: number;
  results: Destination[];
}

export function Destinations() {
  const { data, isLoading, error } = useQuery<DestinationsResponse>({
    queryKey: ['featured-destinations'],
    queryFn: async () => {
      const response = await destinationsApi.getFeatured();
      return response.data;
    },
  });

  const destinations = data?.results?.slice(0, 6) || [];

  return (
    <section className="section-padding bg-gray-50">
      <div className="container-custom">
        {/* Header */}
        <div className="text-center max-w-2xl mx-auto mb-12">
          <motion.span
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-primary-600 font-medium mb-2 block"
          >
            Explore Egypt
          </motion.span>
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.1 }}
            className="heading-2 text-gray-900 mb-4"
          >
            Popular Destinations
          </motion.h2>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.2 }}
            className="text-gray-600"
          >
            From ancient temples to pristine beaches, discover the diverse
            wonders of Egypt.
          </motion.p>
        </div>

        {/* Loading state */}
        {isLoading && (
          <div className="flex items-center justify-center py-16">
            <Loader2 className="w-8 h-8 animate-spin text-primary-500" />
            <span className="ml-3 text-gray-600">Loading destinations...</span>
          </div>
        )}

        {/* Error state */}
        {error && (
          <div className="text-center py-16">
            <p className="text-gray-500">Unable to load destinations. Please try again later.</p>
          </div>
        )}

        {/* Destinations grid */}
        {!isLoading && !error && destinations.length > 0 && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {destinations.map((destination, index) => (
              <motion.div
                key={destination.id}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
              >
                <Link
                  href={`/destinations/${destination.slug}`}
                  className="block relative group overflow-hidden rounded-2xl aspect-[4/3]"
                >
                  {destination.featured_image ? (
                    <Image
                      src={fixImageUrl(destination.featured_image) || ''}
                      alt={destination.name}
                      fill
                      className="object-cover transition-transform duration-700 group-hover:scale-110"
                    />
                  ) : (
                    <div className="w-full h-full bg-gradient-to-br from-primary-400 to-primary-600 flex items-center justify-center">
                      <MapPin className="w-16 h-16 text-white/50" />
                    </div>
                  )}
                  <div className="absolute inset-0 bg-gradient-to-t from-black/80 via-black/30 to-transparent" />

                  {/* Content */}
                  <div className="absolute inset-x-0 bottom-0 p-6">
                    <span className="text-primary-400 text-sm font-medium mb-1 block">
                      {destination.tagline || 'Discover'}
                    </span>
                    <h3 className="text-2xl font-display font-bold text-white mb-2">
                      {destination.name}
                    </h3>
                    <div className="flex items-center justify-between">
                      <span className="text-white/80 text-sm">
                        {destination.tour_count} Tours
                      </span>
                      <span className="inline-flex items-center text-white font-medium group-hover:text-primary-400 transition-colors">
                        Explore
                        <ChevronRight className="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" />
                      </span>
                    </div>
                  </div>

                  {/* Hover overlay */}
                  <div className="absolute inset-0 bg-primary-600/20 opacity-0 group-hover:opacity-100 transition-opacity" />
                </Link>
              </motion.div>
            ))}
          </div>
        )}

        {/* Empty state */}
        {!isLoading && !error && destinations.length === 0 && (
          <div className="text-center py-16">
            <MapPin className="w-16 h-16 text-gray-300 mx-auto mb-4" />
            <p className="text-gray-500">No destinations available at the moment.</p>
          </div>
        )}

        {/* View all link */}
        {!isLoading && !error && destinations.length > 0 && (
          <motion.div
            initial={{ opacity: 0 }}
            whileInView={{ opacity: 1 }}
            viewport={{ once: true }}
            className="text-center mt-10"
          >
            <Link
              href="/destinations"
              className="btn btn-outline btn-lg"
            >
              View All Destinations
              <ChevronRight className="w-5 h-5 ml-1" />
            </Link>
          </motion.div>
        )}
      </div>
    </section>
  );
}
