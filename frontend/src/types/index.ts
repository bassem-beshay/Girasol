// Tour Types
export interface Tour {
  id: number;
  name: string;
  slug: string;
  short_description: string;
  description: string;
  featured_image: string;
  category: TourCategory;
  tour_type: 'package' | 'day_tour' | 'nile_cruise' | 'multi_country';
  destinations: Destination[];
  days: number;
  nights: number;
  duration_display: string;
  price: number;
  discounted_price: number;
  currency: string;
  has_discount: boolean;
  discount_percentage: number | null;
  is_featured: boolean;
  is_best_seller: boolean;
  is_new: boolean;
  average_rating: number;
  review_count: number;
  difficulty_level: 'easy' | 'moderate' | 'challenging';
  max_group_size: number;
  highlights?: TourHighlight[];
  itinerary?: TourItinerary[];
  inclusions?: TourInclusion[];
  departures?: TourDeparture[];
  addons?: Addon[];
  faqs?: TourFAQ[];
}

export interface TourCategory {
  id: number;
  name: string;
  slug: string;
  description: string;
  icon: string;
  image: string;
  tour_count: number;
}

export interface TourHighlight {
  id: number;
  title: string;
  description: string;
  icon: string;
}

export interface TourItinerary {
  id: number;
  day_number: number;
  title: string;
  description: string;
  locations: string;
  meals_included: string;
  accommodation: string;
  image: string | null;
}

export interface TourInclusion {
  id: number;
  item: string;
  is_included: boolean;
}

export interface TourDeparture {
  id: number;
  departure_date: string;
  return_date: string;
  price: number | null;
  available_spots: number;
  is_guaranteed: boolean;
  status: 'available' | 'limited' | 'sold_out' | 'cancelled';
}

export interface TourFAQ {
  id: number;
  question: string;
  answer: string;
}

export interface Addon {
  id: number;
  name: string;
  description: string;
  price: number;
  image: string | null;
  is_per_person: boolean;
}

// Destination Types
export interface Destination {
  id: number;
  name: string;
  slug: string;
  tagline: string;
  description: string;
  featured_image: string;
  banner_image: string | null;
  country: string;
  region: string;
  latitude: number | null;
  longitude: number | null;
  best_time_to_visit: string;
  is_featured: boolean;
  tour_count: number;
  images?: DestinationImage[];
  areas?: Area[];
  activities?: Activity[];
}

export interface DestinationImage {
  id: number;
  image: string;
  caption: string;
  alt_text: string;
}

export interface Area {
  id: number;
  name: string;
  slug: string;
  description: string;
  image: string | null;
  highlights: string;
}

export interface Activity {
  id: number;
  name: string;
  description: string;
  image: string | null;
  price_from: number | null;
  price_to: number | null;
  duration: string;
}

// Booking Types
export interface Booking {
  id: number;
  booking_reference: string;
  tour: Tour;
  travel_date: string;
  return_date: string | null;
  adults: number;
  children: number;
  infants: number;
  total_travelers: number;
  lead_traveler_name: string;
  lead_traveler_email: string;
  lead_traveler_phone: string;
  lead_traveler_country: string;
  base_price: number;
  addons_total: number;
  discount_amount: number;
  total_price: number;
  currency: string;
  status: BookingStatus;
  hotel_upgrade: string;
  special_requests: string;
  travelers: Traveler[];
  booking_addons: BookingAddon[];
  confirmed_at: string | null;
  created_at: string;
}

export type BookingStatus = 'pending' | 'confirmed' | 'cancelled' | 'completed' | 'refunded';

export interface Traveler {
  id: number;
  first_name: string;
  last_name: string;
  full_name: string;
  email: string;
  phone: string;
  passport_number: string;
  passport_expiry: string | null;
  nationality: string;
  date_of_birth: string;
  traveler_type: 'adult' | 'child' | 'infant';
  is_lead: boolean;
  dietary_requirements: string;
  medical_conditions: string;
}

export interface BookingAddon {
  id: number;
  addon: Addon;
  quantity: number;
  price: number;
  total: number;
}

// Review Types
export interface Review {
  id: number;
  reviewer_name: string;
  reviewer_country: string;
  reviewer_avatar: string | null;
  tour: Tour;
  tour_name: string;
  rating: number;
  title: string;
  content: string;
  travel_date: string | null;
  is_verified: boolean;
  images: ReviewImage[];
  admin_response: string;
  admin_response_at: string | null;
  created_at: string;
}

export interface ReviewImage {
  id: number;
  image: string;
  caption: string;
}

export interface Testimonial {
  id: number;
  name: string;
  country: string;
  avatar: string | null;
  quote: string;
  rating: number;
  tour: number | null;
  tour_name: string | null;
}

// Blog Types
export interface BlogPost {
  id: number;
  title: string;
  slug: string;
  excerpt: string;
  content: string;
  featured_image: string;
  category: BlogCategory;
  author_display: string;
  published_at: string;
  reading_time: number;
  view_count: number;
  comment_count: number;
  is_featured: boolean;
  tags?: BlogTag[];
  comments?: Comment[];
}

export interface BlogCategory {
  id: number;
  name: string;
  slug: string;
  description: string;
  image: string | null;
  post_count: number;
}

export interface BlogTag {
  id: number;
  name: string;
  slug: string;
}

export interface Comment {
  id: number;
  author_name: string;
  content: string;
  created_at: string;
  replies: Comment[];
}

// Contact Types
export interface Inquiry {
  name: string;
  email: string;
  phone?: string;
  country?: string;
  inquiry_type: string;
  subject?: string;
  message: string;
  tour?: number;
  travel_date?: string;
  travelers?: number;
  budget?: string;
}

export interface FAQ {
  id: number;
  question: string;
  answer: string;
  category: string;
}

export interface Office {
  id: number;
  name: string;
  city: string;
  address: string;
  phone: string;
  email: string;
  whatsapp: string;
  latitude: number | null;
  longitude: number | null;
  working_hours: string;
  is_headquarters: boolean;
}

// User Types
export interface User {
  id: number;
  email: string;
  first_name: string;
  last_name: string;
  full_name: string;
  phone: string;
  country: string;
  avatar: string | null;
  preferred_language: 'en' | 'ar';
  newsletter_subscribed: boolean;
  date_of_birth: string | null;
  nationality: string;
  profile: UserProfile;
  created_at: string;
}

export interface UserProfile {
  bio: string;
  emergency_contact_name: string;
  emergency_contact_phone: string;
  emergency_contact_relation: string;
  dietary_requirements: string;
  medical_conditions: string;
  special_requests: string;
}

// API Response Types
export interface PaginatedResponse<T> {
  count: number;
  next: string | null;
  previous: string | null;
  results: T[];
}

export interface ApiError {
  detail?: string;
  message?: string;
  errors?: Record<string, string[]>;
}
