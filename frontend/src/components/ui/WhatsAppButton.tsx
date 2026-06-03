'use client';

import { useState } from 'react';
import { MessageCircle, X } from 'lucide-react';
import { useLanguageStore } from '@/store/languageStore';

const texts: Record<string, { cta: string; close: string }> = {
  en: {
    cta: 'Chat with a Travel Specialist on WhatsApp Now!',
    close: 'Close',
  },
  es: {
    cta: '¡Habla con un Especialista en Viajes en WhatsApp ahora!',
    close: 'Cerrar',
  },
  pt: {
    cta: 'Fale com um Especialista em Viagens no WhatsApp Agora!',
    close: 'Fechar',
  },
};

export default function WhatsAppButton() {
  const { language } = useLanguageStore();
  const [showTooltip, setShowTooltip] = useState(false);
  const t = texts[language] || texts.en;

  return (
    <div className="fixed bottom-6 left-6 z-50 flex items-end gap-3">
      <a
        href="https://wa.me/201060873700"
        target="_blank"
        rel="noopener noreferrer"
        onMouseEnter={() => setShowTooltip(true)}
        onClick={() => setShowTooltip(false)}
        className="w-14 h-14 bg-[#25D366] hover:bg-[#20bd5a] text-white rounded-full flex items-center justify-center shadow-lg hover:shadow-xl transition-all hover:scale-110"
        aria-label="WhatsApp"
      >
        <MessageCircle className="w-7 h-7" />
      </a>
      {showTooltip && (
        <div className="bg-white rounded-xl shadow-2xl p-4 max-w-[260px] border border-gray-100 animate-fade-in relative">
          <button
            onClick={() => setShowTooltip(false)}
            className="absolute top-2 right-2 text-gray-400 hover:text-gray-600"
            aria-label={t.close}
          >
            <X className="w-4 h-4" />
          </button>
          <p className="text-sm text-gray-800 font-medium pr-4">{t.cta}</p>
        </div>
      )}
    </div>
  );
}
