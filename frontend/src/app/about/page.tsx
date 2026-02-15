'use client';

import { useState, useEffect, useRef, useCallback } from 'react';
import { motion, useInView } from 'framer-motion';
import Image from 'next/image';
import Link from 'next/link';
import {
  Award,
  Users,
  Globe,
  Calendar,
  MapPin,
  Shield,
  Heart,
  Star,
  CheckCircle,
  Phone,
  ArrowRight,
  Clock,
  LucideIcon,
} from 'lucide-react';
import { contactApi } from '@/lib/api';
import { useLanguageStore } from '@/store/languageStore';
import { aboutT, t } from '@/lib/translations';

const iconMap: Record<string, LucideIcon> = {
  clock: Clock,
  users: Users,
  'map-pin': MapPin,
  globe: Globe,
  award: Award,
  star: Star,
  heart: Heart,
  shield: Shield,
};

const defaultStats = [
  { icon: 'clock', value: '0+', label: 'Years Experience' },
  { icon: 'users', value: '0+', label: 'Happy Travelers' },
  { icon: 'globe', value: '0+', label: 'Countries Covered' },
  { icon: 'award', value: '0+', label: 'Tour Packages' },
];

function parseNumericValue(value: string): { num: number; prefix: string; suffix: string } {
  const match = value.match(/^([^\d]*?)([\d,.]+)(.*)$/);
  if (!match) return { num: 0, prefix: '', suffix: value };
  return {
    prefix: match[1],
    num: parseFloat(match[2].replace(/,/g, '')),
    suffix: match[3],
  };
}

function formatNumber(n: number, original: string): string {
  const { prefix, suffix } = parseNumericValue(original);
  if (original.includes(',')) {
    return prefix + n.toLocaleString('en-US') + suffix;
  }
  if (Number.isInteger(parseNumericValue(original).num)) {
    return prefix + Math.round(n).toString() + suffix;
  }
  return prefix + n.toFixed(1) + suffix;
}

