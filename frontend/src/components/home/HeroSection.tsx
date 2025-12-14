'use client';

import { useRef, useEffect } from 'react';
import Link from 'next/link';
import { motion } from 'framer-motion';
import { ChevronRight, Shield, Award, Clock } from 'lucide-react';

const trustBadges = [
  { icon: Shield, label: 'IATA Certified' },
  { icon: Award, label: '25+ Years Experience' },
  { icon: Clock, label: '24/7 Support' },
];

export function HeroSection() {
  const videoRef = useRef<HTMLVideoElement>(null);

  useEffect(() => {
    if (videoRef.current) {
      videoRef.current.play().catch(() => {
        // Autoplay might be blocked by browser
      });
    }
  }, []);

  return (
    <section className="relative h-screen min-h-[600px] max-h-[900px] overflow-hidden">
      {/* Background Video */}
      <div className="absolute inset-0">
        <video
          ref={videoRef}
          autoPlay
          muted
          loop
          playsInline
          className="absolute inset-0 w-full h-full object-cover"
          poster="/images/hero/pyramids.jpg"
        >
          <source src="/videos/hero-video.mp4" type="video/mp4" />
        </video>
      </div>

      {/* Overlay */}
      <div className="absolute inset-0 bg-gradient-to-r from-black/70 via-black/50 to-transparent" />

      {/* Content */}
      <div className="relative h-full container-custom flex flex-col justify-center">
        <div className="max-w-2xl">
          {/* Badge */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 }}
          >
            <span className="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/10 backdrop-blur-sm text-white text-sm mb-6">
              <span className="w-2 h-2 rounded-full bg-primary-500 animate-pulse" />
              Trusted by 50,000+ travelers worldwide
            </span>
          </motion.div>

          {/* Title */}
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.4 }}
            className="heading-1 text-white mb-4"
          >
            Discover Egypt with{' '}
            <span className="text-primary-400">25+ Years</span> of Excellence
          </motion.h1>

          {/* Subtitle */}
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6 }}
            className="text-xl text-gray-200 mb-8"
          >
            Tailor-made tours, Nile cruises & unforgettable experiences.
            Let us craft your perfect Egyptian adventure.
          </motion.p>

          {/* CTA Buttons */}
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.8 }}
            className="flex flex-wrap gap-4"
          >
            <Link href="/tours" className="btn btn-primary btn-lg">
              Explore Tours
              <ChevronRight className="w-5 h-5 ml-1" />
            </Link>
            <Link
              href="/contact"
              className="btn btn-lg bg-white/10 backdrop-blur-sm text-white border border-white/30 hover:bg-white/20"
            >
              Get Free Quote
            </Link>
          </motion.div>

          {/* Trust badges */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 1 }}
            className="flex flex-wrap gap-6 mt-12 pt-8 border-t border-white/20"
          >
            {trustBadges.map((badge) => (
              <div key={badge.label} className="flex items-center gap-2 text-white/80">
                <badge.icon className="w-5 h-5 text-primary-400" />
                <span className="text-sm">{badge.label}</span>
              </div>
            ))}
          </motion.div>
        </div>

      </div>

      {/* Scroll indicator */}
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1.2 }}
        className="absolute bottom-8 right-8 hidden lg:block"
      >
        <div className="flex flex-col items-center gap-2 text-white/60">
          <span className="text-xs uppercase tracking-widest rotate-90 origin-center translate-x-6">
            Scroll
          </span>
          <div className="w-px h-16 bg-gradient-to-b from-white/60 to-transparent" />
        </div>
      </motion.div>
    </section>
  );
}
