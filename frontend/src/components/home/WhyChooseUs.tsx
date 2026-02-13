'use client';

import { useQuery } from '@tanstack/react-query';
import { contactApi } from '@/lib/api';
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
const getFeatures = (yearsExperience: string) => [
  {
    icon: Award,
    title: 'Experts in Egypt',
    description: `When traveling with Girasol Egypt Travel and Tours, you choose a team of professionals and experts in Egypt with over ${yearsExperience} years of experience. We care for every detail of your journey to ensure an unforgettable experience.`,
    link: '/about/who-we-are',
  },
  {
    icon: MapPin,
    title: 'Privileges & Facilities',
    description: 'With local offices in Cairo, Luxor, Aswan, Sharm El Sheikh, Hurghada, and partners in various countries worldwide. You will receive high-quality services and on-ground support wherever you travel.',
    link: '/about/booking',
  },
  {
    icon: Headphones,
    title: '24/7 Dedicated Support',
    description: 'We care about all your requirements, making your reservations quick and efficient. Our dedicated team is available around the clock via WhatsApp, phone, or email to serve you whenever and wherever you are.',
    link: '/about/service-quality',
  },
  {
    icon: Heart,
    title: 'Our Working Style',
    description: 'Love and care for your needs and requests is our working style with all our clients. Our professional team realizes and advises on all your requirements with personalized attention and genuine hospitality.',
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
  const { data: statisticsData } = useQuery<StatisticsResponse>({
    queryKey: ['statistics'],
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

  const features = getFeatures(yearsExperience);

  return (
    <section className="section-padding bg-gray-50">
      <div className="container-custom">
        {/* Header */}
        <div className="text-center mx-auto mb-16">
          <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
            className="inline-flex items-center gap-2 bg-primary-50 text-primary-600 font-semibold text-sm uppercase tracking-widest px-5 py-2 rounded-full mb-6"
          >
            <span className="w-2 h-2 rounded-full bg-primary-500 animate-pulse" />
            Why Choose Us
          </motion.div>
          <motion.h2
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.1 }}
            className="text-xl sm:text-2xl md:text-4xl lg:text-5xl font-display font-bold text-primary-600 mb-4 whitespace-nowrap"
          >
            Why Girasol Egypt Travel and Tours
          </motion.h2>
          <motion.h3
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="text-xl sm:text-2xl md:text-3xl font-semibold text-gray-900 mb-4"
          >
            Your Trusted Partner in Egyptian Tourism
          </motion.h3>
          <motion.div
            initial={{ scaleX: 0 }}
            whileInView={{ scaleX: 1 }}
            viewport={{ once: true }}
            transition={{ duration: 0.8, delay: 0.3 }}
            className="w-24 h-1 bg-gradient-to-r from-primary-400 to-primary-600 mx-auto rounded-full mb-6"
          />
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: 0.4 }}
            className="text-base md:text-lg text-gray-600"
          >
            We combine deep local knowledge with international service standards
            to deliver experiences that exceed expectations.
          </motion.p>
        </div>

        {/* Features grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 lg:gap-10">
          {features.map((feature, index) => (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, x: index % 2 === 0 ? -60 : 60, y: 30 }}
              whileInView={{ opacity: 1, x: 0, y: 0 }}
              viewport={{ once: true, margin: "-50px" }}
              transition={{ duration: 0.7, delay: index * 0.15, ease: [0.25, 0.46, 0.45, 0.94] }}
              className="group relative bg-white rounded-3xl p-8 lg:p-10 shadow-md hover:shadow-[0_20px_60px_-15px_rgba(0,0,0,0.15)] transition-all duration-500 border border-gray-100 hover:border-primary-300 overflow-hidden"
            >
              {/* Animated gradient background on hover */}
              <div className="absolute inset-0 bg-gradient-to-br from-primary-50/0 via-primary-50/0 to-primary-100/0 group-hover:from-primary-50/50 group-hover:via-white group-hover:to-primary-50/30 transition-all duration-700" />

              {/* Decorative corner accent */}
              <div className="absolute top-0 right-0 w-32 h-32 bg-gradient-to-bl from-primary-100/40 to-transparent rounded-bl-[100px] opacity-0 group-hover:opacity-100 transition-opacity duration-500" />

              <div className="relative flex flex-col sm:flex-row items-center sm:items-start gap-6">
                {/* Icon with animations */}
                <motion.div
                  initial={{ scale: 0, rotate: -180 }}
                  whileInView={{ scale: 1, rotate: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.6, delay: index * 0.15 + 0.3, type: "spring", stiffness: 200 }}
                  className="relative flex-shrink-0"
                >
                  {/* Pulse ring */}
                  <div className="absolute inset-0 w-20 h-20 sm:w-24 sm:h-24 rounded-2xl bg-primary-400/20 group-hover:animate-ping opacity-0 group-hover:opacity-75" style={{ animationDuration: '2s', animationIterationCount: '1' }} />

                  <div className="relative w-20 h-20 sm:w-24 sm:h-24 rounded-2xl bg-gradient-to-br from-primary-500 to-primary-700 flex items-center justify-center shadow-lg shadow-primary-500/25 group-hover:shadow-primary-500/40 group-hover:scale-110 group-hover:rotate-3 transition-all duration-500">
                    <feature.icon className="w-10 h-10 sm:w-12 sm:h-12 text-white group-hover:scale-110 transition-transform duration-300" />
                  </div>
                </motion.div>

                {/* Content with staggered reveal */}
                <div className="text-center sm:text-left flex-1">
                  <motion.h3
                    initial={{ opacity: 0, y: 15 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5, delay: index * 0.15 + 0.4 }}
                    className="text-xl sm:text-2xl font-bold text-gray-900 mb-3 group-hover:text-primary-600 transition-colors duration-300"
                  >
                    {feature.title}
                  </motion.h3>
                  <motion.p
                    initial={{ opacity: 0, y: 15 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5, delay: index * 0.15 + 0.5 }}
                    className="text-gray-600 text-sm sm:text-base leading-relaxed mb-6"
                  >
                    {feature.description}
                  </motion.p>
                  <motion.div
                    initial={{ opacity: 0, x: -20 }}
                    whileInView={{ opacity: 1, x: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5, delay: index * 0.15 + 0.6 }}
                  >
                    <Link
                      href={feature.link}
                      className="inline-flex items-center gap-2 bg-primary-50 text-primary-600 font-semibold text-sm px-6 py-3 rounded-full hover:bg-primary-600 hover:text-white hover:shadow-lg hover:shadow-primary-500/25 hover:-translate-y-0.5 transition-all duration-300 group/link"
                    >
                      Read More
                      <ArrowRight className="w-4 h-4 group-hover/link:translate-x-1.5 transition-transform duration-300" />
                    </Link>
                  </motion.div>
                </div>
              </div>

            </motion.div>
          ))}
        </div>

        {/* Stats - Dynamic from API */}
        {stats.length > 0 && (
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ duration: 0.8 }}
          className="mt-20 relative"
        >
          <div className="absolute inset-0 bg-gradient-to-r from-primary-600 to-primary-700 rounded-3xl transform rotate-1 opacity-10" />
          <div className="relative grid grid-cols-2 md:grid-cols-4 gap-6 md:gap-8 p-8 md:p-12 bg-white rounded-3xl shadow-xl border border-gray-100">
            {stats.map((stat, index) => {
              const IconComponent = iconMap[stat.icon] || Star;
              return (
                <motion.div
                  key={stat.id || stat.label}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: index * 0.08 }}
                  className="text-center group/stat"
                >
                  <div className="w-12 h-12 mx-auto mb-3 rounded-xl bg-primary-50 flex items-center justify-center group-hover/stat:bg-primary-100 group-hover/stat:scale-110 transition-all duration-300">
                    <IconComponent className="w-6 h-6 text-primary-600" />
                  </div>
                  <AnimatedCounter
                    value={stat.value}
                    className="text-3xl md:text-4xl font-bold text-gray-900 mb-1 tabular-nums"
                  />
                  <div className="text-gray-500 text-sm font-medium">{stat.label}</div>
                </motion.div>
              );
            })}
          </div>
        </motion.div>
        )}
      </div>
    </section>
  );
}
