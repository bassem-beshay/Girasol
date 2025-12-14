'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import { FileText, ArrowLeft } from 'lucide-react';

export default function TermsPage() {
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
              <FileText className="w-8 h-8" />
            </div>
            <h1 className="text-4xl md:text-5xl lg:text-6xl font-display font-bold mb-6">
              Terms & Conditions
            </h1>
            <p className="text-xl text-white/80 max-w-2xl mx-auto">
              Please read these terms carefully before booking a tour with Girasol Egypt.
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
              Welcome to Girasol Egypt Travel and Tours. These Terms and Conditions govern your use
              of our website and services. By booking a tour with us, you agree to be bound by these
              terms.
            </p>

            <h2>2. Booking and Payment</h2>
            <h3>2.1 Reservations</h3>
            <p>
              All bookings are subject to availability. A booking is confirmed only after we send
              you a confirmation email and receive the required deposit or full payment.
            </p>

            <h3>2.2 Payment Terms</h3>
            <ul>
              <li>A deposit of 30% of the total tour price is required to confirm your booking.</li>
              <li>The remaining balance must be paid at least 30 days before the tour start date.</li>
              <li>For bookings made within 30 days of departure, full payment is required at the time of booking.</li>
              <li>We accept major credit cards, bank transfers, and PayPal.</li>
            </ul>

            <h3>2.3 Pricing</h3>
            <p>
              All prices are quoted in USD unless otherwise stated. Prices are subject to change
              without notice until a booking is confirmed. Once confirmed, the price is guaranteed
              except in cases of currency fluctuations or government tax changes.
            </p>

            <h2>3. Cancellation Policy</h2>
            <h3>3.1 Cancellation by You</h3>
            <ul>
              <li>More than 60 days before departure: Full refund minus $50 admin fee</li>
              <li>30-60 days before departure: 50% refund</li>
              <li>15-29 days before departure: 25% refund</li>
              <li>Less than 15 days before departure: No refund</li>
            </ul>

            <h3>3.2 Cancellation by Us</h3>
            <p>
              We reserve the right to cancel a tour due to insufficient participants, force majeure,
              or safety concerns. In such cases, you will receive a full refund or the option to
              rebook on an alternative date.
            </p>

            <h2>4. Travel Insurance</h2>
            <p>
              We strongly recommend that all travelers purchase comprehensive travel insurance
              covering trip cancellation, medical emergencies, evacuation, and lost luggage. Travel
              insurance is not included in our tour prices.
            </p>

            <h2>5. Passport, Visa, and Health Requirements</h2>
            <p>
              It is your responsibility to ensure you have valid travel documents, including a
              passport with at least 6 months validity and any required visas. We can assist with
              visa information but are not responsible for obtaining visas on your behalf.
            </p>

            <h2>6. Health and Fitness</h2>
            <p>
              Some tours may require a reasonable level of fitness. Please inform us of any medical
              conditions, dietary requirements, or mobility issues at the time of booking so we can
              accommodate your needs.
            </p>

            <h2>7. Itinerary Changes</h2>
            <p>
              We reserve the right to modify tour itineraries due to weather conditions, local
              regulations, safety concerns, or other factors beyond our control. We will always
              endeavor to provide suitable alternatives.
            </p>

            <h2>8. Limitation of Liability</h2>
            <p>
              Girasol Egypt acts as an agent for hotels, airlines, and other service providers. We
              are not liable for any injury, damage, loss, delay, or inconvenience caused by these
              third parties. Our liability is limited to the tour price paid.
            </p>

            <h2>9. Behavior and Conduct</h2>
            <p>
              We expect all travelers to behave responsibly and respect local customs, laws, and
              fellow travelers. We reserve the right to terminate the tour of any participant whose
              behavior is disruptive or endangers others, without refund.
            </p>

            <h2>10. Photography and Marketing</h2>
            <p>
              By joining our tours, you consent to being photographed or filmed for marketing
              purposes. If you do not wish to be included, please inform your guide at the start of
              the tour.
            </p>

            <h2>11. Complaints</h2>
            <p>
              If you have any complaints during your tour, please inform your guide immediately so
              we can address the issue. For complaints after the tour, please contact us within 14
              days of your return.
            </p>

            <h2>12. Governing Law</h2>
            <p>
              These terms are governed by the laws of Egypt. Any disputes shall be resolved through
              arbitration in Cairo, Egypt.
            </p>

            <h2>13. Contact Information</h2>
            <p>
              For questions about these terms, please contact us at:
            </p>
            <ul>
              <li>Email: info@girasolegypt.com</li>
              <li>Phone: +20 123 456 789</li>
              <li>Address: Cairo, Egypt</li>
            </ul>
          </motion.div>
        </div>
      </section>
    </main>
  );
}
