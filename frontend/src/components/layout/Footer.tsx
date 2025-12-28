'use client';

import Link from 'next/link';
import Image from 'next/image';
import {
  Facebook,
  Instagram,
  MapPin,
  Phone,
  Mail,
  MessageCircle,
} from 'lucide-react';

const quickLinks = [
  { name: 'Home', href: '/' },
  { name: 'Tours', href: '/tours' },
  { name: 'Destinations', href: '/destinations' },
  { name: 'About', href: '/about' },
  { name: 'Blog', href: '/blog' },
  { name: 'Contact', href: '/contact' },
];

const socialLinks = [
  { name: 'Facebook', icon: Facebook, href: 'https://www.facebook.com/share/1C8PJLKaiM/?mibextid=wwXIfr' },
  { name: 'Instagram', icon: Instagram, href: 'https://www.instagram.com/girasolegypt?igsh=MTl5OHlocDFhbzU2dQ==' },
  { name: 'WhatsApp', icon: MessageCircle, href: 'https://wa.me/201060873700' },
];

const memberships = [
  { name: 'Ministry of Tourism & Antiquities', logo: '/images/memberships/ministry-tourism.png' },
  { name: 'Girassol Group', logo: '/images/memberships/girassol-group.png' },
  { name: 'IATA', logo: '/images/memberships/iata.png' },
  { name: 'Egyptian Travel Agents Association', logo: '/images/memberships/etaa.png' },
];

export function Footer() {
  return (
    <footer className="bg-gradient-to-r from-orange-500 via-orange-700 via-[13%] to-gray-900">
      {/* Main Footer */}
      <div className="container-custom py-12 md:py-16 lg:py-20 px-4 sm:px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 md:gap-10 lg:gap-12">

          {/* Brand Section - Mobile: Center, Desktop: Left */}
          <div className="flex flex-col items-center md:items-start">
            <Link href="/" className="inline-block group">
              <Image
                src="/images/logo.webp"
                alt="Girasol Egypt"
                width={400}
                height={180}
                className="h-24 sm:h-32 md:h-36 lg:h-40 w-auto object-contain group-hover:scale-105 transition-transform duration-300"
              />
            </Link>

            {/* Social Links - Mobile only under logo */}
            <div className="flex gap-3 mt-6 md:hidden">
              {socialLinks.map((social) => (
                <a
                  key={social.name}
                  href={social.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center text-white hover:bg-white hover:text-orange-600 transition-all"
                  aria-label={social.name}
                >
                  <social.icon className="w-5 h-5" />
                </a>
              ))}
            </div>
          </div>

          {/* Quick Links */}
          <div className="text-center md:text-left">
            <h4 className="text-white font-bold mb-4 md:mb-5 text-sm md:text-base uppercase tracking-wider">
              Quick Links
            </h4>
            <div className="flex flex-col gap-2 md:gap-3">
              {quickLinks.map((link) => (
                <Link
                  key={link.name}
                  href={link.href}
                  className="text-white/80 hover:text-white hover:translate-x-1 transition-all text-sm md:text-base"
                >
                  {link.name}
                </Link>
              ))}
            </div>
          </div>

          {/* Contact Info */}
          <div className="text-center md:text-left">
            <h4 className="text-white font-bold mb-4 md:mb-5 text-sm md:text-base uppercase tracking-wider">
              Contact Us
            </h4>
            <ul className="space-y-3 md:space-y-4">
              <li className="flex items-center justify-center md:justify-start gap-3">
                <div className="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center">
                  <MapPin className="w-4 h-4 text-orange-300" />
                </div>
                <span className="text-white/80 text-sm md:text-base">
                  Giza, Egypt
                </span>
              </li>
              <li className="flex items-center justify-center md:justify-start gap-3">
                <div className="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center">
                  <Phone className="w-4 h-4 text-orange-300" />
                </div>
                <a href="tel:+20237715511" className="text-white/80 hover:text-white transition-colors text-sm md:text-base">
                  +20 2 3771 5511
                </a>
              </li>
              <li className="flex items-center justify-center md:justify-start gap-3">
                <div className="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center">
                  <Mail className="w-4 h-4 text-orange-300" />
                </div>
                <a href="mailto:info@girasoltours.com" className="text-white/80 hover:text-white transition-colors text-sm md:text-base">
                  info@girasoltours.com
                </a>
              </li>
            </ul>

            {/* Memberships - Under Contact */}
            <div className="mt-8 md:mt-10">
              <p className="text-white/70 text-sm md:text-base uppercase tracking-wider mb-4 text-center md:text-left font-medium">
                Member of
              </p>
              <div className="flex items-center justify-center md:justify-start flex-nowrap gap-5 md:gap-6">
                {memberships.map((member) => (
                  <div
                    key={member.name}
                    className="hover:scale-110 transition-transform duration-300 flex-shrink-0"
                    title={member.name}
                  >
                    <Image
                      src={member.logo}
                      alt={member.name}
                      width={200}
                      height={100}
                      className="h-20 md:h-24 lg:h-28 w-auto object-contain"
                    />
                  </div>
                ))}
              </div>
            </div>
          </div>

          {/* Social Links - Desktop only */}
          <div className="hidden md:block text-center md:text-left">
            <h4 className="text-white font-bold mb-4 md:mb-5 text-sm md:text-base uppercase tracking-wider">
              Follow Us
            </h4>
            <div className="flex gap-3 justify-center md:justify-start">
              {socialLinks.map((social) => (
                <a
                  key={social.name}
                  href={social.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-10 h-10 md:w-11 md:h-11 rounded-full bg-white/20 flex items-center justify-center text-white hover:bg-white hover:text-orange-600 transition-all hover:scale-110"
                  aria-label={social.name}
                >
                  <social.icon className="w-5 h-5" />
                </a>
              ))}
            </div>
            <p className="mt-4 text-white/50 text-xs md:text-sm">
              Follow us for the latest updates and travel inspiration.
            </p>
          </div>
        </div>
      </div>

      {/* Bottom Bar */}
      <div className="border-t border-white/20 bg-black/40">
        <div className="container-custom py-4 md:py-5 px-4 sm:px-6 lg:px-8">
          <div className="flex flex-col md:flex-row items-center justify-center md:justify-between gap-3 text-xs md:text-sm text-white/70">
            <p className="text-center md:text-left">
              © {new Date().getFullYear()} Girasol Egypt. All rights reserved.
            </p>
            <div className="flex items-center gap-4 md:gap-6">
              <Link href="/terms" className="hover:text-white transition-colors">
                Terms & Conditions
              </Link>
              <span className="text-white/30">|</span>
              <Link href="/privacy" className="hover:text-white transition-colors">
                Privacy Policy
              </Link>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
