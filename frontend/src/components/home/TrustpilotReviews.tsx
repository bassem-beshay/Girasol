"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Star, ChevronLeft, ChevronRight, ExternalLink, Quote } from "lucide-react";
import Image from "next/image";

const TRUSTPILOT_URL = "https://www.trustpilot.com/review/girasoltours.com";

const reviews = [
  {
    name: "Juhee",
    rating: 5,
    title: "Professional Coordination & Exceptional Cruise Staff",
    text: "The agency showed great professionalism throughout our 4-Day Nile Journey. The cruise staff were incredibly hospitable, with diverse international and Egyptian cuisine. Truly a wonderful experience!",
    date: "Dec 2025",
    color: "bg-rose-500",
    image: "",
  },
  {
    name: "Carlos Alberto Toriani",
    rating: 5,
    title: "An unforgettable trip",
    text: "All tours are very well planned. The Guide is prepared and experienced. Everything was perfectly organized from start to finish.",
    date: "Oct 2025",
    color: "bg-blue-500",
    image: "https://user-images.trustpilot.com/68f7fd954a804f78fea20604/73x73.png",
  },
  {
    name: "Jeane Da Silva Pantaleao",
    rating: 5,
    title: "Egypt beyond the pyramids and temples!",
    text: "Egypt is incredible! The professional team supported us throughout the entire journey with a remarkable itinerary and unique experiences.",
    date: "Jan 2025",
    color: "bg-purple-500",
    image: "https://user-images.trustpilot.com/67953af3b8b55545ba7949d1/73x73.png",
  },
  {
    name: "Janaina Ferreira",
    rating: 5,
    title: "Making a dream come true",
    text: "The trip exceeded all expectations with proactive agency support and excellent itinerary planning. A truly life-changing experience in Egypt!",
    date: "Jan 2025",
    color: "bg-teal-500",
    image: "",
  },
  {
    name: "Jennifer",
    rating: 5,
    title: "Excellent!!",
    text: "Amazing experience from start to finish. The team made our Egyptian adventure truly special and unforgettable. Highly recommended!",
    date: "Nov 2024",
    color: "bg-pink-500",
    image: "",
  },
  {
    name: "Solange Guedes",
    rating: 5,
    title: "Simply the best!",
    text: "Our experience with Girasol was wonderful. Mr. Walid's airport reception was great, and the staff quality was simply the best throughout our entire stay!",
    date: "May 2024",
    color: "bg-amber-500",
    image: "https://user-images.trustpilot.com/663f38f19aac91270cc525ee/73x73.png",
  },
  {
    name: "Khaled Khalifa",
    rating: 5,
    title: "An amazing Nile cruise experience",
    text: "The Nile cruise was so enjoyable, well organised and incredibly safe. A good mix of tourist locations. Would definitely use Girasol again!",
    date: "Apr 2024",
    color: "bg-emerald-500",
    image: "https://user-images.trustpilot.com/661bf081fc6ed600122d4f13/73x73.png",
  },
  {
    name: "Ralf Risser",
    rating: 5,
    title: "Even better than expected",
    text: "Seven-day cruise with very efficient planning and first class boat quality. Our guide Taher Mohammed was incredibly knowledgeable. Organizer Nessma and assistants were excellent.",
    date: "Feb 2024",
    color: "bg-indigo-500",
    image: "",
  },
  {
    name: "Malati Rai",
    rating: 4,
    title: "Great visit to Egypt",
    text: "Appreciated the punctuality and representative Walid's five-star assistance with airport formalities. Tour guide Ahmed Abdullah had excellent communication and knowledge.",
    date: "Jan 2024",
    color: "bg-cyan-500",
    image: "https://user-images.trustpilot.com/65a8032a49f0e00012a783e3/73x73.png",
  },
  {
    name: "Maria Claudia Giometti",
    rating: 5,
    title: "We had an incredible experience!",
    text: "A perfect trip with no problems. Emad was very attentive and handled flight delays skillfully. Guides Mohamed, assistant Walid and driver were all exceptional. Already planning our next trip!",
    date: "Apr 2023",
    color: "bg-violet-500",
    image: "https://user-images.trustpilot.com/6446b3736ce5cc001294dd03/73x73.png",
  },
  {
    name: "Zulkiflee Bin Abdul Rahman",
    rating: 5,
    title: "Thank you Girasol!",
    text: "Emad responded quickly and called personally to customize our trip. Guides Taha and Hazem were professional, knowledgeable and great company. A hustle-free memorable experience!",
    date: "Dec 2022",
    color: "bg-sky-500",
    image: "",
  },
  {
    name: "Cristina Scorza",
    rating: 5,
    title: "Extraordinary!",
    text: "An extraordinary experience in Egypt. Everything was perfectly organized and the team went above and beyond to make our trip unforgettable.",
    date: "2023",
    color: "bg-fuchsia-500",
    image: "",
  },
  {
    name: "Cristiana Di Fuzio",
    rating: 5,
    title: "We had a great time!",
    text: "We had a great time with Girasol. Everything was well organized, the guides were knowledgeable, and the whole trip was smooth and enjoyable.",
    date: "2023",
    color: "bg-orange-500",
    image: "",
  },
  {
    name: "Luisa Accietto",
    rating: 5,
    title: "Punctuality and professionalism",
    text: "Outstanding punctuality and professionalism throughout our entire Egyptian journey. Every detail was taken care of perfectly.",
    date: "2023",
    color: "bg-lime-600",
    image: "",
  },
  {
    name: "Angela Petralia",
    rating: 5,
    title: "A special journey",
    text: "A truly special journey through Egypt. The team made everything seamless and the experience was beyond our expectations.",
    date: "2023",
    color: "bg-red-500",
    image: "",
  },
  {
    name: "Amilton Morais",
    rating: 5,
    title: "Excellent!",
    text: "Excellent service from start to finish. Girasol made our Egyptian dream come true with impeccable organization and wonderful guides.",
    date: "2023",
    color: "bg-blue-600",
    image: "",
  },
  {
    name: "Diana Santana",
    rating: 5,
    title: "Excellent experience",
    text: "An excellent experience traveling with Girasol. Professional team, great itinerary, and unforgettable memories in Egypt!",
    date: "2023",
    color: "bg-green-500",
    image: "",
  },
  {
    name: "Eduardo Nolla",
    rating: 5,
    title: "Maher 10 out of 10!",
    text: "Our guide Maher was absolutely outstanding - 10 out of 10! The whole trip was perfectly organized and we had the time of our lives.",
    date: "2023",
    color: "bg-yellow-600",
    image: "",
  },
  {
    name: "Mario",
    rating: 5,
    title: "Reliability and efficiency",
    text: "Girasol showed great reliability and efficiency throughout our trip. Professional service with attention to every detail. Highly recommended!",
    date: "2023",
    color: "bg-slate-500",
    image: "",
  },
];

