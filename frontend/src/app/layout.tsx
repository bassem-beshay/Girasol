import type { Metadata } from 'next';
import { Inter, Playfair_Display, Cairo } from 'next/font/google';
import '@/styles/globals.css';
import { Providers } from './providers';
import { Header } from '@/components/layout/Header';
import { Footer } from '@/components/layout/Footer';

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
    default: 'Girasol Egypt - Travel and Tours | Discover Egypt with Excellence',
    template: '%s | Girasol Egypt Tours',
  },
  description:
    'Experience the magic of Egypt with Girasol Egypt Travel and Tours. Tailor-made tours, Nile cruises, and unforgettable experiences. Born from a partnership between Egypt and Brazil.',
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
  authors: [{ name: 'Girasol Egypt' }],
  creator: 'Girasol Egypt',
  publisher: 'Girasol Egypt Travel and Tours',
  formatDetection: {
    email: false,
    address: false,
    telephone: false,
  },
  metadataBase: new URL('https://girasolegypt.com'),
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
    title: 'Girasol Egypt - Travel and Tours',
    description: 'Tailor-made tours, Nile cruises & unforgettable experiences in Egypt',
    url: 'https://girasolegypt.com',
    siteName: 'Girasol Egypt',
    images: [
      {
        url: '/images/og-image.png',
        width: 1200,
        height: 630,
        alt: 'Girasol Egypt - Travel and Tours',
      },
    ],
    locale: 'en_US',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Girasol Egypt - Travel and Tours',
    description: 'Tailor-made tours, Nile cruises & unforgettable experiences in Egypt',
    images: ['/images/og-image.png'],
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
      <body className="font-sans antialiased">
        <Providers>
          <div className="flex min-h-screen flex-col">
            <Header />
            <main className="flex-1">{children}</main>
            <Footer />
          </div>
        </Providers>
      </body>
    </html>
  );
}
