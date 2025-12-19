'use client';

import { Suspense } from 'react';
import { useQuery } from '@tanstack/react-query';
import { useSearchParams } from 'next/navigation';
import { toursApi, fixImageUrl } from '@/lib/api';
import { MapPin, Clock, Star, Users } from 'lucide-react';
import Link from 'next/link';
import Image from 'next/image';

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
  average_rating: string;
  review_count: number;
  difficulty_level: string;
  destination_names: string[];
  max_group_size: number;
}

interface ToursResponse {
  count: number;
  next: string | null;
  previous: string | null;
  results: Tour[];
}

// Page titles for each type
const typeTitles: Record<string, string> = {
  'nile_cruise': 'Nile Cruises',
  'day_tour': 'Day Tours',
  'multi_country': 'Multi-Country Tours',
  'package': 'Package Tours',
};

function ToursLoading() {
  return (
    <div className="min-h-screen pt-32 pb-16">
      <div className="container-custom">
        <div className="text-center">
          <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500 mx-auto"></div>
          <p className="mt-4 text-gray-600">Loading tours...</p>
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
  const searchParams = useSearchParams();
  const typeParam = searchParams.get('type');
  const pageTitle = typeParam ? typeTitles[typeParam] || 'Tours' : 'Explore Our Tours';

  const { data, isLoading, error } = useQuery<ToursResponse>({
    queryKey: ['tours', typeParam],
    queryFn: async () => {
      const params: Record<string, string> = {};
      if (typeParam) {
        params.tour_type = typeParam;
      }
      const response = await toursApi.getAll(params);
      return response.data;
    },
  });

  if (isLoading) {
    return (
      <div className="min-h-screen pt-32 pb-16">
        <div className="container-custom">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500 mx-auto"></div>
            <p className="mt-4 text-gray-600">Loading tours...</p>
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
            <p>Error loading tours. Please try again later.</p>
          </div>
        </div>
      </div>
    );
  }

  const tours = data?.results || [];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-48 sm:h-56 md:h-64 bg-gradient-to-r from-primary-600 to-primary-800">
        <div className="absolute inset-0 bg-black/30"></div>
        <div className="relative container-custom h-full flex items-center justify-center px-4">
          <div className="text-center text-white">
            <h1 className="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold mb-2 sm:mb-4">{pageTitle}</h1>
            <p className="text-sm sm:text-base md:text-xl text-white/80 max-w-xl mx-auto">
              {typeParam
                ? `Browse our ${typeTitles[typeParam]?.toLowerCase() || 'tours'}`
                : 'Discover Egypt with our carefully curated tour packages'
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
              Showing {tours.length} of {data?.count || 0} tours
            </p>
          </div>

          {tours.length === 0 ? (
            <div className="text-center py-16">
              <p className="text-gray-500 text-lg">No tours available at the moment.</p>
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
                      {tour.is_best_seller && (
                        <span className="px-3 py-1 bg-primary-500 text-white text-xs font-medium rounded-full">
                          Best Seller
                        </span>
                      )}
                      {tour.is_new && (
                        <span className="px-3 py-1 bg-green-500 text-white text-xs font-medium rounded-full">
                          New
                        </span>
                      )}
                      {tour.has_discount && tour.discount_percentage && (
                        <span className="px-3 py-1 bg-red-500 text-white text-xs font-medium rounded-full">
                          {tour.discount_percentage}% OFF
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
                        ({tour.review_count} reviews)
                      </span>
                    </div>

                    {/* Group Size - Hidden on very small screens */}
                    <div className="hidden sm:flex items-center text-gray-500 text-sm mb-4">
                      <Users className="w-4 h-4 mr-1" />
                      Max {tour.max_group_size} people
                    </div>

                    {/* Price */}
                    <div className="flex items-center justify-between pt-3 sm:pt-4 border-t">
                      <div>
                        <span className="text-gray-500 text-xs sm:text-sm">From</span>
                        <div className="flex items-center gap-1 sm:gap-2">
                          <span className="text-lg sm:text-xl font-bold text-primary-600">
                            ${parseFloat(tour.discounted_price).toFixed(0)}
                          </span>
                          {tour.has_discount && (
                            <span className="text-xs sm:text-sm text-gray-400 line-through">
                              ${parseFloat(tour.price).toFixed(0)}
                            </span>
                          )}
                        </div>
                      </div>
                      <span className="text-primary-600 font-medium text-sm sm:text-base">
                        View Details
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
