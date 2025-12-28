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
      {/* Mobile Footer - Simple */}
      <div className="md:hidden">
        <div className="px-4 py-8">
          {/* Logo */}
          <div className="flex justify-center mb-6">
            <Link href="/">
              <Image
                src="/images/logo.webp"
                alt="Girasol Egypt"
                width={200}
                height={90}
                className="h-20 w-auto object-contain"
              />
            </Link>
          </div>

          {/* Social Links */}
          <div className="flex justify-center gap-4 mb-6">
            {socialLinks.map((social) => (
              <a
                key={social.name}
                href={social.href}
                target="_blank"
                rel="noopener noreferrer"
                className="w-10 h-10 rounded-full bg-white/20 flex items-center justify-center text-white"
                aria-label={social.name}
              >
                <social.icon className="w-5 h-5" />
              </a>
            ))}
          </div>

          {/* Quick Links - Horizontal */}
          <div className="flex flex-wrap justify-center gap-x-4 gap-y-2 mb-6 text-sm">
            {quickLinks.map((link) => (
              <Link
                key={link.name}
                href={link.href}
                className="text-white/80 hover:text-white"
              >
                {link.name}
              </Link>
            ))}
          </div>

          {/* Contact - Simple inline */}
          <div className="flex flex-col items-center gap-2 text-sm text-white/80 mb-6">
            <a href="tel:+20237715511" className="flex items-center gap-2">
              <Phone className="w-4 h-4" />
              +20 2 3771 5511
            </a>
            <a href="mailto:info@girasoltours.com" className="flex items-center gap-2">
              <Mail className="w-4 h-4" />
              info@girasoltours.com
            </a>
          </div>

          {/* Memberships - Small */}
          <div className="flex justify-center items-center gap-3 mb-4">
            {memberships.map((member) => (
              <Image
                key={member.name}
                src={member.logo}
                alt={member.name}
                width={100}
                height={50}
                className="h-10 w-auto object-contain opacity-80"
              />
            ))}
          </div>
        </div>

        {/* Copyright */}
        <div className="border-t border-white/20 py-3 px-4 text-center text-xs text-white/60">
          © {new Date().getFullYear()} Girasol Egypt
        </div>
      </div>

      {/* Desktop Footer */}
      <div className="hidden md:block">
        <div className="container-custom py-16 lg:py-20 px-6 lg:px-8">
          <div className="grid grid-cols-2 lg:grid-cols-4 gap-10 lg:gap-12">

            {/* Brand Section */}
            <div className="flex flex-col items-start">
              <Link href="/" className="inline-block group">
                <Image
                  src="/images/logo.webp"
                  alt="Girasol Egypt"
                  width={400}
                  height={180}
                  className="h-36 lg:h-40 w-auto object-contain group-hover:scale-105 transition-transform duration-300"
                />
              </Link>
            </div>

            {/* Quick Links */}
            <div>
              <h4 className="text-white font-bold mb-5 text-base uppercase tracking-wider">
                Quick Links
              </h4>
              <div className="flex flex-col gap-3">
                {quickLinks.map((link) => (
                  <Link
                    key={link.name}
                    href={link.href}
                    className="text-white/80 hover:text-white hover:translate-x-1 transition-all text-base"
                  >
                    {link.name}
                  </Link>
                ))}
              </div>
            </div>

            {/* Contact Info */}
            <div>
              <h4 className="text-white font-bold mb-5 text-base uppercase tracking-wider">
                Contact Us
              </h4>
              <ul className="space-y-4">
                <li className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center">
                    <MapPin className="w-4 h-4 text-orange-300" />
                  </div>
                  <span className="text-white/80 text-base">
                    Giza, Egypt
                  </span>
                </li>
                <li className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center">
                    <Phone className="w-4 h-4 text-orange-300" />
                  </div>
                  <a href="tel:+20237715511" className="text-white/80 hover:text-white transition-colors text-base">
                    +20 2 3771 5511
                  </a>
                </li>
                <li className="flex items-center gap-3">
                  <div className="w-8 h-8 rounded-full bg-white/10 flex items-center justify-center">
                    <Mail className="w-4 h-4 text-orange-300" />
                  </div>
                  <a href="mailto:info@girasoltours.com" className="text-white/80 hover:text-white transition-colors text-base">
                    info@girasoltours.com
                  </a>
                </li>
              </ul>

              {/* Memberships */}
              <div className="mt-10">
                <p className="text-white/70 text-base uppercase tracking-wider mb-4 font-medium">
                  Member of
                </p>
                <div className="flex items-center flex-wrap gap-4">
                  {memberships.map((member) => (
                    <div
                      key={member.name}
                      className="hover:scale-110 transition-transform duration-300"
                      title={member.name}
                    >
                      <Image
                        src={member.logo}
                        alt={member.name}
                        width={200}
                        height={100}
                        className="h-24 lg:h-28 w-auto object-contain"
                      />
                    </div>
                  ))}
                </div>
              </div>
            </div>

            {/* Social Links */}
            <div>
              <h4 className="text-white font-bold mb-5 text-base uppercase tracking-wider">
                Follow Us
              </h4>
              <div className="flex gap-3">
                {socialLinks.map((social) => (
                  <a
                    key={social.name}
                    href={social.href}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="w-11 h-11 rounded-full bg-white/20 flex items-center justify-center text-white hover:bg-white hover:text-orange-600 transition-all hover:scale-110"
                    aria-label={social.name}
                  >
                    <social.icon className="w-5 h-5" />
                  </a>
                ))}
              </div>
              <p className="mt-4 text-white/50 text-sm">
                Follow us for the latest updates and travel inspiration.
              </p>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="border-t border-white/20 bg-black/40">
          <div className="container-custom py-5 px-6 lg:px-8">
            <div className="flex flex-row items-center justify-between text-sm text-white/70">
              <p>
                © {new Date().getFullYear()} Girasol Egypt. All rights reserved.
              </p>
              <div className="flex items-center gap-6">
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
      </div>
    </footer>
  );
}
