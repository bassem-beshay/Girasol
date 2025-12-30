'use client';

import { useQuery } from '@tanstack/react-query';
import { toursApi } from '@/lib/api';
import { useParams } from 'next/navigation';
import Link from 'next/link';
import Image from 'next/image';
import { motion } from 'framer-motion';
import { useState, useEffect } from 'react';
import {
  MapPin,
  Clock,
  Star,
  Users,
  Calendar,
  Check,
  X,
  Phone,
  Mail,
  Heart,
  Share2,
  Sparkles,
  Timer,
} from 'lucide-react';
import { InquiryForm } from '@/components/tours/InquiryForm';

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
  // Early Booking fields
  is_early_booking: boolean;
  early_booking_discount: number | null;
  early_booking_price: number | null;
  early_booking_badge: string | null;
  early_booking_end_date: string | null;
}

// Countdown Timer Component
function CountdownTimer({ endDate }: { endDate: string }) {
  const [timeLeft, setTimeLeft] = useState({
    days: 0,
    hours: 0,
    minutes: 0,
    seconds: 0,
  });

  useEffect(() => {
    const calculateTimeLeft = () => {
      const now = new Date().getTime();
      const end = new Date(endDate).getTime();
      const distance = end - now;

      if (distance < 0) {
        return { days: 0, hours: 0, minutes: 0, seconds: 0 };
      }

      return {
        days: Math.floor(distance / (1000 * 60 * 60 * 24)),
        hours: Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
        minutes: Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)),
        seconds: Math.floor((distance % (1000 * 60)) / 1000),
      };
    };

    setTimeLeft(calculateTimeLeft());
    const timer = setInterval(() => setTimeLeft(calculateTimeLeft()), 1000);
    return () => clearInterval(timer);
  }, [endDate]);

  return (
    <div className="flex items-center gap-2 text-sm">
      <div className="bg-gray-900 text-white px-2 py-1 rounded font-mono">
        {String(timeLeft.days).padStart(2, '0')}d
      </div>
      <span className="text-orange-500 font-bold">:</span>
      <div className="bg-gray-900 text-white px-2 py-1 rounded font-mono">
        {String(timeLeft.hours).padStart(2, '0')}h
      </div>
      <span className="text-orange-500 font-bold">:</span>
      <div className="bg-gray-900 text-white px-2 py-1 rounded font-mono">
        {String(timeLeft.minutes).padStart(2, '0')}m
      </div>
      <span className="text-orange-500 font-bold">:</span>
      <div className="bg-gray-900 text-white px-2 py-1 rounded font-mono">
        {String(timeLeft.seconds).padStart(2, '0')}s
      </div>
    </div>
  );
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
            <p className="text-gray-600 mb-8">The tour you&apos;re looking for doesn&apos;t exist.</p>
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
                {tour.is_early_booking && (
                  <span className="px-3 py-1 bg-gradient-to-r from-orange-500 to-amber-500 text-white text-sm font-medium rounded-full flex items-center gap-1">
                    <Sparkles className="w-4 h-4" />
                    {tour.early_booking_badge || 'Early Bird'}
                  </span>
                )}
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
                <h2 className="text-2xl font-bold text-gray-900 mb-6">What&apos;s Included</h2>
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
                  {/* Early Bird Banner */}
                  {tour.is_early_booking && tour.early_booking_end_date && (
                    <div className="mb-6 -mx-6 -mt-6 p-4 bg-gradient-to-r from-orange-500 to-amber-500 rounded-t-2xl">
                      <div className="flex items-center gap-2 text-white mb-2">
                        <Sparkles className="w-5 h-5" />
                        <span className="font-bold">{tour.early_booking_badge || 'Early Bird Offer'}</span>
                        <span className="ml-auto bg-white/20 px-2 py-0.5 rounded text-sm">
                          Save {tour.early_booking_discount}%
                        </span>
                      </div>
                      <div className="flex items-center gap-2 text-white/90 text-sm mb-3">
                        <Timer className="w-4 h-4" />
                        <span>Offer ends in:</span>
                      </div>
                      <CountdownTimer endDate={tour.early_booking_end_date} />
                    </div>
                  )}

                  {/* Price */}
                  <div className="mb-6">
                    <span className="text-gray-500 text-sm">
                      {tour.is_early_booking ? 'Early Bird Price' : 'From'}
                    </span>
                    <div className="flex items-baseline gap-2">
                      <span className={`text-3xl font-bold ${tour.is_early_booking ? 'text-orange-500' : 'text-primary-600'}`}>
                        ${tour.early_booking_price || parseFloat(tour.discounted_price).toFixed(0)}
                      </span>
                      {(tour.has_discount || tour.is_early_booking) && (
                        <span className="text-lg text-gray-400 line-through">
                          ${parseFloat(tour.price).toFixed(0)}
                        </span>
                      )}
                      <span className="text-gray-500">/ person</span>
                    </div>
                    {tour.is_early_booking && tour.early_booking_discount && (
                      <span className="inline-block mt-2 px-2 py-1 bg-orange-100 text-orange-600 text-sm font-medium rounded">
                        Early Bird: Save {tour.early_booking_discount}%
                      </span>
                    )}
                    {!tour.is_early_booking && tour.has_discount && tour.discount_percentage && (
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

                </div>

                {/* Inquiry Form */}
                <InquiryForm
                  tourName={tour.name}
                  tourSlug={tour.slug}
                  tourPrice={`$${tour.early_booking_price || parseFloat(tour.discounted_price).toFixed(0)} per person`}
                  tourDuration={tour.duration_display}
                />

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
