'use client';

import { useState, useEffect } from 'react';
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
  Heart,
  Search,
} from 'lucide-react';

const navigation = [
  { name: 'Home', href: '/' },
  {
    name: 'Tours',
    href: '/tours',
    children: [
      { name: 'All Tours', href: '/tours' },
      { name: 'Nile Cruises', href: '/tours?type=nile_cruise' },
      { name: 'Day Tours', href: '/tours?type=day_tour' },
      { name: 'Multi-Country', href: '/tours?type=multi_country' },
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
  const pathname = usePathname();

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
              src="/images/logo-navbar.png"
              alt="Girasol Egypt - Travel and Tours"
              width={180}
              height={70}
              className="h-16 w-auto object-contain group-hover:scale-105 transition-transform duration-300"
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
            <button className={cn('p-2 hover:opacity-80', textColor)}>
              <Search className="w-5 h-5" />
            </button>
            <button className={cn('flex items-center gap-1 px-2 py-1 rounded hover:bg-black/10', textColor)}>
              <Globe className="w-4 h-4" />
              EN
              <ChevronDown className="w-3 h-3" />
            </button>
            <Link href="/profile" className={cn('p-2 hover:opacity-80', textColor)} title="Wishlist">
              <Heart className="w-5 h-5" />
            </Link>
            <Link href="/auth/login" className={cn('p-2 hover:opacity-80', textColor)} title="Login">
              <User className="w-5 h-5" />
            </Link>
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
        <div className="lg:hidden bg-white border-t animate-slide-down">
          <nav className="container-custom py-4 space-y-4">
            {navigation.map((item) => (
              <div key={item.name}>
                <Link
                  href={item.href}
                  className="block py-2 font-medium text-gray-900 hover:text-primary-500"
                  onClick={() => setIsMobileMenuOpen(false)}
                >
                  {item.name}
                </Link>
                {item.children && (
                  <div className="pl-4 space-y-2">
                    {item.children.map((child) => (
                      <Link
                        key={child.name}
                        href={child.href}
                        className="block py-1 text-gray-600 hover:text-primary-500"
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
            <div className="pt-4 border-t space-y-3">
              <div className="flex items-center justify-between">
                <Link
                  href="/profile"
                  className="flex items-center gap-2 text-gray-700 hover:text-primary-500"
                  onClick={() => setIsMobileMenuOpen(false)}
                >
                  <Heart className="w-5 h-5" />
                  Wishlist
                </Link>
                <Link
                  href="/auth/login"
                  className="flex items-center gap-2 text-gray-700 hover:text-primary-500"
                  onClick={() => setIsMobileMenuOpen(false)}
                >
                  <User className="w-5 h-5" />
                  Login
                </Link>
                <button className="flex items-center gap-1 text-gray-700 hover:text-primary-500">
                  <Globe className="w-5 h-5" />
                  EN
                </button>
              </div>
              <Link
                href="/contact"
                className="btn btn-primary btn-md w-full"
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
