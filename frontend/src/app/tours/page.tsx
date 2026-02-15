'use client';

import { Suspense } from 'react';
import { useQuery } from '@tanstack/react-query';
import { useSearchParams } from 'next/navigation';
import { toursApi, fixImageUrl } from '@/lib/api';
import { MapPin, Clock, Star, Users, Sparkles, Plane } from 'lucide-react';
import Link from 'next/link';
import Image from 'next/image';
import { useLanguageStore } from '@/store/languageStore';
import { toursPageT, t } from '@/lib/translations';

interface Tour {
  id: number;
  name: string;
  slug: string;
  short_description: string;
  featured_image: string | null;
  category: {
    id: number;
    name: string;
    slug: string;
  } | null;
  tour_type: {
    id: number;
    name: string;
    slug: string;
  } | null;
  days: number;
  nights: number;
  duration_display: string;
  price: string;
  discounted_price: string;
  currency: string;
  has_discount: boolean;
  discount_percentage: number | null;
  is_featured: boolean;
  is_best_seller: boolean;
  is_new: boolean;
  is_multi_destination: boolean;
  average_rating: string;
  review_count: number;
  difficulty_level: string;
  destination_names: string[];
  max_group_size: number;
  // Early Booking fields
  is_early_booking: boolean;
  early_booking_discount: number | null;
  early_booking_price: number | null;
  early_booking_badge: string | null;
}

interface ToursResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Tour[];
}

function ToursLoading() {
  const { language } = useLanguageStore();
  return (
    <div className="min-h-screen pt-32 pb-16">
      <div className="container-custom">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500 mx-auto"></div>
          <p className="mt-4 text-gray-600">{t(toursPageT, language, 'loadingTours')}</p>
        </div>
      </div>
    </div>
  );
}

export default function ToursPage() {
  return (
    <Suspense fallback={<ToursLoading />}>
      <ToursContent />
    </Suspense>
  );
}

