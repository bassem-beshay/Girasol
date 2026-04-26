'use client';

import { useRef, useEffect, useState, useCallback } from 'react';
import Link from 'next/link';
import { motion } from 'framer-motion';
import { ChevronRight, Shield, Award, Clock } from 'lucide-react';
import { useQuery } from '@tanstack/react-query';
import { contactApi } from '@/lib/api';
import { useLanguageStore } from '@/store/languageStore';
import { heroT, t } from '@/lib/translations';

interface Statistic {
  id: number;
  value: string;
  label: string;
  icon: string;
}

interface StatisticsResponse {
  count: number;
  results: Statistic[];
}

// Parse stat value like "43,678+", "98%", "4.9"
function parseStatValue(value: string) {
  const prefix = value.match(/^[^0-9]*/)?.[0] || '';
  const suffix = value.match(/[^0-9.,]*$/)?.[0] || '';
  const numStr = value.replace(prefix, '').replace(suffix, '');
  const hasCommas = numStr.includes(',');
  const cleanNum = numStr.replace(/,/g, '');
  const number = parseFloat(cleanNum);
  const decimals = cleanNum.includes('.') ? cleanNum.split('.')[1].length : 0;
  return { number, prefix, suffix, decimals, hasCommas };
}

function formatNumber(num: number, decimals: number, hasCommas: boolean) {
  const fixed = num.toFixed(decimals);
  if (!hasCommas) return fixed;
  const parts = fixed.split('.');
  parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, ',');
  return parts.join('.');
}

function AnimatedCounter({ value, className }: { value: string; className?: string }) {
  const [displayValue, setDisplayValue] = useState('');
  const ref = useRef<HTMLSpanElement>(null);
  const hasAnimated = useRef(false);

  const animate = useCallback(() => {
    const parsed = parseStatValue(value);
    if (isNaN(parsed.number)) { setDisplayValue(value); return; }
    const target = parsed.number;
    const start = Math.floor(target * 0.75);
    const duration = 2000;
    const startTime = performance.now();
    const easeOutExpo = (t: number) => t === 1 ? 1 : 1 - Math.pow(2, -10 * t);

    const step = (currentTime: number) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const current = start + (target - start) * easeOutExpo(progress);
      setDisplayValue(parsed.prefix + formatNumber(current, parsed.decimals, parsed.hasCommas) + parsed.suffix);
      if (progress < 1) requestAnimationFrame(step);
    };

    setDisplayValue(parsed.prefix + formatNumber(start, parsed.decimals, parsed.hasCommas) + parsed.suffix);
    requestAnimationFrame(step);
  }, [value]);

  useEffect(() => {
    if (!ref.current) return;
    const observer = new IntersectionObserver(
      (entries) => {
        if (entries[0].isIntersecting && !hasAnimated.current) {
          hasAnimated.current = true;
          animate();
        }
      },
      { threshold: 0.3 }
    );
    observer.observe(ref.current);
    return () => observer.disconnect();
  }, [animate]);

  return <span ref={ref} className={className}>{displayValue || value}</span>;
}

