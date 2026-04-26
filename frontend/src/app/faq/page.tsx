'use client';

import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';
import { contactApi } from '@/lib/api';
import { motion, AnimatePresence } from 'framer-motion';
import Link from 'next/link';
import { HelpCircle, ChevronDown, Search, Loader2, MessageCircle } from 'lucide-react';
import { useLanguageStore } from '@/store/languageStore';
import { faqT, t } from '@/lib/translations';
import { RichText } from '@/components/ui/RichText';

interface FAQ {
  id: number;
  question: string;
  answer: string;
  category: string;
  order: number;
}

function FAQItem({ faq, isOpen, onToggle }: { faq: FAQ; isOpen: boolean; onToggle: () => void }) {
  return (
    <div className="border-b border-gray-200 last:border-b-0">
      <button
        onClick={onToggle}
        className="w-full py-6 flex items-center justify-between text-left hover:text-primary-600 transition-colors"
      >
        <span className="text-lg font-medium text-gray-900 pr-8">{faq.question}</span>
        <ChevronDown
          className={`w-5 h-5 text-gray-500 transition-transform flex-shrink-0 ${
            isOpen ? 'rotate-180' : ''
          }`}
        />
      </button>
      <AnimatePresence>
        {isOpen && (
          <motion.div
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.2 }}
            className="overflow-hidden"
          >
            <RichText html={faq.answer} className="pb-6 text-gray-600" />
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

export default function FAQPage() {
  const { language } = useLanguageStore();
  const [activeCategory, setActiveCategory] = useState('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [openFAQ, setOpenFAQ] = useState<number | null>(null);

  const categories = [
    { id: 'all', name: t(faqT, language, 'allQuestions') },
    { id: 'booking', name: t(faqT, language, 'booking') },
    { id: 'payment', name: t(faqT, language, 'payment') },
    { id: 'tours', name: t(faqT, language, 'tours') },
    { id: 'travel', name: t(faqT, language, 'travel') },
    { id: 'cancellation', name: t(faqT, language, 'cancellation') },
  ];

  const { data: faqsData, isLoading, error } = useQuery<{ count: number; results: FAQ[] }>({
    queryKey: ['faqs', activeCategory],
    queryFn: async () => {
      const response = await contactApi.getFaqs(activeCategory === 'all' ? undefined : activeCategory);
      return response.data;
    },
  });

  const faqs = faqsData?.results || [];

  // Filter FAQs based on search query
  const filteredFAQs = faqs.filter(
    (faq) =>
      faq.question.toLowerCase().includes(searchQuery.toLowerCase()) ||
      faq.answer.toLowerCase().includes(searchQuery.toLowerCase())
  ) || [];

  return (
    <main className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[40vh] sm:h-[50vh] md:h-[60vh] lg:h-[100vh] min-h-[250px] sm:min-h-[300px] md:min-h-[400px] lg:min-h-[600px] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-primary-900/90 to-primary-800/80 z-10" />
        <div
          className="absolute inset-0 bg-cover bg-center"
          style={{ backgroundImage: "url('/images/contact-hero.jpg')" }}
        />
        <div className="relative z-20 text-center text-white max-w-4xl mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-center"
          >
            <div className="w-12 h-12 sm:w-16 sm:h-16 mx-auto mb-3 sm:mb-6 mt-6 sm:mt-0 rounded-2xl bg-white/10 flex items-center justify-center">
              <HelpCircle className="w-6 h-6 sm:w-8 sm:h-8" />
            </div>
            <h1 className="text-3xl sm:text-4xl md:text-5xl lg:text-6xl font-display font-bold mb-4 sm:mb-6">
              {t(faqT, language, 'title')}
            </h1>
            <p className="text-lg md:text-xl text-white/90 max-w-2xl mx-auto">
              {t(faqT, language, 'description')}
            </p>
          </motion.div>
        </div>
      </section>

      {/* Search and Filter */}
      <section className="py-8 bg-gray-50 border-b">
        <div className="container-custom">
          {/* Search */}
          <div className="max-w-xl mx-auto mb-6">
            <div className="relative">
              <Search className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder={t(faqT, language, 'searchPlaceholder')}
                className="w-full pl-12 pr-4 py-3 rounded-xl border border-gray-200 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent"
              />
            </div>
          </div>

          {/* Category Tabs */}
          <div className="flex flex-wrap justify-center gap-2">
            {categories.map((category) => (
              <button
                key={category.id}
                onClick={() => setActiveCategory(category.id)}
                className={`px-4 py-2 rounded-full text-sm font-medium transition-colors ${
                  activeCategory === category.id
                    ? 'bg-primary-600 text-white'
                    : 'bg-white text-gray-600 hover:bg-gray-100'
                }`}
              >
                {category.name}
              </button>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ List */}
      <section className="section-padding">
        <div className="container-custom max-w-3xl">
          {isLoading ? (
            <div className="flex items-center justify-center py-16">
              <Loader2 className="w-8 h-8 animate-spin text-primary-600" />
              <span className="ml-3 text-gray-600">{t(faqT, language, 'loadingFaqs')}</span>
            </div>
          ) : error ? (
            <div className="text-center py-16">
              <p className="text-red-500">{t(faqT, language, 'failedToLoad')}</p>
            </div>
          ) : filteredFAQs.length === 0 ? (
            <div className="text-center py-16">
              <div className="w-24 h-24 mx-auto mb-6 rounded-full bg-gray-100 flex items-center justify-center">
                <HelpCircle className="w-12 h-12 text-gray-400" />
              </div>
              <h2 className="text-2xl font-bold text-gray-900 mb-4">{t(faqT, language, 'noResults')}</h2>
              <p className="text-gray-600 mb-8">
                {searchQuery
                  ? `${t(faqT, language, 'noMatch')} "${searchQuery}"${t(faqT, language, 'tryDifferent')}`
                  : t(faqT, language, 'noFaqsCategory')}
              </p>
              {searchQuery && (
                <button
                  onClick={() => setSearchQuery('')}
                  className="btn btn-primary"
                >
                  {t(faqT, language, 'clearSearch')}
                </button>
              )}
            </div>
          ) : (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="bg-white rounded-2xl shadow-card p-6 md:p-8"
            >
              {filteredFAQs.map((faq) => (
                <FAQItem
                  key={faq.id}
                  faq={faq}
                  isOpen={openFAQ === faq.id}
                  onToggle={() => setOpenFAQ(openFAQ === faq.id ? null : faq.id)}
                />
              ))}
            </motion.div>
          )}
        </div>
      </section>

      {/* Contact CTA */}
      <section className="section-padding bg-gray-50">
        <div className="container-custom">
          <div className="text-center max-w-2xl mx-auto">
            <div className="w-16 h-16 mx-auto mb-6 rounded-2xl bg-primary-100 flex items-center justify-center">
              <MessageCircle className="w-8 h-8 text-primary-600" />
            </div>
            <h2 className="text-3xl font-display font-bold text-gray-900 mb-4">
              {t(faqT, language, 'stillHaveQuestions')}
            </h2>
            <p className="text-gray-600 mb-8">
              {t(faqT, language, 'cantFindAnswer')}
            </p>
            <Link href="/contact" className="btn btn-primary btn-lg">
              {t(faqT, language, 'contactUs')}
            </Link>
          </div>
        </div>
      </section>
    </main>
  );
}
