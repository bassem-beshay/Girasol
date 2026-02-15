import paramiko, sys
sys.stdout.reconfigure(encoding='utf-8')

HOST = '50.6.250.81'
USER = 'bassem'
PASS = '852456312002Bassem**'
FILE_PATH = '/home/bassem/Girasol/frontend/src/components/layout/Footer.tsx'

new_content = """'use client';

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
"""

print('Starting...')
print(len(new_content))
