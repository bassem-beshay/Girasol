'use client';

import { useState } from 'react';
import { useMutation } from '@tanstack/react-query';
import { contactApi } from '@/lib/api';
import { motion } from 'framer-motion';
import { Mail, Send, Check, Loader2 } from 'lucide-react';
import toast from 'react-hot-toast';

export function Newsletter() {
  const [email, setEmail] = useState('');
  const [isSubscribed, setIsSubscribed] = useState(false);

  // Newsletter subscription mutation
  const subscribeMutation = useMutation({
    mutationFn: async (email: string) => {
      const response = await contactApi.subscribeNewsletter({ email });
      return response.data;
    },
    onSuccess: () => {
      setIsSubscribed(true);
      toast.success('Thank you for subscribing!');
      setEmail('');
    },
    onError: () => {
      toast.error('Something went wrong. Please try again.');
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

  return (
    <section className="section-padding">
      <div className="container-custom">
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="bg-gradient-to-r from-primary-600 to-primary-700 rounded-3xl p-8 md:p-12 lg:p-16 text-center relative overflow-hidden"
        >
          {/* Pattern overlay */}
          <div className="absolute inset-0 bg-hero-pattern opacity-10" />

          {/* Decorative elements */}
          <div className="absolute top-0 right-0 w-64 h-64 bg-primary-400/20 rounded-full blur-3xl" />
          <div className="absolute bottom-0 left-0 w-48 h-48 bg-secondary-400/20 rounded-full blur-2xl" />

          <div className="relative z-10 max-w-2xl mx-auto">
            {/* Icon */}
            <div className="w-16 h-16 mx-auto mb-6 rounded-2xl bg-white/10 flex items-center justify-center">
              <Mail className="w-8 h-8 text-white" />
            </div>

            {/* Content */}
            <h2 className="text-3xl md:text-4xl font-display font-bold text-white mb-4">
              Get Exclusive Deals & Travel Tips
            </h2>
            <p className="text-lg text-white/80 mb-8">
              Subscribe to our newsletter and be the first to know about special
              offers, new tours, and insider travel tips.
            </p>

            {/* Form */}
            {isSubscribed ? (
              <motion.div
                initial={{ scale: 0.9, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                className="flex items-center justify-center gap-3 text-white"
              >
                <div className="w-12 h-12 rounded-full bg-green-500 flex items-center justify-center">
                  <Check className="w-6 h-6" />
                </div>
                <span className="text-lg font-medium">
                  You&apos;re on the list! Check your inbox for a welcome email.
                </span>
              </motion.div>
            ) : (
              <form onSubmit={handleSubmit} className="flex flex-col sm:flex-row gap-4 max-w-md mx-auto">
                <div className="relative flex-1">
                  <Mail className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
                  <input
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Enter your email"
                    className="w-full pl-12 pr-4 py-4 rounded-xl bg-white text-gray-900 placeholder:text-gray-400 focus:outline-none focus:ring-2 focus:ring-white/50"
                  />
                </div>
                <button
                  type="submit"
                  disabled={subscribeMutation.isPending}
                  className="btn btn-lg bg-gray-900 text-white hover:bg-gray-800 disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {subscribeMutation.isPending ? (
                    <span className="flex items-center">
                      <Loader2 className="animate-spin -ml-1 mr-2 h-5 w-5" />
                      Subscribing...
                    </span>
                  ) : (
                    <>
                      Subscribe
                      <Send className="w-5 h-5 ml-2" />
                    </>
                  )}
                </button>
              </form>
            )}

            {/* Disclaimer */}
            {!isSubscribed && (
              <p className="text-sm text-white/60 mt-4 flex items-center justify-center gap-2">
                <Check className="w-4 h-4" />
                No spam, unsubscribe anytime
              </p>
            )}
          </div>
        </motion.div>
      </div>
    </section>
  );
}
