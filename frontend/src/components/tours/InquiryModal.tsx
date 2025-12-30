'use client';

import { useState } from 'react';
import { X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface InquiryModalProps {
  isOpen: boolean;
  onClose: () => void;
  tourName: string;
}

const nationalities = [
  'Select Nationality',
  'American', 'British', 'Canadian', 'Australian', 'German', 'French', 'Italian', 'Spanish',
  'Dutch', 'Belgian', 'Swiss', 'Austrian', 'Swedish', 'Norwegian', 'Danish', 'Finnish',
  'Russian', 'Chinese', 'Japanese', 'Korean', 'Indian', 'Brazilian', 'Mexican', 'Argentinian',
  'Saudi', 'Emirati', 'Kuwaiti', 'Qatari', 'Egyptian', 'Other'
];

export function InquiryModal({ isOpen, onClose, tourName }: InquiryModalProps) {
  const [formData, setFormData] = useState({
    fullName: '',
    email: '',
    nationality: '',
    phone: '',
    fromDate: '',
    toDate: '',
    adults: '',
    children: '',
    infants: '',
    specialRequests: '',
    agreeTerms: false,
  });
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSubmitting(true);

    // Create WhatsApp message
    const message = `*New Booking Inquiry*

*Tour:* ${tourName}

*Personal Details:*
- Name: ${formData.fullName}
- Email: ${formData.email}
- Nationality: ${formData.nationality}
- Phone: ${formData.phone}

*Travel Details:*
- From: ${formData.fromDate}
- To: ${formData.toDate}
- Adults (+12): ${formData.adults || '0'}
- Children (2-11): ${formData.children || '0'}
- Infants (0-2): ${formData.infants || '0'}

*Special Requests:*
${formData.specialRequests || 'None'}`;

    // Open WhatsApp with the message
    const whatsappUrl = `https://wa.me/201060873700?text=${encodeURIComponent(message)}`;
    window.open(whatsappUrl, '_blank');

    setIsSubmitting(false);
    setSubmitted(true);

    // Reset and close after 2 seconds
    setTimeout(() => {
      setSubmitted(false);
      setFormData({
        fullName: '',
        email: '',
        nationality: '',
        phone: '',
        fromDate: '',
        toDate: '',
        adults: '',
        children: '',
        infants: '',
        specialRequests: '',
        agreeTerms: false,
      });
      onClose();
    }, 2000);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    const { name, value, type } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? (e.target as HTMLInputElement).checked : value
    }));
  };

  return (
    <AnimatePresence>
      {isOpen && (
        <>
          {/* Backdrop */}
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={onClose}
            className="fixed inset-0 bg-black/50 z-50"
          />

          {/* Modal */}
          <motion.div
            initial={{ opacity: 0, scale: 0.95, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 0.95, y: 20 }}
            className="fixed inset-0 z-50 flex items-center justify-center p-4"
          >
            <div className="bg-white rounded-2xl shadow-2xl w-full max-w-md max-h-[90vh] overflow-y-auto">
              {/* Header */}
              <div className="sticky top-0 bg-white border-b px-6 py-4 flex items-center justify-between rounded-t-2xl">
                <h2 className="text-xl font-bold text-gray-900">Enquire Now</h2>
                <button
                  onClick={onClose}
                  className="p-2 hover:bg-gray-100 rounded-full transition-colors"
                >
                  <X className="w-5 h-5" />
                </button>
              </div>

              {/* Form */}
              <form onSubmit={handleSubmit} className="p-6 space-y-4">
                {/* Full Name */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Full Name<span className="text-red-500">*</span>
                  </label>
                  <input
                    type="text"
                    name="fullName"
                    value={formData.fullName}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2.5 border-2 border-gray-200 rounded-lg focus:border-primary-500 focus:ring-0 outline-none transition-colors"
                  />
                </div>

                {/* Email */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Email<span className="text-red-500">*</span>
                  </label>
                  <input
                    type="email"
                    name="email"
                    value={formData.email}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2.5 border-2 border-gray-200 rounded-lg focus:border-primary-500 focus:ring-0 outline-none transition-colors"
                  />
                </div>

                {/* Nationality */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Nationality<span className="text-red-500">*</span>
                  </label>
                  <select
                    name="nationality"
                    value={formData.nationality}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2.5 border-2 border-gray-200 rounded-lg focus:border-primary-500 focus:ring-0 outline-none transition-colors bg-white"
                  >
                    {nationalities.map(nat => (
                      <option key={nat} value={nat === 'Select Nationality' ? '' : nat}>
                        {nat}
                      </option>
                    ))}
                  </select>
                </div>

                {/* Phone */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Phone<span className="text-red-500">*</span>
                  </label>
                  <input
                    type="tel"
                    name="phone"
                    value={formData.phone}
                    onChange={handleChange}
                    required
                    className="w-full px-4 py-2.5 border-2 border-gray-200 rounded-lg focus:border-primary-500 focus:ring-0 outline-none transition-colors"
                  />
                </div>

                {/* Date Range */}
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      From
                    </label>
                    <input
                      type="date"
                      name="fromDate"
                      value={formData.fromDate}
                      onChange={handleChange}
                      className="w-full px-4 py-2.5 border-2 border-gray-200 rounded-lg focus:border-primary-500 focus:ring-0 outline-none transition-colors"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      To
                    </label>
                    <input
                      type="date"
                      name="toDate"
                      value={formData.toDate}
                      onChange={handleChange}
                      className="w-full px-4 py-2.5 border-2 border-gray-200 rounded-lg focus:border-primary-500 focus:ring-0 outline-none transition-colors"
                    />
                  </div>
                </div>

                {/* Travelers */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    No. of Adults (+12 Years)
                  </label>
                  <input
                    type="number"
                    name="adults"
                    min="0"
                    value={formData.adults}
                    onChange={handleChange}
                    placeholder="0"
                    className="w-full px-4 py-2.5 border-2 border-gray-200 rounded-lg focus:border-primary-500 focus:ring-0 outline-none transition-colors"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    No. of Children (2 to 11 Years)
                  </label>
                  <input
                    type="number"
                    name="children"
                    min="0"
                    value={formData.children}
                    onChange={handleChange}
                    placeholder="0"
                    className="w-full px-4 py-2.5 border-2 border-gray-200 rounded-lg focus:border-primary-500 focus:ring-0 outline-none transition-colors"
                  />
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    No. of Infants (0 to 2 Years)
                  </label>
                  <input
                    type="number"
                    name="infants"
                    min="0"
                    value={formData.infants}
                    onChange={handleChange}
                    placeholder="0"
                    className="w-full px-4 py-2.5 border-2 border-gray-200 rounded-lg focus:border-primary-500 focus:ring-0 outline-none transition-colors"
                  />
                </div>

                {/* Special Requests */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    Special Requests
                  </label>
                  <textarea
                    name="specialRequests"
                    value={formData.specialRequests}
                    onChange={handleChange}
                    rows={3}
                    className="w-full px-4 py-2.5 border-2 border-gray-200 rounded-lg focus:border-primary-500 focus:ring-0 outline-none transition-colors resize-none"
                  />
                </div>

                {/* Terms */}
                <div className="flex items-start gap-2">
                  <input
                    type="checkbox"
                    name="agreeTerms"
                    id="agreeTerms"
                    checked={formData.agreeTerms}
                    onChange={handleChange}
                    required
                    className="mt-1 w-4 h-4 text-primary-600 border-gray-300 rounded focus:ring-primary-500"
                  />
                  <label htmlFor="agreeTerms" className="text-sm text-gray-600">
                    I agree to the{' '}
                    <a href="/terms" target="_blank" className="text-primary-600 hover:underline">
                      Terms and Conditions
                    </a>
                  </label>
                </div>

                {/* Submit Button */}
                <button
                  type="submit"
                  disabled={isSubmitting || !formData.agreeTerms}
                  className="w-full py-3 bg-gradient-to-r from-amber-500 to-orange-500 text-white font-semibold rounded-lg hover:from-amber-600 hover:to-orange-600 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {isSubmitting ? 'Sending...' : submitted ? 'Sent!' : 'SEND BOOKING INQUIRY'}
                </button>
              </form>
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}
