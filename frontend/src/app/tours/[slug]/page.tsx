'use client';

import { useQuery } from '@tanstack/react-query';
import { toursApi } from '@/lib/api';
import { useParams } from 'next/navigation';
import Link from 'next/link';
import Image from 'next/image';
import { motion } from 'framer-motion';
import { useState, useEffect, useRef } from 'react';
import {
  MapPin,
  Clock,
  Star,
  Users,
  Calendar,
  Check,
  X,
  Phone,
  Mail,
  Heart,
  Share2,
  Sparkles,
  Timer,
  ChevronDown,
  HelpCircle,
  DollarSign,
  User,
  CalendarDays,
  Plane,
  CheckCircle,
  AlertCircle,
  Camera,
  ChevronLeft,
  ChevronRight,
  MessageSquare,
} from 'lucide-react';
import { InquiryForm } from '@/components/tours/InquiryForm';

interface TourDetail {
  id: number;
  name: string;
  name_ar: string;
  slug: string;
  short_description: string;
  description: string;
  featured_image: string | null;
  gallery_images: string[];
  category: {
    id: number;
    name: string;
    slug: string;
  } | null;
  tour_type: string;
  days: number;
  nights: number;
  duration_display: string;
  price: string;
  price_single_supplement: string | null;
  child_price: string | null;
  discounted_price: string;
  currency: string;
  has_discount: boolean;
  discount_percentage: number | null;
  is_featured: boolean;
  is_best_seller: boolean;
  is_new: boolean;
  average_rating: string;
  review_count: number;
  difficulty_level: string;
  departure_city: string;
  languages: string;
  min_group_size: number;
  max_group_size: number;
  destination_names: string[];
  destinations: Array<{
    id: number;
    name: string;
    slug: string;
  }>;
  highlights: Array<{
    id: number;
    title: string;
    description: string;
    icon: string;
  }>;
  inclusions: Array<{
    id: number;
    item: string;
    is_included: boolean;
  }>;
  itinerary: Array<{
    id: number;
    day_number: number;
    title: string;
    description: string;
    locations: string;
    meals_included: string;
    accommodation: string;
  }>;
  faqs: Array<{
    id: number;
    question: string;
    answer: string;
  }>;
  seasonal_pricing: Array<{
    id: number;
    season_name: string;
    start_date: string;
    end_date: string;
    price_per_person: string;
    single_supplement: string;
  }>;
  departures: Array<{
    id: number;
    departure_date: string;
    return_date: string;
    price: string;
    available_spots: number;
    is_guaranteed: boolean;
    status: string;
  }>;
  images: Array<{
    id: number;
    image: string;
    caption: string;
    alt_text: string;
  }>;
  // Early Booking fields
  is_early_booking: boolean;
  early_booking_discount: number | null;
  early_booking_price: number | null;
  early_booking_badge: string | null;
  early_booking_end_date: string | null;
}

// FAQ Accordion Item Component
function FAQItem({ question, answer, isOpen, onClick }: {
  question: string;
  answer: string;
  isOpen: boolean;
  onClick: () => void;
}) {
  return (
    <div className="border border-gray-200 rounded-xl overflow-hidden">
      <button
        onClick={onClick}
        className="w-full flex items-center justify-between p-5 text-left bg-white hover:bg-gray-50 transition-colors"
      >
        <span className="font-medium text-gray-900 pr-4">{question}</span>
        <ChevronDown
          className={`w-5 h-5 text-gray-500 flex-shrink-0 transition-transform duration-200 ${
            isOpen ? 'rotate-180' : ''
          }`}
        />
      </button>
      <motion.div
        initial={false}
        animate={{
          height: isOpen ? 'auto' : 0,
          opacity: isOpen ? 1 : 0,
        }}
        transition={{ duration: 0.2 }}
        className="overflow-hidden"
      >
        <div className="p-5 pt-0 text-gray-600 leading-relaxed">
          {answer}
        </div>
      </motion.div>
    </div>
  );
}

// Countdown Timer Component
function CountdownTimer({ endDate }: { endDate: string }) {
  const [timeLeft, setTimeLeft] = useState({
    days: 0,
    hours: 0,
    minutes: 0,
    seconds: 0,
  });

  useEffect(() => {
    const calculateTimeLeft = () => {
      const now = new Date().getTime();
      const end = new Date(endDate).getTime();
      const distance = end - now;

      if (distance < 0) {
        return { days: 0, hours: 0, minutes: 0, seconds: 0 };
      }

      return {
        days: Math.floor(distance / (1000 * 60 * 60 * 24)),
        hours: Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60)),
        minutes: Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60)),
        seconds: Math.floor((distance % (1000 * 60)) / 1000),
      };
    };

    setTimeLeft(calculateTimeLeft());
    const timer = setInterval(() => setTimeLeft(calculateTimeLeft()), 1000);
    return () => clearInterval(timer);
  }, [endDate]);

  return (
    <div className="flex items-center gap-1 sm:gap-2 text-xs sm:text-sm">
      <div className="bg-gray-900 text-white px-1.5 sm:px-2 py-1 rounded font-mono">
        {String(timeLeft.days).padStart(2, '0')}d
      </div>
      <span className="text-orange-500 font-bold">:</span>
      <div className="bg-gray-900 text-white px-1.5 sm:px-2 py-1 rounded font-mono">
        {String(timeLeft.hours).padStart(2, '0')}h
      </div>
      <span className="text-orange-500 font-bold">:</span>
      <div className="bg-gray-900 text-white px-1.5 sm:px-2 py-1 rounded font-mono">
        {String(timeLeft.minutes).padStart(2, '0')}m
      </div>
      <span className="text-orange-500 font-bold">:</span>
      <div className="bg-gray-900 text-white px-1.5 sm:px-2 py-1 rounded font-mono">
        {String(timeLeft.seconds).padStart(2, '0')}s
      </div>
    </div>
  );
}

