'use client';

import { useState, useEffect } from 'react';
import { useMutation } from '@tanstack/react-query';
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
} from 'lucide-react';
import toast from 'react-hot-toast';
import { useLanguageStore } from '@/store/languageStore';
import { contactT, inquiryFormT, t } from '@/lib/translations';
import { useUserStore } from '@/store/userStore';
import { nationalityPhoneCode } from '@/lib/countryCodeMap';

const contactSchema = z.object({
  firstName: z.string().min(2, 'First name must be at least 2 characters'),
  lastName: z.string().min(2, 'Last name must be at least 2 characters'),
  email: z.string().email('Please enter a valid email address'),
  phone: z.string().optional(),
  nationality: z.string().optional(),
  subject: z.string().min(5, 'Subject must be at least 5 characters'),
  message: z.string().min(20, 'Message must be at least 20 characters'),
  tourInterest: z.string().optional(),
});

type ContactFormData = z.infer<typeof contactSchema>;

const socialLinks = [
  { icon: Facebook, href: 'https://www.facebook.com/girasolegypt', label: 'Facebook' },
  { icon: Instagram, href: 'https://www.instagram.com/girasolegypt/', label: 'Instagram' },
  { icon: Twitter, href: 'https://twitter.com/girasolegypt', label: 'Twitter' },
];

const tourTypeKeys = [
  'egyptTourPackages',
  'nileCruises',
  'dayTours',
  'multiCountry',
  'beach',
  'cultural',
  'spiritual',
  'corporate',
  'other',
] as const;

