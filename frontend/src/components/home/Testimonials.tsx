'use client';

import { useQuery } from '@tanstack/react-query';
import { reviewsApi } from '@/lib/api';
import { motion } from 'framer-motion';
import Image from 'next/image';
import { Star, Quote, Loader2, User } from 'lucide-react';
import { useInView } from '@/hooks/useInView';

interface Testimonial {
  id: number;
  name: string;
  country: string;
  avatar: string | null;
  rating: number;
  comment: string;
  tour_name: string | null;
  is_featured: boolean;
}

interface TestimonialsResponse {
  count: number;
  results: Testimonial[];
}

export function Testimonials() {
  const [ref, isInView] = useInView<HTMLElement>({ rootMargin: '200px' });

  const { data, isLoading, error } = useQuery<TestimonialsResponse>({
    queryKey: ['testimonials'],
    queryFn: async () => {
      const response = await reviewsApi.getTestimonials();
      return response.data;
    },
    enabled: isInView,
    staleTime: 5 * 60 * 1000,
  });

  const testimonials = data?.results?.slice(0, 3) || [];

  // Calculate average rating
  const avgRating = testimonials.length > 0
    ? (testimonials.reduce((sum, t) => sum + t.rating, 0) / testimonials.length).toFixed(1)
    : '5.0';

  return (
    <section ref={ref} className="section-padding">
      <div className="container-custom">
        {/* Header */}
        <div className="text-center max-w-2xl mx-auto mb-12">
          <motion.span
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-primary-600 font-medium mb-2 block"
          >
            Testimonials
          </motion.span>
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.1 }}
            className="heading-2 text-gray-900 mb-4"
          >
            What Our Travelers Say
          </motion.h2>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.2 }}
            className="text-gray-600"
          >
            Don&apos;t just take our word for it. Here&apos;s what our guests have to say
            about their Egyptian adventures.
          </motion.p>
        </div>

        {/* Google Rating */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="flex items-center justify-center gap-4 mb-12"
        >
          <div className="flex">
            {[1, 2, 3, 4, 5].map((star) => (
              <Star key={star} className="w-6 h-6 text-gold-400 fill-current" />
            ))}
          </div>
          <div className="text-gray-600">
            <span className="font-bold text-gray-900">{avgRating}</span> out of 5 based on
            <span className="font-medium text-gray-900"> {data?.count || 500}+ reviews</span>
          </div>
        </motion.div>

        {/* Loading state */}
        {isLoading && (
          <div className="flex items-center justify-center py-16">
            <Loader2 className="w-8 h-8 animate-spin text-primary-500" />
            <span className="ml-3 text-gray-600">Loading testimonials...</span>
          </div>
        )}

        {/* Error state */}
        {error && (
          <div className="text-center py-16">
            <p className="text-gray-500">Unable to load testimonials. Please try again later.</p>
          </div>
        )}

        {/* Testimonials grid */}
        {!isLoading && !error && testimonials.length > 0 && (
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            {testimonials.map((testimonial, index) => (
              <motion.div
                key={testimonial.id}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                className="bg-white rounded-2xl p-8 shadow-card relative"
              >
                {/* Quote icon */}
                <Quote className="absolute top-6 right-6 w-10 h-10 text-primary-100" />

                {/* Rating */}
                <div className="flex gap-1 mb-4">
                  {[...Array(testimonial.rating)].map((_, i) => (
                    <Star key={i} className="w-5 h-5 text-gold-400 fill-current" />
                  ))}
                </div>

                {/* Quote */}
                <p className="text-gray-600 mb-6 relative z-10">
                  &ldquo;{testimonial.comment}&rdquo;
                </p>

                {/* Author */}
                <div className="flex items-center gap-4">
                  <div className="relative w-12 h-12 rounded-full overflow-hidden bg-primary-100 flex items-center justify-center">
                    {testimonial.avatar ? (
                      <Image
                        src={testimonial.avatar}
                        alt={testimonial.name}
                        fill
                        className="object-cover"
                      />
                    ) : (
                      <User className="w-6 h-6 text-primary-500" />
                    )}
                  </div>
                  <div>
                    <div className="font-semibold text-gray-900">
                      {testimonial.name}
                    </div>
                    <div className="text-sm text-gray-500">
                      {testimonial.country}
                      {testimonial.tour_name && ` · ${testimonial.tour_name}`}
                    </div>
                  </div>
                </div>
              </motion.div>
            ))}
          </div>
        )}

        {/* Empty state */}
        {!isLoading && !error && testimonials.length === 0 && (
          <div className="text-center py-16">
            <Quote className="w-16 h-16 text-gray-300 mx-auto mb-4" />
            <p className="text-gray-500">No testimonials available at the moment.</p>
          </div>
        )}
      </div>
    </section>
  );
}
