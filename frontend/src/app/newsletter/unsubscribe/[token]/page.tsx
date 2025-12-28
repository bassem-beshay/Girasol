'use client';

import { useEffect, useState } from 'react';
import { useParams } from 'next/navigation';
import { motion } from 'framer-motion';
import { Check, X, Loader2, MailX } from 'lucide-react';
import Link from 'next/link';

type UnsubscribeStatus = 'loading' | 'unsubscribed' | 'already_unsubscribed' | 'error';

export default function NewsletterUnsubscribePage() {
  const params = useParams();
  const [status, setStatus] = useState<UnsubscribeStatus>('loading');
  const [email, setEmail] = useState<string>('');

  useEffect(() => {
    const unsubscribe = async () => {
      try {
        const response = await fetch(
          `${process.env.NEXT_PUBLIC_API_URL}/contact/newsletter/unsubscribe/${params.token}/`
        );

        const data = await response.json();

        if (response.ok) {
          setStatus(data.status === 'already_unsubscribed' ? 'already_unsubscribed' : 'unsubscribed');
          setEmail(data.email || '');
        } else {
          setStatus('error');
        }
      } catch (error) {
        setStatus('error');
      }
    };

    if (params.token) {
      unsubscribe();
    }
  }, [params.token]);

  const renderContent = () => {
    switch (status) {
      case 'loading':
        return (
          <div className="text-center">
            <div className="w-20 h-20 mx-auto mb-6 rounded-full bg-gray-100 flex items-center justify-center">
              <Loader2 className="w-10 h-10 text-gray-600 animate-spin" />
            </div>
            <h1 className="text-2xl font-bold text-gray-900 mb-2">
              Processing...
            </h1>
            <p className="text-gray-600">Please wait a moment.</p>
          </div>
        );

      case 'unsubscribed':
        return (
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="text-center"
          >
            <div className="w-20 h-20 mx-auto mb-6 rounded-full bg-gray-100 flex items-center justify-center">
              <MailX className="w-10 h-10 text-gray-600" />
            </div>
            <h1 className="text-2xl font-bold text-gray-900 mb-2">
              You&apos;ve Been Unsubscribed
            </h1>
            <p className="text-gray-600 mb-6">
              We&apos;re sorry to see you go{email ? ` (${email})` : ''}.
              <br />
              You won&apos;t receive any more emails from us.
            </p>
            <div className="space-y-3">
              <p className="text-sm text-gray-500">
                Changed your mind?
              </p>
              <Link
                href="/#newsletter"
                className="inline-flex items-center gap-2 bg-primary-600 text-white px-6 py-3 rounded-lg hover:bg-primary-700 transition-colors"
              >
                Subscribe Again
              </Link>
            </div>
          </motion.div>
        );

      case 'already_unsubscribed':
        return (
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="text-center"
          >
            <div className="w-20 h-20 mx-auto mb-6 rounded-full bg-gray-100 flex items-center justify-center">
              <Check className="w-10 h-10 text-gray-600" />
            </div>
            <h1 className="text-2xl font-bold text-gray-900 mb-2">
              Already Unsubscribed
            </h1>
            <p className="text-gray-600 mb-6">
              You were already unsubscribed from our newsletter.
            </p>
            <Link
              href="/"
              className="inline-flex items-center gap-2 bg-primary-600 text-white px-6 py-3 rounded-lg hover:bg-primary-700 transition-colors"
            >
              Go to Homepage
            </Link>
          </motion.div>
        );

      case 'error':
        return (
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="text-center"
          >
            <div className="w-20 h-20 mx-auto mb-6 rounded-full bg-red-100 flex items-center justify-center">
              <X className="w-10 h-10 text-red-600" />
            </div>
            <h1 className="text-2xl font-bold text-gray-900 mb-2">
              Invalid Link
            </h1>
            <p className="text-gray-600 mb-6">
              This unsubscribe link is invalid.
              <br />
              Please contact us if you need help.
            </p>
            <Link
              href="/contact"
              className="inline-flex items-center gap-2 bg-primary-600 text-white px-6 py-3 rounded-lg hover:bg-primary-700 transition-colors"
            >
              Contact Us
            </Link>
          </motion.div>
        );
    }
  };

  return (
    <main className="min-h-screen bg-gray-50 flex items-center justify-center px-4">
      <div className="max-w-md w-full bg-white rounded-2xl shadow-xl p-8">
        {renderContent()}
      </div>
    </main>
  );
}
