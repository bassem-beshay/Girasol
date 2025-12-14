'use client';

import { useState } from 'react';
import { useQuery, useMutation } from '@tanstack/react-query';
import { contactApi } from '@/lib/api';
import { motion } from 'framer-motion';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { z } from 'zod';
import Link from 'next/link';
import {
  Phone,
  Mail,
  MapPin,
  Clock,
  Send,
  Loader2,
  CheckCircle,
  MessageSquare,
  Facebook,
  Instagram,
  Twitter,
  ArrowRight,
  HelpCircle,
} from 'lucide-react';
import toast from 'react-hot-toast';

const contactSchema = z.object({
  firstName: z.string().min(2, 'First name must be at least 2 characters'),
  lastName: z.string().min(2, 'Last name must be at least 2 characters'),
  email: z.string().email('Please enter a valid email address'),
  phone: z.string().optional(),
  subject: z.string().min(5, 'Subject must be at least 5 characters'),
  message: z.string().min(20, 'Message must be at least 20 characters'),
  tourInterest: z.string().optional(),
});

type ContactFormData = z.infer<typeof contactSchema>;

interface FAQ {
  id: number;
  question: string;
  answer: string;
  category: string;
  sort_order: number;
}

interface Office {
  id: number;
  city: string;
  country: string;
  address: string;
  phone: string;
  email: string;
  is_headquarters: boolean;
}

interface FAQsResponse {
  count: number;
  results: FAQ[];
}

interface OfficesResponse {
  count: number;
  results: Office[];
}

const contactInfo = [
  {
    icon: Phone,
    title: 'Phone',
    details: ['+20 2 3771 5511', '+20 1227 011 900'],
    action: 'tel:+20237715511',
  },
  {
    icon: Mail,
    title: 'Email',
    details: ['info@girasoltours.com'],
    action: 'mailto:info@girasoltours.com',
  },
  {
    icon: MapPin,
    title: 'Address',
    details: [
      'Panorama Pyramids Tower',
      'Entrance 1, Apt. 202 - 2nd floor',
      'Al Haram St. Mashaal, Al Haram',
      'Giza, Egypt 12512',
    ],
  },
  {
    icon: Clock,
    title: 'Working Hours',
    details: ['Sunday - Thursday: 9:00 AM - 6:00 PM', 'Friday - Saturday: 10:00 AM - 4:00 PM'],
  },
];

const socialLinks = [
  { icon: Facebook, href: 'https://www.facebook.com/girasolegypt', label: 'Facebook' },
  { icon: Instagram, href: 'https://www.instagram.com/girasolegypt/', label: 'Instagram' },
  { icon: Twitter, href: 'https://twitter.com/girasolegypt', label: 'Twitter' },
];

const tourTypes = [
  'Egypt Tour Packages',
  'Nile Cruises',
  'Day Tours & Excursions',
  'Multi-Country Tours',
  'Beach & Relaxation',
  'Cultural & Historical Tours',
  'Spiritual & Meditation Tours',
  'Corporate Events',
  'Other',
];

