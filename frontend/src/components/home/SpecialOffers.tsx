'use client';

import { useState, useEffect, useMemo } from 'react';
import { useQuery } from '@tanstack/react-query';
import { toursApi } from '@/lib/api';
import { motion } from 'framer-motion';
import Link from 'next/link';
import Image from 'next/image';
import { Clock, ArrowRight, Loader2, Tag } from 'lucide-react';
import { formatCurrency } from '@/lib/utils';

interface Tour {
  id: number;
  name: string;
  slug: string;
  featured_image: string | null;
  days: number;
  nights: number;
  duration_display: string;
  price: string;
  discounted_price: string;
  has_discount: boolean;
  discount_percentage: number | null;
}

interface ToursResponse {
  count: number;
  results: Tour[];
}

// Countdown timer component
function CountdownTimer({ endDate }: { endDate: Date }) {
  const [timeLeft, setTimeLeft] = useState({
    days: 0,
    hours: 0,
    minutes: 0,
    seconds: 0,
  });

  useEffect(() => {
    const timer = setInterval(() => {
      const now = new Date().getTime();
      const distance = endDate.getTime() - now;

      if (distance < 0) {
        clearInterval(timer);
        return;
      }

      setTimeLeft({
        days: Math.floor(distance / (1000 * 60 * 60 * 24)),
        hours: Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
        minutes: Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)),
        seconds: Math.floor((distance % (1000 * 60)) / 1000),
      });
    }, 1000);

    return () => clearInterval(timer);
  }, [endDate]);

  return (
    <div className="flex gap-4">
      {Object.entries(timeLeft).map(([unit, value]) => (
        <div key={unit} className="text-center">
          <div className="bg-white/20 backdrop-blur-sm rounded-lg px-4 py-2 min-w-[60px]">
            <div className="text-2xl font-bold text-white">
              {String(value).padStart(2, '0')}
            </div>
          </div>
          <div className="text-xs text-white/80 mt-1 uppercase">{unit}</div>
        </div>
      ))}
    </div>
  );
}

