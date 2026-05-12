'use client';

import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Toaster } from 'react-hot-toast';
import { useState, useEffect, useRef } from 'react';
import { useImagePreloader } from '@/components/ui/ImagePreloader';
import { useLanguageStore } from '@/store/languageStore';
import { api } from '@/lib/api';

export function Providers({ children }: { children: React.ReactNode }) {
  useImagePreloader();
  const { language } = useLanguageStore();
  const prevLang = useRef(language);
  const [queryClient] = useState(
    () =>
      new QueryClient({
        defaultOptions: {
          queries: {
            staleTime: 5 * 60 * 1000, // 5 minutes
            gcTime: 30 * 60 * 1000, // 30 minutes cache
            refetchOnWindowFocus: false,
            retry: 1,
          },
        },
      })
  );

  // Always keep axios Accept-Language header in sync with current language
  // This runs on EVERY render, ensuring the header is correct before any API call
  api.defaults.headers.common['Accept-Language'] = language;

  // Reset all queries when language changes so they refetch with new header
  useEffect(() => {
    if (prevLang.current !== language) {
      prevLang.current = language;
      queryClient.resetQueries();
    }
  }, [language, queryClient]);

  return (
    <QueryClientProvider client={queryClient}>
      {children}
      <Toaster
        position="top-right"
        toastOptions={{
          duration: 4000,
          style: {
            background: '#363636',
            color: '#fff',
          },
          success: {
            iconTheme: {
              primary: '#22c55e',
              secondary: '#fff',
            },
          },
          error: {
            iconTheme: {
              primary: '#ef4444',
              secondary: '#fff',
            },
          },
        }}
      />
    </QueryClientProvider>
  );
}