export default function ContactPage() {
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [openFaq, setOpenFaq] = useState<number | null>(null);

  // Fetch FAQs from API
  const { data: faqsData } = useQuery<FAQsResponse>({
    queryKey: ['faqs'],
    queryFn: async () => {
      const response = await contactApi.getFaqs();
      return response.data;
    },
  });

  // Fetch Offices from API
  const { data: officesData } = useQuery<OfficesResponse>({
    queryKey: ['offices'],
    queryFn: async () => {
      const response = await contactApi.getOffices();
      return response.data;
    },
  });

  const faqs = faqsData?.results || [];
  const offices = officesData?.results || [];

  // Contact form submission mutation
  const contactMutation = useMutation({
    mutationFn: async (data: ContactFormData) => {
      const response = await contactApi.sendMessage({
        name: `${data.firstName} ${data.lastName}`,
        email: data.email,
        phone: data.phone || '',
        subject: data.subject,
        message: data.message,
        tour_interest: data.tourInterest || '',
      });
      return response.data;
    },
    onSuccess: () => {
      setIsSubmitted(true);
      toast.success('Your message has been sent successfully!');
      reset();
    },
    onError: () => {
      toast.error('Something went wrong. Please try again.');
    },
  });

  const {
    register,
    handleSubmit,
    reset,
    formState: { errors },
  } = useForm<ContactFormData>({
    resolver: zodResolver(contactSchema),
  });

  const onSubmit = (data: ContactFormData) => {
    contactMutation.mutate(data);
  };

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[50vh] min-h-[400px] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-primary-900/90 to-primary-800/80 z-10" />
        <div
          className="absolute inset-0 bg-cover bg-center"
          style={{ backgroundImage: "url('/images/contact-hero.jpg')" }}
        />
        <div className="relative z-20 text-center text-white max-w-4xl mx-auto px-4">
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="text-5xl md:text-6xl font-display font-bold mb-6"
          >
            Contact Us
          </motion.h1>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="text-xl md:text-2xl text-white/90"
          >
            We're here to help you plan your perfect Egyptian adventure
          </motion.p>
        </div>
      </section>

      {/* Contact Info Cards */}
      <section className="py-16 bg-white relative -mt-20 z-30">
        <div className="container-custom">
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {contactInfo.map((info, index) => (
              <motion.div
                key={info.title}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: index * 0.1 }}
                className="bg-white rounded-2xl p-6 shadow-xl hover:shadow-2xl transition-shadow"
              >
                <div className="w-14 h-14 rounded-xl bg-primary-100 flex items-center justify-center mb-4">
                  <info.icon className="w-7 h-7 text-primary-600" />
                </div>
                <h3 className="text-lg font-bold text-gray-900 mb-3">{info.title}</h3>
                {info.details.map((detail, i) => (
                  <p key={i} className="text-gray-600 text-sm">
                    {info.action && i === 0 ? (
                      <a href={info.action} className="hover:text-primary-600 transition-colors">
                        {detail}
                      </a>
                    ) : (
                      detail
                    )}
                  </p>
                ))}
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Main Contact Section */}
      <section className="py-20 bg-gray-50">
        <div className="container-custom">
          <div className="grid lg:grid-cols-2 gap-16">
            {/* Contact Form */}
            <motion.div
              initial={{ opacity: 0, x: -30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
            >
              <h2 className="text-3xl font-display font-bold text-gray-900 mb-2">
                Send Us a Message
              </h2>
              <p className="text-gray-600 mb-8">
                Fill out the form below and we'll get back to you within 24 hours.
              </p>

              {isSubmitted ? (
                <motion.div
                  initial={{ opacity: 0, scale: 0.9 }}
                  animate={{ opacity: 1, scale: 1 }}
                  className="bg-green-50 border border-green-200 rounded-2xl p-8 text-center"
                >
                  <div className="w-16 h-16 mx-auto mb-4 rounded-full bg-green-100 flex items-center justify-center">
                    <CheckCircle className="w-8 h-8 text-green-600" />
                  </div>
                  <h3 className="text-xl font-bold text-gray-900 mb-2">Message Sent!</h3>
                  <p className="text-gray-600 mb-6">
                    Thank you for contacting us. We'll get back to you within 24 hours.
                  </p>
                  <button
                    onClick={() => setIsSubmitted(false)}
                    className="btn btn-primary btn-md"
                  >
                    Send Another Message
                  </button>
                </motion.div>
              ) : (
                <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
                  <div className="grid md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        First Name *
                      </label>
                      <input
                        type="text"
                        {...register('firstName')}
                        className={`w-full px-4 py-3 rounded-xl border ${
                          errors.firstName ? 'border-red-300' : 'border-gray-200'
                        } focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all`}
                        placeholder="John"
                      />
                      {errors.firstName && (
                        <p className="mt-1 text-sm text-red-500">{errors.firstName.message}</p>
                      )}
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Last Name *
                      </label>
                      <input
                        type="text"
                        {...register('lastName')}
                        className={`w-full px-4 py-3 rounded-xl border ${
                          errors.lastName ? 'border-red-300' : 'border-gray-200'
                        } focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all`}
                        placeholder="Doe"
                      />
                      {errors.lastName && (
                        <p className="mt-1 text-sm text-red-500">{errors.lastName.message}</p>
                      )}
                    </div>
                  </div>

                  <div className="grid md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Email Address *
                      </label>
                      <input
                        type="email"
                        {...register('email')}
                        className={`w-full px-4 py-3 rounded-xl border ${
                          errors.email ? 'border-red-300' : 'border-gray-200'
                        } focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all`}
                        placeholder="john@example.com"
                      />
                      {errors.email && (
                        <p className="mt-1 text-sm text-red-500">{errors.email.message}</p>
                      )}
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        Phone Number
                      </label>
                      <input
                        type="tel"
                        {...register('phone')}
                        className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all"
                        placeholder="+1 234 567 8900"
                      />
                    </div>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Tour Interest
                    </label>
                    <select
                      {...register('tourInterest')}
                      className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all"
                    >
                      <option value="">Select a tour type</option>
                      {tourTypes.map((type) => (
                        <option key={type} value={type}>
                          {type}
                        </option>
                      ))}
                    </select>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Subject *
                    </label>
                    <input
                      type="text"
                      {...register('subject')}
                      className={`w-full px-4 py-3 rounded-xl border ${
                        errors.subject ? 'border-red-300' : 'border-gray-200'
                      } focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all`}
                      placeholder="How can we help you?"
                    />
                    {errors.subject && (
                      <p className="mt-1 text-sm text-red-500">{errors.subject.message}</p>
                    )}
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      Message *
                    </label>
                    <textarea
                      {...register('message')}
                      rows={5}
                      className={`w-full px-4 py-3 rounded-xl border ${
                        errors.message ? 'border-red-300' : 'border-gray-200'
                      } focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all resize-none`}
                      placeholder="Tell us about your travel plans, interests, and any questions you have..."
                    />
                    {errors.message && (
                      <p className="mt-1 text-sm text-red-500">{errors.message.message}</p>
                    )}
                  </div>

                  <button
                    type="submit"
                    disabled={contactMutation.isPending}
                    className="w-full py-4 px-6 bg-gradient-to-r from-primary-500 to-primary-600 text-white rounded-xl font-semibold
                             hover:from-primary-600 hover:to-primary-700 focus:ring-4 focus:ring-primary-500/30
                             transition-all duration-300 flex items-center justify-center gap-2 disabled:opacity-70"
                  >
                    {contactMutation.isPending ? (
                      <>
                        <Loader2 className="w-5 h-5 animate-spin" />
                        Sending...
                      </>
                    ) : (
                      <>
                        <Send className="w-5 h-5" />
                        Send Message
                      </>
                    )}
                  </button>
                </form>
              )}
            </motion.div>

            {/* Map & Additional Info */}
            <motion.div
              initial={{ opacity: 0, x: 30 }}
              whileInView={{ opacity: 1, x: 0 }}
              viewport={{ once: true }}
              transition={{ duration: 0.6 }}
              className="space-y-8"
            >
              {/* Map */}
              <div className="bg-white rounded-2xl overflow-hidden shadow-lg h-[300px]">
                <iframe
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3456.0675898561!2d31.1247!3d29.9857!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMjnCsDU5JzA4LjUiTiAzMcKwMDcnMjguOSJF!5e0!3m2!1sen!2seg!4v1620000000000!5m2!1sen!2seg"
                  width="100%"
                  height="100%"
                  style={{ border: 0 }}
                  allowFullScreen
                  loading="lazy"
                  referrerPolicy="no-referrer-when-downgrade"
                />
              </div>

              {/* WhatsApp CTA */}
              <div className="bg-gradient-to-r from-green-500 to-green-600 rounded-2xl p-6 text-white">
                <div className="flex items-center gap-4">
                  <div className="w-14 h-14 rounded-full bg-white/20 flex items-center justify-center">
                    <MessageSquare className="w-7 h-7" />
                  </div>
                  <div className="flex-1">
                    <h3 className="text-lg font-bold mb-1">Chat on WhatsApp</h3>
                    <p className="text-white/80 text-sm">Get instant responses to your queries</p>
                  </div>
                  <a
                    href="https://wa.me/201060873700"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="bg-white text-green-600 px-6 py-3 rounded-xl font-semibold hover:bg-green-50 transition-colors"
                  >
                    Chat Now
                  </a>
                </div>
              </div>

              {/* Social Links */}
              <div className="bg-white rounded-2xl p-6 shadow-lg">
                <h3 className="text-lg font-bold text-gray-900 mb-4">Follow Us</h3>
                <div className="flex gap-4">
                  {socialLinks.map((social) => (
                    <a
                      key={social.label}
                      href={social.href}
                      target="_blank"
                      rel="noopener noreferrer"
                      className="w-12 h-12 rounded-xl bg-gray-100 flex items-center justify-center text-gray-600 hover:bg-primary-500 hover:text-white transition-all"
                    >
                      <social.icon className="w-5 h-5" />
                    </a>
                  ))}
                </div>
              </div>

              {/* Quick Links */}
              <div className="bg-white rounded-2xl p-6 shadow-lg">
                <h3 className="text-lg font-bold text-gray-900 mb-4">Quick Links</h3>
                <div className="space-y-3">
                  <Link
                    href="/tours"
                    className="flex items-center justify-between text-gray-600 hover:text-primary-600 transition-colors"
                  >
                    <span>Browse Our Tours</span>
                    <ArrowRight className="w-4 h-4" />
                  </Link>
                  <Link
                    href="/destinations"
                    className="flex items-center justify-between text-gray-600 hover:text-primary-600 transition-colors"
                  >
                    <span>Explore Destinations</span>
                    <ArrowRight className="w-4 h-4" />
                  </Link>
                  <Link
                    href="/about"
                    className="flex items-center justify-between text-gray-600 hover:text-primary-600 transition-colors"
                  >
                    <span>About Girasol Tours</span>
                    <ArrowRight className="w-4 h-4" />
                  </Link>
                </div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Our Offices Section */}
      <section className="py-20 bg-white">
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
              Visit us at any of our locations across Egypt
            </p>
          </motion.div>

          {offices.length > 0 ? (
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
              {offices.map((office, index) => (
                <motion.div
                  key={office.id}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  className="bg-gray-50 rounded-2xl p-6 hover:shadow-lg transition-shadow"
                >
                  <div className="flex items-start gap-4">
                    <div className="w-12 h-12 rounded-xl bg-primary-100 flex items-center justify-center flex-shrink-0">
                      <MapPin className="w-6 h-6 text-primary-600" />
                    </div>
                    <div>
                      <h3 className="text-lg font-bold text-gray-900 mb-2">
                        {office.city}
                        {office.is_headquarters && (
                          <span className="ml-2 text-xs bg-primary-100 text-primary-700 px-2 py-1 rounded-full">
                            HQ
                          </span>
                        )}
                      </h3>
                      <p className="text-gray-600 text-sm mb-2">{office.address}</p>
                      <a
                        href={`tel:${office.phone.replace(/\s/g, '')}`}
                        className="text-primary-600 text-sm font-medium hover:text-primary-700"
                      >
                        {office.phone}
                      </a>
                    </div>
                  </div>
                </motion.div>
              ))}
            </div>
          ) : (
            <div className="text-center py-8">
              <Loader2 className="w-8 h-8 animate-spin text-primary-500 mx-auto mb-4" />
              <p className="text-gray-500">Loading offices...</p>
            </div>
          )}
        </div>
      </section>

      {/* FAQ Section */}
      <section className="py-20 bg-gray-50">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-4xl font-display font-bold text-gray-900 mb-4">
              Frequently Asked Questions
            </h2>
            <p className="text-xl text-gray-600 max-w-2xl mx-auto">
              Find quick answers to common questions
            </p>
          </motion.div>

          {faqs.length > 0 ? (
            <div className="max-w-3xl mx-auto space-y-4">
              {faqs.map((faq, index) => (
                <motion.div
                  key={faq.id}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ duration: 0.5, delay: index * 0.1 }}
                  className="bg-white rounded-2xl overflow-hidden shadow-md"
                >
                  <button
                    onClick={() => setOpenFaq(openFaq === index ? null : index)}
                    className="w-full px-6 py-4 text-left flex items-center justify-between hover:bg-gray-50 transition-colors"
                  >
                    <span className="font-semibold text-gray-900">{faq.question}</span>
                    <span
                      className={`transform transition-transform ${
                        openFaq === index ? 'rotate-180' : ''
                      }`}
                    >
                      <svg
                        className="w-5 h-5 text-gray-500"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M19 9l-7 7-7-7"
                        />
                      </svg>
                    </span>
                  </button>
                  {openFaq === index && (
                    <div className="px-6 pb-4">
                      <p className="text-gray-600">{faq.answer}</p>
                    </div>
                  )}
                </motion.div>
              ))}
            </div>
          ) : (
            <div className="text-center py-8">
              <HelpCircle className="w-16 h-16 text-gray-300 mx-auto mb-4" />
              <p className="text-gray-500">Loading FAQs...</p>
            </div>
          )}
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
              Ready to Start Your Adventure?
            </h2>
            <p className="text-xl text-white/90 mb-8 max-w-2xl mx-auto">
              Let us help you create the Egyptian journey of your dreams.
              Our team is ready to assist you every step of the way.
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <Link href="/tours" className="btn bg-white text-primary-600 hover:bg-gray-100 btn-lg">
                Explore Tours
              </Link>
              <a
                href="tel:+20237715511"
                className="btn btn-outline border-white text-white hover:bg-white/10 btn-lg"
              >
                <Phone className="w-5 h-5 mr-2" />
                Call Us Now
              </a>
            </div>
          </motion.div>
        </div>
      </section>
    </div>
  );
}