function StarRating({ rating }: { rating: number }) {
  return (
    <div className="flex gap-0.5">
      {[1, 2, 3, 4, 5].map((i) => (
        <div
          key={i}
          className={`w-5 h-5 flex items-center justify-center ${
            i <= rating ? "bg-[#00b67a]" : "bg-[#dcdce6]"
          }`}
        >
          <Star className="w-3 h-3 text-white fill-white" />
        </div>
      ))}
    </div>
  );
}

export function TrustpilotReviews() {
  const [currentIndex, setCurrentIndex] = useState(0);
  const reviewsPerPage = typeof window !== "undefined" && window.innerWidth < 768 ? 1 : 3;
  const totalPages = Math.ceil(reviews.length / reviewsPerPage);

  const next = () => setCurrentIndex((prev) => (prev + 1) % totalPages);
  const prev = () => setCurrentIndex((prev) => (prev - 1 + totalPages) % totalPages);

  const visibleReviews = reviews.slice(
    currentIndex * reviewsPerPage,
    currentIndex * reviewsPerPage + reviewsPerPage
  );

  return (
    <section className="section-padding bg-gray-50">
      <div className="container-custom">
        {/* Header */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          className="text-center mb-12"
        >
          <span className="text-primary-600 font-medium mb-2 block">
            What Our Travelers Say
          </span>
          <h2 className="heading-2 text-gray-900 mb-4">
            Trusted by Travelers Worldwide
          </h2>

          {/* Trustpilot Summary */}
          <div className="flex items-center justify-center gap-3 flex-wrap">
            <div className="flex items-center gap-2">
              <svg viewBox="0 0 24 24" className="w-7 h-7" fill="#00b67a">
                <path d="M12 0L15.09 8.26L24 9.27L17.45 14.14L19.18 22.9L12 18.77L4.82 22.9L6.55 14.14L0 9.27L8.91 8.26L12 0Z" />
              </svg>
              <span className="text-xl font-bold text-gray-900">Trustpilot</span>
            </div>
            <div className="flex items-center gap-2">
              <div className="flex gap-0.5">
                {[1, 2, 3, 4].map((i) => (
                  <div key={i} className="w-7 h-7 bg-[#00b67a] flex items-center justify-center">
                    <Star className="w-4 h-4 text-white fill-white" />
                  </div>
                ))}
                <div className="w-7 h-7 bg-[#73cf11] flex items-center justify-center">
                  <Star className="w-4 h-4 text-white fill-white" />
                </div>
              </div>
              <span className="text-gray-600 font-medium">4.2 / 5</span>
              <span className="text-gray-400">|</span>
              <span className="text-gray-600">26 reviews</span>
            </div>
          </div>
        </motion.div>

        {/* Reviews Carousel */}
        <div className="relative">
          <div className="grid md:grid-cols-3 gap-6 ">
            <AnimatePresence mode="wait">
              {visibleReviews.map((review, idx) => (
                <motion.div
                  key={`${currentIndex}-${idx}`}
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  exit={{ opacity: 0, y: -20 }}
                  transition={{ duration: 0.3, delay: idx * 0.1 }}
                  className="bg-white rounded-2xl p-6 shadow-md hover:shadow-lg transition-shadow relative flex flex-col"
                >
                  <Quote className="absolute top-4 right-4 w-8 h-8 text-gray-100" />

                  <StarRating rating={review.rating} />

                  <h3 className="font-bold text-gray-900 mt-3 mb-2 text-[15px]">
                    {review.title}
                  </h3>

                  <p className="text-gray-600 text-sm leading-relaxed mb-4 flex-1">
                    &ldquo;{review.text}&rdquo;
                  </p>

                  <div className="flex items-center justify-between pt-4 border-t border-gray-100">
                    <div className="flex items-center gap-2.5">
                      {review.image ? (
                        <Image
                          src={review.image}
                          alt={review.name}
                          width={36}
                          height={36}
                          className="w-9 h-9 rounded-full object-cover shadow-sm"
                          unoptimized
                        />
                      ) : (
                        <div className={`w-9 h-9 rounded-full ${review.color} flex items-center justify-center shadow-sm`}>
                          <span className="text-white font-bold text-sm">
                            {review.name.charAt(0)}
                          </span>
                        </div>
                      )}
                      <span className="font-medium text-gray-900 text-sm">{review.name}</span>
                    </div>
                    <span className="text-xs text-gray-400">{review.date}</span>
                  </div>
                </motion.div>
              ))}
            </AnimatePresence>
          </div>

          {/* Navigation */}
          <div className="flex items-center justify-center gap-4 mt-8">
            <button
              onClick={prev}
              className="w-10 h-10 rounded-full bg-white shadow-md flex items-center justify-center hover:bg-gray-50 transition-colors"
              aria-label="Previous reviews"
            >
              <ChevronLeft className="w-5 h-5 text-gray-600" />
            </button>

            <div className="flex gap-1.5">
              {Array.from({ length: totalPages }).map((_, i) => (
                <button
                  key={i}
                  onClick={() => setCurrentIndex(i)}
                  className={`h-2.5 rounded-full transition-all ${
                    i === currentIndex
                      ? "bg-[#00b67a] w-6"
                      : "bg-gray-300 hover:bg-gray-400 w-2.5"
                  }`}
                  aria-label={`Page ${i + 1}`}
                />
              ))}
            </div>

            <button
              onClick={next}
              className="w-10 h-10 rounded-full bg-white shadow-md flex items-center justify-center hover:bg-gray-50 transition-colors"
              aria-label="Next reviews"
            >
              <ChevronRight className="w-5 h-5 text-gray-600" />
            </button>
          </div>
        </div>

        {/* CTA */}
        <div className="text-center mt-10">
          <a
            href={TRUSTPILOT_URL}
            target="_blank"
            rel="noopener noreferrer"
            className="inline-flex items-center gap-2 bg-[#00b67a] hover:bg-[#00a06a] text-white px-6 py-3 rounded-xl font-semibold transition-colors"
          >
            <Star className="w-4 h-4 fill-current" />
            See All Reviews on Trustpilot
            <ExternalLink className="w-4 h-4" />
          </a>
        </div>
      </div>
    </section>
  );
}
