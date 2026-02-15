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
  Camera,
  X,
  ChevronLeft,
  Plane,
  Sun,
} from 'lucide-react';
import { useState } from 'react';
import { useLanguageStore } from '@/store/languageStore';
import { destinationDetailT, t } from '@/lib/translations';

interface Activity {
  id: number;
  name: string;
  description: string;
  price_from: string;
  duration: string;
}

interface DestinationImage {
  id: number;
  image: string;
  caption: string;
  alt_text: string;
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
  images: DestinationImage[];
  country: string;
  region: string;
  latitude: string;
  longitude: string;
  best_time_to_visit: string;
  getting_there: string;
  climate_info: string;
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
  const { language } = useLanguageStore();
  const params = useParams();
  const slug = params.slug as string;
  const [galleryOpen, setGalleryOpen] = useState(false);
  const [currentImageIndex, setCurrentImageIndex] = useState(0);

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
            <p className="mt-4 text-gray-600">{t(destinationDetailT, language, 'loadingDestination')}</p>
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
            <h1 className="text-2xl font-bold text-gray-900 mb-4">{t(destinationDetailT, language, 'destinationNotFound')}</h1>
            <p className="text-gray-600 mb-8">{t(destinationDetailT, language, 'destinationNotFoundDesc')}</p>
            <Link href="/destinations" className="btn btn-primary btn-md">
              {t(destinationDetailT, language, 'browseAllDestinations')}
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
      <section className="relative h-[40vh] sm:h-[50vh] md:h-[70vh] lg:h-[85vh] min-h-[250px] sm:min-h-[300px] md:min-h-[450px] lg:min-h-[700px]">
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

        <div className="absolute inset-0 z-20 flex items-center">
          <div className="container-custom">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
            >
              <span className="text-primary-400 text-sm sm:text-base md:text-lg font-medium mb-1 sm:mb-2 block">
                {destination.tagline}
              </span>
              <h1 className="text-2xl sm:text-3xl md:text-5xl lg:text-6xl font-display font-bold text-white mb-2 sm:mb-4">
                {destination.name}
              </h1>
              <div className="flex flex-wrap items-center gap-6 text-white/90">
                <div className="flex items-center gap-2">
                  <MapPin className="w-5 h-5" />
                  <span>{destination.region}, {destination.country}</span>
                </div>
                <div className="flex items-center gap-2">
                  <Calendar className="w-5 h-5" />
                  <span>{t(destinationDetailT, language, 'toursAvailable').replace('{count}', String(destination.tour_count))}</span>
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
                <h2 className="text-2xl font-bold text-gray-900 mb-4">{t(destinationDetailT, language, 'about').replace('{name}', destination.name)}</h2>
                <p className="text-gray-600 leading-relaxed whitespace-pre-line">
                  {destination.description}
                </p>
              </div>

              {/* Travel Info Section */}
              {(destination.best_time_to_visit || destination.getting_there || destination.climate_info) && (
                <div className="bg-white rounded-2xl p-6 shadow-md">
                  <h2 className="text-2xl font-bold text-gray-900 mb-6">{t(destinationDetailT, language, 'travelInformation')}</h2>
                  <div className="grid md:grid-cols-3 gap-6">
                    {destination.best_time_to_visit && (
                      <div className="bg-gradient-to-br from-blue-50 to-blue-100 rounded-xl p-5">
                        <div className="flex items-center gap-3 mb-3">
                          <div className="w-10 h-10 bg-blue-500 rounded-lg flex items-center justify-center">
                            <Calendar className="w-5 h-5 text-white" />
                          </div>
                          <h3 className="font-semibold text-gray-900">{t(destinationDetailT, language, 'bestTimeToVisit')}</h3>
                        </div>
                        <p className="text-gray-600 text-sm leading-relaxed">
                          {destination.best_time_to_visit}
                        </p>
                      </div>
                    )}
                    {destination.getting_there && (
                      <div className="bg-gradient-to-br from-green-50 to-green-100 rounded-xl p-5">
                        <div className="flex items-center gap-3 mb-3">
                          <div className="w-10 h-10 bg-green-500 rounded-lg flex items-center justify-center">
                            <Plane className="w-5 h-5 text-white" />
                          </div>
                          <h3 className="font-semibold text-gray-900">{t(destinationDetailT, language, 'gettingThere')}</h3>
                        </div>
                        <p className="text-gray-600 text-sm leading-relaxed">
                          {destination.getting_there}
                        </p>
                      </div>
                    )}
                    {destination.climate_info && (
                      <div className="bg-gradient-to-br from-orange-50 to-orange-100 rounded-xl p-5">
                        <div className="flex items-center gap-3 mb-3">
                          <div className="w-10 h-10 bg-orange-500 rounded-lg flex items-center justify-center">
                            <Sun className="w-5 h-5 text-white" />
                          </div>
                          <h3 className="font-semibold text-gray-900">{t(destinationDetailT, language, 'climate')}</h3>
                        </div>
                        <p className="text-gray-600 text-sm leading-relaxed">
                          {destination.climate_info}
                        </p>
                      </div>
                    )}
                  </div>
                </div>
              )}

