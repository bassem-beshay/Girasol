'use client';

import { useState, useEffect, useCallback } from 'react';
import { useQuery } from '@tanstack/react-query';
import { toursApi, fixImageUrl } from '@/lib/api';
import { motion, AnimatePresence } from 'framer-motion';
import Link from 'next/link';
import Image from 'next/image';
import {
  Sparkles,
  Timer,
  ChevronLeft,
  ChevronRight,
  ArrowRight,
  Loader2,
} from 'lucide-react';
import { useInView } from '@/hooks/useInView';

interface EarlyBookingTour {
  id: number;
  name: string;
  slug: string;
  featured_image: string | null;
  days: number;
  nights: number;
  duration_display: string;
  original_price: number;
  early_booking_price: number;
  discount_percentage: number;
  currency: string;
  average_rating: number;
  review_count: number;
}

interface EarlyBookingOffer {
  id: number;
  title: string;
  title_ar: string;
  subtitle: string;
  description: string;
  discount_percentage: number;
  offer_end_date: string;
  tours_with_early_price: EarlyBookingTour[];
  benefits: string[];
  badge_text: string;
  banner_image: string | null;
  background_color: string;
  is_currently_active: boolean;
  is_featured: boolean;
}

interface EarlyBookingResponse {
  count: number;
  results: EarlyBookingOffer[];
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
    const calculate = () => {
      const now = new Date().getTime();
      const end = new Date(endDate).getTime();
      const distance = end - now;
      if (distance < 0) return { days: 0, hours: 0, minutes: 0, seconds: 0 };
      return {
        days: Math.floor(distance / (1000 * 60 * 60 * 24)),
        hours: Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
        minutes: Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)),
        seconds: Math.floor((distance % (1000 * 60)) / 1000),
      };
    };
    setTimeLeft(calculate());
    const timer = setInterval(() => setTimeLeft(calculate()), 1000);
    return () => clearInterval(timer);
  }, [endDate]);

  return (
    <div className="flex items-center gap-2 sm:gap-3">
      <div className="text-center">
        <div className="bg-white/20 backdrop-blur-sm rounded-lg px-3 py-2 min-w-[50px] sm:min-w-[60px]">
          <span className="text-2xl sm:text-3xl md:text-4xl font-bold text-white font-mono">
            {String(timeLeft.days).padStart(2, '0')}
          </span>
        </div>
        <span className="text-[10px] sm:text-xs text-white/70 mt-1 block">Days</span>
      </div>
      <span className="text-xl sm:text-2xl text-white/50 font-bold -mt-4">:</span>
      <div className="text-center">
        <div className="bg-white/20 backdrop-blur-sm rounded-lg px-3 py-2 min-w-[50px] sm:min-w-[60px]">
          <span className="text-2xl sm:text-3xl md:text-4xl font-bold text-white font-mono">
            {String(timeLeft.hours).padStart(2, '0')}
          </span>
        </div>
        <span className="text-[10px] sm:text-xs text-white/70 mt-1 block">Hours</span>
      </div>
      <span className="text-xl sm:text-2xl text-white/50 font-bold -mt-4">:</span>
      <div className="text-center">
        <div className="bg-white/20 backdrop-blur-sm rounded-lg px-3 py-2 min-w-[50px] sm:min-w-[60px]">
          <span className="text-2xl sm:text-3xl md:text-4xl font-bold text-white font-mono">
            {String(timeLeft.minutes).padStart(2, '0')}
          </span>
        </div>
        <span className="text-[10px] sm:text-xs text-white/70 mt-1 block">Mins</span>
      </div>
      <span className="text-xl sm:text-2xl text-white/50 font-bold -mt-4">:</span>
      <div className="text-center">
        <div className="bg-white/20 backdrop-blur-sm rounded-lg px-3 py-2 min-w-[50px] sm:min-w-[60px]">
          <span className="text-2xl sm:text-3xl md:text-4xl font-bold text-white font-mono">
            {String(timeLeft.seconds).padStart(2, '0')}
          </span>
        </div>
        <span className="text-[10px] sm:text-xs text-white/70 mt-1 block">Secs</span>
      </div>
    </div>
  );
}

