'use client';

import { useQuery } from '@tanstack/react-query';
import { destinationsApi } from '@/lib/api';
import { MapPin, ChevronRight } from 'lucide-react';
import Link from 'next/link';
import Image from 'next/image';
import { motion } from 'framer-motion';

interface Destination {
  id: number;
  name: string;
  name_ar: string;
  slug: string;
  tagline: string;
  description: string;
  featured_image: string | null;
  country: string;
  region: string;
  tour_count: number;
  is_featured: boolean;
}

interface DestinationsResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Destination[];
}

export default function DestinationsPage() {
  const { data, isLoading, error } = useQuery<DestinationsResponse>({
    queryKey: ['destinations'],
    queryFn: async () => {
      const response = await destinationsApi.getAll();
      return response.data;
    },
  });

  if (isLoading) {
    return (
      <div className="min-h-screen pt-32 pb-16">
        <div className="container-custom">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500 mx-auto"></div>
            <p className="mt-4 text-gray-600">Loading destinations...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="min-h-screen pt-32 pb-16">
        <div className="container-custom">
          <div className="text-center text-red-500">
            <p>Error loading destinations. Please try again later.</p>
          </div>
        </div>
      </div>
    );
  }

  const destinations = data?.results || [];
  const featuredDestinations = destinations.filter(d => d.is_featured);
  const otherDestinations = destinations.filter(d => !d.is_featured);

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[50vh] min-h-[400px] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-primary-900/90 to-primary-800/80 z-10" />
        <div
          className="absolute inset-0 bg-cover bg-center"
          style={{ backgroundImage: "url('/images/destinations-hero.jpg')" }}
        />
        <div className="relative z-20 text-center text-white max-w-4xl mx-auto px-4">
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="text-5xl md:text-6xl font-display font-bold mb-6"
          >
            Explore Egypt
          </motion.h1>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="text-xl md:text-2xl text-white/90"
          >
            From ancient temples to pristine beaches, discover the diverse wonders of Egypt
          </motion.p>
        </div>
      </section>

      {/* Featured Destinations */}
      {featuredDestinations.length > 0 && (
        <section className="py-16 bg-white">
          <div className="container-custom">
            <div className="text-center max-w-2xl mx-auto mb-12">
              <span className="text-primary-600 font-medium mb-2 block">Top Picks</span>
              <h2 className="heading-2 text-gray-900 mb-4">Featured Destinations</h2>
              <p className="text-gray-600">
                Our most popular destinations, handpicked for unforgettable experiences
              </p>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {featuredDestinations.map((destination, index) => (
                <motion.div
                  key={destination.id}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: index * 0.1 }}
                >
                  <Link
                    href={`/destinations/${destination.slug}`}
                    className="block relative group overflow-hidden rounded-2xl aspect-[4/3]"
                  >
                    {destination.featured_image ? (
                      <Image
                        src={destination.featured_image}
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

                    {/* Featured Badge */}
                    <div className="absolute top-4 left-4">
                      <span className="px-3 py-1 bg-primary-500 text-white text-sm font-medium rounded-full">
                        Featured
                      </span>
                    </div>

                    {/* Content */}
                    <div className="absolute inset-x-0 bottom-0 p-6">
                      <span className="text-primary-400 text-sm font-medium mb-1 block">
                        {destination.tagline}
                      </span>
                      <h3 className="text-2xl font-display font-bold text-white mb-2">
                        {destination.name}
                      </h3>
                      <div className="flex items-center justify-between">
                        <span className="text-white/80 text-sm">
                          {destination.tour_count} Tours Available
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
          </div>
        </section>
      )}

      {/* All Destinations */}
      <section className="py-16 bg-gray-50">
        <div className="container-custom">
          <div className="text-center max-w-2xl mx-auto mb-12">
            <span className="text-primary-600 font-medium mb-2 block">Discover More</span>
            <h2 className="heading-2 text-gray-900 mb-4">All Destinations</h2>
            <p className="text-gray-600">
              Explore all the amazing places Egypt has to offer
            </p>
          </div>

          {destinations.length === 0 ? (
            <div className="text-center py-16">
              <MapPin className="w-16 h-16 text-gray-300 mx-auto mb-4" />
              <p className="text-gray-500 text-lg">No destinations available at the moment.</p>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              {destinations.map((destination, index) => (
                <motion.div
                  key={destination.id}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: index * 0.05 }}
                >
                  <Link
                    href={`/destinations/${destination.slug}`}
                    className="block bg-white rounded-xl shadow-md overflow-hidden hover:shadow-xl transition-shadow group"
                  >
                    <div className="relative h-48">
                      {destination.featured_image ? (
                        <Image
                          src={destination.featured_image}
                          alt={destination.name}
                          fill
                          className="object-cover group-hover:scale-105 transition-transform duration-300"
                        />
                      ) : (
                        <div className="w-full h-full bg-gradient-to-br from-primary-100 to-primary-200 flex items-center justify-center">
                          <MapPin className="w-12 h-12 text-primary-400" />
                        </div>
                      )}
                    </div>

                    <div className="p-5">
                      <div className="flex items-center text-gray-500 text-sm mb-2">
                        <MapPin className="w-4 h-4 mr-1" />
                        {destination.region}, {destination.country}
                      </div>
                      <h3 className="text-xl font-semibold text-gray-900 mb-2 group-hover:text-primary-600 transition-colors">
                        {destination.name}
                      </h3>
                      <p className="text-gray-600 text-sm mb-4 line-clamp-2">
                        {destination.tagline}
                      </p>
                      <div className="flex items-center justify-between pt-4 border-t">
                        <span className="text-primary-600 font-medium">
                          {destination.tour_count} Tours
                        </span>
                        <span className="text-primary-600 font-medium inline-flex items-center">
                          View Details
                          <ChevronRight className="w-4 h-4 ml-1 group-hover:translate-x-1 transition-transform" />
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

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-r from-primary-600 to-secondary-500">
        <div className="container-custom text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-4xl font-display font-bold text-white mb-6">
              Need Help Choosing?
            </h2>
            <p className="text-xl text-white/90 mb-8 max-w-2xl mx-auto">
              Our travel experts are here to help you plan the perfect Egyptian adventure.
              Contact us for personalized recommendations.
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <Link href="/contact" className="btn bg-white text-primary-600 hover:bg-gray-100 btn-lg">
                Get Free Consultation
              </Link>
              <Link href="/tours" className="btn btn-outline border-white text-white hover:bg-white/10 btn-lg">
                Browse All Tours
              </Link>
            </div>
          </motion.div>
        </div>
      </section>
    </div>
  );
}