export function HeroSection() {
  const videoRef = useRef<HTMLVideoElement>(null);
  const { language } = useLanguageStore();

  // Fetch statistics from API
  const { data: statisticsData } = useQuery<StatisticsResponse>({
    queryKey: ['statistics'],
    queryFn: async () => {
      const response = await contactApi.getStatistics();
      return response.data;
    },
  });

  // Get dynamic values from API only - no static fallbacks
  const stats = statisticsData?.results || [];
  const travelersCount = stats.find(s => s.icon === 'users')?.value || '';
  const yearsExperience = stats.find(s => s.icon === 'clock')?.value || '';
  const isLoaded = stats.length > 0;

  const trustBadges = [
    { icon: Shield, label: t(heroT, language, 'iataCertified') },
    { icon: Award, label: isLoaded ? `${yearsExperience} ${t(heroT, language, 'yearsExperience')}` : '' },
    { icon: Clock, label: t(heroT, language, 'support247') },
  ];

  const [shouldLoadVideo, setShouldLoadVideo] = useState(false);

  // Defer the 10MB hero video until the browser is idle so it doesn't
  // block the initial payload / TTI on slow networks.
  useEffect(() => {
    const w = window as Window & {
      requestIdleCallback?: (cb: () => void, opts?: { timeout: number }) => number;
      cancelIdleCallback?: (handle: number) => void;
    };
    const schedule = w.requestIdleCallback
      ? (cb: () => void) => w.requestIdleCallback!(cb, { timeout: 2500 })
      : (cb: () => void) => window.setTimeout(cb, 1200);
    const cancel = w.cancelIdleCallback || window.clearTimeout;
    const handle = schedule(() => setShouldLoadVideo(true));
    return () => {
      try { cancel(handle as number); } catch {}
    };
  }, []);

  useEffect(() => {
    if (shouldLoadVideo && videoRef.current) {
      videoRef.current.play().catch(() => {
        // Autoplay might be blocked by browser
      });
    }
  }, [shouldLoadVideo]);

  return (
    <section className="relative h-[70vh] sm:h-[80vh] md:h-screen min-h-[400px] sm:min-h-[500px] md:min-h-[600px] max-h-[900px] overflow-hidden">
      {/* Background — gradient placeholder paints instantly; video mounts on idle */}
      <div className="absolute inset-0 bg-gradient-to-br from-primary-900 via-primary-800 to-primary-700">
        {shouldLoadVideo && (
          <video
            ref={videoRef}
            autoPlay
            muted
            loop
            playsInline
            preload="metadata"
            className="absolute inset-0 w-full h-full object-cover object-[center_50%]"
          >
            <source src="/videos/hero-video.mp4" type="video/mp4" />
          </video>
        )}
      </div>

      {/* Overlay */}
      <div className="absolute inset-0 bg-gradient-to-r from-black/70 via-black/50 to-transparent" />

      {/* Content — render visible immediately for fast LCP, no framer-motion above the fold */}
      <div className="relative h-full container-custom flex flex-col justify-center px-4 sm:px-6">
        <div className="max-w-2xl pt-14 sm:pt-0">
          {/* Badge */}
          <div>
            <span className="inline-flex items-center gap-1.5 sm:gap-2 px-2.5 sm:px-4 py-1 sm:py-2 rounded-full bg-white/10 backdrop-blur-sm text-white text-[10px] sm:text-xs md:text-sm mb-3 sm:mb-6">
              <span className="w-1 sm:w-1.5 md:w-2 h-1 sm:h-1.5 md:h-2 rounded-full bg-primary-500 animate-pulse" />
              {isLoaded ? <>{t(heroT, language, 'trustedBy')} <AnimatedCounter value={travelersCount} className="tabular-nums" /> {t(heroT, language, 'travelersWorldwide')}</> : t(heroT, language, 'trustedBy')}
            </span>
          </div>

          {/* Title — renders with static fallback so LCP doesn't wait on the stats API */}
          <h1 className="text-xl sm:text-3xl md:text-4xl lg:text-5xl xl:text-6xl font-display font-bold text-white mb-2 sm:mb-4 leading-tight">
            {t(heroT, language, 'discoverEgyptWith')}{' '}
            <span className="text-primary-400">
              {isLoaded ? <><AnimatedCounter value={yearsExperience} className="inline tabular-nums" /> </> : null}
              {t(heroT, language, 'yearsOfExcellence')}
            </span>
          </h1>

          {/* Subtitle */}
          <p className="text-xs sm:text-base md:text-lg lg:text-xl text-gray-200 mb-4 sm:mb-8 leading-relaxed">
            {t(heroT, language, 'subtitle')}
          </p>

          {/* CTA Buttons */}
          <div className="flex flex-col sm:flex-row gap-2 sm:gap-4">
            <Link href="/tours" className="btn btn-primary py-2 sm:py-3 md:py-4 px-4 sm:px-6 md:px-8 text-center font-semibold text-sm sm:text-base">
              {t(heroT, language, 'exploreTours')}
              <ChevronRight className="w-4 h-4 sm:w-5 sm:h-5 ml-1 inline" />
            </Link>
            <Link
              href="/contact#quote-form"
              className="btn py-2 sm:py-3 md:py-4 px-4 sm:px-6 md:px-8 bg-white/10 backdrop-blur-sm text-white border border-white/30 hover:bg-white/20 text-center font-semibold text-sm sm:text-base"
            >
              {t(heroT, language, 'getFreeQuote')}
            </Link>
          </div>

          {/* Trust badges */}
          <div className="flex flex-wrap gap-3 sm:gap-6 mt-5 sm:mt-12 pt-4 sm:pt-8 border-t border-white/20">
            {trustBadges.map((badge) => (
              <div key={badge.label} className="flex items-center gap-1.5 sm:gap-2 text-white/80">
                <badge.icon className="w-3 sm:w-4 md:w-5 h-3 sm:h-4 md:h-5 text-primary-400" />
                <span className="text-[10px] sm:text-xs md:text-sm">{badge.label}</span>
              </div>
            ))}
          </div>
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
            {t(heroT, language, 'scroll')}
          </span>
          <div className="w-px h-16 bg-gradient-to-b from-white/60 to-transparent" />
        </div>
      </motion.div>
    </section>
  );
}
