'use client';

import { useEffect, useRef } from 'react';
import { motion } from 'framer-motion';
import { ExternalLink } from 'lucide-react';

// Trustpilot Configuration - UPDATE THESE VALUES
const TRUSTPILOT_CONFIG = {
  // Your Trustpilot Business Unit ID (find it in Trustpilot Business dashboard)
  businessUnitId: '5e9c7f3e0526f900019f0a1c', // Replace with your actual ID
  // Your company domain on Trustpilot
  domain: 'girasoltours.com',
  // Trustpilot profile URL
  profileUrl: 'https://www.trustpilot.com/review/girasoltours.com',
  // Widget locale (pt-BR, en-US, es-ES, etc.)
  locale: 'pt-BR',
};

// Declare Trustpilot on window
declare global {
  interface Window {
    Trustpilot?: {
      loadFromElement: (element: HTMLElement, rebuildFromScratch?: boolean) => void;
    };
  }
}

export function TrustpilotReviews() {
  const trustboxRef = useRef<HTMLDivElement>(null);

  // Load Trustpilot widget when component mounts
  useEffect(() => {
    if (window.Trustpilot && trustboxRef.current) {
      window.Trustpilot.loadFromElement(trustboxRef.current, true);
    }
  }, []);

  return (
    <section className="section-padding bg-gray-50">
      <div className="container-custom">
        {/* Section Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-8"
        >
          <span className="text-primary-600 font-medium mb-2 block">
            O que nossos clientes dizem
          </span>
          <h2 className="heading-2 text-gray-900">
            Avaliações dos Viajantes
          </h2>
        </motion.div>

        {/* Trustpilot TrustBox Widget - Carousel */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="bg-white rounded-xl p-6 shadow-sm border border-gray-100"
        >
          {/* TrustBox Header with Rating */}
          <div
            ref={trustboxRef}
            className="trustpilot-widget"
            data-locale={TRUSTPILOT_CONFIG.locale}
            data-template-id="53aa8912dec7e10d38f59f36"
            data-businessunit-id={TRUSTPILOT_CONFIG.businessUnitId}
            data-style-height="140px"
            data-style-width="100%"
            data-theme="light"
            data-stars="4,5"
            data-review-languages="pt,en,es"
          >
            <a
              href={TRUSTPILOT_CONFIG.profileUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="text-[#00b67a] hover:underline"
            >
              Trustpilot
            </a>
          </div>

          {/* Reviews Carousel TrustBox */}
          <div
            className="trustpilot-widget mt-6"
            data-locale={TRUSTPILOT_CONFIG.locale}
            data-template-id="54ad5defc6454f065c28af8b"
            data-businessunit-id={TRUSTPILOT_CONFIG.businessUnitId}
            data-style-height="240px"
            data-style-width="100%"
            data-theme="light"
            data-stars="4,5"
            data-review-languages="pt,en,es"
          >
            <a
              href={TRUSTPILOT_CONFIG.profileUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="text-[#00b67a] hover:underline"
            >
              Trustpilot
            </a>
          </div>

          {/* CTA Button */}
          <div className="text-center mt-6">
            <a
              href={TRUSTPILOT_CONFIG.profileUrl}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-2 bg-[#00b67a] hover:bg-[#00a06a] text-white px-6 py-3 rounded-lg font-medium transition-colors"
            >
              Avalie-nos em Trustpilot
              <ExternalLink className="w-4 h-4" />
            </a>
          </div>
        </motion.div>
      </div>
    </section>
  );
}
