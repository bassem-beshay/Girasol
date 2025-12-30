'use client';

import { useState, useEffect } from 'react';
import Link from 'next/link';
import { Share2, X } from 'lucide-react';
import { useUserStore } from '@/store/userStore';

interface InquiryFormProps {
  tourName: string;
  tourSlug: string;
  tourPrice: string;
  tourDuration: string;
}

const nationalities = [
  'Select Nationality',
  'American', 'British', 'Canadian', 'Australian', 'German', 'French', 'Italian', 'Spanish',
  'Dutch', 'Belgian', 'Swiss', 'Austrian', 'Swedish', 'Norwegian', 'Danish', 'Finnish',
  'Russian', 'Chinese', 'Japanese', 'Korean', 'Indian', 'Brazilian', 'Mexican', 'Argentinian',
  'Saudi', 'Emirati', 'Kuwaiti', 'Qatari', 'Egyptian', 'Jordanian', 'Lebanese', 'Moroccan',
  'Turkish', 'Greek', 'Polish', 'Czech', 'Hungarian', 'Romanian', 'Bulgarian',
  'South African', 'Nigerian', 'Kenyan', 'Malaysian', 'Singaporean', 'Thai', 'Vietnamese',
  'Indonesian', 'Filipino', 'Pakistani', 'Bangladeshi', 'Sri Lankan', 'Other'
];

