'use client';

import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { contactApi } from '@/lib/api';
import { motion } from 'framer-motion';
import { Mail, Send, Check, Loader2, MailCheck, RefreshCw } from 'lucide-react';
import toast from 'react-hot-toast';
import { useLanguageStore } from '@/store/languageStore';
import { newsletterT, t } from '@/lib/translations';

// Declare grecaptcha global
declare global {
  interface Window {
    grecaptcha: {
      ready: (cb: () => void) => void;
      execute: (siteKey: string, options: { action: string }) => Promise<string>;
    };
  }
}

const RECAPTCHA_SITE_KEY = process.env.NEXT_PUBLIC_RECAPTCHA_SITE_KEY || '';

type SubscriptionStatus =
  | 'idle'
  | 'pending_confirmation'
  | 'already_subscribed'
  | 'reactivated'
  | 'confirmation_resent';

export function Newsletter() {
  const [email, setEmail] = useState('');
  const [status, setStatus] = useState<SubscriptionStatus>('idle');
  const { language } = useLanguageStore();

  // Newsletter subscription mutation
  const subscribeMutation = useMutation({
    mutationFn: async (email: string) => {
      let recaptcha_token = '';
      try {
        if (window.grecaptcha && RECAPTCHA_SITE_KEY) {
          await new Promise<void>((resolve) => window.grecaptcha.ready(resolve));
          recaptcha_token = await window.grecaptcha.execute(RECAPTCHA_SITE_KEY, { action: 'newsletter_subscribe' });
        }
      } catch {
        // Continue without recaptcha if it fails
      }
      const response = await contactApi.subscribeNewsletter({ email, recaptcha_token });
      return response.data;
    },
    onSuccess: (data) => {
      const responseStatus = data.status as SubscriptionStatus;
      setStatus(responseStatus);

      // Show appropriate toast based on status
      switch (responseStatus) {
        case 'pending_confirmation':
        case 'confirmation_resent':
          toast.success('Please check your email to confirm your subscription!');
          break;
        case 'already_subscribed':
          toast('You are already subscribed!', { icon: '👋' });
          break;
        case 'reactivated':
          toast.success('Welcome back! Your subscription has been reactivated.');
          break;
        default:
          toast.success('Thank you for subscribing!');
      }

      setEmail('');
    },
    onError: (error: any) => {
      if (error?.response?.status === 429) {
        toast.error('Too many attempts. Please try again later.');
      } else {
        toast.error('Something went wrong. Please try again.');
      }
    },
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!email) {
      toast.error('Please enter your email address');
      return;
    }

    // Validate email format
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
      toast.error('Please enter a valid email address');
      return;
    }

    subscribeMutation.mutate(email);
  };

  const renderSuccessMessage = () => {
    switch (status) {
      case 'pending_confirmation':
      case 'confirmation_resent':
        return (
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="flex flex-col items-center gap-4 text-white"
          >
            <div className="w-16 h-16 rounded-full bg-amber-500 flex items-center justify-center">
              <MailCheck className="w-8 h-8" />
            </div>
            <div className="text-center">
              <h3 className="text-xl font-semibold mb-2">{t(newsletterT, language, 'checkEmail')}</h3>
              <p className="text-white/80">
                {t(newsletterT, language, 'confirmationSent')}
                <br />
                {t(newsletterT, language, 'clickToConfirm')}
              </p>
            </div>
            <button
              onClick={() => setStatus('idle')}
              className="mt-4 text-sm text-white/60 hover:text-white flex items-center gap-2"
            >
              <RefreshCw className="w-4 h-4" />
              {t(newsletterT, language, 'differentEmail')}
            </button>
          </motion.div>
        );

      case 'already_subscribed':
        return (
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="flex flex-col items-center gap-4 text-white"
          >
            <div className="w-16 h-16 rounded-full bg-blue-500 flex items-center justify-center">
              <Check className="w-8 h-8" />
            </div>
            <div className="text-center">
              <h3 className="text-xl font-semibold mb-2">{t(newsletterT, language, 'alreadySubscribed')}</h3>
              <p className="text-white/80">
                {t(newsletterT, language, 'alreadyOnList')}
                <br />
                {t(newsletterT, language, 'keepEye')}
              </p>
            </div>
            <button
              onClick={() => setStatus('idle')}
              className="mt-4 text-sm text-white/60 hover:text-white flex items-center gap-2"
            >
              <RefreshCw className="w-4 h-4" />
              {t(newsletterT, language, 'tryAnother')}
            </button>
          </motion.div>
        );

      case 'reactivated':
        return (
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="flex flex-col items-center gap-4 text-white"
          >
            <div className="w-16 h-16 rounded-full bg-green-500 flex items-center justify-center">
              <Check className="w-8 h-8" />
            </div>
            <div className="text-center">
              <h3 className="text-xl font-semibold mb-2">{t(newsletterT, language, 'welcomeBack')}</h3>
              <p className="text-white/80">
                {t(newsletterT, language, 'reactivated')}
                <br />
                {t(newsletterT, language, 'startReceiving')}
              </p>
            </div>
          </motion.div>
        );

      default:
        return null;
    }
  };

  const showForm = status === 'idle';

  return (
    <section className="section-padding">
      <div className="container-custom">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="bg-gradient-to-r from-gray-700 via-gray-600 to-gray-700 rounded-3xl p-8 md:p-12 lg:p-16 text-center relative overflow-hidden"
        >
          {/* Pattern overlay */}
          <div className="absolute inset-0 bg-hero-pattern opacity-10" />

          {/* Decorative elements */}
          <div className="absolute top-0 right-0 w-64 h-64 bg-primary-500/15 rounded-full blur-3xl" />
          <div className="absolute bottom-0 left-0 w-48 h-48 bg-primary-500/10 rounded-full blur-2xl" />

          <div className="relative z-10 max-w-2xl mx-auto">
            {showForm ? (
              <>
                {/* Icon */}
                <div className="w-16 h-16 mx-auto mb-6 rounded-2xl bg-white/10 flex items-center justify-center">
                  <Mail className="w-8 h-8 text-white" />
                </div>

                {/* Content */}
                <h2 className="text-3xl md:text-4xl font-display font-bold text-white mb-4">
                  {t(newsletterT, language, 'title')}
                </h2>
                <p className="text-lg text-white/80 mb-8">
                  {t(newsletterT, language, 'description')}
                </p>

                {/* Form */}
                <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-4 max-w-md mx-auto">
                  <div className="relative flex-1">
                    <Mail className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                    <input
                      type="email"
                      value={email}
                      onChange={(e) => setEmail(e.target.value)}
                      placeholder={t(newsletterT, language, 'placeholder')}
                      className="w-full pl-12 pr-4 py-4 rounded-xl bg-white text-gray-900 placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-white/50"
                    />
                  </div>
                  <button
                    type="submit"
                    disabled={subscribeMutation.isPending}
                    className="btn btn-lg bg-primary-500 text-white hover:bg-primary-600 disabled:opacity-50 disabled:cursor-not-allowed"
                  >
                    {subscribeMutation.isPending ? (
                      <span className="flex items-center">
                        <Loader2 className="animate-spin -ml-1 mr-2 h-5 w-5" />
                        {t(newsletterT, language, 'subscribing')}
                      </span>
                    ) : (
                      <>{t(newsletterT, language, 'subscribe')}
                        <Send className="w-5 h-5 ml-2" />
                      </>
                    )}
                  </button>
                </form>

                {/* Disclaimer */}
                <p className="text-sm text-white/60 mt-4 flex items-center justify-center gap-2">
                  <Check className="w-4 h-4" />
                  {t(newsletterT, language, 'noSpam')}
                </p>
              </>
            ) : (
              renderSuccessMessage()
            )}
          </div>
        </motion.div>
      </div>
    </section>
  );
}