export function SpecialOffers() {
  // Fetch tours with discounts
  const { data, isLoading } = useQuery<ToursResponse>({
    queryKey: ['discounted-tours'],
    queryFn: async () => {
      const response = await toursApi.getAll({ has_discount: true });
      return response.data;
    },
  });

  const discountedTours = data?.results?.filter(t => t.has_discount).slice(0, 2) || [];
  const featuredOffer = discountedTours[0];

  // Offer end date: 7 days from now
  const offerEndDate = useMemo(() => {
    const endDate = new Date();
    endDate.setDate(endDate.getDate() + 7);
    return endDate;
  }, []);

  // Don't render if no discounted tours
  if (!isLoading && discountedTours.length === 0) {
    return null;
  }

  return (
    <section className="relative py-24 overflow-hidden">
      {/* Background */}
      <div className="absolute inset-0 bg-gradient-to-r from-primary-900 via-primary-800 to-primary-600" />

      {/* Pattern overlay */}
      <div className="absolute inset-0 bg-hero-pattern opacity-5" />

      <div className="container-custom relative z-10">
        {isLoading ? (
          <div className="flex items-center justify-center py-16">
            <Loader2 className="w-8 h-8 animate-spin text-white" />
            <span className="ml-3 text-white">Loading offers...</span>
          </div>
        ) : (
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            {/* Content */}
            <motion.div
              initial={{ opacity: 0, x: -20 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
            >
              <span className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/10 text-white text-sm mb-6">
                <Clock className="w-4 h-4" />
                Limited Time Offer
              </span>

              <h2 className="text-4xl md:text-5xl font-display font-bold text-white mb-6">
                Save Up to <span className="text-primary-300">
                  {Math.max(...discountedTours.map(t => t.discount_percentage || 0))}%
                </span> on
                Early Bookings
              </h2>

              <p className="text-lg text-white/80 mb-8">
                Book your dream Egyptian adventure now and enjoy exclusive
                discounts on our most popular packages. Don&apos;t miss this
                opportunity to explore the land of pharaohs!
              </p>

              {/* Offer details */}
              <div className="grid grid-cols-2 gap-6 mb-8">
                {discountedTours.map((tour) => (
                  <Link
                    key={tour.id}
                    href={`/tours/${tour.slug}`}
                    className="bg-white/10 backdrop-blur-sm rounded-xl p-4 hover:bg-white/20 transition-colors"
                  >
                    <div className="text-3xl font-bold text-white mb-1">
                      {formatCurrency(parseFloat(tour.discounted_price))}
                    </div>
                    <div className="text-sm text-white/60 line-through">
                      {formatCurrency(parseFloat(tour.price))}
                    </div>
                    <div className="text-primary-300 font-medium mt-1">
                      {tour.name}
                    </div>
                    {tour.discount_percentage && (
                      <span className="inline-flex items-center gap-1 mt-2 text-xs text-white/80">
                        <Tag className="w-3 h-3" />
                        {tour.discount_percentage}% OFF
                      </span>
                    )}
                  </Link>
                ))}
              </div>

              {/* Countdown */}
              <div className="mb-8">
                <div className="text-sm text-white/60 mb-3">Offer ends in:</div>
                <CountdownTimer endDate={offerEndDate} />
              </div>

              {/* CTA */}
              <Link
                href="/offers"
                className="btn btn-lg bg-white text-primary-600 hover:bg-gray-100"
              >
                View All Offers
                <ArrowRight className="w-5 h-5 ml-2" />
              </Link>
            </motion.div>

            {/* Image/Card */}
            {featuredOffer && (
              <motion.div
                initial={{ opacity: 0, x: 20 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                className="relative hidden lg:block"
              >
                <Link href={`/tours/${featuredOffer.slug}`}>
                  <div className="relative aspect-[4/5] rounded-2xl overflow-hidden">
                    {featuredOffer.featured_image ? (
                      <Image
                        src={featuredOffer.featured_image}
                        alt={featuredOffer.name}
                        fill
                        className="object-cover"
                      />
                    ) : (
                      <div className="w-full h-full bg-gradient-to-br from-primary-400 to-primary-600" />
                    )}
                    <div className="absolute inset-0 bg-gradient-to-t from-black/60 to-transparent" />

                    {/* Discount badge */}
                    {featuredOffer.discount_percentage && (
                      <div className="absolute top-6 right-6 w-20 h-20 rounded-full bg-primary-500 flex items-center justify-center">
                        <div className="text-center">
                          <div className="text-2xl font-bold text-white">
                            {featuredOffer.discount_percentage}%
                          </div>
                          <div className="text-xs text-white/80">OFF</div>
                        </div>
                      </div>
                    )}

                    {/* Content */}
                    <div className="absolute inset-x-0 bottom-0 p-8">
                      <div className="text-white/80 text-sm mb-2">
                        {featuredOffer.duration_display || `${featuredOffer.days} Days / ${featuredOffer.nights} Nights`}
                      </div>
                      <h3 className="text-2xl font-bold text-white mb-4">
                        {featuredOffer.name}
                      </h3>
                      <div className="flex items-center gap-4">
                        <div>
                          <span className="text-3xl font-bold text-white">
                            {formatCurrency(parseFloat(featuredOffer.discounted_price))}
                          </span>
                          <span className="text-white/60 text-sm ml-2 line-through">
                            {formatCurrency(parseFloat(featuredOffer.price))}
                          </span>
                        </div>
                      </div>
                    </div>
                  </div>
                </Link>

                {/* Decorative elements */}
                <div className="absolute -bottom-6 -left-6 w-32 h-32 bg-primary-400/30 rounded-full blur-2xl" />
                <div className="absolute -top-6 -right-6 w-24 h-24 bg-secondary-400/30 rounded-full blur-xl" />
              </motion.div>
            )}
          </div>
        )}
      </div>
    </section>
  );
}
