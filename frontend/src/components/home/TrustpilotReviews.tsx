'use client';

import { useState, useRef, useCallback } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { ExternalLink, Star, ChevronDown, ChevronLeft, ChevronRight, X } from 'lucide-react';
import Image from 'next/image';
import { Swiper, SwiperSlide } from 'swiper/react';
import { Autoplay, Navigation } from 'swiper/modules';
import type { Swiper as SwiperType } from 'swiper';
import { useLanguageStore } from '@/store/languageStore';
import { trustpilotT, t } from '@/lib/translations';

import 'swiper/css';
import 'swiper/css/navigation';

const TRUSTPILOT_URL = 'https://www.trustpilot.com/review/girasoltours.com';

const AVATAR_COLORS = [
  '#00b67a', '#0077b6', '#e85d04', '#7209b7', '#d62828',
  '#2d6a4f', '#4361ee', '#f77f00', '#9b2226', '#3a86a7',
  '#6a4c93', '#588157', '#bc6c25', '#264653', '#e76f51',
  '#2a9d8f', '#023e8a', '#6d6875', '#b5838d', '#e63946',
  '#457b9d', '#1d3557', '#a8dadc', '#f4a261',
];

interface Review {
  name: string;
  rating: number;
  title: string;
  text: string;
  date: string;
  imageUrl?: string;
}