function CountUp({ value, duration = 2000 }: { value: string; duration?: number }) {
  const [display, setDisplay] = useState('0');
  const ref = useRef<HTMLDivElement>(null);
  const inView = useInView(ref, { once: true });
  const lastValue = useRef('');

  useEffect(() => {
    const { num } = parseNumericValue(value);
    if (num === 0) { setDisplay(value); return; }
    if (!inView) return;
    if (value === lastValue.current) return;
    lastValue.current = value;
    const startTime = performance.now();
    const step = (currentTime: number) => {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = eased * num;
      setDisplay(formatNumber(current, value));
      if (progress < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }, [inView, value, duration]);

  return <div ref={ref} className="text-4xl font-bold text-gray-900 mb-2">{display}</div>;
}

const leadership = [
  {
    name: 'Emad Khalifa',
    role: 'Chairman & CEO',
    image: '/images/team/emad-khalifa.jpeg',
    description: 'With over 30 years of expertise in the tourism industry, Emad leads Girasol with a visionary approach to showcasing Egypt\'s timeless beauty to the world.',
  },
  {
    name: 'Delzilene Macedo Costa',
    role: 'Chief Executive',
    image: '/images/team/delzilene-costa.jpeg',
    description: 'Delzilene brings international expertise and strategic leadership, driving Girasol\'s growth and expanding our reach across global markets.',
  },
];

const team = [
  {
    name: 'Tarek Khalifa',
    role: 'Director of Italian Operations',
    image: '/images/team/tarek-khalifa.jpeg',
  },
  {
    name: 'Mostafa Teleb',
    role: 'Administration & Executive Manager',
    image: '/images/team/mostafa-teleb.jpeg',
  },
  {
    name: 'Rania Gamal',
    role: 'Manager of Ticketing Operations',
    image: '/images/team/rania-gamal.jpeg',
  },
  {
    name: 'Salem Gomaa',
    role: 'Purchasing Supervisor',
    image: '/images/team/salem-gomaa.jpeg',
  },
  {
    name: 'Zeinab Gamal',
    role: 'Senior Reservations & Operations Italian Market',
    image: '/images/team/zeinab-gamal.jpeg',
  },
  {
    name: 'Nessma Ragab',
    role: 'Senior Reservations & Operations Brazilian Market',
    image: '/images/team/nessma-ragab.jpeg',
  },
  {
    name: 'Ibrahim Okel',
    role: 'Chief Accountant',
    image: '/images/team/ibrahim-okel.jpeg',
  },
];

export default function AboutPage() {
  const { language } = useLanguageStore();
  const [stats, setStats] = useState(defaultStats);
  const [offices, setOffices] = useState<{ city: string; is_headquarters: boolean }[]>([]);

  const values = [
    {
      icon: Shield,
      title: t(aboutT, language, 'trustSafety'),
      description: t(aboutT, language, 'trustSafetyDesc'),
    },
    {
      icon: Heart,
      title: t(aboutT, language, 'passionTravel'),
      description: t(aboutT, language, 'passionTravelDesc'),
    },
    {
      icon: Star,
      title: t(aboutT, language, 'excellence'),
      description: t(aboutT, language, 'excellenceDesc'),
    },
    {
      icon: Users,
      title: t(aboutT, language, 'customerFirst'),
      description: t(aboutT, language, 'customerFirstDesc'),
    },
  ];

  const milestones = [
    { year: '2010', title: t(aboutT, language, 'milestone1Title'), description: t(aboutT, language, 'milestone1Desc') },
    { year: '2012', title: t(aboutT, language, 'milestone2Title'), description: t(aboutT, language, 'milestone2Desc') },
    { year: '2015', title: t(aboutT, language, 'milestone3Title'), description: t(aboutT, language, 'milestone3Desc') },
    { year: '2018', title: t(aboutT, language, 'milestone4Title'), description: t(aboutT, language, 'milestone4Desc') },
    { year: '2020', title: t(aboutT, language, 'milestone5Title'), description: t(aboutT, language, 'milestone5Desc') },
    { year: '2023', title: t(aboutT, language, 'milestone6Title'), description: t(aboutT, language, 'milestone6Desc') },
  ];

  const services = [
    t(aboutT, language, 'service1'),
    t(aboutT, language, 'service2'),
    t(aboutT, language, 'service3'),
    t(aboutT, language, 'service4'),
    t(aboutT, language, 'service5'),
    t(aboutT, language, 'service6'),
    t(aboutT, language, 'service7'),
    t(aboutT, language, 'service8'),
    t(aboutT, language, 'service9'),
  ];

  useEffect(() => {
    contactApi.getStatistics().then((res) => {
      const data = res.data?.results || res.data;
      if (Array.isArray(data) && data.length > 0) {
        setStats(data.map((s: { icon: string; value: string; label: string }) => ({
          icon: s.icon,
          value: s.value,
          label: s.label,
        })));
      }
    }).catch(() => {});

    contactApi.getOffices().then((res) => {
      const data = res.data?.results || res.data;
      if (Array.isArray(data) && data.length > 0) {
        setOffices(data);
      }
    }).catch(() => {});
  }, []);

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[40vh] sm:h-[50vh] md:h-[70vh] lg:h-[85vh] min-h-[250px] sm:min-h-[300px] md:min-h-[450px] lg:min-h-[700px] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-primary-900/90 to-primary-800/80 z-10" />
        <div
          className="absolute inset-0 bg-cover bg-center"
          style={{ backgroundImage: "url('/images/about-hero.jpg')" }}
        />
        <div className="relative z-20 text-center text-white max-w-4xl mx-auto px-4">
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="text-2xl sm:text-3xl md:text-5xl lg:text-6xl font-display font-bold mb-3 sm:mb-6"
          >
            {t(aboutT, language, 'heroTitle')}
          </motion.h1>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="text-xl md:text-2xl text-white/90"
          >
            {t(aboutT, language, 'heroSubtitle')}
          </motion.p>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-16 bg-white">
        <div className="container-custom">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
            {stats.map((stat, index) => {
              const IconComponent = iconMap[stat.icon] || Star;
              return (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  className="text-center"
                >
                  <div className="w-16 h-16 mx-auto mb-4 rounded-2xl bg-primary-100 flex items-center justify-center">
                    <IconComponent className="w-8 h-8 text-primary-600" />
                  </div>
                  <CountUp value={stat.value} />
                  <div className="text-gray-600">{stat.label}</div>
                </motion.div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Our Story Section */}
      <section className="py-20 bg-gray-50">
        <div className="container-custom">
          <div className="grid lg:grid-cols-2 gap-16 items-center">
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
            >
              <h2 className="text-4xl font-display font-bold text-gray-900 mb-6">
                {t(aboutT, language, 'ourStory')}
              </h2>
              <div className="space-y-4 text-gray-600 leading-relaxed">
                <p>
                  {t(aboutT, language, 'storyP1')}
                </p>
                <p>
                  {t(aboutT, language, 'storyP2')}
                </p>
                <p>
                  {t(aboutT, language, 'storyP3')}
                </p>
              </div>
              <div className="mt-8 flex flex-wrap gap-4">
                <Link href="/tours" className="btn btn-primary btn-lg">
                  {t(aboutT, language, 'exploreOurTours')}
                  <ArrowRight className="w-5 h-5 ml-2" />
                </Link>
                <Link href="/contact" className="btn btn-outline btn-lg">
                  {t(aboutT, language, 'contactUs')}
                </Link>
              </div>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, x: 30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="relative"
            >
              <div className="relative h-[500px] rounded-2xl overflow-hidden shadow-2xl">
                <Image
                  src="/images/about-story.jpg"
                  alt="Girasol Tours Team"
                  fill
                  sizes="(max-width: 768px) 100vw, 50vw"
                  className="object-cover"
                />
              </div>
              <div className="absolute -bottom-8 -left-8 bg-white p-6 rounded-2xl shadow-xl">
                <div className="flex items-center gap-4">
                  <div className="w-16 h-16 rounded-full bg-primary-500 flex items-center justify-center">
                    <Award className="w-8 h-8 text-white" />
                  </div>
                  <div>
                    <div className="text-2xl font-bold text-gray-900">{t(aboutT, language, 'licensed')}</div>
                    <div className="text-gray-600">{t(aboutT, language, 'travelAgency')}</div>
                  </div>
                </div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Our Values Section */}
      <section className="py-20 bg-white">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl font-display font-bold text-gray-900 mb-4">
              {t(aboutT, language, 'ourValues')}
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              {t(aboutT, language, 'valuesSubtitle')}
            </p>
          </motion.div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {values.map((value, index) => (
              <motion.div
                key={value.title}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="bg-gray-50 rounded-2xl p-8 hover:shadow-lg transition-shadow"
              >
                <div className="w-14 h-14 rounded-xl bg-primary-100 flex items-center justify-center mb-6">
                  <value.icon className="w-7 h-7 text-primary-600" />
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-3">{value.title}</h3>
                <p className="text-gray-600">{value.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section className="py-20 bg-gradient-to-br from-primary-600 to-primary-800 text-white">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl font-display font-bold mb-4">
              {t(aboutT, language, 'whatWeOffer')}
            </h2>
            <p className="text-xl text-white/80 max-w-2xl mx-auto">
              {t(aboutT, language, 'offerSubtitle')}
            </p>
          </motion.div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {services.map((service, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: -20 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, delay: index * 0.05 }}
                className="flex items-center gap-3 bg-white/10 backdrop-blur-sm rounded-xl p-4"
              >
                <CheckCircle className="w-6 h-6 text-secondary-400 flex-shrink-0" />
                <span className="text-white/90">{service}</span>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Timeline Section */}
      <section className="py-20 bg-gray-50">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl font-display font-bold text-gray-900 mb-4">
              {t(aboutT, language, 'ourJourney')}
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              {t(aboutT, language, 'journeySubtitle')}
            </p>
          </motion.div>

          <div className="relative">
            {/* Timeline line */}
            <div className="absolute left-1/2 transform -translate-x-1/2 h-full w-1 bg-primary-200 hidden md:block" />

            <div className="space-y-12">
              {milestones.map((milestone, index) => (
                <motion.div
                  key={milestone.year}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  className={`flex flex-col md:flex-row items-center gap-8 ${
                    index % 2 === 0 ? 'md:flex-row' : 'md:flex-row-reverse'
                  }`}
                >
                  <div className={`flex-1 ${index % 2 === 0 ? 'md:text-right' : 'md:text-left'}`}>
                    <div className="bg-white p-6 rounded-2xl shadow-lg inline-block">
                      <div className="text-primary-600 font-bold text-lg mb-2">{milestone.year}</div>
                      <h3 className="text-xl font-bold text-gray-900 mb-2">{milestone.title}</h3>
                      <p className="text-gray-600">{milestone.description}</p>
                    </div>
                  </div>
                  <div className="w-4 h-4 rounded-full bg-primary-500 border-4 border-white shadow-lg z-10" />
                  <div className="flex-1" />
                </motion.div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* Team Section */}
      <section className="py-20 bg-white">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl font-display font-bold text-gray-900 mb-4">
              {t(aboutT, language, 'leadershipTeam')}
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              {t(aboutT, language, 'teamSubtitle')}
            </p>
          </motion.div>

          {/* Leadership Row */}
          <div className="grid md:grid-cols-2 gap-6 mb-16">
            {leadership.map((member, index) => (
              <motion.div
                key={member.name}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.15 }}
                className="group bg-gray-50 rounded-2xl overflow-hidden shadow-lg hover:shadow-xl transition-shadow flex flex-col sm:flex-row"
              >
                <div className="relative w-full sm:w-72 h-72 sm:h-auto flex-shrink-0">
                  <Image
                    src={member.image}
                    alt={member.name}
                    fill
                    sizes="(max-width: 768px) 100vw, 50vw"
                    className="object-cover"
                  />
                </div>
                <div className="p-6 flex flex-col justify-center">
                  <span className="inline-block px-4 py-1 bg-primary-50 text-primary-600 font-semibold text-sm rounded-full mb-3 w-fit uppercase tracking-wide">
                    {member.role}
                  </span>
                  <h3 className="text-2xl font-bold text-gray-900 mb-3">{member.name}</h3>
                  <p className="text-gray-600 leading-relaxed">{member.description}</p>
                </div>
              </motion.div>
            ))}
          </div>

          {/* Team Members */}
          <div className="grid grid-cols-3 sm:grid-cols-4 lg:grid-cols-7 gap-4">
            {team.map((member, index) => (
              <motion.div
                key={member.name}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.07 }}
                className="group bg-white rounded-lg overflow-hidden shadow-sm hover:shadow-md transition-shadow border border-gray-100"
              >
                <div className="relative w-full aspect-square">
                  <Image
                    src={member.image}
                    alt={member.name}
                    fill
                    sizes="(max-width: 768px) 33vw, (max-width: 1024px) 25vw, 14vw"
                    className="object-cover"
                  />
                </div>
                <div className="p-2.5 text-center">
                  <h3 className="text-sm font-bold text-gray-900 mb-0.5">{member.name}</h3>
                  <p className="text-primary-600 font-medium text-xs leading-tight">{member.role}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Offices Section */}
      {offices.length > 0 && (
      <section className="py-20 bg-gray-50">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl font-display font-bold text-gray-900 mb-4">
              {t(aboutT, language, 'ourOffices')}
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              {t(aboutT, language, 'officesSubtitle')}
            </p>
          </motion.div>

          <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-6">
            {offices.map((office, index) => (
              <motion.div
                key={office.city}
                initial={{ opacity: 0, scale: 0.9 }}
                whileInView={{ opacity: 1, scale: 1 }}
                viewport={{ once: true }}
                transition={{ duration: 0.4, delay: index * 0.05 }}
                className="bg-white rounded-xl p-6 text-center shadow-md hover:shadow-lg transition-shadow"
              >
                <MapPin className="w-8 h-8 text-primary-500 mx-auto mb-3" />
                <h3 className="font-bold text-gray-900">
                  {office.city}{office.is_headquarters ? ' (HQ)' : ''}
                </h3>
                <p className="text-gray-500 text-sm">Egypt</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>
      )}

      {/* CTA Section */}
      <section className="py-20 mb-12 bg-gray-900">
        <div className="container-custom text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-4xl font-display font-bold text-white mb-6">
              {t(aboutT, language, 'readyToExplore')}
            </h2>
            <p className="text-xl text-white/90 mb-8 max-w-2xl mx-auto">
              {t(aboutT, language, 'ctaDescription')}
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <Link href="/tours" className="btn bg-white text-primary-600 hover:bg-gray-100 btn-lg">
                {t(aboutT, language, 'browseTours')}
              </Link>
              <Link href="/contact" className="btn btn-outline border-white text-white hover:bg-white/10 btn-lg">
                <Phone className="w-5 h-5 mr-2" />
                {t(aboutT, language, 'contactUs')}
              </Link>
            </div>
          </motion.div>
        </div>
      </section>
    </div>
  );
}
