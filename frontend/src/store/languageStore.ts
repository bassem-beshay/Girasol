import { create } from 'zustand';
import { persist } from 'zustand/middleware';

export type Language = 'en' | 'es' | 'pt';

export interface LanguageOption {
  code: Language;
  name: string;
  nativeName: string;
  flag: string;
}

export const languages: LanguageOption[] = [
  { code: 'en', name: 'English', nativeName: 'English', flag: '🇬🇧' },
  { code: 'es', name: 'Spanish', nativeName: 'Español', flag: '🇪🇸' },
  { code: 'pt', name: 'Portuguese', nativeName: 'Português', flag: '🇧🇷' },
];

interface LanguageState {
  language: Language;
  setLanguage: (lang: Language) => void;
  getLanguageOption: () => LanguageOption;
}

export const useLanguageStore = create<LanguageState>()(
  persist(
    (set, get) => ({
      language: 'en',

      setLanguage: (lang: Language) => {
        set({ language: lang });
      },

      getLanguageOption: () => {
        const currentLang = get().language;
        return languages.find(l => l.code === currentLang) || languages[0];
      },
    }),
    {
      name: 'language-storage',
    }
  )
);

// Helper function to get localized field from API response
export function getLocalizedField<T extends Record<string, unknown>>(
  item: T,
  field: string,
  language: Language
): string {
  if (language === 'en') {
    return (item[field] as string) || '';
  }

  const localizedField = `${field}_${language}`;
  const localizedValue = item[localizedField] as string;

  // Fallback to English if translation not available
  return localizedValue || (item[field] as string) || '';
}