              {/* Photo Gallery */}
              {destination.images && destination.images.length > 0 && (
                <div className="bg-white rounded-2xl p-6 shadow-md">
                  <div className="flex items-center gap-3 mb-6">
                    <div className="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
                      <Camera className="w-6 h-6 text-purple-600" />
                    </div>
                    <div>
                      <h2 className="text-2xl font-bold text-gray-900">{t(destinationDetailT, language, 'photoGallery')}</h2>
                      <p className="text-sm text-gray-500">{t(destinationDetailT, language, 'photos').replace('{count}', String(destination.images.length))}</p>
                    </div>
                  </div>
                  <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                    {destination.images.map((img, index) => (
                      <div
                        key={img.id}
                        className="relative aspect-[4/3] rounded-xl overflow-hidden cursor-pointer group"
                        onClick={() => {
                          setCurrentImageIndex(index);
                          setGalleryOpen(true);
                        }}
                      >
                        <Image
                          src={img.image}
                          alt={img.alt_text || `${destination.name} photo ${index + 1}`}
                          fill
                          className="object-cover transition-transform duration-300 group-hover:scale-110"
                        />
                        <div className="absolute inset-0 bg-black/0 group-hover:bg-black/30 transition-colors flex items-center justify-center">
                          <Camera className="w-8 h-8 text-white opacity-0 group-hover:opacity-100 transition-opacity" />
                        </div>
                        {img.caption && (
                          <div className="absolute bottom-0 left-0 right-0 p-2 bg-gradient-to-t from-black/70 to-transparent">
                            <p className="text-white text-sm truncate">{img.caption}</p>
                          </div>
                        )}
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Activities */}
              {destination.activities && destination.activities.length > 0 && (
                <div className="bg-white rounded-2xl p-6 shadow-md">
                  <h2 className="text-2xl font-bold text-gray-900 mb-6">{t(destinationDetailT, language, 'thingsToDo')}</h2>
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
                            {t(destinationDetailT, language, 'fromPrice').replace('{price}', parseFloat(activity.price_from).toFixed(0))}
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
                    <h2 className="text-2xl font-bold text-gray-900">{t(destinationDetailT, language, 'toursIn').replace('{name}', destination.name)}</h2>
                    <Link
                      href={`/tours?destination=${destination.slug}`}
                      className="text-primary-600 font-medium flex items-center gap-1 hover:underline"
                    >
                      {t(destinationDetailT, language, 'viewAll')}
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
                  <h3 className="text-xl font-bold text-gray-900 mb-4">{t(destinationDetailT, language, 'travelInformation')}</h3>

                  <div className="space-y-4">
                    <div className="flex items-start gap-3">
                      <Thermometer className="w-5 h-5 text-primary-500 mt-1" />
                      <div>
                        <div className="font-medium text-gray-900">{t(destinationDetailT, language, 'bestTimeToVisit')}</div>
                        <div className="text-sm text-gray-600">{destination.best_time_to_visit}</div>
                      </div>
                    </div>

                    <div className="flex items-start gap-3">
                      <MapPin className="w-5 h-5 text-primary-500 mt-1" />
                      <div>
                        <div className="font-medium text-gray-900">{t(destinationDetailT, language, 'location')}</div>
                        <div className="text-sm text-gray-600">{destination.region}, {destination.country}</div>
                      </div>
                    </div>

                    <div className="flex items-start gap-3">
                      <Info className="w-5 h-5 text-primary-500 mt-1" />
                      <div>
                        <div className="font-medium text-gray-900">{t(destinationDetailT, language, 'toursAvailableInfo')}</div>
                        <div className="text-sm text-gray-600">{t(destinationDetailT, language, 'toursFromDest').replace('{count}', String(destination.tour_count))}</div>
                      </div>
                    </div>
                  </div>
                </div>

                {/* CTA */}
                <div className="bg-gradient-to-br from-primary-500 to-primary-600 rounded-2xl p-6 text-white">
                  <h3 className="text-xl font-bold mb-2">{t(destinationDetailT, language, 'planYourVisit')}</h3>
                  <p className="text-white/80 text-sm mb-4">
                    {t(destinationDetailT, language, 'planYourVisitDesc').replace('{name}', destination.name)}
                  </p>
                  <Link
                    href="/contact"
                    className="btn bg-white text-primary-600 hover:bg-gray-100 w-full"
                  >
                    {t(destinationDetailT, language, 'getFreeQuote')}
                  </Link>
                </div>

                {/* Quick Links */}
                <div className="bg-gray-50 rounded-2xl p-6">
                  <h3 className="font-semibold text-gray-900 mb-4">{t(destinationDetailT, language, 'exploreMore')}</h3>
                  <div className="space-y-2">
                    <Link
                      href="/tours"
                      className="flex items-center justify-between p-3 bg-white rounded-lg hover:bg-primary-50 transition-colors"
                    >
                      <span className="text-gray-700">{t(destinationDetailT, language, 'allTours')}</span>
                      <ChevronRight className="w-4 h-4 text-gray-400" />
                    </Link>
                    <Link
                      href="/destinations"
                      className="flex items-center justify-between p-3 bg-white rounded-lg hover:bg-primary-50 transition-colors"
                    >
                      <span className="text-gray-700">{t(destinationDetailT, language, 'allDestinations')}</span>
                      <ChevronRight className="w-4 h-4 text-gray-400" />
                    </Link>
                    <Link
                      href="/contact"
                      className="flex items-center justify-between p-3 bg-white rounded-lg hover:bg-primary-50 transition-colors"
                    >
                      <span className="text-gray-700">{t(destinationDetailT, language, 'contactUs')}</span>
                      <ChevronRight className="w-4 h-4 text-gray-400" />
                    </Link>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Image Lightbox Modal */}
      {galleryOpen && destination.images && destination.images.length > 0 && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-50 bg-black/95 flex items-center justify-center"
          onClick={() => setGalleryOpen(false)}
        >
          {/* Close Button */}
          <button
            onClick={() => setGalleryOpen(false)}
            className="absolute top-4 right-4 z-10 p-2 bg-white/10 hover:bg-white/20 rounded-full transition-colors"
          >
            <X className="w-6 h-6 text-white" />
          </button>

          {/* Previous Button */}
          <button
            onClick={(e) => {
              e.stopPropagation();
              setCurrentImageIndex((prev) =>
                prev === 0 ? destination.images.length - 1 : prev - 1
              );
            }}
            className="absolute left-4 z-10 p-3 bg-white/10 hover:bg-white/20 rounded-full transition-colors"
          >
            <ChevronLeft className="w-6 h-6 text-white" />
          </button>

          {/* Image */}
          <div
            className="relative w-full max-w-5xl h-[80vh] mx-4"
            onClick={(e) => e.stopPropagation()}
          >
            <Image
              src={destination.images[currentImageIndex].image}
              alt={destination.images[currentImageIndex].alt_text || `${destination.name} photo ${currentImageIndex + 1}`}
              fill
              className="object-contain"
            />
            {destination.images[currentImageIndex].caption && (
              <div className="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/80 to-transparent">
                <p className="text-white text-center text-lg">
                  {destination.images[currentImageIndex].caption}
                </p>
              </div>
            )}
          </div>

          {/* Next Button */}
          <button
            onClick={(e) => {
              e.stopPropagation();
              setCurrentImageIndex((prev) =>
                prev === destination.images.length - 1 ? 0 : prev + 1
              );
            }}
            className="absolute right-4 z-10 p-3 bg-white/10 hover:bg-white/20 rounded-full transition-colors"
          >
            <ChevronRight className="w-6 h-6 text-white" />
          </button>

          {/* Image Counter */}
          <div className="absolute bottom-4 left-1/2 -translate-x-1/2 px-4 py-2 bg-white/10 rounded-full">
            <span className="text-white text-sm">
              {currentImageIndex + 1} / {destination.images.length}
            </span>
          </div>
        </motion.div>
      )}
    </div>
  );
}
