'use client';

import { useQuery } from '@tanstack/react-query';
import { toursApi } from '@/lib/api';
import { useParams } from 'next/navigation';
import Link from 'next/link';
import Image from 'next/image';
import { motion } from 'framer-motion';
import {
  MapPin,
  Clock,
  Star,
  Users,
  Calendar,
  Check,
  X,
  ChevronRight,
  Phone,
  Mail,
  Heart,
  Share2,
} from 'lucide-react';

interface TourDetail {
  id: number;
  name: string;
  name_ar: string;
  slug: string;
  short_description: string;
  description: string;
  featured_image: string | null;
  gallery_images: string[];
  category: {
    id: number;
    name: string;
    slug: string;
  } | null;
  tour_type: string;
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
  departure_city: string;
  languages: string;
  min_group_size: number;
  max_group_size: number;
  destination_names: string[];
  destinations: Array<{
    id: number;
    name: string;
    slug: string;
  }>;
  highlights: Array<{
    id: number;
    title: string;
    description: string;
    icon: string;
  }>;
  inclusions: Array<{
    id: number;
    item: string;
    is_included: boolean;
  }>;
  itinerary: Array<{
    id: number;
    day_number: number;
    title: string;
    description: string;
    locations: string;
    meals_included: string;
    accommodation: string;
  }>;
}