function ToursContent() {
  const { language } = useLanguageStore();
  const searchParams = useSearchParams();
  const typeParam = searchParams.get('type');
  const earlyBookingParam = searchParams.get('early_booking');
  const multiDestParam = searchParams.get('multi_destination');
  const isEarlyBookingFilter = earlyBookingParam === 'true';
  const isMultiDestFilter = multiDestParam === 'true' || typeParam === 'multi-destination';

  const typeTitles: Record<string, string> = {
    'nile_cruise': t(toursPageT, language, 'nileCruises'),
    'day_tour': t(toursPageT, language, 'dayTours'),
    'multi_country': t(toursPageT, language, 'multiCountryTours'),
    'multi-destination': t(toursPageT, language, 'multiDestinationTours'),
    'package': t(toursPageT, language, 'packageTours'),
  };

  const pageTitle = isEarlyBookingFilter
    ? t(toursPageT, language, 'earlyBirdTours')
    : isMultiDestFilter
      ? t(toursPageT, language, 'multiDestinationTours')
      : typeParam
        ? typeTitles[typeParam] || t(toursPageT, language, 'tours')
        : t(toursPageT, language, 'exploreOurTours');

  const { data, isLoading, error } = useQuery<ToursResponse>({
    queryKey: ['tours', typeParam, earlyBookingParam, multiDestParam],
    queryFn: async () => {
      const params: Record<string, string> = {};
      // For multi-destination, only use is_multi_destination filter (not tour_type)
      if (isMultiDestFilter) {
        params.is_multi_destination = 'true';
      } else if (typeParam) {
        params.tour_type = typeParam;
      }
      const response = await toursApi.getAll(params);
      return response.data;
    },
  });

  // Filter for early booking tours if parameter is set
  const allTours = data?.results || [];
  const tours = isEarlyBookingFilter
    ? allTours.filter(tour => tour.is_early_booking)
    : allTours;

  if (isLoading) {
    return (
      <div className="min-h-screen pt-32 pb-16">
        <div className="container-custom">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500 mx-auto"></div>
            <p className="mt-4 text-gray-600">{t(toursPageT, language, 'loadingTours')}</p>
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
            <p>{t(toursPageT, language, 'errorLoading')}</p>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className={`relative h-[40vh] sm:h-[50vh] md:h-[70vh] lg:h-[110vh] min-h-[250px] sm:min-h-[300px] md:min-h-[400px] lg:min-h-[600px] ${
        isEarlyBookingFilter
          ? 'bg-gradient-to-r from-orange-500 to-amber-600'
          : isMultiDestFilter
            ? 'bg-gradient-to-r from-blue-600 to-indigo-700'
            : 'bg-gradient-to-r from-primary-600 to-primary-800'
      }`}>
        {!isEarlyBookingFilter && (
          <div
            className="absolute inset-0 bg-cover bg-bottom"
            style={{ backgroundImage: `url(${process.env.NEXT_PUBLIC_API_URL?.replace('/api', '')}/media/tours/tours-hero.jpg)` }}
          />
        )}
        <div className="absolute inset-0 bg-black/40"></div>
        <div className="relative container-custom h-full flex items-center justify-center px-4">
          <div className="text-center text-white">
            {isEarlyBookingFilter && (
              <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/20 text-sm font-medium mb-3">
                <Sparkles className="w-4 h-4" />
                {t(toursPageT, language, 'limitedTimeOffers')}
              </div>
            )}
            {isMultiDestFilter && (
              <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-white/20 text-sm font-medium mb-3">
                <Plane className="w-4 h-4" />
                {t(toursPageT, language, 'exploreMultipleCountries')}
              </div>
            )}
            <h1 className="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold mb-2 sm:mb-4">{pageTitle}</h1>
            <p className="text-sm sm:text-base md:text-xl text-white/80 max-w-xl mx-auto">
              {isEarlyBookingFilter
                ? t(toursPageT, language, 'earlyBirdSubtitle')
                : isMultiDestFilter
                  ? t(toursPageT, language, 'multiDestSubtitle')
                  : typeParam
                    ? `${t(toursPageT, language, 'browseOur')} ${typeTitles[typeParam]?.toLowerCase() || t(toursPageT, language, 'tours').toLowerCase()}`
                    : t(toursPageT, language, 'defaultSubtitle')
              }
            </p>
          </div>
        </div>
      </section>

      {/* Tours Grid */}
      <section className="py-8 sm:py-12 md:py-16">
        <div className="container-custom px-4 sm:px-6">
          <div className="mb-4 sm:mb-8">
            <p className="text-gray-600 text-sm sm:text-base">
              {isEarlyBookingFilter
                ? t(toursPageT, language, 'showingEarlyBird').replace('{count}', String(tours.length))
                : t(toursPageT, language, 'showingOf').replace('{count}', String(tours.length)).replace('{total}', String(data?.count || 0))
              }
            </p>
          </div>

          {tours.length === 0 ? (
            <div className="text-center py-16">
              <Sparkles className="w-12 h-12 text-gray-300 mx-auto mb-4" />
              <p className="text-gray-500 text-lg">
                {isEarlyBookingFilter
                  ? t(toursPageT, language, 'noEarlyBird')
                  : t(toursPageT, language, 'noTours')
                }
              </p>
            </div>
          ) : (
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6 lg:gap-8">
              {tours.map((tour) => (
                <Link
                  key={tour.id}
                  href={`/tours/${tour.slug}`}
                  className="group bg-white rounded-xl shadow-lg overflow-hidden hover:shadow-xl transition-shadow"
                >
                  {/* Image */}
                  <div className="relative h-44 sm:h-48 md:h-56 bg-gray-200">
                    {tour.featured_image ? (
                      <Image
                        src={fixImageUrl(tour.featured_image) || ''}
                        alt={tour.name}
                        fill
                        className="object-cover group-hover:scale-105 transition-transform duration-300"
                      />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center bg-gradient-to-br from-primary-100 to-primary-200">
                        <span className="text-primary-400 text-lg font-medium">
                          {tour.name}
                        </span>
                      </div>
                    )}

                    {/* Badges */}
                    <div className="absolute top-4 left-4 flex flex-col gap-2">
                      {tour.is_multi_destination && (
                        <span className="px-3 py-1 bg-gradient-to-r from-blue-600 to-indigo-600 text-white text-xs font-medium rounded-full flex items-center gap-1">
                          <Plane className="w-3 h-3" />
                          {t(toursPageT, language, 'multiDestination')}
                        </span>
                      )}
                      {tour.is_early_booking && (
                        <span className="px-3 py-1 bg-gradient-to-r from-orange-500 to-amber-500 text-white text-xs font-medium rounded-full flex items-center gap-1">
                          <Sparkles className="w-3 h-3" />
                          {tour.early_booking_badge || t(toursPageT, language, 'earlyBird')}
                        </span>
                      )}
                      {tour.is_best_seller && (
                        <span className="px-3 py-1 bg-primary-500 text-white text-xs font-medium rounded-full">
                          {t(toursPageT, language, 'bestSeller')}
                        </span>
                      )}
                      {tour.is_new && (
                        <span className="px-3 py-1 bg-green-500 text-white text-xs font-medium rounded-full">
                          {t(toursPageT, language, 'new')}
                        </span>
                      )}
                      {tour.has_discount && tour.discount_percentage && (
                        <span className="px-3 py-1 bg-red-500 text-white text-xs font-medium rounded-full">
                          {tour.discount_percentage}% {t(toursPageT, language, 'off')}
                        </span>
                      )}
                    </div>

                    {/* Duration Badge */}
                    <div className="absolute bottom-4 left-4">
                      <span className="inline-flex items-center gap-1 px-3 py-1 bg-white/90 rounded-full text-sm font-medium">
                        <Clock className="w-4 h-4" />
                        {tour.duration_display}
                      </span>
                    </div>
                  </div>

                  {/* Content */}
                  <div className="p-4 sm:p-5">
                    {/* Category */}
                    {tour.category && (
                      <span className="text-[10px] sm:text-xs text-primary-600 font-medium uppercase tracking-wide">
                        {tour.category.name}
                      </span>
                    )}

                    {/* Title */}
                    <h3 className="text-base sm:text-lg font-semibold text-gray-900 mt-1 mb-2 group-hover:text-primary-600 transition-colors line-clamp-2">
                      {tour.name}
                    </h3>

                    {/* Destinations */}
                    <div className="flex items-center text-gray-600 text-xs sm:text-sm mb-2 sm:mb-3">
                      <MapPin className="w-3 sm:w-4 h-3 sm:h-4 mr-1 text-primary-500 flex-shrink-0" />
                      <span className="truncate">{tour.destination_names.join(', ')}</span>
                    </div>

                    {/* Rating */}
                    <div className="flex items-center gap-2 mb-2 sm:mb-3">
                      <div className="flex items-center">
                        <Star className="w-3 sm:w-4 h-3 sm:h-4 text-yellow-400 fill-current" />
                        <span className="ml-1 text-xs sm:text-sm font-medium">
                          {tour.average_rating}
                        </span>
                      </div>
                      <span className="text-gray-400 text-xs sm:text-sm">
                        ({tour.review_count} {t(toursPageT, language, 'reviews')})
                      </span>
                    </div>

                    {/* Group Size - Hidden on very small screens */}
                    <div className="hidden sm:flex items-center text-gray-500 text-sm mb-4">
                      <Users className="w-4 h-4 mr-1" />
                      {t(toursPageT, language, 'maxPeople').replace('{count}', String(tour.max_group_size))}
                    </div>

                    {/* Price */}
                    <div className="flex items-center justify-between pt-3 sm:pt-4 border-t">
                      <div>
                        <span className="text-gray-500 text-xs sm:text-sm">
                          {tour.is_early_booking ? t(toursPageT, language, 'earlyBird') : t(toursPageT, language, 'from')}
                        </span>
                        <div className="flex items-center gap-1 sm:gap-2">
                          <span className={`text-lg sm:text-xl font-bold ${tour.is_early_booking ? 'text-orange-500' : 'text-primary-600'}`}>
                            ${tour.early_booking_price || parseFloat(tour.discounted_price).toFixed(0)}
                          </span>
                          {(tour.has_discount || tour.is_early_booking) && (
                            <span className="text-xs sm:text-sm text-gray-400 line-through">
                              ${parseFloat(tour.price).toFixed(0)}
                            </span>
                          )}
                        </div>
                      </div>
                      <span className="text-primary-600 font-medium text-sm sm:text-base">
                        {t(toursPageT, language, 'viewDetails')}
                      </span>
                    </div>
                  </div>
                </Link>
              ))}
            </div>
          )}
        </div>
      </section>
    </div>
  );
}