export function EarlyBookingSlider() {
  const [currentSlide, setCurrentSlide] = useState(0);
  const [isPaused, setIsPaused] = useState(false);
  const [ref, isInView] = useInView<HTMLElement>({ rootMargin: '200px' });

  const { data, isLoading, error } = useQuery<EarlyBookingResponse>({
    queryKey: ['early-booking-slider'],
    queryFn: async () => {
      const response = await toursApi.getEarlyBookingOffers();
      return response.data;
    },
    enabled: isInView,
    staleTime: 5 * 60 * 1000,
  });

  const offers = data?.results?.filter(o => o.is_currently_active) || [];

  const nextSlide = useCallback(() => {
    if (offers.length > 0) {
      setCurrentSlide((prev) => (prev + 1) % offers.length);
    }
  }, [offers.length]);

  const prevSlide = useCallback(() => {
    if (offers.length > 0) {
      setCurrentSlide((prev) => (prev - 1 + offers.length) % offers.length);
    }
  }, [offers.length]);

  // Auto-slide every 6 seconds
  useEffect(() => {
    if (offers.length <= 1 || isPaused) return;
    const interval = setInterval(nextSlide, 6000);
    return () => clearInterval(interval);
  }, [offers.length, isPaused, nextSlide]);

  if (isLoading || !isInView) {
    return (
      <section ref={ref} className="py-16 bg-gray-100">
        <div className="container-custom">
          <div className="flex items-center justify-center py-20">
            <Loader2 className="w-8 h-8 animate-spin text-primary-500" />
          </div>
        </div>
      </section>
    );
  }

  if (error || offers.length === 0) {
    return <section ref={ref} className="hidden" />;
  }

  const currentOffer = offers[currentSlide];

  return (
    <section
      className="relative overflow-hidden"
      onMouseEnter={() => setIsPaused(true)}
      onMouseLeave={() => setIsPaused(false)}
    >
      <AnimatePresence mode="wait">
        <motion.div
          key={currentOffer.id}
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          transition={{ duration: 0.5 }}
          className="relative min-h-[500px] sm:min-h-[550px] md:min-h-[600px] flex items-center"
        >
          {/* Background Image */}
          {currentOffer.banner_image ? (
            <Image
              src={fixImageUrl(currentOffer.banner_image) || ''}
              alt={currentOffer.title}
              fill
              className="object-cover"
              priority
            />
          ) : (
            <div
              className="absolute inset-0"
              style={{
                background: `linear-gradient(135deg, ${currentOffer.background_color} 0%, ${currentOffer.background_color}dd 50%, ${currentOffer.background_color}99 100%)`
              }}
            />
          )}

          {/* Overlay */}
          <div className="absolute inset-0 bg-black/50" />

          {/* Decorative Elements */}
          <div className="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none">
            <div className="absolute top-10 left-10 w-64 h-64 bg-white/5 rounded-full blur-3xl" />
            <div className="absolute bottom-10 right-10 w-96 h-96 bg-white/5 rounded-full blur-3xl" />
          </div>

          {/* Content */}
          <div className="relative z-10 container-custom py-16 sm:py-20">
            <div className="max-w-4xl mx-auto text-center">
              {/* Badge */}
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.2 }}
                className="inline-flex items-center gap-2 px-5 py-2.5 rounded-full bg-white/15 backdrop-blur-sm text-white text-sm font-semibold mb-6 border border-white/20"
              >
                <Sparkles className="w-4 h-4" />
                {currentOffer.badge_text || 'Early Bird Offer'}
              </motion.div>

              {/* Title */}
              <motion.h2
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.3 }}
                className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-display font-bold text-white mb-4"
              >
                {currentOffer.title}
              </motion.h2>

              {/* Discount */}
              <motion.div
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: 0.4 }}
                className="mb-6"
              >
                <span className="text-5xl sm:text-6xl md:text-7xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-yellow-300 to-orange-400">
                  {currentOffer.discount_percentage}% OFF
                </span>
              </motion.div>

              {/* Subtitle */}
              <motion.p
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.5 }}
                className="text-lg sm:text-xl text-white/80 mb-8 max-w-2xl mx-auto"
              >
                {currentOffer.subtitle || currentOffer.description}
              </motion.p>

              {/* Countdown */}
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.6 }}
                className="mb-10"
              >
                <div className="flex items-center justify-center gap-2 text-white/70 text-sm mb-4">
                  <Timer className="w-4 h-4" />
                  <span>Offer Ends In</span>
                </div>
                <div className="flex justify-center">
                  <CountdownTimer endDate={currentOffer.offer_end_date} />
                </div>
              </motion.div>

              {/* Tours Count & CTA */}
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.7 }}
                className="flex flex-col sm:flex-row items-center justify-center gap-4"
              >
                {currentOffer.tours_with_early_price && currentOffer.tours_with_early_price.length > 0 && (
                  <span className="text-white/70 text-sm">
                    {currentOffer.tours_with_early_price.length} tours available
                  </span>
                )}
                <Link
                  href="/tours?early_booking=true"
                  className="inline-flex items-center gap-2 px-8 py-4 bg-white text-gray-900 font-semibold rounded-full hover:bg-gray-100 transition-all hover:scale-105 shadow-xl"
                >
                  View Early Bird Tours
                  <ArrowRight className="w-5 h-5" />
                </Link>
              </motion.div>
            </div>
          </div>
        </motion.div>
      </AnimatePresence>

      {/* Navigation Arrows */}
      {offers.length > 1 && (
        <>
          <button
            onClick={prevSlide}
            className="absolute left-4 sm:left-8 top-1/2 -translate-y-1/2 z-20 w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-white/10 backdrop-blur-sm border border-white/20 flex items-center justify-center text-white hover:bg-white/20 transition-all"
            aria-label="Previous offer"
          >
            <ChevronLeft className="w-6 h-6" />
          </button>
          <button
            onClick={nextSlide}
            className="absolute right-4 sm:right-8 top-1/2 -translate-y-1/2 z-20 w-12 h-12 sm:w-14 sm:h-14 rounded-full bg-white/10 backdrop-blur-sm border border-white/20 flex items-center justify-center text-white hover:bg-white/20 transition-all"
            aria-label="Next offer"
          >
            <ChevronRight className="w-6 h-6" />
          </button>
        </>
      )}

      {/* Dots Indicator */}
      {offers.length > 1 && (
        <div className="absolute bottom-6 sm:bottom-8 left-1/2 -translate-x-1/2 z-20 flex items-center gap-2">
          {offers.map((_, index) => (
            <button
              key={index}
              onClick={() => setCurrentSlide(index)}
              className={`w-2.5 h-2.5 sm:w-3 sm:h-3 rounded-full transition-all ${
                index === currentSlide
                  ? 'bg-white w-8 sm:w-10'
                  : 'bg-white/40 hover:bg-white/60'
              }`}
              aria-label={`Go to slide ${index + 1}`}
            />
          ))}
        </div>
      )}
    </section>
  );
}
