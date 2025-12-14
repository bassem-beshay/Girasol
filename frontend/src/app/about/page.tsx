'use client';

import { motion } from 'framer-motion';
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
} from 'lucide-react';

const stats = [
  { icon: Calendar, value: '25+', label: 'Years of Experience' },
  { icon: Users, value: '50,000+', label: 'Happy Travelers' },
  { icon: Globe, value: '15+', label: 'Countries Covered' },
  { icon: Award, value: '100+', label: 'Tour Packages' },
];

const values = [
  {
    icon: Shield,
    title: 'Trust & Safety',
    description: 'Your safety is our priority. We ensure all our tours meet the highest safety standards.',
  },
  {
    icon: Heart,
    title: 'Passion for Travel',
    description: 'We love what we do, and it shows in every tour we organize and every experience we create.',
  },
  {
    icon: Star,
    title: 'Excellence',
    description: 'We strive for excellence in every aspect, from planning to execution of your dream vacation.',
  },
  {
    icon: Users,
    title: 'Customer First',
    description: 'Your satisfaction is our success. We go above and beyond to exceed your expectations.',
  },
];

const milestones = [
  { year: '2010', title: 'Company Founded', description: 'Girasol Egypt Travel and Tours was established in Cairo' },
  { year: '2012', title: 'First 1000 Customers', description: 'Reached our first milestone of happy travelers' },
  { year: '2015', title: 'Expanded Operations', description: 'Opened offices in Luxor, Aswan, and Sharm El Sheikh' },
  { year: '2018', title: 'International Tours', description: 'Started offering tours to Greece, Jordan, and Turkey' },
  { year: '2020', title: 'Digital Transformation', description: 'Launched our online booking platform' },
  { year: '2023', title: '50K+ Travelers', description: 'Celebrated serving over 50,000 happy customers' },
];

const team = [
  {
    name: 'Ahmed Hassan',
    role: 'Founder & CEO',
    image: '/images/team/ceo.jpg',
    description: 'With over 30 years in tourism, Ahmed founded Girasol with a vision to showcase Egypt\'s beauty.',
  },
  {
    name: 'Sarah Mohamed',
    role: 'Operations Director',
    image: '/images/team/operations.jpg',
    description: 'Sarah ensures every tour runs smoothly, from logistics to customer experience.',
  },
  {
    name: 'Omar Khalil',
    role: 'Head of Sales',
    image: '/images/team/sales.jpg',
    description: 'Omar leads our sales team with passion and dedication to customer satisfaction.',
  },
  {
    name: 'Nadia Farouk',
    role: 'Customer Relations',
    image: '/images/team/customer.jpg',
    description: 'Nadia is the friendly voice that helps travelers plan their perfect Egyptian adventure.',
  },
];

const offices = [
  { city: 'Cairo (HQ)', country: 'Egypt' },
  { city: 'Luxor', country: 'Egypt' },
  { city: 'Aswan', country: 'Egypt' },
  { city: 'Hurghada', country: 'Egypt' },
  { city: 'Sharm El Sheikh', country: 'Egypt' },
  { city: 'Dahab', country: 'Egypt' },
];

