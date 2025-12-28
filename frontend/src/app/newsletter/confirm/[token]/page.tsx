'use client';

import { useEffect, useState } from 'react';
import { useParams, useRouter } from 'next/navigation';
import { motion } from 'framer-motion';
import { Check, X, Loader2, Mail } from 'lucide-react';
import Link from 'next/link';

type ConfirmStatus = 'loading' | 'confirmed' | 'already_confirmed' | 'error';

export default function NewsletterConfirmPage() {
  const params = useParams();
  const router = useRouter();
  const [status, setStatus] = useState<ConfirmStatus>('loading');
  const [email, setEmail] = useState<string>('');

  useEffect(() => {
    const confirmSubscription = async () => {
      try {
        const response = await fetch(
          `${process.env.NEXT_PUBLIC_API_URL}/contact/newsletter/confirm/${params.token}/`
        );

        const data = await response.json();

        if (response.ok) {
          setStatus(data.status === 'already_confirmed' ? 'already_confirmed' : 'confirmed');
          setEmail(data.email || '');
        } else {
          setStatus('error');
        }
      } catch (error) {
        setStatus('error');
      }
    };

    if (params.token) {
      confirmSubscription();
    }
  }, [params.token]);

  const renderContent = () => {
    switch (status) {
      case 'loading':
        return (
          <div className="text-center">
            <div className="w-20 h-20 mx-auto mb-6 rounded-full bg-primary-100 flex items-center justify-center">
              <Loader2 className="w-10 h-10 text-primary-600 animate-spin" />
            </div>
            <h1 className="text-2xl font-bold text-gray-900 mb-2">
              Confirming Your Subscription...
            </h1>
            <p className="text-gray-600">Please wait a moment.</p>
          </div>
        );

      case 'confirmed':
        return (
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="text-center"
          >
            <div className="w-20 h-20 mx-auto mb-6 rounded-full bg-green-100 flex items-center justify-center">
              <Check className="w-10 h-10 text-green-600" />
            </div>
            <h1 className="text-2xl font-bold text-gray-900 mb-2">
              Subscription Confirmed!
            </h1>
            <p className="text-gray-600 mb-6">
              Thank you for confirming your email{email ? ` (${email})` : ''}.
              <br />
              You&apos;ll now receive our exclusive deals and travel tips!
            </p>
            <Link
              href="/tours"
              className="inline-flex items-center gap-2 bg-primary-600 text-white px-6 py-3 rounded-lg hover:bg-primary-700 transition-colors"
            >
              Explore Our Tours
            </Link>
          </motion.div>
        );

      case 'already_confirmed':
        return (
          <motion.div
            initial={{ scale: 0.9, opacity: 0 }}
            animate={{ scale: 1, opacity: 1 }}
            className="text-center"
          >
            <div className="w-20 h-20 mx-auto mb-6 rounded-full bg-blue-100 flex items-center justify-center">
              <Mail className="w-10 h-10 text-blue-600" />
            </div>
            <h1 className="text-2xl font-bold text-gray-900 mb-2">
              Already Confirmed!
            </h1>
            <p className="text-gray-600 mb-6">
              Your subscription was already confirmed.
              <br />
              You&apos;re all set to receive our updates!
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
              Invalid or Expired Link
            </h1>
            <p className="text-gray-600 mb-6">
              This confirmation link is invalid or has expired.
              <br />
              Please try subscribing again.
            </p>
            <Link
              href="/#newsletter"
              className="inline-flex items-center gap-2 bg-primary-600 text-white px-6 py-3 rounded-lg hover:bg-primary-700 transition-colors"
            >
              Subscribe Again
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
