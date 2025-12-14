import { HeroSection } from '@/components/home/HeroSection';
import { WhyChooseUs } from '@/components/home/WhyChooseUs';
import { PopularTours } from '@/components/home/PopularTours';
import { Destinations } from '@/components/home/Destinations';
import { Testimonials } from '@/components/home/Testimonials';
import { SpecialOffers } from '@/components/home/SpecialOffers';
import { BlogPreview } from '@/components/home/BlogPreview';
import { Newsletter } from '@/components/home/Newsletter';

export default function HomePage() {
  return (
    <>
      <HeroSection />
      <WhyChooseUs />
      <PopularTours />
      <Destinations />
      <Testimonials />
      <SpecialOffers />
      <BlogPreview />
      <Newsletter />
    </>
  );
}