export default function TourDetailPage() {
  const params = useParams();
  const slug = params.slug as string;

  const { data: tour, isLoading, error } = useQuery<TourDetail>({
    queryKey: ['tour', slug],
    queryFn: async () => {
      const response = await toursApi.getBySlug(slug);
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
            <p className="mt-4 text-gray-600">Loading tour details...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error || !tour) {
    return (
      <div className="min-h-screen pt-32 pb-16">
        <div className="container-custom">
          <div className="text-center">
            <h1 className="text-2xl font-bold text-gray-900 mb-4">Tour Not Found</h1>
            <p className="text-gray-600 mb-8">The tour you're looking for doesn't exist.</p>
            <Link href="/tours" className="btn btn-primary btn-md">
              Browse All Tours
            </Link>
          </div>
        </div>
      </div>
    );
  }

  const included = tour.inclusions?.filter(i => i.is_included) || [];
  const notIncluded = tour.inclusions?.filter(i => !i.is_included) || [];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[60vh] min-h-[500px]">
        <div className="absolute inset-0 bg-black/40 z-10" />
        {tour.featured_image ? (
          <Image
            src={tour.featured_image}
            alt={tour.name}
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
              {/* Badges */}
              <div className="flex flex-wrap gap-2 mb-4">
                {tour.is_best_seller && (
                  <span className="px-3 py-1 bg-primary-500 text-white text-sm font-medium rounded-full">
                    Best Seller
                  </span>
                )}
                {tour.is_new && (
                  <span className="px-3 py-1 bg-green-500 text-white text-sm font-medium rounded-full">
                    New
                  </span>
                )}
                {tour.has_discount && tour.discount_percentage && (
                  <span className="px-3 py-1 bg-red-500 text-white text-sm font-medium rounded-full">
                    {tour.discount_percentage}% OFF
                  </span>
                )}
                {tour.category && (
                  <span className="px-3 py-1 bg-white/20 backdrop-blur text-white text-sm font-medium rounded-full">
                    {tour.category.name}
                  </span>
                )}
              </div>

              <h1 className="text-4xl md:text-5xl font-display font-bold text-white mb-4">
                {tour.name}
              </h1>

              <div className="flex flex-wrap items-center gap-6 text-white/90">
                <div className="flex items-center gap-2">
                  <MapPin className="w-5 h-5" />
                  <span>{tour.destination_names?.join(', ') || 'Egypt'}</span>
                </div>
                <div className="flex items-center gap-2">
                  <Clock className="w-5 h-5" />
                  <span>{tour.duration_display || `${tour.days || 0} Days`}</span>
                </div>
                <div className="flex items-center gap-2">
                  <Star className="w-5 h-5 text-yellow-400 fill-current" />
                  <span>{tour.average_rating || 0} ({tour.review_count || 0} reviews)</span>
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
            {/* Left Column - Tour Details */}
            <div className="lg:col-span-2 space-y-8">
              {/* Overview */}
              <div className="bg-white rounded-2xl p-6 shadow-md">
                <h2 className="text-2xl font-bold text-gray-900 mb-4">Overview</h2>
                <p className="text-gray-600 leading-relaxed">{tour.description}</p>

                {/* Quick Info */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-6 pt-6 border-t">
                  <div className="text-center">
                    <Clock className="w-8 h-8 text-primary-500 mx-auto mb-2" />
                    <div className="text-sm text-gray-500">Duration</div>
                    <div className="font-semibold">{tour.duration_display}</div>
                  </div>
                  <div className="text-center">
                    <Users className="w-8 h-8 text-primary-500 mx-auto mb-2" />
                    <div className="text-sm text-gray-500">Group Size</div>
                    <div className="font-semibold">{tour.min_group_size}-{tour.max_group_size}</div>
                  </div>
                  <div className="text-center">
                    <MapPin className="w-8 h-8 text-primary-500 mx-auto mb-2" />
                    <div className="text-sm text-gray-500">Start</div>
                    <div className="font-semibold">{tour.departure_city}</div>
                  </div>
                  <div className="text-center">
                    <Calendar className="w-8 h-8 text-primary-500 mx-auto mb-2" />
                    <div className="text-sm text-gray-500">Difficulty</div>
                    <div className="font-semibold capitalize">{tour.difficulty_level}</div>
                  </div>
                </div>
              </div>

              {/* Highlights */}
              {tour.highlights && tour.highlights.length > 0 && (
                <div className="bg-white rounded-2xl p-6 shadow-md">
                  <h2 className="text-2xl font-bold text-gray-900 mb-6">Tour Highlights</h2>
                  <div className="grid md:grid-cols-2 gap-4">
                    {tour.highlights.map((highlight) => (
                      <div key={highlight.id} className="flex items-start gap-3 p-4 bg-primary-50 rounded-xl">
                        <div className="w-10 h-10 bg-primary-100 rounded-lg flex items-center justify-center flex-shrink-0">
                          <Star className="w-5 h-5 text-primary-600" />
                        </div>
                        <div>
                          <h3 className="font-semibold text-gray-900">{highlight.title}</h3>
                          <p className="text-sm text-gray-600">{highlight.description}</p>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Itinerary */}
              {tour.itinerary && tour.itinerary.length > 0 && (
                <div className="bg-white rounded-2xl p-6 shadow-md">
                  <h2 className="text-2xl font-bold text-gray-900 mb-6">Day by Day Itinerary</h2>
                  <div className="space-y-4">
                    {tour.itinerary.map((day) => (
                      <div key={day.id} className="border rounded-xl p-5">
                        <div className="flex items-center gap-4 mb-3">
                          <span className="w-12 h-12 bg-primary-500 text-white rounded-full flex items-center justify-center font-bold">
                            {day.day_number}
                          </span>
                          <h3 className="text-lg font-semibold text-gray-900">{day.title}</h3>
                        </div>
                        <p className="text-gray-600 mb-4">{day.description}</p>
                        <div className="grid grid-cols-3 gap-4 text-sm">
                          {day.locations && (
                            <div className="flex items-center gap-2 text-gray-500">
                              <MapPin className="w-4 h-4" />
                              {day.locations}
                            </div>
                          )}
                          {day.meals_included && (
                            <div className="flex items-center gap-2 text-gray-500">
                              <span>Meals: {day.meals_included}</span>
                            </div>
                          )}
                          {day.accommodation && (
                            <div className="flex items-center gap-2 text-gray-500">
                              <span>Stay: {day.accommodation}</span>
                            </div>
                          )}
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              )}

              {/* Inclusions */}
              <div className="bg-white rounded-2xl p-6 shadow-md">
                <h2 className="text-2xl font-bold text-gray-900 mb-6">What's Included</h2>
                <div className="grid md:grid-cols-2 gap-8">
                  {included.length > 0 && (
                    <div>
                      <h3 className="font-semibold text-green-600 mb-4 flex items-center gap-2">
                        <Check className="w-5 h-5" />
                        Included
                      </h3>
                      <ul className="space-y-2">
                        {included.map((item) => (
                          <li key={item.id} className="flex items-center gap-2 text-gray-600">
                            <Check className="w-4 h-4 text-green-500" />
                            {item.item}
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                  {notIncluded.length > 0 && (
                    <div>
                      <h3 className="font-semibold text-red-600 mb-4 flex items-center gap-2">
                        <X className="w-5 h-5" />
                        Not Included
                      </h3>
                      <ul className="space-y-2">
                        {notIncluded.map((item) => (
                          <li key={item.id} className="flex items-center gap-2 text-gray-600">
                            <X className="w-4 h-4 text-red-500" />
                            {item.item}
                          </li>
                        ))}
                      </ul>
                    </div>
                  )}
                </div>
              </div>
            </div>

            {/* Right Column - Booking Card */}
            <div className="lg:col-span-1">
              <div className="sticky top-32">
                <div className="bg-white rounded-2xl p-6 shadow-lg">
                  {/* Price */}
                  <div className="mb-6">
                    <span className="text-gray-500 text-sm">From</span>
                    <div className="flex items-baseline gap-2">
                      <span className="text-3xl font-bold text-primary-600">
                        ${parseFloat(tour.discounted_price).toFixed(0)}
                      </span>
                      {tour.has_discount && (
                        <span className="text-lg text-gray-400 line-through">
                          ${parseFloat(tour.price).toFixed(0)}
                        </span>
                      )}
                      <span className="text-gray-500">/ person</span>
                    </div>
                    {tour.has_discount && tour.discount_percentage && (
                      <span className="inline-block mt-2 px-2 py-1 bg-red-100 text-red-600 text-sm font-medium rounded">
                        Save {tour.discount_percentage}%
                      </span>
                    )}
                  </div>

                  {/* Quick Info */}
                  <div className="space-y-3 mb-6 pb-6 border-b">
                    <div className="flex items-center justify-between text-sm">
                      <span className="text-gray-500">Duration</span>
                      <span className="font-medium">{tour.duration_display}</span>
                    </div>
                    <div className="flex items-center justify-between text-sm">
                      <span className="text-gray-500">Group Size</span>
                      <span className="font-medium">Max {tour.max_group_size} people</span>
                    </div>
                    <div className="flex items-center justify-between text-sm">
                      <span className="text-gray-500">Languages</span>
                      <span className="font-medium">{tour.languages}</span>
                    </div>
                  </div>

                  {/* CTA Buttons */}
                  <div className="space-y-3">
                    <a
                      href={`https://wa.me/201060873700?text=${encodeURIComponent(`Hi, I'm interested in booking the tour: ${tour.name}\n\nPrice: $${parseFloat(tour.discounted_price).toFixed(0)} per person\nDuration: ${tour.duration_display}\n\nPlease provide more details.`)}`}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="btn btn-primary btn-lg w-full flex items-center justify-center gap-2"
                    >
                      <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
                      </svg>
                      Book via WhatsApp
                    </a>
                    <Link
                      href="/contact"
                      className="btn btn-outline btn-lg w-full"
                    >
                      Inquire Now
                    </Link>
                  </div>

                  {/* Actions */}
                  <div className="flex items-center justify-center gap-4 mt-6 pt-6 border-t">
                    <button className="flex items-center gap-2 text-gray-500 hover:text-primary-600">
                      <Heart className="w-5 h-5" />
                      Save
                    </button>
                    <button className="flex items-center gap-2 text-gray-500 hover:text-primary-600">
                      <Share2 className="w-5 h-5" />
                      Share
                    </button>
                  </div>
                </div>

                {/* Contact Card */}
                <div className="bg-gray-50 rounded-2xl p-6 mt-6">
                  <h3 className="font-semibold text-gray-900 mb-4">Need Help?</h3>
                  <div className="space-y-3">
                    <a
                      href="tel:+20237715511"
                      className="flex items-center gap-3 text-gray-600 hover:text-primary-600"
                    >
                      <Phone className="w-5 h-5" />
                      +20 2 3771 5511
                    </a>
                    <a
                      href="mailto:info@girasoltours.com"
                      className="flex items-center gap-3 text-gray-600 hover:text-primary-600"
                    >
                      <Mail className="w-5 h-5" />
                      info@girasoltours.com
                    </a>
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