export default function TourDetailPage() {
  const params = useParams();
  const slug = params.slug as string;
  const [openFAQ, setOpenFAQ] = useState<number | null>(null);
  const [galleryOpen, setGalleryOpen] = useState(false);
  const [currentImageIndex, setCurrentImageIndex] = useState(0);
  const [activeSection, setActiveSection] = useState('overview');
  const [openSections, setOpenSections] = useState<Set<string>>(new Set(['overview']));

  const toggleSection = (id: string) => {
    setOpenSections(prev => {
      const next = new Set(prev);
      if (next.has(id)) next.delete(id);
      else next.add(id);
      return next;
    });
  };

  // Section refs for scrolling
  const sectionRefs = {
    overview: useRef<HTMLDivElement>(null),
    gallery: useRef<HTMLDivElement>(null),
    highlights: useRef<HTMLDivElement>(null),
    itinerary: useRef<HTMLDivElement>(null),
    inclusions: useRef<HTMLDivElement>(null),
    pricing: useRef<HTMLDivElement>(null),
    departures: useRef<HTMLDivElement>(null),
    faqs: useRef<HTMLDivElement>(null),
  };

  const scrollToSection = (sectionId: string) => {
    // Open the section if it's closed
    setOpenSections(prev => {
      const next = new Set(prev);
      next.add(sectionId);
      return next;
    });
    // Delay scroll slightly to allow section to open
    setTimeout(() => {
      const ref = sectionRefs[sectionId as keyof typeof sectionRefs];
      if (ref?.current) {
        const yOffset = -120;
        const y = ref.current.getBoundingClientRect().top + window.pageYOffset + yOffset;
        window.scrollTo({ top: y, behavior: 'smooth' });
        setActiveSection(sectionId);
      }
    }, 50);
  };

  // Track active section on scroll
  useEffect(() => {
    const handleScroll = () => {
      const scrollPosition = window.scrollY + 150;

      for (const [key, ref] of Object.entries(sectionRefs)) {
        if (ref.current) {
          const { offsetTop, offsetHeight } = ref.current;
          if (scrollPosition >= offsetTop && scrollPosition < offsetTop + offsetHeight) {
            setActiveSection(key);
            break;
          }
        }
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const { data: tour, isLoading, error } = useQuery<TourDetail>({
    queryKey: ['tour', slug],
    queryFn: async () => {
      const response = await toursApi.getBySlug(slug);
      return response.data;
    },
    enabled: !!slug,
  });

  if (isLoading) {
    return (
      <div className="min-h-screen pt-32 pb-16">
        <div className="container-custom">
          <div className="text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-primary-500 mx-auto"></div>
            <p className="mt-4 text-gray-600">Loading tour details...</p>
          </div>
        </div>
      </div>
    );
  }

  if (error || !tour) {
    return (
      <div className="min-h-screen pt-32 pb-16">
        <div className="container-custom">
          <div className="text-center">
            <h1 className="text-2xl font-bold text-gray-900 mb-4">Tour Not Found</h1>
            <p className="text-gray-600 mb-8">The tour you&apos;re looking for doesn&apos;t exist.</p>
            <Link href="/tours" className="btn btn-primary btn-md">
              Browse All Tours
            </Link>
          </div>
        </div>
      </div>
    );
  }

  const included = tour.inclusions?.filter(i => i.is_included) || [];
  const notIncluded = tour.inclusions?.filter(i => !i.is_included) || [];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[60vh] sm:h-[65vh] md:h-[70vh] lg:h-[85vh] min-h-[350px] sm:min-h-[400px] md:min-h-[450px] lg:min-h-[700px]">
        <div className="absolute inset-0 bg-black/40 z-10" />
        {tour.featured_image ? (
          <Image
            src={tour.featured_image}
            alt={tour.name}
            fill
            className="object-cover"
            priority
          />
        ) : (
          <div className="w-full h-full bg-gradient-to-br from-primary-500 to-primary-700" />
        )}

        <div className="absolute inset-0 z-20 flex items-center">
          <div className="container-custom">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.6 }}
            >
              {/* Badges */}
              <div className="flex flex-wrap gap-2 mb-4">
                {tour.is_early_booking && (
                  <span className="px-3 py-1 bg-gradient-to-r from-orange-500 to-amber-500 text-white text-sm font-medium rounded-full flex items-center gap-1">
                    <Sparkles className="w-4 h-4" />
                    {tour.early_booking_badge || 'Early Bird'}
                  </span>
                )}
                {tour.is_best_seller && (
                  <span className="px-3 py-1 bg-primary-500 text-white text-sm font-medium rounded-full">
                    Best Seller
                  </span>
                )}
                {tour.is_new && (
                  <span className="px-3 py-1 bg-green-500 text-white text-sm font-medium rounded-full">
                    New
                  </span>
                )}
                {tour.has_discount && tour.discount_percentage && (
                  <span className="px-3 py-1 bg-red-500 text-white text-sm font-medium rounded-full">
                    {tour.discount_percentage}% OFF
                  </span>
                )}
                {tour.category && (
                  <span className="px-3 py-1 bg-white/20 backdrop-blur text-white text-sm font-medium rounded-full">
                    {tour.category.name}
                  </span>
                )}
              </div>

              <h1 className="text-2xl sm:text-3xl md:text-5xl font-display font-bold text-white mb-4 break-words">
                {tour.name}
              </h1>

              <div className="flex flex-wrap items-center gap-6 text-white/90">
                <div className="flex items-center gap-2">
                  <MapPin className="w-5 h-5" />
                  <span>{tour.destination_names?.join(', ') || 'Egypt'}</span>
                </div>
                <div className="flex items-center gap-2">
                  <Clock className="w-5 h-5" />
                  <span>{tour.duration_display || `${tour.days || 0} Days`}</span>
                </div>
                <div className="flex items-center gap-2">
                  <Star className="w-5 h-5 text-yellow-400 fill-current" />
                  <span>{tour.average_rating || 0} ({tour.review_count || 0} reviews)</span>
                </div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* Section Navigation */}
      <div className="sticky top-[72px] z-40 bg-white border-b shadow-sm">
        <div className="container-custom">
          <div className="flex items-center gap-1 overflow-x-auto py-3 scrollbar-hide">
            {[
              { id: 'overview', label: 'Overview' },
              { id: 'gallery', label: 'Photos', show: tour.images && tour.images.length > 0 },
              { id: 'highlights', label: 'Highlights', show: tour.highlights && tour.highlights.length > 0 },
              { id: 'itinerary', label: 'Itinerary', show: tour.itinerary && tour.itinerary.length > 0 },
              { id: 'inclusions', label: 'Inclusions', show: tour.inclusions && tour.inclusions.length > 0 },
              { id: 'pricing', label: 'Pricing', show: tour.seasonal_pricing && tour.seasonal_pricing.length > 0 },
              { id: 'departures', label: 'Departures', show: tour.departures && tour.departures.length > 0 },
              { id: 'faqs', label: 'FAQs', show: tour.faqs && tour.faqs.length > 0 },
            ]
              .filter(item => item.show !== false)
              .map((item) => (
                <button
                  key={item.id}
                  onClick={() => scrollToSection(item.id)}
                  className={`px-4 py-2 rounded-full text-sm font-medium whitespace-nowrap transition-all ${
                    activeSection === item.id
                      ? 'bg-primary-500 text-white shadow-md'
                      : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                  }`}
                >
                  {item.label}
                </button>
              ))}
          </div>
        </div>
      </div>

      {/* Main Content */}
      <section className="py-12">
        <div className="container-custom">
          <div className="grid lg:grid-cols-3 gap-8">
            {/* Left Column - Tour Details */}
            <div className="lg:col-span-2 space-y-8">
              {/* Overview */}
              <div ref={sectionRefs.overview} className="bg-white rounded-2xl shadow-md overflow-hidden">
                <button
                  onClick={() => toggleSection('overview')}
                  className="w-full flex items-center justify-between p-6 text-left hover:bg-gray-50 transition-colors"
                >
                  <h2 className="text-2xl font-bold text-gray-900">Overview</h2>
                  <ChevronDown className={`w-6 h-6 text-gray-400 transition-transform duration-300 ${openSections.has('overview') ? 'rotate-180' : ''}`} />
                </button>
                <motion.div
                  initial={false}
                  animate={{ height: openSections.has('overview') ? 'auto' : 0, opacity: openSections.has('overview') ? 1 : 0 }}
                  transition={{ duration: 0.3 }}
                  className="overflow-hidden"
                >
                  <div className="px-6 pb-6">
                    <p className="text-gray-600 leading-relaxed">{tour.description}</p>

                    {/* Quick Info */}
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mt-6 pt-6 border-t">
                      <div className="text-center">
                        <Clock className="w-8 h-8 text-primary-500 mx-auto mb-2" />
                        <div className="text-sm text-gray-500">Duration</div>
                        <div className="font-semibold">{tour.duration_display}</div>
                      </div>
                      <div className="text-center">
                        <Users className="w-8 h-8 text-primary-500 mx-auto mb-2" />
                        <div className="text-sm text-gray-500">Group Size</div>
                        <div className="font-semibold">{tour.min_group_size}-{tour.max_group_size}</div>
                      </div>
                      <div className="text-center">
                        <MapPin className="w-8 h-8 text-primary-500 mx-auto mb-2" />
                        <div className="text-sm text-gray-500">Start</div>
                        <div className="font-semibold">{tour.departure_city}</div>
                      </div>
                      <div className="text-center">
                        <Calendar className="w-8 h-8 text-primary-500 mx-auto mb-2" />
                        <div className="text-sm text-gray-500">Difficulty</div>
                        <div className="font-semibold capitalize">{tour.difficulty_level}</div>
                      </div>
                    </div>
                  </div>
                </motion.div>
              </div>

              {/* Photo Gallery */}
              {tour.images && tour.images.length > 0 && (
                <div ref={sectionRefs.gallery} className="bg-white rounded-2xl shadow-md overflow-hidden">
                  <button
                    onClick={() => toggleSection('gallery')}
                    className="w-full flex items-center justify-between p-6 text-left hover:bg-gray-50 transition-colors"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center">
                        <Camera className="w-6 h-6 text-purple-600" />
                      </div>
                      <div>
                        <h2 className="text-2xl font-bold text-gray-900">Photo Gallery</h2>
                        <p className="text-sm text-gray-500">{tour.images.length} photos</p>
                      </div>
                    </div>
                    <ChevronDown className={`w-6 h-6 text-gray-400 transition-transform duration-300 ${openSections.has('gallery') ? 'rotate-180' : ''}`} />
                  </button>
                  <motion.div
                    initial={false}
                    animate={{ height: openSections.has('gallery') ? 'auto' : 0, opacity: openSections.has('gallery') ? 1 : 0 }}
                    transition={{ duration: 0.3 }}
                    className="overflow-hidden"
                  >
                    <div className="px-6 pb-6">
                      <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                        {tour.images.map((image, index) => (
                          <div
                            key={image.id}
                            className="relative aspect-[4/3] rounded-xl overflow-hidden cursor-pointer group"
                            onClick={() => {
                              setCurrentImageIndex(index);
                              setGalleryOpen(true);
                            }}
                          >
                            <Image
                              src={image.image}
                              alt={image.alt_text || image.caption || `Tour photo ${index + 1}`}
                              fill
                              className="object-cover transition-transform duration-300 group-hover:scale-110"
                            />
                            <div className="absolute inset-0 bg-black/0 group-hover:bg-black/30 transition-colors flex items-center justify-center">
                              <Camera className="w-8 h-8 text-white opacity-0 group-hover:opacity-100 transition-opacity" />
                            </div>
                            {image.caption && (
                              <div className="absolute bottom-0 left-0 right-0 p-3 bg-gradient-to-t from-black/70 to-transparent">
                                <p className="text-white text-sm truncate">{image.caption}</p>
                              </div>
                            )}
                          </div>
                        ))}
                      </div>
                    </div>
                  </motion.div>
                </div>
              )}

              {/* Highlights */}
              {tour.highlights && tour.highlights.length > 0 && (
                <div ref={sectionRefs.highlights} className="bg-white rounded-2xl shadow-md overflow-hidden">
                  <button
                    onClick={() => toggleSection('highlights')}
                    className="w-full flex items-center justify-between p-6 text-left hover:bg-gray-50 transition-colors"
                  >
                    <h2 className="text-2xl font-bold text-gray-900">Tour Highlights</h2>
                    <ChevronDown className={`w-6 h-6 text-gray-400 transition-transform duration-300 ${openSections.has('highlights') ? 'rotate-180' : ''}`} />
                  </button>
                  <motion.div
                    initial={false}
                    animate={{ height: openSections.has('highlights') ? 'auto' : 0, opacity: openSections.has('highlights') ? 1 : 0 }}
                    transition={{ duration: 0.3 }}
                    className="overflow-hidden"
                  >
                    <div className="px-6 pb-6">
                      <div className="grid md:grid-cols-2 gap-4">
                        {tour.highlights.map((highlight) => (
                          <div key={highlight.id} className="flex items-start gap-3 p-4 bg-primary-50 rounded-xl">
                            <div className="w-10 h-10 bg-primary-100 rounded-lg flex items-center justify-center flex-shrink-0">
                              <Star className="w-5 h-5 text-primary-600" />
                            </div>
                            <div>
                              <h3 className="font-semibold text-gray-900">{highlight.title}</h3>
                              <p className="text-sm text-gray-600">{highlight.description}</p>
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  </motion.div>
                </div>
              )}

              {/* Itinerary */}
              {tour.itinerary && tour.itinerary.length > 0 && (
                <div ref={sectionRefs.itinerary} className="bg-white rounded-2xl shadow-md overflow-hidden">
                  <button
                    onClick={() => toggleSection('itinerary')}
                    className="w-full flex items-center justify-between p-6 text-left hover:bg-gray-50 transition-colors"
                  >
                    <h2 className="text-2xl font-bold text-gray-900">Day by Day Itinerary</h2>
                    <ChevronDown className={`w-6 h-6 text-gray-400 transition-transform duration-300 ${openSections.has('itinerary') ? 'rotate-180' : ''}`} />
                  </button>
                  <motion.div
                    initial={false}
                    animate={{ height: openSections.has('itinerary') ? 'auto' : 0, opacity: openSections.has('itinerary') ? 1 : 0 }}
                    transition={{ duration: 0.3 }}
                    className="overflow-hidden"
                  >
                    <div className="px-6 pb-6">
                      <div className="space-y-4">
                        {tour.itinerary.map((day) => (
                          <div key={day.id} className="border rounded-xl p-5">
                            <div className="flex items-center gap-4 mb-3">
                              <span className="w-12 h-12 bg-primary-500 text-white rounded-full flex items-center justify-center font-bold">
                                {day.day_number}
                              </span>
                              <h3 className="text-lg font-semibold text-gray-900">{day.title}</h3>
                            </div>
                            <p className="text-gray-600 mb-4">{day.description}</p>
                            <div className="flex flex-wrap gap-3 text-sm">
                              {day.locations && (
                                <div className="flex items-center gap-2 text-gray-500">
                                  <MapPin className="w-4 h-4 flex-shrink-0" />
                                  <span className="break-words">{day.locations}</span>
                                </div>
                              )}
                              {day.meals_included && (
                                <div className="flex items-center gap-2 text-gray-500">
                                  <span className="break-words">Meals: {day.meals_included}</span>
                                </div>
                              )}
                              {day.accommodation && (
                                <div className="flex items-center gap-2 text-gray-500">
                                  <span className="break-words">Stay: {day.accommodation}</span>
                                </div>
                              )}
                            </div>
                          </div>
                        ))}
                      </div>
                    </div>
                  </motion.div>
                </div>
              )}

              {/* Inclusions */}
              <div ref={sectionRefs.inclusions} className="bg-white rounded-2xl shadow-md overflow-hidden">
                <button
                  onClick={() => toggleSection('inclusions')}
                  className="w-full flex items-center justify-between p-6 text-left hover:bg-gray-50 transition-colors"
                >
                  <h2 className="text-2xl font-bold text-gray-900">What&apos;s Included</h2>
                  <ChevronDown className={`w-6 h-6 text-gray-400 transition-transform duration-300 ${openSections.has('inclusions') ? 'rotate-180' : ''}`} />
                </button>
                <motion.div
                  initial={false}
                  animate={{ height: openSections.has('inclusions') ? 'auto' : 0, opacity: openSections.has('inclusions') ? 1 : 0 }}
                  transition={{ duration: 0.3 }}
                  className="overflow-hidden"
                >
                  <div className="px-6 pb-6">
                    <div className="grid md:grid-cols-2 gap-8">
                      {included.length > 0 && (
                        <div>
                          <h3 className="font-semibold text-green-600 mb-4 flex items-center gap-2">
                            <Check className="w-5 h-5" />
                            Included
                          </h3>
                          <ul className="space-y-2">
                            {included.map((item) => (
                              <li key={item.id} className="flex items-center gap-2 text-gray-600">
                                <Check className="w-4 h-4 text-green-500" />
                                {item.item}
                              </li>
                            ))}
                          </ul>
                        </div>
                      )}
                      {notIncluded.length > 0 && (
                        <div>
                          <h3 className="font-semibold text-red-600 mb-4 flex items-center gap-2">
                            <X className="w-5 h-5" />
                            Not Included
                          </h3>
                          <ul className="space-y-2">
                            {notIncluded.map((item) => (
                              <li key={item.id} className="flex items-center gap-2 text-gray-600">
                                <X className="w-4 h-4 text-red-500" />
                                {item.item}
                              </li>
                            ))}
                          </ul>
                        </div>
                      )}
                    </div>
                  </div>
                </motion.div>
              </div>

              {/* Seasonal Pricing */}
              {tour.seasonal_pricing && tour.seasonal_pricing.length > 0 && (
                <div ref={sectionRefs.pricing} className="bg-white rounded-2xl shadow-md overflow-hidden">
                  <button
                    onClick={() => toggleSection('pricing')}
                    className="w-full flex items-center justify-between p-6 text-left hover:bg-gray-50 transition-colors"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center">
                        <DollarSign className="w-6 h-6 text-green-600" />
                      </div>
                      <div>
                        <h2 className="text-2xl font-bold text-gray-900">Seasonal Pricing</h2>
                        <p className="text-sm text-gray-500">Prices vary by season</p>
                      </div>
                    </div>
                    <ChevronDown className={`w-6 h-6 text-gray-400 transition-transform duration-300 ${openSections.has('pricing') ? 'rotate-180' : ''}`} />
                  </button>
                  <motion.div
                    initial={false}
                    animate={{ height: openSections.has('pricing') ? 'auto' : 0, opacity: openSections.has('pricing') ? 1 : 0 }}
                    transition={{ duration: 0.3 }}
                    className="overflow-hidden"
                  >
                    <div className="px-6 pb-6">
                  {/* Mobile View - Cards */}
                  <div className="md:hidden space-y-3">
                    {tour.seasonal_pricing.map((pricing) => (
                      <div
                        key={pricing.id}
                        className="bg-gray-50 rounded-xl p-4"
                      >
                        <div className="flex items-center justify-between mb-3">
                          <span className={`inline-flex items-center gap-2 font-medium ${
                            pricing.season_name === 'High Season'
                              ? 'text-red-600'
                              : pricing.season_name === 'Low Season'
                              ? 'text-green-600'
                              : 'text-amber-600'
                          }`}>
                            {pricing.season_name === 'High Season' && '🔥'}
                            {pricing.season_name === 'Low Season' && '💰'}
                            {pricing.season_name === 'Shoulder Season' && '⭐'}
                            {pricing.season_name}
                          </span>
                          <span className="font-bold text-lg text-gray-900">${parseFloat(pricing.price_per_person).toFixed(0)}</span>
                        </div>
                        <div className="text-sm text-gray-600 mb-2">
                          {new Date(pricing.start_date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })} - {new Date(pricing.end_date).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}
                        </div>
                        <div className="text-sm text-gray-500 flex items-center gap-1">
                          <User className="w-4 h-4" />
                          Single Supplement: +${parseFloat(pricing.single_supplement).toFixed(0)}
                        </div>
                      </div>
                    ))}
                  </div>
                  {/* Desktop View - Table */}
                  <div className="hidden md:block overflow-x-auto">
                    <table className="w-full">
                      <thead>
                        <tr className="border-b border-gray-200">
                          <th className="text-left py-3 px-4 font-semibold text-gray-700">Season</th>
                          <th className="text-left py-3 px-4 font-semibold text-gray-700">Period</th>
                          <th className="text-right py-3 px-4 font-semibold text-gray-700">Price/Person</th>
                          <th className="text-right py-3 px-4 font-semibold text-gray-700">Single Supplement</th>
                        </tr>
                      </thead>
                      <tbody>
                        {tour.seasonal_pricing.map((pricing, index) => (
                          <tr
                            key={pricing.id}
                            className={`border-b border-gray-100 ${index % 2 === 0 ? 'bg-gray-50' : ''}`}
                          >
                            <td className="py-4 px-4">
                              <span className={`inline-flex items-center gap-2 font-medium ${
                                pricing.season_name === 'High Season'
                                  ? 'text-red-600'
                                  : pricing.season_name === 'Low Season'
                                  ? 'text-green-600'
                                  : 'text-amber-600'
                              }`}>
                                {pricing.season_name === 'High Season' && '🔥'}
                                {pricing.season_name === 'Low Season' && '💰'}
                                {pricing.season_name === 'Shoulder Season' && '⭐'}
                                {pricing.season_name}
                              </span>
                            </td>
                            <td className="py-4 px-4 text-gray-600 text-sm">
                              {new Date(pricing.start_date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })} - {new Date(pricing.end_date).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}
                            </td>
                            <td className="py-4 px-4 text-right">
                              <span className="font-bold text-gray-900">${parseFloat(pricing.price_per_person).toFixed(0)}</span>
                            </td>
                            <td className="py-4 px-4 text-right">
                              <span className="text-gray-600 flex items-center justify-end gap-1">
                                <User className="w-4 h-4" />
                                +${parseFloat(pricing.single_supplement).toFixed(0)}
                              </span>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                  <div className="mt-4 p-4 bg-blue-50 rounded-xl">
                    <p className="text-sm text-blue-800">
                      <strong>Note:</strong> Prices are per person based on double occupancy. Single supplement applies for solo travelers requiring a private room.
                    </p>
                  </div>
                    </div>
                  </motion.div>
                </div>
              )}

              {/* Upcoming Departures */}
              {tour.departures && tour.departures.length > 0 && (
                <div ref={sectionRefs.departures} className="bg-white rounded-2xl shadow-md overflow-hidden">
                  <button
                    onClick={() => toggleSection('departures')}
                    className="w-full flex items-center justify-between p-6 text-left hover:bg-gray-50 transition-colors"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center">
                        <CalendarDays className="w-6 h-6 text-blue-600" />
                      </div>
                      <div>
                        <h2 className="text-2xl font-bold text-gray-900">Upcoming Departures</h2>
                        <p className="text-sm text-gray-500">Choose your preferred travel date</p>
                      </div>
                    </div>
                    <ChevronDown className={`w-6 h-6 text-gray-400 transition-transform duration-300 ${openSections.has('departures') ? 'rotate-180' : ''}`} />
                  </button>
                  <motion.div
                    initial={false}
                    animate={{ height: openSections.has('departures') ? 'auto' : 0, opacity: openSections.has('departures') ? 1 : 0 }}
                    transition={{ duration: 0.3 }}
                    className="overflow-hidden"
                  >
                    <div className="px-6 pb-6">
                  <div className="space-y-3">
                    {tour.departures.slice(0, 8).map((departure) => (
                      <div
                        key={departure.id}
                        className={`p-4 rounded-xl border-2 transition-colors ${
                          departure.status === 'available'
                            ? 'border-gray-200 hover:border-primary-300 bg-white'
                            : 'border-orange-200 bg-orange-50'
                        }`}
                      >
                        {/* Mobile Layout */}
                        <div className="sm:hidden">
                          <div className="flex items-start justify-between mb-3">
                            <div className="flex items-center gap-3">
                              <div className="text-center min-w-[50px]">
                                <div className="text-2xl font-bold text-gray-900">
                                  {new Date(departure.departure_date).getDate()}
                                </div>
                                <div className="text-xs text-gray-500">
                                  {new Date(departure.departure_date).toLocaleDateString('en-US', { month: 'short' })}
                                </div>
                              </div>
                              <div>
                                <div className="font-medium text-gray-900 text-sm">
                                  {new Date(departure.departure_date).toLocaleDateString('en-US', { weekday: 'short', month: 'short', day: 'numeric' })}
                                </div>
                                <div className="text-xs text-gray-500 mt-1">
                                  Returns: {new Date(departure.return_date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}
                                </div>
                              </div>
                            </div>
                            <div className="text-right">
                              <div className="text-lg font-bold text-primary-600">
                                ${parseFloat(departure.price).toFixed(0)}
                              </div>
                            </div>
                          </div>
                          <div className="flex items-center justify-between pt-3 border-t border-gray-100">
                            <div className={`text-xs flex items-center gap-1 ${
                              departure.available_spots <= 5 ? 'text-orange-600' : 'text-gray-500'
                            }`}>
                              {departure.available_spots <= 5 && <AlertCircle className="w-3 h-3" />}
                              {departure.available_spots} spots left
                            </div>
                            {departure.is_guaranteed && (
                              <span className="flex items-center gap-1 text-green-600 text-xs">
                                <CheckCircle className="w-3 h-3" />
                                Guaranteed
                              </span>
                            )}
                          </div>
                        </div>
                        {/* Desktop Layout */}
                        <div className="hidden sm:flex sm:flex-wrap sm:items-center sm:justify-between">
                          <div className="flex items-center gap-4">
                            <div className="text-center">
                              <div className="text-2xl font-bold text-gray-900">
                                {new Date(departure.departure_date).getDate()}
                              </div>
                              <div className="text-sm text-gray-500">
                                {new Date(departure.departure_date).toLocaleDateString('en-US', { month: 'short' })}
                              </div>
                            </div>
                            <div>
                              <div className="flex items-center gap-2">
                                <Plane className="w-4 h-4 text-gray-400" />
                                <span className="font-medium text-gray-900">
                                  {new Date(departure.departure_date).toLocaleDateString('en-US', { weekday: 'long', month: 'long', day: 'numeric', year: 'numeric' })}
                                </span>
                              </div>
                              <div className="flex items-center gap-3 mt-1 text-sm text-gray-500">
                                <span>Returns: {new Date(departure.return_date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}</span>
                                {departure.is_guaranteed && (
                                  <span className="flex items-center gap-1 text-green-600">
                                    <CheckCircle className="w-4 h-4" />
                                    Guaranteed
                                  </span>
                                )}
                              </div>
                            </div>
                          </div>
                          <div className="flex items-center gap-4 mt-3 sm:mt-0">
                            <div className="text-right">
                              <div className="text-xl font-bold text-primary-600">
                                ${parseFloat(departure.price).toFixed(0)}
                              </div>
                              <div className={`text-sm flex items-center gap-1 justify-end ${
                                departure.available_spots <= 5 ? 'text-orange-600' : 'text-gray-500'
                              }`}>
                                {departure.available_spots <= 5 && <AlertCircle className="w-4 h-4" />}
                                {departure.available_spots} spots left
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                  {tour.departures.length > 8 && (
                    <div className="mt-4 text-center">
                      <p className="text-sm text-gray-500">
                        + {tour.departures.length - 8} more departure dates available
                      </p>
                    </div>
                  )}
                    </div>
                  </motion.div>
                </div>
              )}

              {/* FAQs */}
              {tour.faqs && tour.faqs.length > 0 && (
                <div ref={sectionRefs.faqs} className="bg-white rounded-2xl shadow-md overflow-hidden">
                  <button
                    onClick={() => toggleSection('faqs')}
                    className="w-full flex items-center justify-between p-6 text-left hover:bg-gray-50 transition-colors"
                  >
                    <div className="flex items-center gap-3">
                      <div className="w-10 h-10 bg-primary-100 rounded-lg flex items-center justify-center">
                        <HelpCircle className="w-6 h-6 text-primary-600" />
                      </div>
                      <h2 className="text-2xl font-bold text-gray-900">Frequently Asked Questions</h2>
                    </div>
                    <ChevronDown className={`w-6 h-6 text-gray-400 transition-transform duration-300 ${openSections.has('faqs') ? 'rotate-180' : ''}`} />
                  </button>
                  <motion.div
                    initial={false}
                    animate={{ height: openSections.has('faqs') ? 'auto' : 0, opacity: openSections.has('faqs') ? 1 : 0 }}
                    transition={{ duration: 0.3 }}
                    className="overflow-hidden"
                  >
                    <div className="px-6 pb-6">
                      <div className="space-y-3">
                        {tour.faqs.map((faq, index) => (
                          <FAQItem
                            key={faq.id}
                            question={faq.question}
                            answer={faq.answer}
                            isOpen={openFAQ === index}
                            onClick={() => setOpenFAQ(openFAQ === index ? null : index)}
                          />
                        ))}
                      </div>
                    </div>
                  </motion.div>
                </div>
              )}
            </div>

            {/* Right Column - Booking Card */}
            <div className="lg:col-span-1">
              <div className="sticky top-32">
                <div className="bg-white rounded-2xl p-6 shadow-lg">
                  {/* Early Bird Banner */}
                  {tour.is_early_booking && tour.early_booking_end_date && (
                    <div className="mb-6 -mx-6 -mt-6 p-4 bg-gradient-to-r from-orange-500 to-amber-500 rounded-t-2xl">
                      <div className="flex items-center gap-2 text-white mb-2">
                        <Sparkles className="w-5 h-5" />
                        <span className="font-bold">{tour.early_booking_badge || 'Early Bird Offer'}</span>
                        <span className="ml-auto bg-white/20 px-2 py-0.5 rounded text-sm">
                          Save {tour.early_booking_discount}%
                        </span>
                      </div>
                      <div className="flex items-center gap-2 text-white/90 text-sm mb-3">
                        <Timer className="w-4 h-4" />
                        <span>Offer ends in:</span>
                      </div>
                      <CountdownTimer endDate={tour.early_booking_end_date} />
                    </div>
                  )}

                  {/* Price */}
                  <div className="mb-6">
                    <span className="text-gray-500 text-sm">
                      {tour.is_early_booking ? 'Early Bird Price' : 'From'}
                    </span>
                    <div className="flex items-baseline gap-2">
                      <span className={`text-3xl font-bold ${tour.is_early_booking ? 'text-orange-500' : 'text-primary-600'}`}>
                        ${tour.early_booking_price || parseFloat(tour.discounted_price).toFixed(0)}
                      </span>
                      {(tour.has_discount || tour.is_early_booking) && (
                        <span className="text-lg text-gray-400 line-through">
                          ${parseFloat(tour.price).toFixed(0)}
                        </span>
                      )}
                      <span className="text-gray-500">/ person</span>
                    </div>
                    {tour.is_early_booking && tour.early_booking_discount && (
                      <span className="inline-block mt-2 px-2 py-1 bg-orange-100 text-orange-600 text-sm font-medium rounded">
                        Early Bird: Save {tour.early_booking_discount}%
                      </span>
                    )}
                    {!tour.is_early_booking && tour.has_discount && tour.discount_percentage && (
                      <span className="inline-block mt-2 px-2 py-1 bg-red-100 text-red-600 text-sm font-medium rounded">
                        Save {tour.discount_percentage}%
                      </span>
                    )}
                    {(tour.price_single_supplement || tour.child_price) && (
                      <div className="mt-4 space-y-2 pt-4 border-t border-gray-100">
                        {tour.price_single_supplement && (
                          <div className="flex items-center justify-between text-sm">
                            <span className="text-gray-500">Single Supplement</span>
                            <span className="font-semibold text-gray-900">
                              +${parseFloat(tour.price_single_supplement).toFixed(0)}
                            </span>
                          </div>
                        )}
                        {tour.child_price && (
                          <div className="flex items-center justify-between text-sm">
                            <span className="text-gray-500">Child Price</span>
                            <span className="font-semibold text-gray-900">
                              ${parseFloat(tour.child_price).toFixed(0)}
                            </span>
                          </div>
                        )}
                      </div>
                    )}
                  </div>

                  {/* Quick Info */}
                  <div className="space-y-3 mb-6 pb-6 border-b">
                    <div className="flex items-center justify-between text-sm">
                      <span className="text-gray-500">Duration</span>
                      <span className="font-medium">{tour.duration_display}</span>
                    </div>
                    <div className="flex items-center justify-between text-sm">
                      <span className="text-gray-500">Group Size</span>
                      <span className="font-medium">Max {tour.max_group_size} people</span>
                    </div>
                    <div className="flex items-center justify-between text-sm">
                      <span className="text-gray-500">Languages</span>
                      <span className="font-medium">{tour.languages}</span>
                    </div>
                  </div>

                </div>

                {/* Inquiry Form */}
                <InquiryForm
                  tourName={tour.name}
                  tourSlug={tour.slug}
                  tourPrice={`$${tour.early_booking_price || parseFloat(tour.discounted_price).toFixed(0)} per person`}
                  tourDuration={tour.duration_display}
                />

                {/* WhatsApp CTA */}
                <a
                  href={`https://wa.me/201060873700?text=${encodeURIComponent(`Hi, I'm interested in: ${tour.name}`)}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="flex items-center gap-3 mt-4 px-4 py-3 bg-green-500 hover:bg-green-600 text-white rounded-xl transition-colors"
                >
                  <MessageSquare className="w-5 h-5 flex-shrink-0" />
                  <span className="font-semibold text-sm">Ask about this tour on WhatsApp</span>
                </a>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Image Lightbox Modal */}
      {galleryOpen && tour.images && tour.images.length > 0 && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          className="fixed inset-0 z-50 bg-black/95 flex items-center justify-center"
          onClick={() => setGalleryOpen(false)}
        >
          {/* Close Button */}
          <button
            onClick={() => setGalleryOpen(false)}
            className="absolute top-4 right-4 z-10 p-2 bg-white/10 hover:bg-white/20 rounded-full transition-colors"
          >
            <X className="w-6 h-6 text-white" />
          </button>

          {/* Previous Button */}
          <button
            onClick={(e) => {
              e.stopPropagation();
              setCurrentImageIndex((prev) =>
                prev === 0 ? tour.images.length - 1 : prev - 1
              );
            }}
            className="absolute left-4 z-10 p-3 bg-white/10 hover:bg-white/20 rounded-full transition-colors"
          >
            <ChevronLeft className="w-6 h-6 text-white" />
          </button>

          {/* Image */}
          <div
            className="relative w-full max-w-5xl h-[80vh] mx-4"
            onClick={(e) => e.stopPropagation()}
          >
            <Image
              src={tour.images[currentImageIndex].image}
              alt={tour.images[currentImageIndex].alt_text || tour.images[currentImageIndex].caption || ''}
              fill
              className="object-contain"
            />
            {tour.images[currentImageIndex].caption && (
              <div className="absolute bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-black/80 to-transparent">
                <p className="text-white text-center text-lg">
                  {tour.images[currentImageIndex].caption}
                </p>
              </div>
            )}
          </div>

          {/* Next Button */}
          <button
            onClick={(e) => {
              e.stopPropagation();
              setCurrentImageIndex((prev) =>
                prev === tour.images.length - 1 ? 0 : prev + 1
              );
            }}
            className="absolute right-4 z-10 p-3 bg-white/10 hover:bg-white/20 rounded-full transition-colors"
          >
            <ChevronRight className="w-6 h-6 text-white" />
          </button>

          {/* Image Counter */}
          <div className="absolute bottom-4 left-1/2 -translate-x-1/2 px-4 py-2 bg-white/10 rounded-full">
            <span className="text-white text-sm">
              {currentImageIndex + 1} / {tour.images.length}
            </span>
          </div>
        </motion.div>
      )}
    </div>
  );
}
