import axios from 'axios';

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export const api = axios.create({
  baseURL: `${API_BASE_URL}/api`,
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

// Request interceptor for adding auth token
api.interceptors.request.use(
  (config) => {
    const token = typeof window !== 'undefined' ? localStorage.getItem('access_token') : null;
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
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
  getByDestination: (slug: string) => api.get(`/tours/destination/${slug}/`),
  getByCategory: (slug: string) => api.get(`/tours/category/${slug}/`),
  getCategories: () => api.get('/tours/categories/'),
  getRelated: (slug: string) => api.get(`/tours/${slug}/related/`),
  getDepartures: (slug: string) => api.get(`/tours/${slug}/departures/`),
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

// Wishlist API
export const wishlistApi = {
  getAll: () => api.get('/users/wishlist/'),
  add: (tourId: number) => api.post('/users/wishlist/', { tour_id: tourId }),
  remove: (tourId: number) => api.delete(`/users/wishlist/${tourId}/`),
};

export default api;
