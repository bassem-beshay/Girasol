import { HeroSection } from '@/components/home/HeroSection';
import { WhyChooseUs } from '@/components/home/WhyChooseUs';
import { PopularTours } from '@/components/home/PopularTours';
import dynamic from 'next/dynamic';

// Lazy load far-below-fold sections (code splitting only, SSR enabled)
const MultiDestinationTours = dynamic(() => import('@/components/home/MultiDestinationTours').then(m => ({ default: m.MultiDestinationTours })));
const EarlyBookingSlider = dynamic(() => import('@/components/home/EarlyBookingSlider').then(m => ({ default: m.EarlyBookingSlider })));
const Destinations = dynamic(() => import('@/components/home/Destinations').then(m => ({ default: m.Destinations })));
const TrustpilotReviews = dynamic(() => import('@/components/home/TrustpilotReviews').then(m => ({ default: m.TrustpilotReviews })));
const BlogPreview = dynamic(() => import('@/components/home/BlogPreview').then(m => ({ default: m.BlogPreview })));
const Newsletter = dynamic(() => import('@/components/home/Newsletter').then(m => ({ default: m.Newsletter })));

export default function HomePage() {
  return (
    <>
      <HeroSection />
      <WhyChooseUs />
      <PopularTours />
      <MultiDestinationTours />
      <EarlyBookingSlider />
      <Destinations />
      <TrustpilotReviews />
      <BlogPreview />
      <Newsletter />
    </>
  );
}
