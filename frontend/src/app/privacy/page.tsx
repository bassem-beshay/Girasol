'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import { FileText, ArrowLeft } from 'lucide-react';
import { useLanguageStore } from '@/store/languageStore';
import { privacyT, t } from '@/lib/translations';

const rows = [1, 2, 3, 4, 5, 6, 7, 8] as const;

export default function CancellationPolicyPage() {
  const { language } = useLanguageStore();

  return (
    <main className="min-h-screen">
      {/* Hero Section */}
      <section className="relative py-24 bg-gradient-to-r from-primary-600 to-primary-700">
        <div className="absolute inset-0 bg-hero-pattern opacity-10" />
        <div className="container-custom relative z-10">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-center text-white"
          >
            <div className="w-16 h-16 mx-auto mb-6 rounded-2xl bg-white/10 flex items-center justify-center">
              <FileText className="w-8 h-8" />
            </div>
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-display font-bold mb-6">
              {t(privacyT, language, 'title')}
            </h1>
            <p className="text-xl text-white/80 max-w-2xl mx-auto">
              {t(privacyT, language, 'description')}
            </p>
          </motion.div>
        </div>
      </section>

      {/* Content */}
      <section className="section-padding">
        <div className="container-custom max-w-4xl">
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-primary-600 hover:text-primary-700 mb-8"
          >
            <ArrowLeft className="w-4 h-4" />
            {t(privacyT, language, 'backToHome')}
          </Link>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
          >
            <p className="text-gray-500 mb-8">{t(privacyT, language, 'lastUpdated')}</p>

            {/* Intro */}
            <p className="text-gray-700 text-lg leading-relaxed mb-8">
              {t(privacyT, language, 'intro')}
            </p>

            {/* Cancellation Table */}
            <div className="overflow-x-auto mb-12">
              <table className="w-full border-collapse rounded-xl overflow-hidden shadow-md">
                <thead>
                  <tr className="bg-primary-600 text-white">
                    <th className="px-6 py-4 text-left font-semibold text-sm">
                      {t(privacyT, language, 'tableHeaderDays')}
                    </th>
                    <th className="px-6 py-4 text-left font-semibold text-sm">
                      {t(privacyT, language, 'tableHeaderFee')}
                    </th>
                  </tr>
                </thead>
                <tbody>
                  {rows.map((num, index) => (
                    <tr
                      key={num}
                      className={`${index % 2 === 0 ? 'bg-white' : 'bg-gray-50'} ${num === 8 ? 'bg-red-50' : ''} border-b border-gray-100`}
                    >
                      <td className={`px-6 py-4 text-sm ${num === 8 ? 'text-red-700 font-semibold' : 'text-gray-700'}`}>
                        {t(privacyT, language, `row${num}Days`)}
                      </td>
                      <td className={`px-6 py-4 text-sm font-medium ${num === 8 ? 'text-red-600 font-bold' : 'text-gray-900'}`}>
                        {t(privacyT, language, `row${num}Fee`)}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {/* Refund Rules */}
            <div className="bg-white rounded-xl border border-gray-100 shadow-sm overflow-hidden mb-8">
              <div className="bg-gray-50 px-6 py-4 border-b border-gray-100">
                <h2 className="text-xl font-bold text-gray-900">
                  {t(privacyT, language, 'refundTitle')}
                </h2>
              </div>
              <div className="px-6 py-5 space-y-4">
                <p className="text-gray-600 text-justify leading-relaxed">
                  {t(privacyT, language, 'refundP1')}
                </p>
                <p className="text-gray-600 text-justify leading-relaxed">
                  {t(privacyT, language, 'refundP2')}
                </p>
              </div>
            </div>

            {/* Processing Time */}
            <div className="bg-white rounded-xl border border-gray-100 shadow-sm overflow-hidden mb-8">
              <div className="bg-gray-50 px-6 py-4 border-b border-gray-100">
                <h2 className="text-xl font-bold text-gray-900">
                  {t(privacyT, language, 'processingTitle')}
                </h2>
              </div>
              <div className="px-6 py-5 space-y-4">
                <p className="text-gray-600 text-justify leading-relaxed">
                  {t(privacyT, language, 'processingP1')}
                </p>
                <p className="text-gray-600 text-justify leading-relaxed">
                  {t(privacyT, language, 'processingP2')}
                </p>
                <p className="text-gray-600 text-justify leading-relaxed">
                  {t(privacyT, language, 'processingP3')}
                </p>
              </div>
            </div>
          </motion.div>
        </div>
      </section>
    </main>
  );
}