const reviews: Review[] = [
  {
    name: 'Juhee',
    rating: 5,
    title: 'Professional Coordination by Girasol Tour and Exceptional Cruise Staff',
    text: 'I booked a 3-night, 4-day Nile Cruise (December 5\u20138, 2025) through Girasol Tours. The correspondence with the agency was timely and professional, and all information provided prior to the trip was accurate. The Jamila 5 Nile Cruise ship was modest but clean and satisfactory. The menu offered a great variety of international dishes\u2014including beef, chicken, vegetables, and fruit\u2014alongside traditional Egyptian cuisine. Most of all, the true highlight of our journey was the cheerful hospitality and professionalism of the Jamila staff. Thank you all for making us feel so welcome!',
    date: 'Dec 2025',
  },
  {
    name: 'Carlos Alberto Toriani',
    rating: 5,
    title: 'An unforgettable trip.',
    text: 'All tours are very well planned. The Guide is prepared and experienced.',
    date: 'Oct 2025',
    imageUrl: 'https://user-images.trustpilot.com/68f7fd954a804f78fea20604/73x73.png',
  },
  {
    name: 'Cristina Scorza',
    rating: 5,
    title: 'Extraordinario!',
    text: 'Una Experiencia Extraordinaria! Los gu\u00edas excelentes y el trato VIP. Cristina y Germ\u00e1n',
    date: 'Oct 2025',
    imageUrl: 'https://user-images.trustpilot.com/68e2e8b3412e4c77115fa59c/73x73.png',
  },
  {
    name: 'Cliente',
    rating: 5,
    title: 'Experiencia fant\u00e1stica',
    text: 'Vivo em Brasil y estaba buscando una agencia para hacer un viaje para Egipto y Jordania, con otra pareja de amigos uruguayos como nosotros. Buscando en la internet encontr\u00e9 la Girasol Egypt Travel and Tours. Desde el comienzo me pareci\u00f3 una agencia confiable. Trat\u00e9 directamente con Emad que desde el principio se mostr\u00f3 super solicito respondiendo siempre inmediatamente. Consegu\u00ed montar con \u00e9l un viaje personalizado y a mejor precio. En Egipto todo funcion\u00f3 perfectamente a lo planeado. Tuvimos siempre un van a nuestra disposici\u00f3n y un gu\u00eda Sameh que nos acompa\u00f1\u00f3 por todos los viajes. Sam fue excepcional, nos mostr\u00f3 un gran conocimiento de historia y cultura egipcia. Destaco la buena organizaci\u00f3n de la empresa Girasol, la puntualidad de todos los servicios y la calidad humana del personal. Recomiendo fuertemente esta empresa.',
    date: 'Oct 2025',
  },
  {
    name: 'Cristiana Di Fuzio',
    rating: 5,
    title: 'Ci siamo trovati molto bene',
    text: "Ci siamo trovati molto bene con la nostra guida e l'hotel era molto bello. Abbiamo trascorso al Cairo una settimana e la nostra guida ci ha fatto fare un tour bellissimo.",
    date: 'Jun 2025',
    imageUrl: 'https://user-images.trustpilot.com/683dd0cf8a5375f6285aaa8d/73x73.png',
  },
  {
    name: 'Luisa Accietto',
    rating: 5,
    title: 'Puntualit\u00e0 e professionalit\u00e0',
    text: "La settimana scorsa siamo stati in Cairo e grazie alla compagnia Girasol questo viaggio \u00e8 stato bellissimo. Sono stati molto scrupolosi in ogni dettaglio, dalla scelta dell'hotel, situato in una posizione strategica con vista sulle piramidi, alla scelta della guida, che si \u00e8 dimostrato sempre disponibile, gentile e molto preparato.",
    date: 'Jun 2025',
    imageUrl: 'https://user-images.trustpilot.com/683c00184e662d13812cb71c/73x73.png',
  },
  {
    name: 'Angela Petralia',
    rating: 5,
    title: 'Un viaggio speciale',
    text: "Un viaggio speciale organizzato da Tarek Khalifa e l'agenzia Girasol Travel. Dal Cairo in fuoristrada alle Oasi del Deserto Occidentale Egiziano sino a Luxor per rientrare in aeroporto al Cairo. Dieci giorni magnifici dall'ambiente desertico delle magnifiche oasi all'Egitto dei Faraoni. Due viaggi in uno. Ottima guida Mohamed sempre con noi. Le sistemazioni tutte di ottimo livello. Siamo partiti in otto amici e tutti molto soddisfatti con il desiderio di ritornare. Grazie Tarek!",
    date: 'May 2025',
  },
  {
    name: 'Amilton Morais do Sacramento',
    rating: 5,
    title: 'Excelente\u2026',
    text: 'Excelente assist\u00eancia desde a chegada no aeroporto do Cairo, check in nos aeroportos, check in nos hoteis, servi\u00e7o dos hot\u00e9is, transfer, passeios, transporte, motoristas, guias... com destaque para o guia Maher.',
    date: 'Feb 2025',
  },
  {
    name: 'Jeane Da Silva Pantaleao',
    rating: 5,
    title: 'Egypt beyond the pyramids and temples!',
    text: 'Egypt has proven to be an incredible, safe, beautiful destination, with lots of history, culture, art, impeccable cuisine and warm and friendly people. Girasol Egypt travel and tours created an itinerary that provided remarkable, unique and unforgettable experiences. The entire team, from the very first contact, was very professional and attentive. We received all the support and every moment of the trip.',
    date: 'Jan 2025',
    imageUrl: 'https://user-images.trustpilot.com/67953af3b8b55545ba7949d1/73x73.png',
  },
  {
    name: 'Janaina Ferreira',
    rating: 5,
    title: 'Making a dream come true',
    text: 'The trip was an incredible experience, it exceeded expectations. The Girasol Egypt agency was very proactive and gave us the best itinerary. The trip was incredible and unforgettable.',
    date: 'Jan 2025',
  },
  {
    name: 'Jennifer',
    rating: 5,
    title: 'Excellent!!',
    text: 'Excellent!!',
    date: 'Nov 2024',
  },
  {
    name: 'Jumil Ortiz',
    rating: 5,
    title: 'Nuestro guia Sam hizo que nuestra experiencia sea super agradable',
    text: 'Nuestro guia Sam hizo que nuestra experiencia sea super agradable, tiene conocimiento de la historia y nos explicaba en cada templo. 10/10 para nuestro guia!',
    date: 'Nov 2024',
    imageUrl: 'https://user-images.trustpilot.com/672a771b0580f520196e0df2/73x73.png',
  },
  {
    name: 'Diana Santana',
    rating: 5,
    title: 'Excelente experiencia',
    text: 'El gu\u00eda Sam Massoud recomendado al 100%, respetuoso, maneja muy bien la historia de todo Egipto, se nota que le apasiona lo que hace; adicional, es atento y cuida a los turistas. La agencia tiene un itinerario muy organizado, son puntuales con los horarios y se preocupan porque est\u00e9s cuidado. Adicional el representante es muy atento, te buscan y te ayudan hacer las gestiones en los aeropuertos.',
    date: 'Nov 2024',
  },
  {
    name: 'Eduardo Nolla',
    rating: 5,
    title: 'Maher nota 10/10',
    text: 'Maher foi um excelente guia, nos explicou tudo sobre a hist\u00f3ria do Egito, tem forma\u00e7\u00e3o em Hist\u00f3ria e conseguiu traduzir super bem tudo que foi Egito Antigo para a sociedade e civiliza\u00e7\u00e3o atual. Foi super pontual, correto, fala o portugu\u00eas muito bem e nos levou para todos os lugares que pedimos. Excelente experi\u00eancia e dias com ele!',
    date: 'Jun 2024',
    imageUrl: 'https://user-images.trustpilot.com/6661951bb579e15bb4b47d91/73x73.png',
  },
  {
    name: 'Mario',
    rating: 5,
    title: "Serieta', efficienza, affidabilita'",
    text: "Agenzia efficiente e puntuale. Ci si pu\u00f2 fidare nel mandare i soldi in anticipo, Tarek \u00e8 una persona molto seria. Disponibile anche a cambiare il programma durante il viaggio. Le macchine private sempre pulite e abbastanza nuove. Autisti capaci e prudenti. Gli hotel prenotati e la nave sul Nilo si sono rivelati pi\u00f9 che buoni; il cibo scelto sempre all'altezza anche per italiani. Il viaggio \u00e8 andato benissimo e molto ben cadenzato. Guida ben preparata, con un pi\u00f9 che buono italiano.",
    date: 'May 2024',
  },
  {
    name: 'Solange Guedes',
    rating: 5,
    title: 'Our experience with Girasol was just great!',
    text: "Our experience with Girasol company was just great! Since our arrival we were received by Mr Walid who welcomed us at the airport and supported us in all our transfers to the hotels and local flights with all safety and commodity. We were very lucky and pleased to have met such special persons like Mr Walid during our stay in Egypt. Girasol's staff are simply the best!",
    date: 'May 2024',
    imageUrl: 'https://user-images.trustpilot.com/663f38f19aac91270cc525ee/73x73.png',
  },
  {
    name: 'Khaled Khalifa',
    rating: 5,
    title: 'Well organised and incredibly safe',
    text: 'Have just come back from the Nile cruise of Egypt organised by Girasol Travel and Tours. The tour was so enjoyable, well organised, and it was incredibly safe. There was a really good mix of different tourist spots to satisfy most of the group. Would definitely use Girasol Travel and Tours again.',
    date: 'Apr 2024',
    imageUrl: 'https://user-images.trustpilot.com/661bf081fc6ed600122d4f13/73x73.png',
  },
  {
    name: 'Ralf Risser',
    rating: 5,
    title: 'Even better than expected',
    text: 'Seven day cruise on the Nile between Assuan/Abu Simbel and Luxor, including transfers Airport Cairo to hotel, hotel to train in Cairo, train to boat in Luxor et vice versa. A very efficient planning and strict following of the plans. The most impressive aspect was the acting persons: organising agent Nessma, local assistants Waleed and Abdullah, and our fantastic tour guide Taher Mohammed. The boat contracted by the agency Girasol was first class, everything \u2014 room, food, personnel \u2014 extraordinary.',
    date: 'Feb 2024',
  },
  {
    name: 'Malati Rai',
    rating: 4,
    title: 'Visit to Egypt.',
    text: 'This travel seems to be perfect in all sense \u2014 punctuality, vehicle etc. Provision of representatives is a great idea. We met Walid our representative in the airport. For our every travel he was there right on time doing all the formalities up to the extent of filling up immigration form. All 5 Stars to him. Ahmed Abdullah a tour guide was with us in Luxor and Aswan. He could communicate excellently, good English and well versed in his subject. Very nice with good behaviorism. 4 Stars for Ahmed.',
    date: 'Jan 2024',
    imageUrl: 'https://user-images.trustpilot.com/65a8032a49f0e00012a783e3/73x73.png',
  },
  {
    name: 'Maria Claudia Giometti',
    rating: 5,
    title: 'Tivemos uma experi\u00eancia incr\u00edvel!',
    text: 'Tivemos uma experi\u00eancia incr\u00edvel! A viagem foi perfeita. N\u00e3o tivemos nenhum problema, ao contr\u00e1rio, todos os cuidados e detalhes foram tomados para tornar nossa experi\u00eancia \u00fanica. O Emad foi super atencioso todo o tempo. Tivemos atrasos nos voos mas ele conciliou tudo com maestria. Os guias Mohamed(s), o assistente Wallid, o motorista Ramad\u00e3\u2026 J\u00e1 estamos programando o pr\u00f3ximo destino com a Girasol.',
    date: 'Apr 2023',
    imageUrl: 'https://user-images.trustpilot.com/6446b3736ce5cc001294dd03/73x73.png',
  },
  {
    name: 'Zulkiflee Bin Abdul Rahman',
    rating: 5,
    title: 'Thank you Girasol!',
    text: "From the moment we touched down until we left Cairo, Girasol's Mr Emad and his team made sure it was smooth sailing and a memorable vacation for us. Our guides Mr Taha (Cairo) and Mr Hazem (Nile cruise) are very professional, knowledgeable, witty and good company. Mr Walid from Girasol made sure that for our domestic and international departure flights, we were escorted by the airport assistance to help with the procedures. This is what a vacation is meant to be. Hustle free, great company and no worries about admin and logistics. Thank you Girasol!",
    date: 'Dec 2022',
  },
];

