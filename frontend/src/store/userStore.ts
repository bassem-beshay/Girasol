import { create } from 'zustand';
import { persist } from 'zustand/middleware';

interface UserInfo {
  fullName: string;
  email: string;
  nationality: string;
  phone: string;
}

interface UserState {
  user: UserInfo | null;
  isLoggedIn: boolean;

  // Actions
  setUser: (user: UserInfo) => void;
  logout: () => void;
  getInitial: () => string;
}

export const useUserStore = create<UserState>()(
  persist(
    (set, get) => ({
      user: null,
      isLoggedIn: false,

      setUser: (user: UserInfo) => {
        set({ user, isLoggedIn: true });
      },

      logout: () => {
        set({ user: null, isLoggedIn: false });
      },

      getInitial: () => {
        const { user } = get();
        if (!user?.fullName) return '';
        return user.fullName.charAt(0).toUpperCase();
      },
    }),
    {
      name: 'user-storage',
    }
  )
);