export default function ContactPage() {
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [phoneCode, setPhoneCode] = useState<{ flag: string; dial: string } | null>(null);
  const { user } = useUserStore();
  const nationalities = Object.keys(nationalityPhoneCode);
  const { language } = useLanguageStore();

  const contactInfo = [
    {
      icon: Phone,
      title: t(contactT, language, 'phone'),
      details: ['+20 2 3771 5511', '+20 1227 011 900'],
      action: 'tel:+20237715511',
    },
    {
      icon: Mail,
      title: t(contactT, language, 'email'),
      details: ['info@girasoltours.com'],
      action: 'mailto:info@girasoltours.com',
    },
    {
      icon: MapPin,
      title: t(contactT, language, 'address'),
      details: [
        'Panorama Pyramids Tower',
        'Entrance 1, Apt. 202 - 2nd floor',
        'Al Haram St. Mashaal, Al Haram',
        'Giza, Egypt 12512',
      ],
    },
    {
      icon: Clock,
      title: t(contactT, language, 'workingHours'),
      details: ['Sunday - Thursday: 9:00 AM - 6:00 PM', 'Friday - Saturday: 10:00 AM - 4:00 PM'],
    },
  ];

  const tourTypes = tourTypeKeys.map(
    (key) => t(contactT, language, `tourType_${key}`)
  );

  // Contact form submission mutation
  const contactMutation = useMutation({
    mutationFn: async (data: ContactFormData) => {
      const response = await contactApi.sendMessage({
        name: `${data.firstName} ${data.lastName}`,
        email: data.email,
        phone: (phoneCode ? phoneCode.dial + ' ' : '') + (data.phone || ''),
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
    setValue,
    watch,
    formState: { errors },
  } = useForm<ContactFormData>({
    resolver: zodResolver(contactSchema),
  });

  const watchedNationality = watch('nationality');

  // Auto-fill from saved user data
  useEffect(() => {
    if (user) {
      const names = (user.fullName || '').trim().split(/\s+/);
      if (names[0]) setValue('firstName', names[0]);
      if (names.length > 1) setValue('lastName', names.slice(1).join(' '));
      if (user.email) setValue('email', user.email);
      if (user.nationality) setValue('nationality', user.nationality);
      if (user.phone) {
        const codeInfo = user.nationality ? nationalityPhoneCode[user.nationality] : null;
        if (codeInfo && user.phone.startsWith(codeInfo.dial)) {
          setValue('phone', user.phone.slice(codeInfo.dial.length).trim());
        } else {
          setValue('phone', user.phone);
        }
      }
    }
  }, [user, setValue]);

  // Auto-update phone code when nationality changes
  useEffect(() => {
    if (watchedNationality && nationalityPhoneCode[watchedNationality]) {
      setPhoneCode(nationalityPhoneCode[watchedNationality]);
    } else {
      setPhoneCode(null);
    }
  }, [watchedNationality]);

  const onSubmit = (data: ContactFormData) => {
    contactMutation.mutate(data);
  };

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[50vh] sm:h-[50vh] md:h-[80vh] lg:h-[120vh] min-h-[300px] sm:min-h-[300px] md:min-h-[450px] lg:min-h-[600px] flex items-center justify-center overflow-hidden">
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
            className="text-2xl sm:text-3xl md:text-5xl lg:text-6xl font-display font-bold mb-3 sm:mb-6"
          >
            {t(contactT, language, 'contactUs')}
          </motion.h1>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6, delay: 0.2 }}
            className="text-xl md:text-2xl text-white/90 mb-8"
          >
            {t(contactT, language, 'heroSubtitle')}
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
      <section id="quote-form" className="py-20 bg-gray-50 scroll-mt-20">
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
                {t(contactT, language, 'sendUsMessage')}
              </h2>
              <p className="text-gray-600 mb-8">
                {t(contactT, language, 'formDescription')}
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
                  <h3 className="text-xl font-bold text-gray-900 mb-2">{t(contactT, language, 'messageSent')}</h3>
                  <p className="text-gray-600 mb-6">
                    {t(contactT, language, 'thankYouMessage')}
                  </p>
                  <button
                    onClick={() => setIsSubmitted(false)}
                    className="btn btn-primary btn-md"
                  >
                    {t(contactT, language, 'sendAnother')}
                  </button>
                </motion.div>
              ) : (
                <form onSubmit={handleSubmit(onSubmit)} className="space-y-6">
                  <div className="grid md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        {t(contactT, language, 'firstName')}
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
                        {t(contactT, language, 'lastName')}
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
                        {t(contactT, language, 'emailAddress')}
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
                        {t(inquiryFormT, language, 'nationality')}
                      </label>
                      <select
                        {...register('nationality')}
                        className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all"
                      >
                        <option value="">{t(inquiryFormT, language, 'selectNationality')}</option>
                        {nationalities.map((nat) => (
                          <option key={nat} value={nat}>{nat}</option>
                        ))}
                      </select>
                    </div>
                  </div>

                  <div className="grid md:grid-cols-2 gap-6">
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        {t(contactT, language, 'phoneNumber')}
                      </label>
                      <div className="flex">
                        {phoneCode && (
                          <span className="inline-flex items-center px-3 border border-r-0 border-gray-200 rounded-l-xl bg-gray-50 text-sm text-gray-600 whitespace-nowrap select-none gap-1.5">
                            <span className="text-base leading-none">{phoneCode.flag}</span>
                            <span className="font-medium">{phoneCode.dial}</span>
                          </span>
                        )}
                        <input
                          type="tel"
                          {...register('phone')}
                          className={`flex-1 min-w-0 px-4 py-3 border border-gray-200 ${phoneCode ? 'rounded-r-xl' : 'rounded-xl'} focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all`}
                          placeholder="234 567 8900"
                        />
                      </div>
                    </div>
                    <div>
                      <label className="block text-sm font-medium text-gray-700 mb-2">
                        {t(contactT, language, 'tourInterest')}
                      </label>
                      <select
                        {...register('tourInterest')}
                        className="w-full px-4 py-3 rounded-xl border border-gray-200 focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all"
                      >
                        <option value="">{t(contactT, language, 'selectTourType')}</option>
                        {tourTypes.map((type) => (
                          <option key={type} value={type}>
                            {type}
                          </option>
                        ))}
                      </select>
                    </div>
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      {t(contactT, language, 'subject')}
                    </label>
                    <input
                      type="text"
                      {...register('subject')}
                      className={`w-full px-4 py-3 rounded-xl border ${
                        errors.subject ? 'border-red-300' : 'border-gray-200'
                      } focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all`}
                      placeholder={t(contactT, language, 'subjectPlaceholder')}
                    />
                    {errors.subject && (
                      <p className="mt-1 text-sm text-red-500">{errors.subject.message}</p>
                    )}
                  </div>

                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-2">
                      {t(contactT, language, 'message')}
                    </label>
                    <textarea
                      {...register('message')}
                      rows={5}
                      className={`w-full px-4 py-3 rounded-xl border ${
                        errors.message ? 'border-red-300' : 'border-gray-200'
                      } focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all resize-none`}
                      placeholder={t(contactT, language, 'messagePlaceholder')}
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
                        {t(contactT, language, 'sending')}
                      </>
                    ) : (
                      <>
                        <Send className="w-5 h-5" />
                        {t(contactT, language, 'sendMessage')}
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
                    <h3 className="text-lg font-bold mb-1">{t(contactT, language, 'chatOnWhatsApp')}</h3>
                    <p className="text-white/80 text-sm">{t(contactT, language, 'instantResponses')}</p>
                  </div>
                  <a
                    href="https://wa.me/201060873700"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="bg-white text-green-600 px-6 py-3 rounded-xl font-semibold hover:bg-green-50 transition-colors"
                  >
                    {t(contactT, language, 'chatNow')}
                  </a>
                </div>
              </div>

              {/* Social Links */}
              <div className="bg-white rounded-2xl p-6 shadow-lg">
                <h3 className="text-lg font-bold text-gray-900 mb-4">{t(contactT, language, 'followUs')}</h3>
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
                <h3 className="text-lg font-bold text-gray-900 mb-4">{t(contactT, language, 'quickLinks')}</h3>
                <div className="space-y-3">
                  <Link
                    href="/tours"
                    className="flex items-center justify-between text-gray-600 hover:text-primary-600 transition-colors"
                  >
                    <span>{t(contactT, language, 'browseOurTours')}</span>
                    <ArrowRight className="w-4 h-4" />
                  </Link>
                  <Link
                    href="/destinations"
                    className="flex items-center justify-between text-gray-600 hover:text-primary-600 transition-colors"
                  >
                    <span>{t(contactT, language, 'exploreDestinations')}</span>
                    <ArrowRight className="w-4 h-4" />
                  </Link>
                  <Link
                    href="/about"
                    className="flex items-center justify-between text-gray-600 hover:text-primary-600 transition-colors"
                  >
                    <span>{t(contactT, language, 'aboutGirasol')}</span>
                    <ArrowRight className="w-4 h-4" />
                  </Link>
                </div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-12 sm:py-16 md:py-20 mx-4 lg:mx-16 mb-16 bg-gradient-to-r from-gray-700 via-gray-600 to-gray-700 rounded-3xl">
        <div className="container-custom text-center">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-4xl font-display font-bold text-white mb-6">
              {t(contactT, language, 'readyToStart')}
            </h2>
            <p className="text-xl text-white/90 mb-8 max-w-2xl mx-auto">
              {t(contactT, language, 'adventureDesc')}
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <Link href="/tours" className="btn bg-white text-primary-600 hover:bg-gray-100 btn-lg">
                {t(contactT, language, 'exploreTours')}
              </Link>
              <a
                href="https://wa.me/201060873700"
                target="_blank"
                rel="noopener noreferrer"
                className="btn btn-outline border-white text-white hover:bg-white/10 btn-lg"
              >
                <MessageSquare className="w-5 h-5 mr-2" />
                {t(contactT, language, 'whatsAppUs')}
              </a>
            </div>
          </motion.div>
        </div>
      </section>
    </div>
  );
}