// Real Trustpilot stats (not calculated from filtered array)
const totalReviews = 27;
const avgRating = '4.3';

function StarRating({ rating, size = 'sm' }: { rating: number; size?: 'sm' | 'lg' }) {
  const sizeClass = size === 'lg' ? 'w-5 h-5' : 'w-4 h-4';
  return (
    <div className="flex gap-0.5">
      {[1, 2, 3, 4, 5].map((star) => (
        <Star
          key={star}
          className={`${sizeClass} ${
            star <= rating ? 'text-[#00b67a] fill-[#00b67a]' : 'text-gray-300 fill-gray-300'
          }`}
        />
      ))}
    </div>
  );
}

function getInitials(name: string) {
  const parts = name.split(' ');
  if (parts.length === 1) return parts[0].charAt(0).toUpperCase();
  return (parts[0].charAt(0) + parts[parts.length - 1].charAt(0)).toUpperCase();
}

function ReviewCard({ review, index, onReadMore }: { review: Review; index: number; onReadMore: (review: Review, index: number) => void }) {
  const { language } = useLanguageStore();
  const isLong = review.text.length > 150;

  return (
    <div className="bg-white rounded-xl p-6 shadow-sm border border-gray-100 flex flex-col h-full">
      {/* Top: Avatar + Name + Date */}
      <div className="flex items-center gap-3 mb-4 flex-shrink-0">
        {review.imageUrl ? (
          <Image
            src={review.imageUrl}
            alt={review.name}
            width={44}
            height={44}
            className="w-11 h-11 rounded-full object-cover flex-shrink-0"
            unoptimized
          />
        ) : (
          <div
            className="w-11 h-11 rounded-full flex items-center justify-center text-white font-bold text-sm flex-shrink-0"
            style={{ backgroundColor: AVATAR_COLORS[index % AVATAR_COLORS.length] }}
          >
            {getInitials(review.name)}
          </div>
        )}
        <div className="min-w-0">
          <p className="font-semibold text-gray-900 text-sm truncate">{review.name}</p>
          <p className="text-xs text-gray-400">{review.date}</p>
        </div>
      </div>

      {/* Stars */}
      <div className="mb-3 flex-shrink-0">
        <StarRating rating={review.rating} />
      </div>

      {/* Title */}
      <h3 className="font-semibold text-gray-900 text-[15px] mb-2 line-clamp-1 flex-shrink-0">
        {review.title}
      </h3>

      {/* Review text */}
      <div className="flex-grow">
        <p className="text-gray-600 text-sm leading-relaxed line-clamp-4">
          {review.text}
        </p>
        {isLong && (
          <button
            onClick={() => onReadMore(review, index)}
            className="text-[#00b67a] text-xs font-medium mt-2 hover:underline inline-flex items-center gap-0.5"
          >
            Read more <ChevronDown className="w-3 h-3" />
          </button>
        )}
      </div>

      {/* Footer: Verified badge */}
      <div className="mt-4 pt-3 border-t border-gray-100 flex items-center justify-between flex-shrink-0">
        <span className="text-[11px] text-[#00b67a] font-medium flex items-center gap-1">
          <svg viewBox="0 0 16 16" className="w-3.5 h-3.5 fill-[#00b67a]">
            <path d="M8 0l2.2 5.1L16 5.8l-4 3.7 1 5.5L8 12.4 2.9 15l1-5.5-4-3.7 5.9-.7z"/>
          </svg>
          {t(trustpilotT, language, 'verifiedReview')}
        </span>
        <a
          href={TRUSTPILOT_URL}
          target="_blank"
          rel="noopener noreferrer"
          className="text-[11px] text-gray-400 hover:text-[#00b67a] transition-colors"
        >
          Trustpilot
        </a>
      </div>
    </div>
  );
}

