import dynamic from 'next/dynamic';
import { HeroSection } from '@/components/home/HeroSection';
import { WhyChooseUs } from '@/components/home/WhyChooseUs';
import { PopularTours } from '@/components/home/PopularTours';

// Lazy load below-fold components
const MultiDestinationTours = dynamic(() => import('@/components/home/MultiDestinationTours').then(mod => ({ default: mod.MultiDestinationTours })), { ssr: true });
const EarlyBookingSlider = dynamic(() => import('@/components/home/EarlyBookingSlider').then(mod => ({ default: mod.EarlyBookingSlider })), { ssr: true });
const Destinations = dynamic(() => import('@/components/home/Destinations').then(mod => ({ default: mod.Destinations })), { ssr: true });
const TrustpilotReviews = dynamic(() => import('@/components/home/TrustpilotReviews').then(mod => ({ default: mod.TrustpilotReviews })), { ssr: true });
const BlogPreview = dynamic(() => import('@/components/home/BlogPreview').then(mod => ({ default: mod.BlogPreview })), { ssr: true });
const Newsletter = dynamic(() => import('@/components/home/Newsletter').then(mod => ({ default: mod.Newsletter })), { ssr: true });

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
