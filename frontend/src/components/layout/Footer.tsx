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
import { useLanguageStore } from '@/store/languageStore';
import { footerT, t } from '@/lib/translations';

const socialLinks = [
  { name: 'Facebook', icon: Facebook, href: 'https://www.facebook.com/share/1C8PJLKaiM/?mibextid=wwXIfr' },
  { name: 'Instagram', icon: Instagram, href: 'https://www.instagram.com/girasolegypt?igsh=MTl5OHlocDFhbzU2dQ==' },
  { name: 'WhatsApp', icon: MessageCircle, href: 'https://wa.me/201060873700' },
];

const memberships = [
  {
    name: 'Ministry of Tourism & Antiquities',
    logo: '/images/memberships/ministry-tourism.webp',
    licence: '2208 A'
  },
  {
    name: 'IATA',
    logo: '/images/memberships/girassol-group.webp',
    licence: null
  },
  {
    name: 'Egyptian Travel Agents Association',
    logo: '/images/memberships/new-logo.webp',
    licence: null
  },
  {
    name: 'Girassol Group',
    logo: '/images/memberships/etaa.webp',
    licence: null
  },
];

export function Footer() {
  const { language } = useLanguageStore();

  const quickLinks = [
    { name: t(footerT, language, 'home'), href: '/' },
    { name: t(footerT, language, 'tours'), href: '/tours' },
    { name: t(footerT, language, 'destinations'), href: '/destinations' },
    { name: t(footerT, language, 'about'), href: '/about' },
    { name: t(footerT, language, 'blog'), href: '/blog' },
    { name: t(footerT, language, 'contact'), href: '/contact' },
  ];

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
              loading="lazy" />
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
                key={link.href}
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

          {/* Memberships - Mobile */}
          <div className="mb-6">
            <p className="text-white/60 text-xs uppercase tracking-wider text-center mb-4">
              {t(footerT, language, 'memberOf')}
            </p>
            <div className="grid grid-cols-2 gap-3">
              {memberships.map((member) => (
                <div
                  key={member.name}
                  className="bg-white/10 rounded-lg p-4 flex flex-col items-center justify-center min-h-[120px]"
                >
                  <Image
                    src={member.logo}
                    alt={member.name}
                    width={120}
                    height={60}
                    className="h-14 w-auto object-contain mb-2"
                  loading="lazy" />
                  <span className="text-white/80 text-[11px] text-center leading-tight font-medium">
                    {member.name}
                  </span>
                  {member.licence && (
                    <span className="text-orange-300 text-[10px] mt-1 font-medium">
                      {t(footerT, language, 'licence')}: {member.licence}
                    </span>
                  )}
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Copyright */}
        <div className="border-t border-white/20 py-4 px-4 text-center text-xs text-white/60 space-y-2">
          <div className="flex items-center justify-center gap-3">
            <Link href="/terms" className="hover:text-white transition-colors">{t(footerT, language, 'termsConditions')}</Link>
            <span className="text-white/30">|</span>
            <Link href="/privacy" className="hover:text-white transition-colors">{t(footerT, language, 'privacyPolicy')}</Link>
          </div>
          <p>© {new Date().getFullYear()} Girasol Egypt Travel and Tours. {t(footerT, language, 'allRightsReserved')}</p>
          <p>Designed by <a href="https://wa.me/201228986508" target="_blank" rel="noopener noreferrer" className="underline text-white/80 hover:text-white transition-colors">ENG-Bassem Beshay</a></p>
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
                loading="lazy" />
              </Link>
            </div>

            {/* Quick Links */}
            <div>
              <h4 className="text-white font-bold mb-5 text-base uppercase tracking-wider">
                {t(footerT, language, 'quickLinks')}
              </h4>
              <div className="flex flex-col gap-3">
                {quickLinks.map((link) => (
                  <Link
                    key={link.href}
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
                {t(footerT, language, 'contactUs')}
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

            </div>

            {/* Social Links */}
            <div>
              <h4 className="text-white font-bold mb-5 text-base uppercase tracking-wider">
                {t(footerT, language, 'followUs')}
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
                {t(footerT, language, 'followUsDesc')}
              </p>
            </div>
          </div>

          {/* Memberships - Centered Layout */}
          <div className="mt-12 pt-10 border-t border-white/10">
            <div className="flex flex-col items-center gap-8">
              <p className="text-white text-lg uppercase tracking-widest font-semibold">
                {t(footerT, language, 'memberOf')}
              </p>
              <div className="grid grid-cols-2 lg:grid-cols-4 gap-6 w-full max-w-5xl">
                {memberships.map((member) => (
                  <div
                    key={member.name}
                    className="group bg-white/5 hover:bg-white/10 rounded-xl p-6 flex flex-col items-center justify-center transition-all duration-300 hover:scale-105 min-h-[180px]"
                  >
                    <div className="h-24 flex items-center justify-center mb-4">
                      <Image
                        src={member.logo}
                        alt={member.name}
                        width={180}
                        height={90}
                        className="max-h-24 w-auto object-contain group-hover:brightness-110 transition-all"
                      loading="lazy" />
                    </div>
                    <span className="text-white/90 text-sm text-center font-medium leading-tight">
                      {member.name}
                    </span>
                    {member.licence && (
                      <span className="text-orange-300 text-sm mt-2 font-semibold">
                        {t(footerT, language, 'licence')}: {member.licence}
                      </span>
                    )}
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>

        {/* Bottom Bar */}
        <div className="border-t border-white/20 bg-black/40">
          <div className="container-custom py-5 px-6 lg:px-8">
            <div className="flex flex-col md:flex-row items-center gap-2 md:gap-3 text-xs text-white/70">
              <p className="text-center md:text-left">
                © {new Date().getFullYear()} Girasol Egypt Travel and Tours. {t(footerT, language, 'allRightsReserved')} | Designed by <a href="https://wa.me/201228986508" target="_blank" rel="noopener noreferrer" className="underline text-white/90 hover:text-white transition-colors">ENG-Bassem Beshay</a>
              </p>
              <div className="flex items-center gap-3 md:gap-4 md:ml-auto md:mr-[10%] whitespace-nowrap">
                <Link href="/terms" className="hover:text-white transition-colors">
                  {t(footerT, language, 'termsConditions')}
                </Link>
                <span className="text-white/30">|</span>
                <Link href="/privacy" className="hover:text-white transition-colors">
                  {t(footerT, language, 'privacyPolicy')}
                </Link>
              </div>
            </div>
          </div>
        </div>
      </div>
    </footer>
  );
}
