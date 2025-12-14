'use client';

import Link from 'next/link';
import Image from 'next/image';
import {
  Facebook,
  Instagram,
  Twitter,
  Youtube,
  MapPin,
  Phone,
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
  { name: 'Facebook', icon: Facebook, href: 'https://facebook.com/girasoltours' },
  { name: 'Instagram', icon: Instagram, href: 'https://instagram.com/girasoltours' },
  { name: 'Twitter', icon: Twitter, href: 'https://twitter.com/girasoltours' },
  { name: 'YouTube', icon: Youtube, href: 'https://youtube.com/girasoltours' },
];

export function Footer() {
  return (
    <footer className="bg-gradient-to-r from-orange-500 via-orange-700 via-[13%] to-gray-900">
      {/* Main Footer */}
      <div className="container-custom py-12">
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-10">
          {/* Brand Section */}
          <div className="lg:col-span-1">
            <Link href="/" className="inline-block group -ml-4">
              <Image
                src="/images/logo.png"
                alt="Girasol Egypt"
                width={400}
                height={180}
                className="h-52 w-auto object-contain group-hover:scale-105 transition-transform duration-300"
              />
            </Link>
          </div>

          {/* Quick Links */}
          <div>
            <h4 className="text-white font-semibold mb-5 text-sm uppercase tracking-wider">
              Quick Links
            </h4>
            <div className="grid grid-cols-2 gap-x-6 gap-y-3">
              {quickLinks.map((link) => (
                <Link
                  key={link.name}
                  href={link.href}
                  className="text-white/80 hover:text-white transition-colors text-sm"
                >
                  {link.name}
                </Link>
              ))}
            </div>
          </div>

          {/* Contact Info */}
          <div>
            <h4 className="text-white font-semibold mb-5 text-sm uppercase tracking-wider">
              Contact Us
            </h4>
            <ul className="space-y-4">
              <li className="flex items-start gap-3">
                <MapPin className="w-4 h-4 text-white flex-shrink-0 mt-0.5" />
                <span className="text-white/80 text-sm">
                  Giza, Egypt
                </span>
              </li>
              <li className="flex items-center gap-3">
                <Phone className="w-4 h-4 text-white flex-shrink-0" />
                <a href="tel:+20237715511" className="text-white/80 hover:text-white transition-colors text-sm">
                  +20 2 3771 5511
                </a>
              </li>
            </ul>
          </div>

          {/* Social & Newsletter */}
          <div>
            <h4 className="text-white font-semibold mb-5 text-sm uppercase tracking-wider">
              Follow Us
            </h4>
            <div className="flex gap-2">
              {socialLinks.map((social) => (
                <a
                  key={social.name}
                  href={social.href}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-10 h-10 rounded-lg bg-white/20 flex items-center justify-center text-white hover:bg-white hover:text-primary-600 transition-all"
                  aria-label={social.name}
                >
                  <social.icon className="w-4 h-4" />
                </a>
              ))}
            </div>
            <div className="mt-6">
              <p className="text-white/60 text-xs">
                Licensed by Egyptian Tourism Authority
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Bottom Bar */}
      <div className="border-t border-white/20">
        <div className="container-custom py-5">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-3 text-xs text-white/70">
            <p>
              © {new Date().getFullYear()} Girasol Egypt. All rights reserved.
            </p>
            <div className="flex items-center gap-5">
              <Link href="/terms" className="hover:text-white transition-colors">
                Terms & Conditions
              </Link>
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
