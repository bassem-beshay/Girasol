'use client';

import { useState, useEffect, useRef } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { usePathname } from 'next/navigation';
import { cn } from '@/lib/utils';
import {
  Menu,
  X,
  ChevronDown,
  Globe,
  User,
  Check,
} from 'lucide-react';
import { useLanguageStore, languages, Language } from '@/store/languageStore';
import { useUserStore } from '@/store/userStore';

const navigation = [
  { name: 'Home', href: '/' },
  {
    name: 'Tours',
    href: '/tours',
    children: [
      { name: 'All Tours', href: '/tours' },
      { name: 'Package Tours', href: '/tours?type=package' },
      { name: 'Nile Cruises', href: '/tours?type=nile_cruise' },
      { name: 'Day Tours', href: '/tours?type=day_tour' },
      { name: 'Multi Destination', href: '/tours?type=multi-destination' },
    ],
  },
  {
    name: 'Destinations',
    href: '/destinations',
    children: [
      { name: 'Cairo', href: '/destinations/cairo' },
      { name: 'Luxor', href: '/destinations/luxor' },
      { name: 'Aswan', href: '/destinations/aswan' },
      { name: 'Sharm El Sheikh', href: '/destinations/sharm-el-sheikh' },
      { name: 'Hurghada', href: '/destinations/hurghada' },
      { name: 'Alexandria', href: '/destinations/alexandria' },
    ],
  },
  { name: 'About', href: '/about' },
  { name: 'Blog', href: '/blog' },
  { name: 'Contact', href: '/contact' },
];

