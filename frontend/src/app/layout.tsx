import type { Metadata } from 'next';
import { Inter, Playfair_Display, Cairo } from 'next/font/google';
import '@/styles/globals.css';
import { Providers } from './providers';
import { Header } from '@/components/layout/Header';
import { Footer } from '@/components/layout/Footer';
import WhatsAppButton from '@/components/ui/WhatsAppButton';
import RecaptchaScript from "@/components/RecaptchaScript";

const inter = Inter({
  subsets: ['latin'],
  variable: '--font-inter',
  display: 'swap',
});

const playfair = Playfair_Display({
  subsets: ['latin'],
  variable: '--font-playfair',
  display: 'swap',
});

const cairo = Cairo({
  subsets: ['arabic'],
  variable: '--font-cairo',
  display: 'swap',
});

export const metadata: Metadata = {
  title: {
    default: 'Girasol Egypt Travel and Tours | Complete Egypt Packages: Pyramids + Nile Cruise',
    template: '%s | Girasol Egypt Travel and Tours',
  },
  description:
    'Complete Egypt packages: pyramids + Nile cruise. Travel with safety and comfort. Your journey starts now! Tailor-made tours and unforgettable experiences with Girasol Egypt Travel and Tours.',
  keywords: [
    'Egypt tours',
    'Nile cruise',
    'Cairo tours',
    'Luxor tours',
    'Pyramids tour',
    'Egypt travel',
    'Egypt vacation',
    'DMC Egypt',
    'Girasol Egypt',
    'Egypt Brazil tourism',
  ],
  authors: [{ name: 'Girasol Egypt Travel and Tours' }],
  creator: 'Girasol Egypt Travel and Tours',
  publisher: 'Girasol Egypt Travel and Tours',
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  metadataBase: new URL('https://girasoltours.com'),
  icons: {
    icon: [
      { url: '/favicon.png', type: 'image/png' },
    ],
    apple: [
      { url: '/favicon.png', sizes: '180x180', type: 'image/png' },
    ],
    shortcut: '/favicon.png',
  },
  openGraph: {
    title: 'Girasol Egypt Travel and Tours',
    description: 'Complete Egypt packages: pyramids + Nile cruise. Travel with safety and comfort. Your journey starts now!',
    url: 'https://girasoltours.com',
    siteName: 'Girasol Egypt Travel and Tours',
    images: [
      {
        url: '/images/og-image.jpg',
        width: 1200,
        height: 630,
        alt: 'Girasol Egypt Travel and Tours - Pyramids, Nile Cruise & Abu Simbel',
      },
    ],
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Girasol Egypt Travel and Tours',
    description: 'Complete Egypt packages: pyramids + Nile cruise. Travel with safety and comfort. Your journey starts now!',
    images: ['/images/og-image.jpg'],
  },
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  verification: {
    google: 'your-google-verification-code',
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className={`${inter.variable} ${playfair.variable} ${cairo.variable}`}>
      <head>
        {/* Establish connections early for deferred third parties so the first
            request to them doesn't pay TLS + DNS cost. */}
        <link rel="preconnect" href="https://www.google.com" crossOrigin="anonymous" />
        <link rel="dns-prefetch" href="https://user-images.trustpilot.com" />
      </head>
      <body className="font-sans antialiased">
        {/* Google reCAPTCHA v3 - loaded after page interaction */}
        <RecaptchaScript />
        <Providers>
          <div className="flex min-h-screen flex-col">
            <Header />
            <main className="flex-1">{children}</main>
            <Footer />
            <WhatsAppButton />
          </div>
        </Providers>
      </body>
    </html>
  );
}