function ReviewModal({ review, index, onClose }: { review: Review; index: number; onClose: () => void }) {
  const { language } = useLanguageStore();

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-black/50 backdrop-blur-sm"
      onClick={onClose}
    >
      <motion.div
        initial={{ opacity: 0, scale: 0.95, y: 20 }}
        animate={{ opacity: 1, scale: 1, y: 0 }}
        exit={{ opacity: 0, scale: 0.95, y: 20 }}
        transition={{ duration: 0.2 }}
        className="bg-white rounded-2xl p-6 md:p-8 max-w-lg w-full max-h-[80vh] overflow-y-auto shadow-2xl"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="flex items-center gap-3 mb-5">
          {review.imageUrl ? (
            <Image
              src={review.imageUrl}
              alt={review.name}
              width={52}
              height={52}
              className="w-13 h-13 rounded-full object-cover flex-shrink-0"
              style={{ width: 52, height: 52 }}
              unoptimized
            />
          ) : (
            <div
              className="rounded-full flex items-center justify-center text-white font-bold text-base flex-shrink-0"
              style={{ backgroundColor: AVATAR_COLORS[index % AVATAR_COLORS.length], width: 52, height: 52 }}
            >
              {getInitials(review.name)}
            </div>
          )}
          <div>
            <p className="font-semibold text-gray-900">{review.name}</p>
            <p className="text-sm text-gray-400">{review.date}</p>
          </div>
        </div>

        {/* Stars */}
        <div className="mb-4">
          <StarRating rating={review.rating} size="lg" />
        </div>

        {/* Title */}
        <h3 className="font-bold text-gray-900 text-lg mb-4">
          {review.title}
        </h3>

        {/* Full text */}
        <p className="text-gray-600 text-[15px] leading-relaxed whitespace-pre-line">
          {review.text}
        </p>

        {/* Footer */}
        <div className="mt-6 pt-4 border-t border-gray-100 flex items-center justify-between">
          <span className="text-xs text-[#00b67a] font-medium flex items-center gap-1">
            <svg viewBox="0 0 16 16" className="w-4 h-4 fill-[#00b67a]">
              <path d="M8 0l2.2 5.1L16 5.8l-4 3.7 1 5.5L8 12.4 2.9 15l1-5.5-4-3.7 5.9-.7z"/>
            </svg>
            {t(trustpilotT, language, 'verifiedReview')} — Trustpilot
          </span>
          <button
            onClick={onClose}
            className="text-sm text-gray-500 hover:text-gray-800 font-medium"
          >
            Close
          </button>
        </div>
      </motion.div>
    </motion.div>
  );
}