export function Header() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);
  const [activeDropdown, setActiveDropdown] = useState<string | null>(null);
  const [isLangDropdownOpen, setIsLangDropdownOpen] = useState(false);
  const langDropdownRef = useRef<HTMLDivElement>(null);
  const pathname = usePathname();

  // Language store
  const { language, setLanguage } = useLanguageStore();
  const currentLangOption = languages.find(l => l.code === language) || languages[0];

  // User store
  const { user, isLoggedIn, getInitial, logout } = useUserStore();

  // Handle language change
  const handleLanguageChange = (langCode: Language) => {
    setLanguage(langCode);
    setIsLangDropdownOpen(false);
    // Trigger a page refresh to reload data with new language
    window.location.reload();
  };

  // Close language dropdown when clicking outside
  useEffect(() => {
    const handleClickOutside = (event: MouseEvent) => {
      if (langDropdownRef.current && !langDropdownRef.current.contains(event.target as Node)) {
        setIsLangDropdownOpen(false);
      }
    };
    document.addEventListener('mousedown', handleClickOutside);
    return () => document.removeEventListener('mousedown', handleClickOutside);
  }, []);

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 10);
    };
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const isHomePage = pathname === '/';
  const showWhiteBg = isScrolled || !isHomePage;
  const headerBg = showWhiteBg ? 'bg-white/95 backdrop-blur-md shadow-md' : 'bg-gradient-to-b from-black/50 to-transparent';
  const textColor = showWhiteBg ? 'text-gray-900' : 'text-white';

  return (
    <header className={cn('fixed top-0 left-0 right-0 z-50 transition-all duration-300', headerBg)}>
      {/* Main header */}
      <div className="container-custom py-3">
        <div className="flex items-center justify-between">
          {/* Logo */}
          <Link href="/" className="flex items-center group">
            <Image
              src="/images/logo-navbar.webp"
              alt="Girasol Egypt - Travel and Tours"
              width={180}
              height={70}
              className="h-10 sm:h-12 md:h-14 lg:h-16 w-auto object-contain group-hover:scale-105 transition-transform duration-300"
              priority
            />
          </Link>

          {/* Desktop Navigation */}
          <nav className="hidden lg:flex items-center gap-8">
            {navigation.map((item) => (
              <div
                key={item.name}
                className="relative"
                onMouseEnter={() => item.children && setActiveDropdown(item.name)}
                onMouseLeave={() => setActiveDropdown(null)}
              >
                <Link
                  href={item.href}
                  className={cn(
                    'flex items-center gap-1 font-medium transition-colors hover:text-primary-500',
                    pathname === item.href ? 'text-primary-500' : textColor
                  )}
                >
                  {item.name}
                  {item.children && <ChevronDown className="w-4 h-4" />}
                </Link>

                {/* Dropdown */}
                {item.children && activeDropdown === item.name && (
                  <div className="absolute top-full left-0 pt-2 animate-fade-in">
                    <div className="bg-white rounded-lg shadow-lg py-2 min-w-[200px]">
                      {item.children.map((child) => (
                        <Link
                          key={child.name}
                          href={child.href}
                          className="block px-4 py-2 text-gray-700 hover:bg-primary-50 hover:text-primary-600"
                        >
                          {child.name}
                        </Link>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            ))}
          </nav>

          {/* Right Side - Actions */}
          <div className="hidden lg:flex items-center gap-3">
            {/* Language Selector */}
            <div className="relative" ref={langDropdownRef}>
              <button
                onClick={() => setIsLangDropdownOpen(!isLangDropdownOpen)}
                className={cn(
                  'flex items-center gap-1.5 px-3 py-1.5 rounded-lg hover:bg-black/10 transition-colors',
                  textColor
                )}
              >
                <Globe className="w-4 h-4" />
                <span className="text-sm font-medium">{currentLangOption.code.toUpperCase()}</span>
                <ChevronDown className={cn('w-3 h-3 transition-transform', isLangDropdownOpen && 'rotate-180')} />
              </button>

              {/* Language Dropdown */}
              {isLangDropdownOpen && (
                <div className="absolute top-full right-0 mt-2 bg-white rounded-lg shadow-lg border border-gray-100 py-1 min-w-[160px] animate-fade-in z-50">
                  {languages.map((lang) => (
                    <button
                      key={lang.code}
                      onClick={() => handleLanguageChange(lang.code)}
                      className={cn(
                        'w-full flex items-center justify-between px-4 py-2.5 text-left hover:bg-primary-50 transition-colors',
                        language === lang.code ? 'text-primary-600 bg-primary-50/50' : 'text-gray-700'
                      )}
                    >
                      <div className="flex items-center gap-2.5">
                        <span className="text-lg">{lang.flag}</span>
                        <div>
                          <div className="font-medium text-sm">{lang.nativeName}</div>
                          <div className="text-xs text-gray-500">{lang.name}</div>
                        </div>
                      </div>
                      {language === lang.code && (
                        <Check className="w-4 h-4 text-primary-600" />
                      )}
                    </button>
                  ))}
                </div>
              )}
            </div>

{isLoggedIn && user ? (
              <div className="relative group">
                <button
                  className={cn(
                    'w-9 h-9 rounded-full bg-gradient-to-br from-amber-500 to-orange-500 flex items-center justify-center text-white font-bold text-sm shadow-md hover:shadow-lg transition-shadow',
                    'ring-2 ring-white/30'
                  )}
                  title={user.fullName}
                >
                  {getInitial()}
                </button>
                <div className="absolute top-full right-0 mt-2 bg-white rounded-lg shadow-lg border border-gray-100 py-2 min-w-[180px] opacity-0 invisible group-hover:opacity-100 group-hover:visible transition-all z-50">
                  <div className="px-4 py-2 border-b border-gray-100">
                    <p className="font-medium text-gray-900 text-sm truncate">{user.fullName}</p>
                    <p className="text-xs text-gray-500 truncate">{user.email}</p>
                  </div>
                  <button
                    onClick={logout}
                    className="w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50 transition-colors"
                  >
                    Logout
                  </button>
                </div>
              </div>
            ) : null}
            <Link href="/contact" className="btn btn-primary btn-md">
              Get Free Quote
            </Link>
          </div>

          {/* Mobile menu button */}
          <button
            className={cn('lg:hidden p-2', textColor)}
            onClick={() => setIsMobileMenuOpen(!isMobileMenuOpen)}
          >
            {isMobileMenuOpen ? <X className="w-6 h-6" /> : <Menu className="w-6 h-6" />}
          </button>
        </div>
      </div>

      {/* Mobile menu */}
      {isMobileMenuOpen && (
        <div className="lg:hidden bg-white border-t shadow-lg max-h-[80vh] overflow-y-auto">
          <nav className="container-custom py-4 space-y-1">
            {navigation.map((item) => (
              <div key={item.name} className="border-b border-gray-100 last:border-0">
                <Link
                  href={item.href}
                  className="flex items-center justify-between py-3 font-medium text-gray-900 hover:text-primary-500 active:bg-primary-50 px-2 rounded-lg transition-colors"
                  onClick={() => !item.children && setIsMobileMenuOpen(false)}
                >
                  {item.name}
                  {item.children && <ChevronDown className="w-4 h-4 text-gray-400" />}
                </Link>
                {item.children && (
                  <div className="pl-4 pb-2 space-y-1">
                    {item.children.map((child) => (
                      <Link
                        key={child.name}
                        href={child.href}
                        className="block py-2 px-3 text-gray-600 hover:text-primary-500 hover:bg-primary-50 rounded-lg transition-colors text-sm"
                        onClick={() => setIsMobileMenuOpen(false)}
                      >
                        {child.name}
                      </Link>
                    ))}
                  </div>
                )}
              </div>
            ))}
            {/* Mobile Actions */}
            <div className="pt-4 mt-2 border-t border-gray-200 space-y-3">
              {/* Language Selection for Mobile */}
              <div className="mb-3">
                <p className="text-xs text-gray-500 uppercase tracking-wider mb-2 px-2">Language</p>
                <div className="flex gap-2">
                  {languages.map((lang) => (
                    <button
                      key={lang.code}
                      onClick={() => handleLanguageChange(lang.code)}
                      className={cn(
                        'flex-1 flex items-center justify-center gap-2 py-2.5 px-3 rounded-lg border transition-all',
                        language === lang.code
                          ? 'border-primary-500 bg-primary-50 text-primary-700'
                          : 'border-gray-200 text-gray-600 hover:border-gray-300'
                      )}
                    >
                      <span>{lang.flag}</span>
                      <span className="text-sm font-medium">{lang.code.toUpperCase()}</span>
                    </button>
                  ))}
                </div>
              </div>

{isLoggedIn && user && (
                <div className="flex items-center justify-between p-3 bg-gray-50 rounded-xl border border-gray-200">
                  <div className="flex items-center gap-3">
                    <div className="w-10 h-10 rounded-full bg-gradient-to-br from-amber-500 to-orange-500 flex items-center justify-center text-white font-bold text-sm shadow-md">
                      {getInitial()}
                    </div>
                    <div>
                      <p className="font-medium text-gray-900 text-sm">{user.fullName}</p>
                      <p className="text-xs text-gray-500">{user.email}</p>
                    </div>
                  </div>
                  <button
                    onClick={() => {
                      logout();
                      setIsMobileMenuOpen(false);
                    }}
                    className="text-sm text-red-600 hover:text-red-700 font-medium"
                  >
                    Logout
                  </button>
                </div>
              )}
              <Link
                href="/contact"
                className="btn btn-primary w-full py-3 text-center font-semibold"
                onClick={() => setIsMobileMenuOpen(false)}
              >
                Get Free Quote
              </Link>
            </div>
          </nav>
        </div>
      )}
    </header>
  );
}
