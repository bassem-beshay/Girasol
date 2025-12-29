import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// Helper function to fix image URLs (replace localhost with actual API URL)
export const fixImageUrl = (url: string | null | undefined): string | null => {
  if (!url) return null;

  // If it's a relative path starting with /media, prepend the API base URL
  if (url.startsWith('/media')) {
    return `${API_BASE_URL}${url}`;
  }

  // Replace localhost:8000 with actual API URL
  return url.replace(/http:\/\/localhost:8000/g, API_BASE_URL)
            .replace(/http:\/\/127\.0\.0\.1:8000/g, API_BASE_URL);
};

export const api = axios.create({
  baseURL: `${API_BASE_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

// Request interceptor for adding auth token and language
api.interceptors.request.use(
  (config) => {
    const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }

    // Add language header from localStorage (set by languageStore)
    if (typeof window !== 'undefined') {
      const languageStorage = localStorage.getItem('language-storage');
      if (languageStorage) {
        try {
          const parsed = JSON.parse(languageStorage);
          const language = parsed.state?.language || 'en';
          config.headers['Accept-Language'] = language;
        } catch {
          config.headers['Accept-Language'] = 'en';
        }
      }
    }

    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor for handling errors
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // Handle 401 errors - token refresh
    if (error.response?.status === 401 && !originalRequest._retry) {
      originalRequest._retry = true;

      try {
        const refreshToken = localStorage.getItem('refresh_token');
        if (refreshToken) {
          const response = await axios.post(`${API_BASE_URL}/api/auth/token/refresh/`, {
            refresh: refreshToken,
          });

          const { access } = response.data;
          localStorage.setItem('access_token', access);

          originalRequest.headers.Authorization = `Bearer ${access}`;
          return api(originalRequest);
        }
      } catch (refreshError) {
        // Clear tokens and redirect to login
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        window.location.href = '/auth/login';
      }
    }

    return Promise.reject(error);
  }
);

// Tours API
export const toursApi = {
  getAll: (params?: Record<string, unknown>) => api.get('/tours/', { params }),
  getBySlug: (slug: string) => api.get(`/tours/${slug}/`),
  getFeatured: () => api.get('/tours/featured/'),
  getPopular: () => api.get('/tours/popular/'),
  getMultiDestination: () => api.get('/tours/multi-destination/'),
  getByDestination: (slug: string) => api.get(`/tours/destination/${slug}/`),
  getByCategory: (slug: string) => api.get(`/tours/category/${slug}/`),
  getCategories: () => api.get('/tours/categories/'),
  getRelated: (slug: string) => api.get(`/tours/${slug}/related/`),
  getDepartures: (slug: string) => api.get(`/tours/${slug}/departures/`),
  // Early Booking Offers (الحجز المبكر)
  getEarlyBookingOffers: () => api.get('/tours/early-booking/'),
  getFeaturedEarlyBooking: () => api.get('/tours/early-booking/featured/'),
  getEarlyBookingCountdown: () => api.get('/tours/early-booking/countdown/'),
  getEarlyBookingDetail: (id: number) => api.get(`/tours/early-booking/${id}/`),
};

// Destinations API
export const destinationsApi = {
  getAll: (params?: Record<string, unknown>) => api.get('/destinations/', { params }),
  getBySlug: (slug: string) => api.get(`/destinations/${slug}/`),
  getFeatured: () => api.get('/destinations/featured/'),
};

// Bookings API
export const bookingsApi = {
  create: (data: unknown) => api.post('/bookings/create/', data),
  getAll: () => api.get('/bookings/'),
  getByReference: (ref: string) => api.get(`/bookings/${ref}/`),
  cancel: (ref: string, reason?: string) => api.post(`/bookings/${ref}/cancel/`, { reason }),
  lookup: (reference: string, email: string) => api.post('/bookings/lookup/', { booking_reference: reference, email }),
  validatePromo: (code: string, tourId?: number, total?: number) =>
    api.post('/bookings/promo/validate/', { code, tour_id: tourId, total }),
};

// Reviews API
export const reviewsApi = {
  getAll: (params?: Record<string, unknown>) => api.get('/reviews/', { params }),
  getByTour: (tourSlug: string) => api.get(`/reviews/tour/${tourSlug}/`),
  getFeatured: () => api.get('/reviews/featured/'),
  create: (data: unknown) => api.post('/reviews/create/', data),
  getTestimonials: () => api.get('/reviews/testimonials/'),
};

// Blog API
export const blogApi = {
  getPosts: (params?: Record<string, unknown>) => api.get('/blog/posts/', { params }),
  getPost: (slug: string) => api.get(`/blog/posts/${slug}/`),
  getFeatured: () => api.get('/blog/posts/featured/'),
  getLatest: () => api.get('/blog/posts/latest/'),
  getCategories: () => api.get('/blog/categories/'),
  createComment: (data: unknown) => api.post('/blog/comments/', data),
};

// Contact API
export const contactApi = {
  submitInquiry: (data: unknown) => api.post('/contact/inquiry/', data),
  sendMessage: (data: {
    name: string;
    email: string;
    phone?: string;
    subject: string;
    message: string;
    tour_interest?: string;
  }) => api.post('/contact/inquiry/', data),
  subscribeNewsletter: (data: { email: string }) => api.post('/contact/newsletter/subscribe/', data),
  unsubscribeNewsletter: (email: string) => api.post('/contact/newsletter/unsubscribe/', { email }),
  getFaqs: (category?: string) => api.get('/contact/faq/', { params: { category } }),
  getOffices: () => api.get('/contact/offices/'),
  getStatistics: () => api.get('/contact/statistics/'),
};

// Auth API
export const authApi = {
  login: (email: string, password: string) => api.post('/auth/login/', { email, password }),
  register: (data: unknown) => api.post('/auth/registration/', data),
  logout: () => api.post('/auth/logout/'),
  getUser: () => api.get('/users/me/'),
  updateUser: (data: unknown) => api.patch('/users/me/', data),
  updateProfile: (data: unknown) => api.patch('/users/me/profile/', data),
  changePassword: (data: unknown) => api.post('/auth/password/change/', data),
  resetPassword: (email: string) => api.post('/auth/password/reset/', { email }),
  confirmResetPassword: (data: unknown) => api.post('/auth/password/reset/confirm/', data),
};

export default api;
