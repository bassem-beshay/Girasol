'use client';

import { useState, useEffect, useCallback } from 'react';
import { X } from 'lucide-react';
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
  const [mounted, setMounted] = useState(false);
  const [ring, setRing] = useState(false);
  const tt = texts[language] || texts.en;

  useEffect(() => {
    const timer = setTimeout(() => setMounted(true), 800);
    return () => clearTimeout(timer);
  }, []);

  // Periodic ring animation every 8 seconds
  const triggerRing = useCallback(() => {
    setRing(true);
    setTimeout(() => setRing(false), 1200);
  }, []);

  useEffect(() => {
    const initialDelay = setTimeout(() => {
      triggerRing();
      const interval = setInterval(triggerRing, 8000);
      return () => clearInterval(interval);
    }, 3000);
    return () => clearTimeout(initialDelay);
  }, [triggerRing]);

  return (
    <>
      <style jsx>{`
        @keyframes wa-enter {
          0% { transform: scale(0) rotate(-180deg); opacity: 0; }
          60% { transform: scale(1.15) rotate(10deg); opacity: 1; }
          80% { transform: scale(0.95) rotate(-5deg); }
          100% { transform: scale(1) rotate(0deg); }
        }
        @keyframes wa-ring {
          0% { transform: rotate(0deg); }
          10% { transform: rotate(15deg); }
          20% { transform: rotate(-13deg); }
          30% { transform: rotate(10deg); }
          40% { transform: rotate(-8deg); }
          50% { transform: rotate(5deg); }
          60% { transform: rotate(-3deg); }
          70% { transform: rotate(0deg); }
          100% { transform: rotate(0deg); }
        }
        @keyframes wa-ripple {
          0% { transform: scale(1); opacity: 0.4; }
          100% { transform: scale(2.2); opacity: 0; }
        }
        @keyframes wa-tooltip-in {
          0% { transform: translateX(-12px) scale(0.9); opacity: 0; }
          100% { transform: translateX(0) scale(1); opacity: 1; }
        }
        .wa-btn-enter {
          animation: wa-enter 0.7s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
        }
        .wa-btn-ring {
          animation: wa-ring 1.2s ease-in-out;
        }
        .wa-ripple {
          animation: wa-ripple 1.8s cubic-bezier(0.25, 0.46, 0.45, 0.94) infinite;
        }
        .wa-tooltip-enter {
          animation: wa-tooltip-in 0.3s cubic-bezier(0.22, 1, 0.36, 1) forwards;
        }
      `}</style>

      <div className="fixed bottom-6 left-6 z-50 flex items-end gap-3">
        {/* Ripple ring */}
        {mounted && (
          <div className="absolute bottom-0 left-0 w-12 h-12 rounded-full bg-[#25D366]/30 wa-ripple pointer-events-none" />
        )}

        {/* Button */}
        <a
          href="https://wa.me/201060873700"
          target="_blank"
          rel="noopener noreferrer"
          onMouseEnter={() => setShowTooltip(true)}
          onMouseLeave={() => setShowTooltip(false)}
          onClick={() => setShowTooltip(false)}
          className={`
            w-12 h-12 bg-[#25D366] text-white rounded-full
            flex items-center justify-center
            shadow-[0_4px_14px_rgba(37,211,102,0.4)]
            hover:shadow-[0_6px_20px_rgba(37,211,102,0.6)]
            hover:bg-[#22c55e] active:scale-95
            transition-shadow duration-300
            ${mounted ? 'wa-btn-enter' : 'opacity-0 scale-0'}
            ${ring && !showTooltip ? 'wa-btn-ring' : ''}
          `}
          aria-label="WhatsApp"
        >
          <svg viewBox="0 0 24 24" className="w-6 h-6 fill-current">
            <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
          </svg>
        </a>

        {/* Tooltip */}
        {showTooltip && (
          <div className="bg-white rounded-xl shadow-2xl p-4 max-w-[260px] border border-gray-100 relative wa-tooltip-enter">
            <button
              onClick={() => setShowTooltip(false)}
              className="absolute top-2 right-2 text-gray-400 hover:text-gray-600"
              aria-label={tt.close}
            >
              <X className="w-4 h-4" />
            </button>
            <p className="text-sm text-gray-800 font-medium pr-4">{tt.cta}</p>
          </div>
        )}
      </div>
    </>
  );
}
