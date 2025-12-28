'use client';

import { useQuery } from '@tanstack/react-query';
import { contactApi } from '@/lib/api';
import { motion } from 'framer-motion';
import { Clock, MapPin, Headphones, BadgePercent, Users, Globe, Award, Star, Heart, Shield, LucideIcon, ArrowRight } from 'lucide-react';
import Link from 'next/link';

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

// Features will use dynamic data from API
const getFeatures = (yearsExperience: string) => [
  {
    icon: Award,
    title: 'Experts in Egypt',
    description: `When traveling with Girasol Egypt Travel and Tours, you choose a team of professionals and experts in Egypt with over ${yearsExperience} years of experience. We care for every detail of your journey to ensure an unforgettable experience.`,
  },
  {
    icon: MapPin,
    title: 'Privileges & Facilities',
    description: 'With local offices in Cairo, Luxor, Aswan, Sharm El Sheikh, Hurghada, and partners in various countries worldwide. You will receive high-quality services and on-ground support wherever you travel.',
  },
  {
    icon: Headphones,
    title: '24/7 Dedicated Support',
    description: 'We care about all your requirements, making your reservations quick and efficient. Our dedicated team is available around the clock via WhatsApp, phone, or email to serve you whenever and wherever you are.',
  },
  {
    icon: Heart,
    title: 'Our Working Style',
    description: 'Love and care for your needs and requests is our working style with all our clients. Our professional team realizes and advises on all your requirements with personalized attention and genuine hospitality.',
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

// Fallback stats if API fails
const fallbackStats: Statistic[] = [
  { id: 0, value: '25+', label: 'Years Experience', label_es: '', label_pt: '', icon: 'clock', description: '', sort_order: 1 },
  { id: 0, value: '50,000+', label: 'Happy Travelers', label_es: '', label_pt: '', icon: 'users', description: '', sort_order: 2 },
  { id: 0, value: '6', label: 'Local Offices', label_es: '', label_pt: '', icon: 'map-pin', description: '', sort_order: 3 },
  { id: 0, value: '10+', label: 'Countries Partners', label_es: '', label_pt: '', icon: 'globe', description: '', sort_order: 4 },
];

export function WhyChooseUs() {
  const { data: statisticsData } = useQuery<StatisticsResponse>({
    queryKey: ['statistics'],
    queryFn: async () => {
      const response = await contactApi.getStatistics();
      return response.data;
    },
  });

  const stats = statisticsData?.results && statisticsData.results.length > 0
    ? statisticsData.results
    : fallbackStats;

  // Get years experience for features description
  const yearsExperience = stats.find(s =>
    s.label.toLowerCase().includes('experience') || s.label.toLowerCase().includes('years')
  )?.value?.replace('+', '') || '25';

  const features = getFeatures(yearsExperience);

  return (
    <section className="section-padding bg-gray-50">
      <div className="container-custom">
        {/* Header */}
        <div className="text-center max-w-2xl mx-auto mb-12">
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-3xl sm:text-4xl md:text-5xl font-display font-bold text-primary-600 mb-4"
          >
            Why Girasol Tours
          </motion.h2>
          <motion.h3
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.1 }}
            className="text-xl sm:text-2xl md:text-3xl font-semibold text-gray-900 mb-4"
          >
            Your Trusted Partner in Egyptian Tourism
          </motion.h3>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.2 }}
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
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
              className="group bg-white rounded-3xl p-8 shadow-md hover:shadow-2xl transition-all duration-300 border border-gray-100 hover:border-primary-200"
            >
              <div className="flex flex-col sm:flex-row items-center sm:items-start gap-6">
                {/* Large Icon */}
                <div className="w-20 h-20 sm:w-24 sm:h-24 flex-shrink-0 rounded-2xl bg-gradient-to-br from-primary-500 to-primary-600 flex items-center justify-center shadow-lg group-hover:scale-110 transition-transform duration-300">
                  <feature.icon className="w-10 h-10 sm:w-12 sm:h-12 text-white" />
                </div>

                {/* Content */}
                <div className="text-center sm:text-left flex-1">
                  <h3 className="text-xl sm:text-2xl font-bold text-gray-900 mb-3 group-hover:text-primary-600 transition-colors">
                    {feature.title}
                  </h3>
                  <p className="text-gray-600 text-sm sm:text-base leading-relaxed mb-5">
                    {feature.description}
                  </p>
                  <Link
                    href="/about"
                    className="inline-flex items-center gap-2 bg-primary-50 text-primary-600 font-semibold text-sm px-5 py-2.5 rounded-full hover:bg-primary-600 hover:text-white transition-all duration-300 group/link"
                  >
                    Read More
                    <ArrowRight className="w-4 h-4 group-hover/link:translate-x-1 transition-transform" />
                  </Link>
                </div>
              </div>
            </motion.div>
          ))}
        </div>

        {/* Stats - Dynamic from API */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mt-16 grid grid-cols-2 md:grid-cols-4 gap-8 p-8 bg-white rounded-2xl shadow-lg"
        >
          {stats.map((stat) => {
            const IconComponent = iconMap[stat.icon] || Star;
            return (
              <div key={stat.id || stat.label} className="text-center">
                <div className="text-3xl md:text-4xl font-bold text-primary-600 mb-1">
                  {stat.value}
                </div>
                <div className="text-gray-600 text-sm">{stat.label}</div>
              </div>
            );
          })}
        </motion.div>
      </div>
    </section>
  );
}