export function InquiryForm({ tourName, tourSlug, tourPrice, tourDuration }: InquiryFormProps) {
  const [showShareMenu, setShowShareMenu] = useState(false);
  const { user, setUser } = useUserStore();
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
  const [isSubmitting, setIsSubmitting] = useState<'whatsapp' | 'email' | null>(null);

  // Pre-fill form with saved user data
  useEffect(() => {
    if (user) {
      setFormData(prev => ({
        ...prev,
        fullName: user.fullName || prev.fullName,
        email: user.email || prev.email,
        nationality: user.nationality || prev.nationality,
        phone: user.phone || prev.phone,
      }));
    }
  }, [user]);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement | HTMLTextAreaElement>) => {
    const { name, value, type } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? (e.target as HTMLInputElement).checked : value
    }));
  };

  const createMessage = () => {
    return `*New Booking Inquiry*

*Tour:* ${tourName}
*Price:* ${tourPrice}
*Duration:* ${tourDuration}

*Personal Details:*
- Name: ${formData.fullName}
- Email: ${formData.email}
- Nationality: ${formData.nationality}
- Phone: ${formData.phone}

*Travel Details:*
- From: ${formData.fromDate || 'Not specified'}
- To: ${formData.toDate || 'Not specified'}
- Adults (+12): ${formData.adults || '0'}
- Children (2-11): ${formData.children || '0'}
- Infants (0-2): ${formData.infants || '0'}

*Special Requests:*
${formData.specialRequests || 'None'}`;
  };

  const saveUserData = () => {
    if (formData.fullName && formData.email && formData.phone) {
      setUser({
        fullName: formData.fullName,
        email: formData.email,
        nationality: formData.nationality,
        phone: formData.phone,
      });
    }
  };

  const handleWhatsApp = () => {
    if (!formData.fullName || !formData.email || !formData.nationality || !formData.phone || !formData.agreeTerms) {
      alert('Please fill in all required fields and agree to the terms.');
      return;
    }
    setIsSubmitting('whatsapp');
    saveUserData();
    const message = createMessage();
    const whatsappUrl = `https://wa.me/201060873700?text=${encodeURIComponent(message)}`;
    window.open(whatsappUrl, '_blank');
    setTimeout(() => setIsSubmitting(null), 1000);
  };

  const handleEmail = () => {
    if (!formData.fullName || !formData.email || !formData.nationality || !formData.phone || !formData.agreeTerms) {
      alert('Please fill in all required fields and agree to the terms.');
      return;
    }
    setIsSubmitting('email');
    saveUserData();

    const subject = `Tour Inquiry: ${tourName}`;
    const body = `New Booking Inquiry

Tour: ${tourName}
Price: ${tourPrice}
Duration: ${tourDuration}

Personal Details:
- Name: ${formData.fullName}
- Email: ${formData.email}
- Nationality: ${formData.nationality}
- Phone: ${formData.phone}

Travel Details:
- From: ${formData.fromDate || 'Not specified'}
- To: ${formData.toDate || 'Not specified'}
- Adults (+12): ${formData.adults || '0'}
- Children (2-11): ${formData.children || '0'}
- Infants (0-2): ${formData.infants || '0'}

Special Requests:
${formData.specialRequests || 'None'}`;

    const mailtoUrl = `mailto:info@girasoltours.com?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    window.location.href = mailtoUrl;
    setTimeout(() => setIsSubmitting(null), 1000);
  };

  return (
    <div className="bg-white rounded-2xl shadow-lg border p-6">
      <h3 className="text-xl font-bold text-gray-900 mb-6 text-center">Enquire Now</h3>

      <div className="space-y-4">
        {/* === REQUIRED FIELDS === */}
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
            className="w-full px-3 py-2 border-2 border-amber-200 rounded-lg focus:border-amber-400 focus:ring-0 outline-none transition-colors text-sm"
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
            className="w-full px-3 py-2 border-2 border-amber-200 rounded-lg focus:border-amber-400 focus:ring-0 outline-none transition-colors text-sm"
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
            className="w-full px-3 py-2 border-2 border-amber-200 rounded-lg focus:border-amber-400 focus:ring-0 outline-none transition-colors bg-white text-sm"
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
            className="w-full px-3 py-2 border-2 border-amber-200 rounded-lg focus:border-amber-400 focus:ring-0 outline-none transition-colors text-sm"
          />
        </div>

        {/* === OPTIONAL FIELDS === */}
        <div className="pt-4 mt-4 border-t border-gray-200">
          <p className="text-xs text-gray-500 mb-4 uppercase tracking-wider">Optional Information</p>

          {/* Date Range */}
          <div className="grid grid-cols-2 gap-3 mb-4">
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">From</label>
              <input
                type="date"
                name="fromDate"
                value={formData.fromDate}
                onChange={handleChange}
                className="w-full px-3 py-2 border-2 border-gray-200 rounded-lg focus:border-amber-400 focus:ring-0 outline-none transition-colors text-sm"
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-1">To</label>
              <input
                type="date"
                name="toDate"
                value={formData.toDate}
                onChange={handleChange}
                className="w-full px-3 py-2 border-2 border-gray-200 rounded-lg focus:border-amber-400 focus:ring-0 outline-none transition-colors text-sm"
              />
            </div>
          </div>

          {/* Travelers - Compact Row */}
          <div className="grid grid-cols-3 gap-2 mb-4">
            <div>
              <label className="block text-xs font-medium text-gray-700 mb-1">Adults (+12)</label>
              <input
                type="number"
                name="adults"
                min="0"
                placeholder="0"
                value={formData.adults}
                onChange={handleChange}
                className="w-full px-2 py-2 border-2 border-gray-200 rounded-lg focus:border-amber-400 focus:ring-0 outline-none transition-colors text-sm text-center"
              />
            </div>
            <div>
              <label className="block text-xs font-medium text-gray-700 mb-1">Children (2-11)</label>
              <input
                type="number"
                name="children"
                min="0"
                placeholder="0"
                value={formData.children}
                onChange={handleChange}
                className="w-full px-2 py-2 border-2 border-gray-200 rounded-lg focus:border-amber-400 focus:ring-0 outline-none transition-colors text-sm text-center"
              />
            </div>
            <div>
              <label className="block text-xs font-medium text-gray-700 mb-1">Infants (0-2)</label>
              <input
                type="number"
                name="infants"
                min="0"
                placeholder="0"
                value={formData.infants}
                onChange={handleChange}
                className="w-full px-2 py-2 border-2 border-gray-200 rounded-lg focus:border-amber-400 focus:ring-0 outline-none transition-colors text-sm text-center"
              />
            </div>
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
              rows={2}
              placeholder="Any special requirements..."
              className="w-full px-3 py-2 border-2 border-gray-200 rounded-lg focus:border-amber-400 focus:ring-0 outline-none transition-colors resize-none text-sm"
            />
          </div>
        </div>

        {/* Terms */}
        <div className="flex items-start gap-2 pt-4">
          <input
            type="checkbox"
            name="agreeTerms"
            id="agreeTermsInline"
            checked={formData.agreeTerms}
            onChange={handleChange}
            className="mt-1 w-4 h-4 text-amber-500 border-gray-300 rounded focus:ring-amber-400"
          />
          <label htmlFor="agreeTermsInline" className="text-sm text-gray-600">
            I agree to the{' '}
            <Link href="/terms" target="_blank" className="text-amber-600 hover:underline">
              Terms and Conditions
            </Link>
            <span className="text-red-500">*</span>
          </label>
        </div>

        {/* Buttons - At the bottom */}
        <div className="space-y-3 pt-4">
          <button
            onClick={handleWhatsApp}
            disabled={isSubmitting === 'whatsapp'}
            className="w-full py-3 bg-gradient-to-r from-amber-500 to-orange-500 text-white font-semibold rounded-lg hover:from-amber-600 hover:to-orange-600 transition-all flex items-center justify-center gap-2 disabled:opacity-70"
          >
            <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
            </svg>
            {isSubmitting === 'whatsapp' ? 'Opening WhatsApp...' : 'Get a Free Quote Now'}
          </button>

          <button
            onClick={handleEmail}
            disabled={isSubmitting === 'email'}
            className="w-full py-3 border-2 border-gray-300 text-gray-700 font-semibold rounded-lg hover:bg-gray-50 transition-all flex items-center justify-center gap-2 disabled:opacity-70"
          >
            <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            {isSubmitting === 'email' ? 'Opening Email...' : 'Inquire via Email'}
          </button>

          {/* Share Button */}
          <div className="relative">
            <button
              onClick={() => setShowShareMenu(!showShareMenu)}
              className="w-full py-3 border-2 border-gray-200 text-gray-600 font-semibold rounded-lg hover:bg-gray-50 transition-all flex items-center justify-center gap-2"
            >
              <Share2 className="w-5 h-5" />
              Share This Tour
            </button>

            {/* Share Menu */}
            {showShareMenu && (
              <div className="absolute bottom-full left-0 right-0 mb-2 bg-white rounded-xl shadow-xl border p-4 z-10">
                <div className="flex items-center justify-between mb-3">
                  <span className="font-semibold text-gray-900">Share via</span>
                  <button onClick={() => setShowShareMenu(false)} className="text-gray-400 hover:text-gray-600">
                    <X className="w-4 h-4" />
                  </button>
                </div>
                <div className="grid grid-cols-2 gap-2">
                  {/* WhatsApp */}
                  <a
                    href={`https://wa.me/?text=${encodeURIComponent(`Check out this amazing tour!\n\n${tourName}\nPrice: ${tourPrice}\nDuration: ${tourDuration}\n\nhttps://girasoltours.com/tours/${tourSlug}`)}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center gap-2 p-3 rounded-lg bg-green-50 hover:bg-green-100 text-green-700 transition-colors"
                  >
                    <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
                    </svg>
                    WhatsApp
                  </a>

                  {/* Facebook */}
                  <a
                    href={`https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(`https://girasoltours.com/tours/${tourSlug}`)}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center gap-2 p-3 rounded-lg bg-blue-50 hover:bg-blue-100 text-blue-700 transition-colors"
                  >
                    <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M12 2C6.477 2 2 6.145 2 11.243c0 2.936 1.444 5.544 3.7 7.254V22l3.405-1.869c.91.252 1.87.388 2.895.388 5.523 0 10-4.145 10-9.243S17.523 2 12 2zm.994 12.469l-2.547-2.72-4.97 2.72 5.468-5.804 2.61 2.72 4.907-2.72-5.468 5.804z"/>
                    </svg>
                    Facebook
                  </a>

                  {/* Twitter/X */}
                  <a
                    href={`https://twitter.com/intent/tweet?text=${encodeURIComponent(`Check out this amazing tour: ${tourName}\n${tourPrice} | ${tourDuration}`)}&url=${encodeURIComponent(`https://girasoltours.com/tours/${tourSlug}`)}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center gap-2 p-3 rounded-lg bg-gray-100 hover:bg-gray-200 text-gray-700 transition-colors"
                  >
                    <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                      <path d="M18.244 2.25h3.308l-7.227 8.26 8.502 11.24H16.17l-5.214-6.817L4.99 21.75H1.68l7.73-8.835L1.254 2.25H8.08l4.713 6.231zm-1.161 17.52h1.833L7.084 4.126H5.117z"/>
                    </svg>
                    X (Twitter)
                  </a>

                  {/* Copy Link */}
                  <button
                    onClick={() => {
                      navigator.clipboard.writeText(`https://girasoltours.com/tours/${tourSlug}`);
                      alert('Link copied to clipboard!');
                      setShowShareMenu(false);
                    }}
                    className="flex items-center gap-2 p-3 rounded-lg bg-purple-50 hover:bg-purple-100 text-purple-700 transition-colors"
                  >
                    <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 16H6a2 2 0 01-2-2V6a2 2 0 012-2h8a2 2 0 012 2v2m-6 12h8a2 2 0 002-2v-8a2 2 0 00-2-2h-8a2 2 0 00-2 2v8a2 2 0 002 2z" />
                    </svg>
                    Copy Link
                  </button>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
