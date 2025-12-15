'use client';

import { useQuery } from '@tanstack/react-query';
import { destinationsApi, toursApi } from '@/lib/api';
import { useParams } from 'next/navigation';
import Link from 'next/link';
import Image from 'next/image';
import { motion } from 'framer-motion';
import {
  MapPin,
  Clock,
  Star,
  Calendar,
  ChevronRight,
  Thermometer,
  Info,
} from 'lucide-react';

interface Activity {
  id: number;
  name: string;
  description: string;
  price_from: string;
  duration: string;
}

interface DestinationDetail {
  id: number;
  name: string;
  name_ar: string;
  slug: string;
  tagline: string;
  description: string;
  description_ar: string;
  featured_image: string | null;
  gallery_images: string[];
  country: string;
  region: string;
  latitude: string;
  longitude: string;
  best_time_to_visit: string;
  is_featured: boolean;
  tour_count: number;
  activities: Activity[];
}

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
  average_rating: string;
  review_count: number;
  destination_names: string[];
}

export default function DestinationDetailPage() {
  const params = useParams();
  const slug = params.slug as string;

  const { data: destination, isLoading, error } = useQuery<DestinationDetail>({
    queryKey: ['destination', slug],
    queryFn: async () => {
      const response = await destinationsApi.getBySlug(slug);
      return response.data;
    },
    enabled: !!slug,
  });

  const { data: toursData } = useQuery({
    queryKey: ['destination-tours', slug],
    queryFn: async () => {
      const response = await toursApi.getByDestination(slug);
      return response.data;
    },
    enabled: !!slug,
  });

  if (isLoading) {
    return (
      <div className="min-h-screen pt-32 pb-16">
        <div className="container-custom">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500 mx-auto"></div>
            <p className="mt-4 text-gray-600">Loading destination...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error || !destination) {
    return (
      <div className="min-h-screen pt-32 pb-16">
        <div className="container-custom">
          <div className="text-center">
            <h1 className="text-2xl font-bold text-gray-900 mb-4">Destination Not Found</h1>
            <p className="text-gray-600 mb-8">The destination you&apos;re looking for doesn&apos;t exist.</p>
            <Link href="/destinations" className="btn btn-primary btn-md">
              Browse All Destinations
            </Link>
          </div>
        </div>
      </div>
    );
  }

  const tours: Tour[] = toursData?.results || [];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[60vh] min-h-[500px]">
        <div className="absolute inset-0 bg-black/40 z-10" />
        {destination.featured_image ? (
          <Image
            src={destination.featured_image}
            alt={destination.name}
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
            >
              <span className="text-primary-400 text-lg font-medium mb-2 block">
                {destination.tagline}
              </span>
              <h1 className="text-5xl md:text-6xl font-display font-bold text-white mb-4">
                {destination.name}
              </h1>
              <div className="flex flex-wrap items-center gap-6 text-white/90">
                <div className="flex items-center gap-2">
                  <MapPin className="w-5 h-5" />
                  <span>{destination.region}, {destination.country}</span>
                </div>
                <div className="flex items-center gap-2">
                  <Calendar className="w-5 h-5" />
                  <span>{destination.tour_count} Tours Available</span>
                </div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Main Content */}
      <section className="py-12">
        <div className="container-custom">
          <div className="grid lg:grid-cols-3 gap-8">
            {/* Left Column */}
            <div className="lg:col-span-2 space-y-8">
              {/* About */}
              <div className="bg-white rounded-2xl p-6 shadow-md">
                <h2 className="text-2xl font-bold text-gray-900 mb-4">About {destination.name}</h2>
                <p className="text-gray-600 leading-relaxed whitespace-pre-line">
                  {destination.description}
                </p>
              </div>

              {/* Activities */}
              {destination.activities && destination.activities.length > 0 && (
                <div className="bg-white rounded-2xl p-6 shadow-md">
                  <h2 className="text-2xl font-bold text-gray-900 mb-6">Things to Do</h2>
                  <div className="grid md:grid-cols-2 gap-4">
                    {destination.activities.map((activity) => (
                      <div
                        key={activity.id}
                        className="p-4 border rounded-xl hover:border-primary-500 transition-colors"
                      >
                        <h3 className="font-semibold text-gray-900 mb-2">{activity.name}</h3>
                        <p className="text-sm text-gray-600 mb-3">{activity.description}</p>
                        <div className="flex items-center justify-between text-sm">
                          <span className="text-primary-600 font-medium">
                            From ${parseFloat(activity.price_from).toFixed(0)}
                          </span>
                          <span className="text-gray-500">
                            <Clock className="w-4 h-4 inline mr-1" />
                            {activity.duration}
                          </span>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Tours in this Destination */}
              {tours.length > 0 && (
                <div className="bg-white rounded-2xl p-6 shadow-md">
                  <div className="flex items-center justify-between mb-6">
                    <h2 className="text-2xl font-bold text-gray-900">Tours in {destination.name}</h2>
                    <Link
                      href={`/tours?destination=${destination.slug}`}
                      className="text-primary-600 font-medium flex items-center gap-1 hover:underline"
                    >
                      View All
                      <ChevronRight className="w-4 h-4" />
                    </Link>
                  </div>

                  <div className="grid md:grid-cols-2 gap-6">
                    {tours.slice(0, 4).map((tour) => (
                      <Link
                        key={tour.id}
                        href={`/tours/${tour.slug}`}
                        className="group block bg-gray-50 rounded-xl overflow-hidden hover:shadow-md transition-shadow"
                      >
                        <div className="relative h-40">
                          {tour.featured_image ? (
                            <Image
                              src={tour.featured_image}
                              alt={tour.name}
                              fill
                              className="object-cover group-hover:scale-105 transition-transform duration-300"
                            />
                          ) : (
                            <div className="w-full h-full bg-gradient-to-br from-primary-100 to-primary-200 flex items-center justify-center">
                              <MapPin className="w-8 h-8 text-primary-400" />
                            </div>
                          )}
                          {tour.has_discount && tour.discount_percentage && (
                            <span className="absolute top-2 left-2 px-2 py-1 bg-red-500 text-white text-xs font-medium rounded">
                              {tour.discount_percentage}% OFF
                            </span>
                          )}
                        </div>
                        <div className="p-4">
                          <h3 className="font-semibold text-gray-900 mb-1 group-hover:text-primary-600 transition-colors">
                            {tour.name}
                          </h3>
                          <div className="flex items-center gap-2 text-sm text-gray-500 mb-2">
                            <Clock className="w-4 h-4" />
                            {tour.duration_display}
                            <span className="mx-1">|</span>
                            <Star className="w-4 h-4 text-yellow-400 fill-current" />
                            {tour.average_rating}
                          </div>
                          <div className="flex items-center justify-between">
                            <span className="text-primary-600 font-bold">
                              ${parseFloat(tour.discounted_price).toFixed(0)}
                            </span>
                            {tour.has_discount && (
                              <span className="text-gray-400 text-sm line-through">
                                ${parseFloat(tour.price).toFixed(0)}
                              </span>
                            )}
                          </div>
                        </div>
                      </Link>
                    ))}
                  </div>
                </div>
              )}
            </div>

            {/* Right Column - Info Card */}
            <div className="lg:col-span-1">
              <div className="sticky top-32 space-y-6">
                {/* Travel Info */}
                <div className="bg-white rounded-2xl p-6 shadow-md">
                  <h3 className="text-xl font-bold text-gray-900 mb-4">Travel Information</h3>

                  <div className="space-y-4">
                    <div className="flex items-start gap-3">
                      <Thermometer className="w-5 h-5 text-primary-500 mt-1" />
                      <div>
                        <div className="font-medium text-gray-900">Best Time to Visit</div>
                        <div className="text-sm text-gray-600">{destination.best_time_to_visit}</div>
                      </div>
                    </div>

                    <div className="flex items-start gap-3">
                      <MapPin className="w-5 h-5 text-primary-500 mt-1" />
                      <div>
                        <div className="font-medium text-gray-900">Location</div>
                        <div className="text-sm text-gray-600">{destination.region}, {destination.country}</div>
                      </div>
                    </div>

                    <div className="flex items-start gap-3">
                      <Info className="w-5 h-5 text-primary-500 mt-1" />
                      <div>
                        <div className="font-medium text-gray-900">Tours Available</div>
                        <div className="text-sm text-gray-600">{destination.tour_count} tours from this destination</div>
                      </div>
                    </div>
                  </div>
                </div>

                {/* CTA */}
                <div className="bg-gradient-to-br from-primary-500 to-primary-600 rounded-2xl p-6 text-white">
                  <h3 className="text-xl font-bold mb-2">Plan Your Visit</h3>
                  <p className="text-white/80 text-sm mb-4">
                    Let our experts help you plan the perfect trip to {destination.name}.
                  </p>
                  <Link
                    href="/contact"
                    className="btn bg-white text-primary-600 hover:bg-gray-100 w-full"
                  >
                    Get Free Quote
                  </Link>
                </div>

                {/* Quick Links */}
                <div className="bg-gray-50 rounded-2xl p-6">
                  <h3 className="font-semibold text-gray-900 mb-4">Explore More</h3>
                  <div className="space-y-2">
                    <Link
                      href="/tours"
                      className="flex items-center justify-between p-3 bg-white rounded-lg hover:bg-primary-50 transition-colors"
                    >
                      <span className="text-gray-700">All Tours</span>
                      <ChevronRight className="w-4 h-4 text-gray-400" />
                    </Link>
                    <Link
                      href="/destinations"
                      className="flex items-center justify-between p-3 bg-white rounded-lg hover:bg-primary-50 transition-colors"
                    >
                      <span className="text-gray-700">All Destinations</span>
                      <ChevronRight className="w-4 h-4 text-gray-400" />
                    </Link>
                    <Link
                      href="/contact"
                      className="flex items-center justify-between p-3 bg-white rounded-lg hover:bg-primary-50 transition-colors"
                    >
                      <span className="text-gray-700">Contact Us</span>
                      <ChevronRight className="w-4 h-4 text-gray-400" />
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}