export function TrustpilotReviews() {
  const { language } = useLanguageStore();
  const swiperRef = useRef<SwiperType | null>(null);
  const [modalReview, setModalReview] = useState<{ review: Review; index: number } | null>(null);

  const handleReadMore = useCallback((review: Review, index: number) => {
    setModalReview({ review, index });
    // Pause autoplay when modal is open
    swiperRef.current?.autoplay?.stop();
  }, []);

  const handleCloseModal = useCallback(() => {
    setModalReview(null);
    swiperRef.current?.autoplay?.start();
  }, []);

  return (
    <section className="section-padding bg-gray-50">
      <div className="container-custom">
        {/* Section Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-10"
        >
          <span className="text-primary-600 font-medium mb-2 block">
            {t(trustpilotT, language, 'whatClientsSay')}
          </span>
          <h2 className="heading-2 text-gray-900 mb-4">
            {t(trustpilotT, language, 'travelerReviews')}
          </h2>

          {/* Overall Rating */}
          <div className="flex flex-wrap items-center justify-center gap-3">
            <div className="flex items-center gap-2">
              <StarRating rating={4} size="lg" />
              <span className="text-2xl font-bold text-gray-900">{avgRating}</span>
            </div>
            <span className="text-gray-500 text-sm">
              {t(trustpilotT, language, 'basedOn')} {totalReviews} {t(trustpilotT, language, 'reviews')}
            </span>
            <a
              href={TRUSTPILOT_URL}
              target="_blank"
              rel="noopener noreferrer"
              className="inline-flex items-center gap-1 text-[#00b67a] font-semibold hover:underline text-sm"
            >
              Trustpilot
              <ExternalLink className="w-3.5 h-3.5" />
            </a>
          </div>
        </motion.div>

        {/* Reviews Carousel */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="relative"
        >
          {/* Custom Navigation Arrows - Desktop only */}
          <button
            onClick={() => swiperRef.current?.slidePrev()}
            className="hidden lg:flex absolute -left-5 top-1/2 -translate-y-1/2 z-10 w-10 h-10 rounded-full bg-white shadow-md border border-gray-200 items-center justify-center hover:bg-gray-50 hover:shadow-lg transition-all"
            aria-label="Previous review"
          >
            <ChevronLeft className="w-5 h-5 text-gray-700" />
          </button>
          <button
            onClick={() => swiperRef.current?.slideNext()}
            className="hidden lg:flex absolute -right-5 top-1/2 -translate-y-1/2 z-10 w-10 h-10 rounded-full bg-white shadow-md border border-gray-200 items-center justify-center hover:bg-gray-50 hover:shadow-lg transition-all"
            aria-label="Next review"
          >
            <ChevronRight className="w-5 h-5 text-gray-700" />
          </button>

          <Swiper
            modules={[Autoplay, Navigation]}
            onSwiper={(swiper) => { swiperRef.current = swiper; }}
            spaceBetween={24}
            slidesPerView={1}
            loop={true}
            grabCursor={true}
            autoplay={{ delay: 4000, disableOnInteraction: false, pauseOnMouseEnter: true }}
            breakpoints={{
              640: { slidesPerView: 2 },
              1024: { slidesPerView: 3 },
            }}
            className="pb-4 [&_.swiper-slide]:!h-auto"
          >
            {reviews.map((review, index) => (
              <SwiperSlide key={index}>
                <ReviewCard review={review} index={index} onReadMore={handleReadMore} />
              </SwiperSlide>
            ))}
          </Swiper>
        </motion.div>

      </div>

      {/* Review Modal */}
      <AnimatePresence>
        {modalReview && (
          <ReviewModal
            review={modalReview.review}
            index={modalReview.index}
            onClose={handleCloseModal}
          />
        )}
      </AnimatePresence>
    </section>
  );
}
