'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import { ArrowLeft, Headphones, CheckCircle, Calendar, Shield, Clock, Award, MessageSquare, Heart } from 'lucide-react';
import { useLanguageStore, Language } from '@/store/languageStore';

const content: Record<Language, {
  title: string;
  subtitle: string;
  intro: string[];
  pillars: {
    title: string;
    items: Array<{
      icon: string;
      title: string;
      description: string;
    }>;
  };
}> = {
  en: {
    title: 'Service Quality & Commitment',
    subtitle: 'Excellence in Every Detail',
    intro: [
      'Our entire operation is built upon an unwavering commitment to service quality, respect, and integrity. We prioritize our travelers\' needs and requirements above all else, dedicating ourselves to delivering exceptional service that honors both your trust and your valuable time. We consider it our fundamental duty not merely to meet your expectations, but to thoughtfully anticipate them—providing effective and insightful solutions at every step.',
      'Our team consists of professional specialists who possess deep, firsthand expertise in every destination we offer. We don\'t just sell trips—we share knowledge and passion. Your dedicated consultant provides personalized tips, insights, and advice tailored to you, transforming a standard itinerary into a seamless, enriching, and deeply personal journey. Driven by a spirit of attentive care and swift response, we are committed to a greater purpose: fulfilling dreams and crafting truly memorable travel experiences.',
    ],
    pillars: {
      title: 'The Pillars of Our Service Excellence',
      items: [
        {
          icon: 'calendar',
          title: 'Ease & Flexibility in Booking',
          description: 'We ensure a smooth, straightforward, and adaptable booking process for all our travel packages, accommodating your preferences and circumstances.',
        },
        {
          icon: 'shield',
          title: 'Responsibility & Service Commitment',
          description: 'We take full ownership of your journey. Our commitment is a promise—from the initial planning to your safe return home—ensuring reliability at every step.',
        },
        {
          icon: 'clock',
          title: 'Promptness & Proactive Support',
          description: 'We prioritize rapid and attentive responses to all your inquiries and needs, valuing your time as our most important resource.',
        },
        {
          icon: 'award',
          title: 'Expert Execution & Tailored Guidance',
          description: 'As the creators and operators of your package, we possess authoritative knowledge. This allows us to offer authentic, insider suggestions and recommendations that elevate your experience.',
        },
        {
          icon: 'message',
          title: 'Grateful for Feedback & Dedicated to Evolution',
          description: 'We receive our travelers\' feedback with genuine gratitude and appreciation. Sharing your experience is a gift that enables us to continuously refine our services and curate even better journeys for the future. Your voice is integral to our cycle of improvement.',
        },
      ],
    },
  },
  es: {
    title: 'Calidad en el Servicio y Compromiso',
    subtitle: 'Excelencia en Cada Detalle',
    intro: [
      'Toda nuestra operación está construida sobre un compromiso inquebrantable con la calidad en el servicio, el respeto y la integridad. Priorizamos las necesidades y exigencias de nuestros viajantes por encima de todo, dedicándonos a ofrecer un servicio excepcional que honra tanto su confianza como su valioso tiempo. Consideramos nuestro deber fundamental no solo atender, sino anticipar ponderadamente sus expectativas — brindando soluciones eficaces y perceptivas en cada etapa.',
      'Nuestro equipo está formado por especialistas profesionales con una profunda experiencia práctica y directa en cada destino que ofrecemos. No solo vendemos viajes — compartimos conocimiento y pasión. Su consultor dedicado proporciona consejos, perspectivas y recomendaciones personalizadas hechas a su medida, transformando un itinerario estándar en un viaje perfecto, enriquecedor y profundamente personal. Guiados por un espíritu de cuidado atento y respuesta rápida, nos comprometemos con un propósito mayor: hacer realidad sueños y crear experiencias de viaje verdaderamente memorables.',
    ],
    pillars: {
      title: 'Los Pilares de Nuestra Excelencia en Servicio',
      items: [
        {
          icon: 'calendar',
          title: 'Facilidad y Flexibilidad en la Reserva',
          description: 'Garantizamos un proceso de reserva tranquilo, directo y adaptable para todos nuestros paquetes, acomodando sus preferencias y circunstancias.',
        },
        {
          icon: 'shield',
          title: 'Responsabilidad y Compromiso con el Servicio',
          description: 'Asumimos total responsabilidad por su travesía. Nuestro compromiso es una promesa — desde la planificación inicial hasta su regreso seguro a casa — asegurando confiabilidad en cada paso.',
        },
        {
          icon: 'clock',
          title: 'Prontitud y Soporte Proactivo',
          description: 'Priorizamos respuestas rápidas y atentas a todas sus consultas y necesidades, valorando su tiempo como nuestro recurso más importante.',
        },
        {
          icon: 'award',
          title: 'Ejecución Especializada y Orientación Personalizada',
          description: 'Como creadores y operadores de su paquete, poseemos conocimiento autorizado. Esto nos permite ofrecer sugerencias y recomendaciones auténticas y privilegiadas que elevan su experiencia.',
        },
        {
          icon: 'message',
          title: 'Gratitud por los Comentarios y Dedicación a la Evolución',
          description: 'Recibimos los comentarios de nuestros viajeros con genuina gratitud y aprecio. Compartir su experiencia es un regalo que nos permite refinar continuamente nuestros servicios y crear viajes aún mejores para el futuro. Su voz es parte fundamental de nuestro ciclo de mejora.',
        },
      ],
    },
  },
  pt: {
    title: 'Qualidade no Atendimento & Compromisso',
    subtitle: 'Excelência em Cada Detalhe',
    intro: [
      'Toda a nossa operação é construída sobre um compromisso inabalável com a qualidade no atendimento, respeito e integridade. Priorizamos as necessidades e exigências de nossos viajantes acima de tudo, dedicando-nos a oferecer um serviço excepcional que honra tanto a sua confiança quanto o seu tempo valioso. Consideramos nosso dever fundamental não apenas atender, mas antecipar ponderadamente suas expectativas — fornecendo soluções eficazes e perceptivas em cada etapa.',
      'Nossa equipe é formada por especialistas profissionais com profunda expertise prática e direta em cada destino que oferecemos. Não vendemos apenas viagens — compartilhamos conhecimento e paixão. Seu consultor dedicado fornece dicas, insights e conselhos personalizados feitos sob medida para você, transformando um itinerário padrão em uma jornada perfeita, enriquecedora e profundamente pessoal. Guiados por um espírito de cuidado atento e resposta rápida, comprometemo-nos com um propósito maior: realizar sonhos e criar experiências de viagem verdadeiramente memoráveis.',
    ],
    pillars: {
      title: 'Os Pilares da Nossa Excelência em Serviço',
      items: [
        {
          icon: 'calendar',
          title: 'Facilidade & Flexibilidade na Reserva',
          description: 'Garantimos um processo de reserva tranquilo, direto e adaptável para todos os nossos pacotes, acomodando suas preferências e circunstâncias.',
        },
        {
          icon: 'shield',
          title: 'Responsabilidade & Compromisso com o Serviço',
          description: 'Assumimos total responsabilidade por sua jornada. Nosso compromisso é uma promessa — desde o planejamento inicial até o seu retorno seguro para casa — assegurando confiabilidade em cada etapa.',
        },
        {
          icon: 'clock',
          title: 'Prontidão & Suporte Proativo',
          description: 'Priorizamos respostas rápidas e atentas a todos os seus questionamentos e necessidades, valorizando seu tempo como nosso recurso mais importante.',
        },
        {
          icon: 'award',
          title: 'Execução Especializada & Orientação Personalizada',
          description: 'Como criadores e operadores do seu pacote, possuímos conhecimento autoritativo. Isso nos permite oferecer sugestões e recomendações autênticas e privilegiadas que elevam sua experiência.',
        },
        {
          icon: 'message',
          title: 'Gratidão pelo Feedback & Dedicação à Evolução',
          description: 'Recebemos o feedback de nossos viajantes com genuína gratidão e apreço. Compartilhar sua experiência é um presente que nos permite refinar continuamente nossos serviços e criar jornadas ainda melhores para o futuro. Sua voz é parte fundamental do nosso ciclo de melhoria.',
        },
      ],
    },
  },
};

