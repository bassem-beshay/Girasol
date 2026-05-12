'use client';

import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { Toaster } from 'react-hot-toast';
import { useState, useEffect, useRef } from 'react';
import { useImagePreloader } from '@/components/ui/ImagePreloader';
import { useLanguageStore } from '@/store/languageStore';

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

  // Force all queries to refetch when language changes
  useEffect(() => {
    if (prevLang.current !== language) {
      prevLang.current = language;
      queryClient.invalidateQueries();
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