export default function AboutPage() {
  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[60vh] min-h-[500px] flex items-center justify-center overflow-hidden">
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
            className="text-5xl md:text-6xl font-display font-bold mb-6"
          >
            About Girasol Tours
          </motion.h1>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="text-xl md:text-2xl text-white/90"
          >
            Your trusted partner for unforgettable Egyptian adventures since 2010
          </motion.p>
        </div>
      </section>

      {/* Stats Section */}
      <section className="py-16 bg-white">
        <div className="container-custom">
          <div className="grid grid-cols-2 md:grid-cols-4 gap-8">
            {stats.map((stat, index) => (
              <motion.div
                key={stat.label}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="text-center"
              >
                <div className="w-16 h-16 mx-auto mb-4 rounded-2xl bg-primary-100 flex items-center justify-center">
                  <stat.icon className="w-8 h-8 text-primary-600" />
                </div>
                <div className="text-4xl font-bold text-gray-900 mb-2">{stat.value}</div>
                <div className="text-gray-600">{stat.label}</div>
              </motion.div>
            ))}
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
                Our Story
              </h2>
              <div className="space-y-4 text-gray-600 leading-relaxed">
                <p>
                  Girasol Egypt Travel and Tours was established in 2010 in Cairo, Egypt,
                  with a passion for sharing the wonders of this ancient land with the world.
                  Our management team brings over 25 years of expertise in the tourism industry,
                  ensuring every journey is crafted with knowledge, care, and attention to detail.
                </p>
                <p>
                  We operate as a receptive incoming travel company specializing in Egypt tours
                  and excursions. From the majestic pyramids of Giza to the serene waters of the Nile,
                  from the vibrant coral reefs of the Red Sea to the timeless temples of Luxor and Aswan,
                  we bring Egypt's treasures to life.
                </p>
                <p>
                  Today, we have local offices throughout Egypt including Aswan, Luxor, Hurghada,
                  Dahab, and Sharm El Sheikh. We also maintain qualified service suppliers across
                  multiple international destinations including Brazil, Peru, Greece, Turkey, Jordan,
                  the UAE, Morocco, India, Thailand, and Vietnam.
                </p>
              </div>
              <div className="mt-8 flex flex-wrap gap-4">
                <Link href="/tours" className="btn btn-primary btn-lg">
                  Explore Our Tours
                  <ArrowRight className="w-5 h-5 ml-2" />
                </Link>
                <Link href="/contact" className="btn btn-outline btn-lg">
                  Contact Us
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
                  className="object-cover"
                />
              </div>
              <div className="absolute -bottom-8 -left-8 bg-white p-6 rounded-2xl shadow-xl">
                <div className="flex items-center gap-4">
                  <div className="w-16 h-16 rounded-full bg-primary-500 flex items-center justify-center">
                    <Award className="w-8 h-8 text-white" />
                  </div>
                  <div>
                    <div className="text-2xl font-bold text-gray-900">Licensed</div>
                    <div className="text-gray-600">Travel Agency</div>
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
              Our Values
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              These core values guide everything we do at Girasol Tours
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
              What We Offer
            </h2>
            <p className="text-xl text-white/80 max-w-2xl mx-auto">
              Comprehensive tourism services tailored to your needs
            </p>
          </motion.div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {[
              'Short and long-duration Egypt tour packages',
              'Multi-destination combination tours',
              'Spiritual and meditation-focused journeys',
              'Cultural and educational programs',
              'Nile River cruises (3-7 nights)',
              'Daily city excursions',
              'Hotel reservations',
              'Domestic and international airline ticketing',
              'Event and conference organization',
            ].map((service, index) => (
              <motion.div
                key={service}
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
              Our Journey
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Key milestones in our story
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
              Meet Our Team
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Dedicated professionals passionate about creating unforgettable experiences
            </p>
          </motion.div>

          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
            {team.map((member, index) => (
              <motion.div
                key={member.name}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="group"
              >
                <div className="relative h-80 rounded-2xl overflow-hidden mb-6">
                  <div className="absolute inset-0 bg-gradient-to-t from-gray-900/80 to-transparent z-10" />
                  <div className="absolute inset-0 bg-primary-600 flex items-center justify-center">
                    <Users className="w-20 h-20 text-white/30" />
                  </div>
                  <div className="absolute bottom-0 left-0 right-0 p-6 z-20">
                    <h3 className="text-xl font-bold text-white mb-1">{member.name}</h3>
                    <p className="text-primary-300">{member.role}</p>
                  </div>
                </div>
                <p className="text-gray-600 text-center">{member.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Offices Section */}
      <section className="py-20 bg-gray-50">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl font-display font-bold text-gray-900 mb-4">
              Our Offices
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              We have presence across major Egyptian destinations
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
                <h3 className="font-bold text-gray-900">{office.city}</h3>
                <p className="text-gray-500 text-sm">{office.country}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-r from-primary-600 to-secondary-500">
        <div className="container-custom text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-4xl font-display font-bold text-white mb-6">
              Ready to Explore Egypt?
            </h2>
            <p className="text-xl text-white/90 mb-8 max-w-2xl mx-auto">
              Let us help you create memories that will last a lifetime.
              Contact us today to start planning your dream Egyptian adventure.
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <Link href="/tours" className="btn bg-white text-primary-600 hover:bg-gray-100 btn-lg">
                Browse Tours
              </Link>
              <Link href="/contact" className="btn btn-outline border-white text-white hover:bg-white/10 btn-lg">
                <Phone className="w-5 h-5 mr-2" />
                Contact Us
              </Link>
            </div>
          </motion.div>
        </div>
      </section>
    </div>
  );
}
