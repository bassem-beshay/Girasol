'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import { Shield, ArrowLeft } from 'lucide-react';

export default function PrivacyPage() {
  return (
    <main className="min-h-screen">
      {/* Hero Section */}
      <section className="relative py-24 bg-gradient-to-r from-primary-600 to-primary-700">
        <div className="absolute inset-0 bg-hero-pattern opacity-10" />
        <div className="container-custom relative z-10">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-center text-white"
          >
            <div className="w-16 h-16 mx-auto mb-6 rounded-2xl bg-white/10 flex items-center justify-center">
              <Shield className="w-8 h-8" />
            </div>
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-display font-bold mb-6">
              Privacy Policy
            </h1>
            <p className="text-xl text-white/80 max-w-2xl mx-auto">
              Your privacy is important to us. This policy explains how we collect, use, and protect your information.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Content */}
      <section className="section-padding">
        <div className="container-custom max-w-4xl">
          <Link
            href="/"
            className="inline-flex items-center gap-2 text-primary-600 hover:text-primary-700 mb-8"
          >
            <ArrowLeft className="w-4 h-4" />
            Back to Home
          </Link>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="prose prose-lg max-w-none"
          >
            <p className="text-gray-500 mb-8">Last updated: December 2024</p>

            <h2>1. Introduction</h2>
            <p>
              Girasol Egypt Travel and Tours (&quot;we,&quot; &quot;our,&quot; or &quot;us&quot;) is committed to protecting your
              privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard
              your information when you visit our website or use our services.
            </p>

            <h2>2. Information We Collect</h2>
            <h3>2.1 Personal Information</h3>
            <p>We may collect personal information that you provide directly to us, including:</p>
            <ul>
              <li>Name, email address, phone number, and postal address</li>
              <li>Passport details and date of birth (for booking purposes)</li>
              <li>Payment information (processed securely through payment providers)</li>
              <li>Travel preferences and dietary requirements</li>
              <li>Emergency contact information</li>
            </ul>

            <h3>2.2 Automatically Collected Information</h3>
            <p>When you visit our website, we may automatically collect:</p>
            <ul>
              <li>IP address and browser type</li>
              <li>Device information and operating system</li>
              <li>Pages visited and time spent on our site</li>
              <li>Referring website or source</li>
              <li>Cookies and similar tracking technologies</li>
            </ul>

            <h2>3. How We Use Your Information</h2>
            <p>We use the information we collect to:</p>
            <ul>
              <li>Process and manage your tour bookings</li>
              <li>Communicate with you about your reservations</li>
              <li>Send you marketing communications (with your consent)</li>
              <li>Improve our website and services</li>
              <li>Comply with legal obligations</li>
              <li>Protect against fraud and unauthorized transactions</li>
            </ul>

            <h2>4. Information Sharing</h2>
            <p>We may share your information with:</p>
            <ul>
              <li><strong>Service Providers:</strong> Hotels, airlines, and tour operators necessary to fulfill your booking</li>
              <li><strong>Payment Processors:</strong> To securely process your transactions</li>
              <li><strong>Legal Authorities:</strong> When required by law or to protect our rights</li>
              <li><strong>Business Partners:</strong> With your consent, for joint marketing initiatives</li>
            </ul>
            <p>We do not sell your personal information to third parties.</p>

            <h2>5. Cookies and Tracking</h2>
            <p>
              We use cookies and similar technologies to enhance your browsing experience, analyze
              website traffic, and personalize content. You can control cookie preferences through
              your browser settings.
            </p>
            <h3>Types of Cookies We Use:</h3>
            <ul>
              <li><strong>Essential Cookies:</strong> Required for website functionality</li>
              <li><strong>Analytics Cookies:</strong> Help us understand how visitors use our site</li>
              <li><strong>Marketing Cookies:</strong> Used to deliver relevant advertisements</li>
            </ul>

            <h2>6. Data Security</h2>
            <p>
              We implement appropriate technical and organizational measures to protect your personal
              information, including:
            </p>
            <ul>
              <li>SSL encryption for data transmission</li>
              <li>Secure server infrastructure</li>
              <li>Regular security assessments</li>
              <li>Employee training on data protection</li>
            </ul>
            <p>
              However, no method of transmission over the Internet is 100% secure. While we strive
              to protect your information, we cannot guarantee absolute security.
            </p>

            <h2>7. Your Rights</h2>
            <p>Depending on your location, you may have the right to:</p>
            <ul>
              <li>Access the personal information we hold about you</li>
              <li>Request correction of inaccurate information</li>
              <li>Request deletion of your personal information</li>
              <li>Object to processing of your information</li>
              <li>Request data portability</li>
              <li>Withdraw consent at any time</li>
            </ul>
            <p>To exercise these rights, please contact us using the information below.</p>

            <h2>8. Data Retention</h2>
            <p>
              We retain your personal information for as long as necessary to fulfill the purposes
              for which it was collected, including legal, accounting, or reporting requirements.
              Typically, booking information is retained for 7 years after the tour completion.
            </p>

            <h2>9. International Data Transfers</h2>
            <p>
              Your information may be transferred to and processed in countries other than your
              country of residence. We ensure appropriate safeguards are in place for such transfers
              in compliance with applicable data protection laws.
            </p>

            <h2>10. Children&apos;s Privacy</h2>
            <p>
              Our services are not directed to children under 16. We do not knowingly collect
              personal information from children. If you believe we have collected information from
              a child, please contact us immediately.
            </p>

            <h2>11. Third-Party Links</h2>
            <p>
              Our website may contain links to third-party websites. We are not responsible for the
              privacy practices of these external sites. We encourage you to review their privacy
              policies.
            </p>

            <h2>12. Changes to This Policy</h2>
            <p>
              We may update this Privacy Policy from time to time. We will notify you of any
              material changes by posting the new policy on this page and updating the &quot;Last
              updated&quot; date.
            </p>

            <h2>13. Contact Us</h2>
            <p>
              If you have questions about this Privacy Policy or our data practices, please contact
              us:
            </p>
            <ul>
              <li>Email: privacy@girasolegypt.com</li>
              <li>Phone: +20 123 456 789</li>
              <li>Address: Cairo, Egypt</li>
            </ul>

            <h2>14. Consent</h2>
            <p>
              By using our website and services, you consent to the collection and use of your
              information as described in this Privacy Policy.
            </p>
          </motion.div>
        </div>
      </section>
    </main>
  );
}
