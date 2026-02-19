'use client';

import { useState, useEffect } from 'react';
import { X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { useLanguageStore } from '@/store/languageStore';
import { inquiryFormT, t } from '@/lib/translations';
import { nationalityPhoneCode } from '@/lib/countryCodeMap';

interface InquiryModalProps {
  isOpen: boolean;
  onClose: () => void;
  tourName: string;
}

const nationalities = [
  'Select Nationality',
  // A
  'Afghan', 'Albanian', 'Algerian', 'American', 'Andorran', 'Angolan', 'Antiguan', 'Argentine',
  'Armenian', 'Australian', 'Austrian', 'Azerbaijani',
  // B
  'Bahamian', 'Bahraini', 'Bangladeshi', 'Barbadian', 'Belarusian', 'Belgian', 'Belizean',
  'Beninese', 'Bhutanese', 'Bolivian', 'Bosnian', 'Botswanan', 'Brazilian', 'British',
  'Bruneian', 'Bulgarian', 'Burkinabe', 'Burmese', 'Burundian',
  // C
  'Cambodian', 'Cameroonian', 'Canadian', 'Cape Verdean', 'Central African', 'Chadian',
  'Chilean', 'Chinese', 'Colombian', 'Comoran', 'Congolese', 'Costa Rican', 'Croatian',
  'Cuban', 'Cypriot', 'Czech',
  // D
  'Danish', 'Djiboutian', 'Dominican', 'Dutch',
  // E
  'East Timorese', 'Ecuadorian', 'Egyptian', 'Emirati', 'Equatorial Guinean', 'Eritrean',
  'Estonian', 'Ethiopian',
  // F
  'Fijian', 'Filipino', 'Finnish', 'French',
  // G
  'Gabonese', 'Gambian', 'Georgian', 'German', 'Ghanaian', 'Greek', 'Grenadian', 'Guatemalan',
  'Guinean', 'Guyanese',
  // H
  'Haitian', 'Honduran', 'Hungarian',
  // I
  'Icelandic', 'Indian', 'Indonesian', 'Iranian', 'Iraqi', 'Irish', 'Israeli', 'Italian',
  'Ivorian',
  // J
  'Jamaican', 'Japanese', 'Jordanian',
  // K
  'Kazakh', 'Kenyan', 'Kiribati', 'Korean', 'Kosovar', 'Kuwaiti', 'Kyrgyz',
  // L
  'Laotian', 'Latvian', 'Lebanese', 'Liberian', 'Libyan', 'Liechtensteiner', 'Lithuanian',
  'Luxembourgish',
  // M
  'Macedonian', 'Malagasy', 'Malawian', 'Malaysian', 'Maldivian', 'Malian', 'Maltese',
  'Marshallese', 'Mauritanian', 'Mauritian', 'Mexican', 'Micronesian', 'Moldovan',
  'Monacan', 'Mongolian', 'Montenegrin', 'Moroccan', 'Mozambican',
  // N
  'Namibian', 'Nauruan', 'Nepalese', 'New Zealander', 'Nicaraguan', 'Nigerian', 'Nigerien',
  'Norwegian',
  // O
  'Omani',
  // P
  'Pakistani', 'Palauan', 'Palestinian', 'Panamanian', 'Papua New Guinean', 'Paraguayan',
  'Peruvian', 'Polish', 'Portuguese',
  // Q
  'Qatari',
  // R
  'Romanian', 'Russian', 'Rwandan',
  // S
  'Saint Lucian', 'Salvadoran', 'Samoan', 'San Marinese', 'Sao Tomean', 'Saudi',
  'Senegalese', 'Serbian', 'Seychellois', 'Sierra Leonean', 'Singaporean', 'Slovak',
  'Slovenian', 'Solomon Islander', 'Somali', 'South African', 'South Sudanese', 'Spanish',
  'Sri Lankan', 'Sudanese', 'Surinamese', 'Swazi', 'Swedish', 'Swiss', 'Syrian',
  // T
  'Taiwanese', 'Tajik', 'Tanzanian', 'Thai', 'Togolese', 'Tongan', 'Trinidadian', 'Tunisian',
  'Turkish', 'Turkmen', 'Tuvaluan',
  // U
  'Ugandan', 'Ukrainian', 'Uruguayan', 'Uzbek',
  // V
  'Vanuatuan', 'Vatican', 'Venezuelan', 'Vietnamese',
  // Y
  'Yemeni',
  // Z
  'Zambian', 'Zimbabwean',
  // Other
  'Other'
];

export function InquiryModal({ isOpen, onClose, tourName }: InquiryModalProps) {
  const { language } = useLanguageStore();
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
  const [phoneCode, setPhoneCode] = useState<{ flag: string; dial: string } | null>(null);
  const [submitted, setSubmitted] = useState(false);

  // Auto-update phone code when nationality changes
  useEffect(() => {
    if (formData.nationality && nationalityPhoneCode[formData.nationality]) {
      setPhoneCode(nationalityPhoneCode[formData.nationality]);
    } else {
      setPhoneCode(null);
    }
  }, [formData.nationality]);

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
- Phone: ${phoneCode ? phoneCode.dial + ' ' : ''}${formData.phone}

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
                <h2 className="text-xl font-bold text-gray-900">{t(inquiryFormT, language, 'enquireNow')}</h2>
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
                    {t(inquiryFormT, language, 'fullName')}<span className="text-red-500">*</span>
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
                    {t(inquiryFormT, language, 'email')}<span className="text-red-500">*</span>
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
                    {t(inquiryFormT, language, 'nationality')}<span className="text-red-500">*</span>
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
                        {nat === 'Select Nationality' ? t(inquiryFormT, language, 'selectNationality') : nat}
                      </option>
                    ))}
                  </select>
                </div>

                {/* Phone */}
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-1">
                    {t(inquiryFormT, language, 'phone')}<span className="text-red-500">*</span>
                  </label>
                  <div className="flex">
                    {phoneCode && (
                      <span className="inline-flex items-center px-2.5 border-2 border-r-0 border-gray-200 rounded-l-lg bg-gray-50 text-sm text-gray-600 whitespace-nowrap select-none gap-1.5">
                        <span className="text-base leading-none">{phoneCode.flag}</span>
                        <span className="font-medium">{phoneCode.dial}</span>
                      </span>
                    )}
                    <input
                      type="tel"
                      name="phone"
                      value={formData.phone}
                      onChange={handleChange}
                      required
                      className={`flex-1 min-w-0 px-4 py-2.5 border-2 border-gray-200 ${phoneCode ? 'rounded-r-lg' : 'rounded-lg'} focus:border-primary-500 focus:ring-0 outline-none transition-colors`}
                    />
                  </div>
                </div>

                {/* Date Range */}
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-gray-700 mb-1">
                      {t(inquiryFormT, language, 'from')}
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
                      {t(inquiryFormT, language, 'to')}
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
                    {t(inquiryFormT, language, 'noAdults')}
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
                    {t(inquiryFormT, language, 'noChildren')}
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
                    {t(inquiryFormT, language, 'noInfants')}
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
                    {t(inquiryFormT, language, 'specialRequests')}
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
                    {t(inquiryFormT, language, 'agreeTerms')}{' '}
                    <a href="/terms" target="_blank" className="text-primary-600 hover:underline">
                      {t(inquiryFormT, language, 'termsAndConditions')}
                    </a>
                  </label>
                </div>

                {/* Submit Button */}
                <button
                  type="submit"
                  disabled={isSubmitting || !formData.agreeTerms}
                  className="w-full py-3 bg-gradient-to-r from-amber-500 to-orange-500 text-white font-semibold rounded-lg hover:from-amber-600 hover:to-orange-600 transition-all disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  {isSubmitting ? t(inquiryFormT, language, 'sending') : submitted ? t(inquiryFormT, language, 'sent') : t(inquiryFormT, language, 'sendBookingInquiry')}
                </button>
              </form>
            </div>
          </motion.div>
        </>
      )}
    </AnimatePresence>
  );
}
