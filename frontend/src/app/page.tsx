import { HeroSection } from '@/components/home/HeroSection';
import { WhyChooseUs } from '@/components/home/WhyChooseUs';
import { PopularTours } from '@/components/home/PopularTours';
import { MultiDestinationTours } from '@/components/home/MultiDestinationTours';
import { EarlyBookingSlider } from '@/components/home/EarlyBookingSlider';
import { Destinations } from '@/components/home/Destinations';
import { Testimonials } from '@/components/home/Testimonials';
import { BlogPreview } from '@/components/home/BlogPreview';
import { Newsletter } from '@/components/home/Newsletter';

export default function HomePage() {
  return (
    <>
      <HeroSection />
      <WhyChooseUs />
      <PopularTours />
      <MultiDestinationTours />
      <EarlyBookingSlider />
      <Destinations />
      <Testimonials />
      <BlogPreview />
      <Newsletter />
    </>
  );
}
