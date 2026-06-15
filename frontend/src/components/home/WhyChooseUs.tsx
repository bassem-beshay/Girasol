'use client';

import { useQuery } from '@tanstack/react-query';
import { contactApi } from '@/lib/api';
import { useLanguageStore, Language } from '@/store/languageStore';
import { whyChooseUsT, t } from '@/lib/translations';
import { motion } from 'framer-motion';
import { Clock, MapPin, Headphones, BadgePercent, Users, Globe, Award, Star, Heart, Shield, LucideIcon, ArrowRight } from 'lucide-react';
import Link from 'next/link';
import { useRef, useCallback, useState, useEffect } from 'react';

// Icon mapping from backend to Lucide icons
const iconMap: Record<string, LucideIcon> = {
  'clock': Clock,
  'users': Users,
  'map-pin': MapPin,
  'globe': Globe,
  'award': Award,
  'star': Star,
  'heart': Heart,
  'shield': Shield,
};

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
  const ref = useRef<HTMLDivElement>(null);
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

  return <div ref={ref} className={className}>{displayValue || value}</div>;
}

// Features will use dynamic data from API
const getFeatures = (yearsExperience: string, lang: Language) => [
  {
    icon: Award,
    title: t(whyChooseUsT, lang, 'expertsTitle'),
    description: `${t(whyChooseUsT, lang, 'expertsPrefix')}${yearsExperience} ${t(whyChooseUsT, lang, 'expertsSuffix')}`,
    link: '/about/who-we-are',
  },
  {
    icon: MapPin,
    title: t(whyChooseUsT, lang, 'privilegesTitle'),
    description: t(whyChooseUsT, lang, 'privilegesDesc'),
    link: '/about/booking',
  },
  {
    icon: Headphones,
    title: t(whyChooseUsT, lang, 'supportTitle'),
    description: t(whyChooseUsT, lang, 'supportDesc'),
    link: '/about/service-quality',
  },
  {
    icon: Heart,
    title: t(whyChooseUsT, lang, 'styleTitle'),
    description: t(whyChooseUsT, lang, 'styleDesc'),
    link: '/about/our-philosophy',
  },
];

interface Statistic {
  id: number;
  value: string;
  label: string;
  label_es: string;
  label_pt: string;
  icon: string;
  description: string;
  sort_order: number;
}

interface StatisticsResponse {
  count: number;
  results: Statistic[];
}