const iconMap: Record<string, React.ElementType> = {
  calendar: Calendar,
  shield: Shield,
  clock: Clock,
  award: Award,
  message: MessageSquare,
};

export default function ServiceQualityPage() {
  const { language } = useLanguageStore();
  const t = content[language];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[50vh] min-h-[400px] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-blue-900/90 to-indigo-800/80 z-10" />
        <div
          className="absolute inset-0 bg-cover bg-center"
          style={{ backgroundImage: "url('/images/about-hero.jpg')" }}
        />
        <div className="relative z-20 text-center text-white max-w-4xl mx-auto px-4">
          <motion.div
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            className="mb-4"
          >
            <Headphones className="w-16 h-16 mx-auto text-blue-300" />
          </motion.div>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-blue-200 text-lg mb-2"
          >
            {t.subtitle}
          </motion.p>
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="text-4xl md:text-5xl lg:text-6xl font-display font-bold"
          >
            {t.title}
          </motion.h1>
        </div>
      </section>

      {/* Back Link */}
      <div className="container-custom py-6">
        <Link href="/about" className="inline-flex items-center text-primary-600 hover:text-primary-700 font-medium">
          <ArrowLeft className="w-4 h-4 mr-2" />
          {language === 'en' ? 'Back to About' : language === 'es' ? 'Volver a Nosotros' : 'Voltar para Sobre'}
        </Link>
      </div>

      {/* Intro Section */}
      <section className="py-16 bg-white">
        <div className="container-custom">
          <div className="max-w-4xl mx-auto space-y-6">
            {t.intro.map((paragraph, index) => (
              <motion.p
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                className="text-lg text-gray-700 leading-relaxed"
              >
                {paragraph}
              </motion.p>
            ))}
          </div>
        </div>
      </section>

      {/* Pillars Section */}
      <section className="py-20 bg-gray-50">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-16"
          >
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">{t.pillars.title}</h2>
          </motion.div>

          <div className="max-w-5xl mx-auto">
            <div className="space-y-6">
              {t.pillars.items.map((item, index) => {
                const Icon = iconMap[item.icon] || CheckCircle;
                return (
                  <motion.div
                    key={index}
                    initial={{ opacity: 0, x: index % 2 === 0 ? -30 : 30 }}
                    whileInView={{ opacity: 1, x: 0 }}
                    viewport={{ once: true }}
                    transition={{ delay: index * 0.1 }}
                    className="bg-white rounded-2xl p-8 shadow-lg hover:shadow-xl transition-shadow flex flex-col md:flex-row items-start gap-6"
                  >
                    <div className="w-16 h-16 rounded-2xl bg-gradient-to-br from-primary-500 to-primary-600 flex items-center justify-center flex-shrink-0">
                      <Icon className="w-8 h-8 text-white" />
                    </div>
                    <div>
                      <h3 className="text-xl font-bold text-gray-900 mb-3">{item.title}</h3>
                      <p className="text-gray-600 leading-relaxed">{item.description}</p>
                    </div>
                  </motion.div>
                );
              })}
            </div>
          </div>
        </div>
      </section>

      {/* Quote Section */}
      <section className="py-16 bg-gradient-to-r from-primary-600 to-primary-800 text-white">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="max-w-3xl mx-auto text-center"
          >
            <Heart className="w-12 h-12 mx-auto mb-6 text-red-300" />
            <blockquote className="text-2xl md:text-3xl font-medium italic leading-relaxed">
              {language === 'en'
                ? '"Driven by a spirit of attentive care and swift response, we are committed to a greater purpose: fulfilling dreams and crafting truly memorable travel experiences."'
                : language === 'es'
                  ? '"Guiados por un espíritu de cuidado atento y respuesta rápida, nos comprometemos con un propósito mayor: hacer realidad sueños y crear experiencias de viaje verdaderamente memorables."'
                  : '"Guiados por um espírito de cuidado atento e resposta rápida, comprometemo-nos com um propósito maior: realizar sonhos e criar experiências de viagem verdadeiramente memoráveis."'
              }
            </blockquote>
          </motion.div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 bg-white text-center">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-2xl md:text-3xl font-bold text-gray-900 mb-6">
              {language === 'en' ? 'Experience Our Commitment Firsthand' : language === 'es' ? 'Experimente Nuestro Compromiso de Primera Mano' : 'Experimente Nosso Compromisso em Primeira Mão'}
            </h2>
            <div className="flex flex-wrap justify-center gap-4">
              <Link href="/tours" className="btn btn-primary btn-lg">
                {language === 'en' ? 'Explore Tours' : language === 'es' ? 'Explorar Tours' : 'Explorar Passeios'}
              </Link>
              <Link href="/contact" className="btn btn-outline btn-lg">
                {language === 'en' ? 'Contact Us' : language === 'es' ? 'Contáctenos' : 'Fale Conosco'}
              </Link>
            </div>
          </motion.div>
        </div>
      </section>
    </div>
  );
}
