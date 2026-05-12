'use client';

import { useState } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import {
  Facebook,
  Instagram,
  MapPin,
  Phone,
  Mail,
  MessageCircle,
  ChevronDown,
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
  const [linksOpen, setLinksOpen] = useState(false);

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
      {/* Mobile & Tablet Footer */}
      <div className="lg:hidden">
        <div className="px-5 pt-10 pb-6">

          {/* Logo + Social */}
          <div className="flex flex-col items-center mb-8">
            <Link href="/">
              <Image
                src="/images/logo.webp"
                alt="Girasol Egypt"
                width={200}
                height={90}
                className="h-20 w-auto object-contain"
                loading="lazy"
              />
            </Link>
            <div className="flex justify-center gap-4 mt-5">
              {socialLinks.map((social) => (
                <a
                  key={social.name}
                  href={social.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-11 h-11 rounded-full bg-white/15 backdrop-blur-sm flex items-center justify-center text-white hover:bg-white/25 transition-colors"
                  aria-label={social.name}
                >
                  <social.icon className="w-5 h-5" />
                </a>
              ))}
            </div>
          </div>

          {/* Quick Links - Accordion */}
          <div className="mb-6">
            <button
              onClick={() => setLinksOpen(!linksOpen)}
              className="w-full flex items-center justify-between bg-white/10 backdrop-blur-sm rounded-xl px-5 py-3.5 text-white font-semibold text-sm"
            >
              {t(footerT, language, 'quickLinks')}
              <ChevronDown className={`w-4 h-4 transition-transform duration-300 ${linksOpen ? 'rotate-180' : ''}`} />
            </button>
            <div
              className={`overflow-hidden transition-all duration-300 ${linksOpen ? 'max-h-60 mt-2' : 'max-h-0'}`}
            >
              <div className="bg-white/5 backdrop-blur-sm rounded-xl px-5 py-3 grid grid-cols-2 gap-x-4 gap-y-2.5">
                {quickLinks.map((link) => (
                  <Link
                    key={link.href}
                    href={link.href}
                    className="text-white/80 hover:text-white text-sm transition-colors"
                  >
                    {link.name}
                  </Link>
                ))}
              </div>
            </div>
          </div>

          {/* Contact Buttons */}
          <div className="flex flex-col gap-3 mb-8">
            <a
              href="tel:+20237715511"
              className="flex items-center justify-center gap-3 bg-white/10 backdrop-blur-sm rounded-xl px-5 py-3.5 text-white text-sm font-medium hover:bg-white/20 transition-colors"
            >
              <Phone className="w-4 h-4 text-orange-300" />
              +20 2 3771 5511
            </a>
            <a
              href="tel:+201227011900"
              className="flex items-center justify-center gap-3 bg-white/10 backdrop-blur-sm rounded-xl px-5 py-3.5 text-white text-sm font-medium hover:bg-white/20 transition-colors"
            >
              <Phone className="w-4 h-4 text-orange-300" />
              +20 1227 011 900
            </a>
          </div>

          {/* Memberships - 2x2 Grid */}
          <div className="mb-6">
            <p className="text-white/50 text-[11px] uppercase tracking-widest text-center mb-4 font-semibold">
              {t(footerT, language, 'memberOf')}
            </p>
            <div className="grid grid-cols-2 gap-3">
              {memberships.map((member) => (
                <div
                  key={member.name}
                  className="bg-white/8 backdrop-blur-sm rounded-xl p-4 flex flex-col items-center justify-center"
                >
                  <Image
                    src={member.logo}
                    alt={member.name}
                    width={100}
                    height={50}
                    className="h-11 w-auto object-contain mb-2"
                    loading="lazy"
                  />
                  <span className="text-white/70 text-[10px] text-center leading-tight font-medium">
                    {member.name}
                  </span>
                  {member.licence && (
                    <span className="text-orange-300 text-[9px] mt-1 font-semibold">
                      {t(footerT, language, 'licence')}: {member.licence}
                    </span>
                  )}
                </div>
              ))}
            </div>
          </div>
        </div>

        {/* Copyright */}
        <div className="border-t border-white/15 py-5 px-5 text-[11px] text-white/50">
          <p className="text-start mb-1">© {new Date().getFullYear()} Girasol Egypt Travel and Tours. {t(footerT, language, 'allRightsReserved')}</p>
          <div className="flex items-center justify-center gap-3">
            <Link href="/terms" className="hover:text-white transition-colors">{t(footerT, language, 'termsConditions')}</Link>
            <span className="text-white/20">|</span>
            <Link href="/privacy" className="hover:text-white transition-colors">{t(footerT, language, 'privacyPolicy')}</Link>
          </div>
        </div>
      </div>

      {/* Desktop Footer */}
      <div className="hidden lg:block">
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
                    {t(footerT, language, 'gizaEgypt')}
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
                    <Phone className="w-4 h-4 text-orange-300" />
                  </div>
                  <a href="tel:+201227011900" className="text-white/80 hover:text-white transition-colors text-base">
                    +20 1227 011 900
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
                © {new Date().getFullYear()} Girasol Egypt Travel and Tours. {t(footerT, language, 'allRightsReserved')}
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
