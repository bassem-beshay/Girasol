import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { authApi } from '@/lib/api';
import { User } from '@/types';

interface AuthState {
  user: User | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  error: string | null;

  // Actions
  login: (email: string, password: string) => Promise<void>;
  register: (data: RegisterData) => Promise<void>;
  logout: () => Promise<void>;
  fetchUser: () => Promise<void>;
  updateProfile: (data: Partial<User>) => Promise<void>;
  clearError: () => void;
}

interface RegisterData {
  email: string;
  password1: string;
  password2: string;
  first_name: string;
  last_name: string;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set, get) => ({
      user: null,
      isAuthenticated: false,
      isLoading: false,
      error: null,

      login: async (email: string, password: string) => {
        set({ isLoading: true, error: null });
        try {
          const response = await authApi.login(email, password);

          if (typeof window !== 'undefined') {
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
          }

          // Fetch user data after login
          await get().fetchUser();

          set({ isAuthenticated: true, isLoading: false });
        } catch (error: unknown) {
          const err = error as { response?: { data?: { detail?: string; non_field_errors?: string[] } } };
          const message = err.response?.data?.detail ||
                         err.response?.data?.non_field_errors?.[0] ||
                         'Login failed. Please check your credentials.';
          set({ error: message, isLoading: false });
          throw error;
        }
      },

      register: async (data: RegisterData) => {
        set({ isLoading: true, error: null });
        try {
          const response = await authApi.register(data);

          if (typeof window !== 'undefined') {
            localStorage.setItem('access_token', response.data.access);
            localStorage.setItem('refresh_token', response.data.refresh);
          }

          // Fetch user data after registration
          await get().fetchUser();

          set({ isAuthenticated: true, isLoading: false });
        } catch (error: unknown) {
          const err = error as { response?: { data?: { email?: string[]; password1?: string[]; non_field_errors?: string[] } } };
          const errors = err.response?.data;
          let message = 'Registration failed. Please try again.';

          if (errors?.email) {
            message = errors.email[0];
          } else if (errors?.password1) {
            message = errors.password1[0];
          } else if (errors?.non_field_errors) {
            message = errors.non_field_errors[0];
          }

          set({ error: message, isLoading: false });
          throw error;
        }
      },

      logout: async () => {
        set({ isLoading: true });
        try {
          await authApi.logout();
        } catch {
          // Continue with logout even if API call fails
        } finally {
          if (typeof window !== 'undefined') {
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
          }
          set({ user: null, isAuthenticated: false, isLoading: false });
        }
      },

      fetchUser: async () => {
        try {
          const response = await authApi.getUser();
          set({ user: response.data, isAuthenticated: true });
        } catch {
          set({ user: null, isAuthenticated: false });
        }
      },

      updateProfile: async (data: Partial<User>) => {
        set({ isLoading: true, error: null });
        try {
          const response = await authApi.updateUser(data);
          set({ user: response.data, isLoading: false });
        } catch (error: unknown) {
          const err = error as { response?: { data?: { detail?: string } } };
          const message = err.response?.data?.detail || 'Failed to update profile.';
          set({ error: message, isLoading: false });
          throw error;
        }
      },

      clearError: () => set({ error: null }),
    }),
    {
      name: 'auth-storage',
      partialize: (state) => ({
        isAuthenticated: state.isAuthenticated,
      }),
    }
  )
);
