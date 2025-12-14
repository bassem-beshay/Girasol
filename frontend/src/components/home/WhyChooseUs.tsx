'use client';

import { motion } from 'framer-motion';
import { Clock, MapPin, Headphones, BadgePercent } from 'lucide-react';

const features = [
  {
    icon: Clock,
    title: '25+ Years Experience',
    description: 'Decades of expertise in crafting unforgettable Egyptian journeys',
  },
  {
    icon: MapPin,
    title: 'Local Offices in 6 Cities',
    description: 'On-ground support in Cairo, Luxor, Aswan, Sharm, Hurghada & Dahab',
  },
  {
    icon: Headphones,
    title: '24/7 WhatsApp Support',
    description: 'Instant assistance whenever you need it, wherever you are',
  },
  {
    icon: BadgePercent,
    title: 'Best Price Guarantee',
    description: 'Competitive prices with no hidden costs or surprise fees',
  },
];

export function WhyChooseUs() {
  return (
    <section className="section-padding bg-gray-50">
      <div className="container-custom">
        {/* Header */}
        <div className="text-center max-w-2xl mx-auto mb-12">
          <motion.span
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-primary-600 font-medium mb-2 block"
          >
            Why Girasol Tours
          </motion.span>
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.1 }}
            className="heading-2 text-gray-900 mb-4"
          >
            Your Trusted Partner in Egyptian Tourism
          </motion.h2>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ delay: 0.2 }}
            className="text-gray-600"
          >
            We combine deep local knowledge with international service standards
            to deliver experiences that exceed expectations.
          </motion.p>
        </div>

        {/* Features grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {features.map((feature, index) => (
            <motion.div
              key={feature.title}
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: index * 0.1 }}
              className="text-center group"
            >
              <div className="w-16 h-16 mx-auto mb-4 rounded-2xl bg-primary-100 flex items-center justify-center group-hover:bg-primary-500 transition-colors">
                <feature.icon className="w-8 h-8 text-primary-600 group-hover:text-white transition-colors" />
              </div>
              <h3 className="text-lg font-semibold text-gray-900 mb-2">
                {feature.title}
              </h3>
              <p className="text-gray-600 text-sm">
                {feature.description}
              </p>
            </motion.div>
          ))}
        </div>

        {/* Stats */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="mt-16 grid grid-cols-2 md:grid-cols-4 gap-8 p-8 bg-white rounded-2xl shadow-lg"
        >
          {[
            { value: '25+', label: 'Years Experience' },
            { value: '50,000+', label: 'Happy Travelers' },
            { value: '6', label: 'Local Offices' },
            { value: '10+', label: 'Countries Partners' },
          ].map((stat, index) => (
            <div key={stat.label} className="text-center">
              <div className="text-3xl md:text-4xl font-bold text-primary-600 mb-1">
                {stat.value}
              </div>
              <div className="text-gray-600 text-sm">{stat.label}</div>
            </div>
          ))}
        </motion.div>
      </div>
    </section>
  );
}