export function WhyChooseUs() {
  const { language } = useLanguageStore();

  const { data: statisticsData } = useQuery<StatisticsResponse>({
    queryKey: ['statistics', language],
    queryFn: async () => {
      const response = await contactApi.getStatistics();
      return response.data;
    },
  });

  const stats = statisticsData?.results || [];

  // Get years experience for features description
  const yearsExperience = stats.find(s =>
    s.label.toLowerCase().includes('experience') || s.label.toLowerCase().includes('years')
  )?.value?.replace('+', '') || '';

  const features = getFeatures(yearsExperience, language);

  return (
    <motion.section
      initial={{ opacity: 0, y: 20 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true, margin: '-80px' }}
      transition={{ duration: 0.6 }}
      className="section-padding bg-gray-50"
    >
      <div className="container-custom">
        {/* Header */}
        <div className="text-center mx-auto mb-16">
          <div className="inline-flex items-center gap-2 bg-primary-50 text-primary-600 font-semibold text-sm uppercase tracking-widest px-5 py-2 rounded-full mb-6">
            <span className="w-2 h-2 rounded-full bg-primary-500 animate-pulse" />
            {t(whyChooseUsT, language, 'whyChooseUs')}
          </div>
          <h2 className="text-xl sm:text-2xl md:text-4xl lg:text-5xl font-display font-bold text-primary-600 mb-4 whitespace-nowrap">
            {t(whyChooseUsT, language, 'mainTitle')}
          </h2>
          <h3 className="text-xl sm:text-2xl md:text-3xl font-semibold text-gray-900 mb-4">
            {t(whyChooseUsT, language, 'subtitle')}
          </h3>
          <div className="w-24 h-1 bg-gradient-to-r from-primary-400 to-primary-600 mx-auto rounded-full mb-6" />
          <p className="text-base md:text-lg text-gray-600">
            {t(whyChooseUsT, language, 'description')}
          </p>
        </div>

        {/* Features grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-10">
          {features.map((feature) => (
            <div
              key={feature.title}
              className="group relative bg-white rounded-3xl p-8 lg:p-10 shadow-md hover:shadow-[0_20px_60px_-15px_rgba(0,0,0,0.15)] transition-all duration-500 border border-gray-100 hover:border-primary-300 overflow-hidden"
            >
              {/* Animated gradient background on hover */}
              <div className="absolute inset-0 bg-gradient-to-br from-primary-50/0 via-primary-50/0 to-primary-100/0 group-hover:from-primary-50/50 group-hover:via-white group-hover:to-primary-50/30 transition-all duration-700" />

              {/* Decorative corner accent */}
              <div className="absolute top-0 right-0 w-32 h-32 bg-gradient-to-bl from-primary-100/40 to-transparent rounded-bl-[100px] opacity-0 group-hover:opacity-100 transition-opacity duration-500" />

              <div className="relative flex flex-col sm:flex-row items-center sm:items-start gap-6">
                {/* Icon */}
                <div className="relative flex-shrink-0">
                  {/* Pulse ring */}
                  <div className="absolute inset-0 w-20 h-20 sm:w-24 sm:h-24 rounded-2xl bg-primary-400/20 group-hover:animate-ping opacity-0 group-hover:opacity-75" style={{ animationDuration: '2s', animationIterationCount: '1' }} />

                  <div className="relative w-20 h-20 sm:w-24 sm:h-24 rounded-2xl bg-gradient-to-br from-primary-500 to-primary-700 flex items-center justify-center shadow-lg shadow-primary-500/25 group-hover:shadow-primary-500/40 group-hover:scale-110 group-hover:rotate-3 transition-all duration-500">
                    <feature.icon className="w-10 h-10 sm:w-12 sm:h-12 text-white group-hover:scale-110 transition-transform duration-300" />
                  </div>
                </div>

                {/* Content */}
                <div className="text-center sm:text-left flex-1">
                  <h3 className="text-xl sm:text-2xl font-bold text-gray-900 mb-3 group-hover:text-primary-600 transition-colors duration-300">
                    {feature.title}
                  </h3>
                  <p className="text-gray-600 text-sm sm:text-base leading-relaxed mb-6">
                    {feature.description}
                  </p>
                  <Link
                    href={feature.link}
                    className="inline-flex items-center gap-2 bg-primary-50 text-primary-600 font-semibold text-sm px-6 py-3 rounded-full hover:bg-primary-600 hover:text-white hover:shadow-lg hover:shadow-primary-500/25 hover:-translate-y-0.5 transition-all duration-300 group/link"
                  >
                    {t(whyChooseUsT, language, 'readMore')}
                    <ArrowRight className="w-4 h-4 group-hover/link:translate-x-1.5 transition-transform duration-300" />
                  </Link>
                </div>
              </div>

            </div>
          ))}
        </div>

        {/* Stats - Dynamic from API */}
        {stats.length > 0 && (
          <div className="mt-20 relative">
            <div className="absolute inset-0 bg-gradient-to-r from-primary-600 to-primary-700 rounded-3xl transform rotate-1 opacity-10" />
            <div className="relative grid grid-cols-2 md:grid-cols-4 gap-6 md:gap-8 p-8 md:p-12 bg-white rounded-3xl shadow-xl border border-gray-100">
              {stats.map((stat) => {
                const IconComponent = iconMap[stat.icon] || Star;
                return (
                  <div key={stat.id || stat.label} className="text-center group/stat">
                    <div className="w-12 h-12 mx-auto mb-3 rounded-xl bg-primary-50 flex items-center justify-center group-hover/stat:bg-primary-100 group-hover/stat:scale-110 transition-all duration-300">
                      <IconComponent className="w-6 h-6 text-primary-600" />
                    </div>
                    <AnimatedCounter
                      value={stat.value}
                      className="text-3xl md:text-4xl font-bold text-gray-900 mb-1 tabular-nums"
                    />
                    <div className="text-gray-500 text-sm font-medium">
                      {language === 'es' ? stat.label_es : language === 'pt' ? stat.label_pt : stat.label}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>
        )}
      </div>
    </motion.section>
  );
}
