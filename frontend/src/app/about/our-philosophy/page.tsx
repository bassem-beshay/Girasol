'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import { ArrowLeft, Heart, Shield, Crown, Gift, CreditCard, Compass, Wifi, Leaf, MessageCircle, Users, Star, CheckCircle } from 'lucide-react';
import { useLanguageStore, Language } from '@/store/languageStore';

const content: Record<Language, {
  title: string;
  subtitle: string;
  intro: string;
  values: Array<{ title: string; description: string }>;
  vision: {
    title: string;
    subtitle: string;
    description: string;
    legacy: string;
    logo: string;
  };
  standard: {
    title: string;
    subtitle: string;
    sections: Array<{
      icon: string;
      title: string;
      points: string[];
    }>;
  };
  feedback: {
    title: string;
    subtitle: string;
    intro: string;
    points: string[];
  };
}> = {
  en: {
    title: 'Our Philosophy',
    subtitle: 'Love & Care',
    intro: 'Our Philosophy in Girasol Egypt Travel is, in essence, Love & Care – the cornerstone that has guided every decision in Egyptian and combined tourism for 31 years. We cultivate a culture of unbreakable ethics, social consciousness, and sacred respect, where untouchable values shape our excellence:',
    values: [
      { title: 'Multicultural Wisdom', description: 'Our Egyptian and Brazilian directors and specialists fuse ancestral knowledge with a contemporary vision, mastering every technical detail with unique sensitivity.' },
      { title: 'Respect that Personalizes', description: 'We honor individual culture, tastes, and customs, creating unique solutions for every traveler profile.' },
      { title: 'Satisfaction as a Mission', description: 'We permanently prioritize the happiness and comfort of our clients and passengers, transforming expectations into reality.' },
      { title: 'Operational Excellence', description: 'We apply maximum standards of agility, care, and perfection in all services, from planning to post-trip.' },
      { title: 'Conscious Credibility', description: 'We align profitability, professional success, and ethics to build lasting partnerships and solid growth.' },
      { title: 'Innovation with Roots', description: 'We grow in harmony with the global community through agile management that preserves Egyptian traditions.' },
      { title: 'Sustainable Legacy', description: 'We actively contribute to local communities and environmental preservation – every trip supports social projects in Egypt.' },
      { title: 'Welcoming Environment', description: 'We guarantee dignified treatment and mutual respect among our team and collaborators – because incredible journeys are born from inspired teams.' },
    ],
    vision: {
      title: 'Soul & Zeal',
      subtitle: 'A Vision Born from 31 Years of Passion for Egypt',
      description: 'Our Vision is to elevate your journey to Egypt into an unforgettable and deeply rich experience, guided by our unique principle of Soul & Zeal. With 31 years of expertise in Egyptian tourism and combined itineraries, we create adapted journeys where premium safety and exceptional quality unveil millennia-old stories with absolute comfort.',
      legacy: 'Our legacy? 31 years of passion for Egypt, materialized in every journey of our travelers.',
      logo: 'Our logo? Maat seated with open wings—mythologically, the goddess who symbolizes justice and the cosmic force to maintain universal balance with truth, discipline, harmony, and justice.',
    },
    standard: {
      title: 'The LOVE & CARE Standard',
      subtitle: 'Our living promise: an ecosystem of exclusive benefits that transforms your journey in Egypt into a peerless experience.',
      sections: [
        {
          icon: 'shield',
          title: 'Unbreakable Commitment',
          points: [
            'Triple-service guarantee of integral responsibility',
            'Certified quality and radical transparency',
            'Clear contracts and audited operations',
            'Immediate solutions for any unforeseen event',
          ],
        },
        {
          icon: 'crown',
          title: 'Personal Management by Directors',
          points: [
            'Egyptian-Brazilian specialists treat your itinerary as a masterpiece',
            'Cultural sensitivity and logistical precision',
            'Personalized details from visiting hours to restaurants with Nile views',
          ],
        },
        {
          icon: 'gift',
          title: 'Benefits Beyond the Journey',
          points: [
            '5-10% discount on future travels',
            'Specific discounts on international flights (EgyptAir partnership)',
            'Up to 10% discount on Egyptian domestic flights',
            'Possible surprising upgrades (Hotels 4★ → 5★, Cruises 5★ → 5★ Deluxe)',
            'VIP Courtesies: Complimentary visa, private transfers, exclusive events',
          ],
        },
        {
          icon: 'credit',
          title: 'Financial Flexibility',
          points: [
            'Installments in up to 5x via credit card',
            'Extended payment plan up to 4x via secure links',
            'Special discount for full payment in US$',
            'Special conditions on combined packages',
          ],
        },
        {
          icon: 'compass',
          title: '360° Consultancy',
          points: [
            'Personalized pre-trip guidance (climate checklist, cultural etiquette)',
            'Dedicated support throughout your journey via WhatsApp',
            'Post-trip experience analysis + tips for your next adventure',
          ],
        },
        {
          icon: 'wifi',
          title: 'Uninterrupted Connectivity',
          points: [
            '24/7 support in Portuguese via WhatsApp, Telegram, and direct line',
            'From medical emergencies to café recommendations in Cairo',
            'We resolve any challenge within 2 hours, wherever you are',
          ],
        },
        {
          icon: 'leaf',
          title: 'A Legacy that Regenerates',
          points: [
            'Support social actions in Cairo',
            'Resources to local orphanages and underprivileged students',
            'Contributions to hospitals serving vulnerable communities',
            'Real help needs no publicity, only consistent action',
          ],
        },
      ],
    },
    feedback: {
      title: 'Reviews & Feedback',
      subtitle: 'The Voice that Reigns Our Excellence',
      intro: 'Your opinion is not just welcome – it is essential. By sharing real experiences, you shape the future of thousands of journeys and strengthen social projects in Egypt.',
      points: [
        'We transform critiques into practical improvements: routes, safety, and experiences.',
        'Evaluate through multiple channels (online, Trustpilot, email, or in-person meetings).',
        'Earn 5% OFF your next trip by sharing your journey.',
        'See real changes in our quarterly "Evolution Report."',
      ],
    },
  },
  es: {
    title: 'Nuestra Filosofía',
    subtitle: 'Amor y Cuidado',
    intro: 'Nuestra Filosofía en Girasol Egypt Travel es, en esencia, Amor y Cuidado – la piedra angular que ha guiado cada decisión en el turismo egipcio y combinado a lo largo de 31 años. Cultivamos una cultura de ética inquebrantable, conciencia social y respeto sagrado, donde valores intocables moldean nuestra excelencia:',
    values: [
      { title: 'Sabiduría Multicultural', description: 'Nuestros directores y especialistas egipcios y brasileños fusionan conocimiento ancestral con una visión contemporánea, dominando cada detalle técnico con sensibilidad única.' },
      { title: 'Respeto que Personaliza', description: 'Honramos la cultura, los gustos y las costumbres individuales, creando soluciones únicas para cada perfil de viajero.' },
      { title: 'Satisfacción como Misión', description: 'Priorizamos permanentemente la felicidad y la comodidad de nuestros clientes y pasajeros, transformando expectativas en realidad.' },
      { title: 'Excelencia Operacional', description: 'Aplicamos estándares máximos de agilidad, cuidado y perfección en todos los servicios, desde la planificación hasta el post-viaje.' },
      { title: 'Credibilidad Consciente', description: 'Alineamos rentabilidad, éxito profesional y ética para construir alianzas duraderas y un crecimiento sólido.' },
      { title: 'Innovación con Raíces', description: 'Crecemos en armonía con la comunidad global mediante una gestión ágil que preserva las tradiciones egipcias.' },
      { title: 'Legado Sostenible', description: 'Contribuimos activamente a las comunidades locales y a la preservación ambiental – cada viaje apoya proyectos sociales en Egipto.' },
      { title: 'Ambiente Acogedor', description: 'Garantizamos un tratamiento digno y respeto mutuo entre nuestro equipo y colaboradores – porque los viajes increíbles nacen de equipos inspirados.' },
    ],
    vision: {
      title: 'Alma y Brío',
      subtitle: 'Una Visión Nacida de 31 Años de Pasión por Egipto',
      description: 'Nuestra Visión es elevar su viaje a Egipto a una experiencia inolvidable y profundamente enriquecedora, guiada por nuestro principio único de Alma y Brío. Con 31 años de experiencia en turismo egipcio e itinerarios combinados, creamos travesías adaptadas donde la seguridad premium y una calidad excepcional desvelan historias milenarias con confort absoluto.',
      legacy: '¿Nuestro legado? 31 años de pasión por Egipto, materializados en cada travesía de nuestros viajeros.',
      logo: '¿Nuestro logo? Maat sentada con las alas abiertas — mitológicamente, la diosa que simboliza la justicia y la fuerza cósmica para mantener el equilibrio universal con verdad, disciplina, armonía y justicia.',
    },
    standard: {
      title: 'El Estándar AMOR y CUIDADO',
      subtitle: 'Nuestra promesa viva: un ecosistema de beneficios exclusivos que transforma su viaje en Egipto en una experiencia sin igual.',
      sections: [
        {
          icon: 'shield',
          title: 'Compromiso Inquebrantable',
          points: [
            'Garantía triple de responsabilidad integral',
            'Calidad certificada y transparencia radical',
            'Contratos claros y operaciones auditadas',
            'Solución inmediata para cualquier imprevisto',
          ],
        },
        {
          icon: 'crown',
          title: 'Gestión Personal por Directores',
          points: [
            'Especialistas egipcio-brasileños tratan su itinerario como una obra maestra',
            'Sensibilidad cultural y precisión logística',
            'Detalles personalizados desde horarios de visitas hasta restaurantes con vista al Nilo',
          ],
        },
        {
          icon: 'gift',
          title: 'Ventajas Más Allá del Viaje',
          points: [
            '5-10% de descuento en viajes futuros',
            'Descuentos específicos en pasajes internacionales (alianza con EgyptAir)',
            'Hasta 10% de descuento en vuelos domésticos egipcios',
            'Posibles mejoras sorprendentes (Hoteles 4★ → 5★, Cruceros 5★ → 5★ Deluxe)',
            'Cortesías VIP: Visado gratuito, transfers privados, eventos exclusivos',
          ],
        },
        {
          icon: 'credit',
          title: 'Flexibilidad Financiera',
          points: [
            'Pagos a plazos en hasta 5 cuotas con tarjeta de crédito',
            'Plan de pago extendido hasta 4 cuotas mediante enlaces seguros',
            'Descuento especial por pago completo en US$',
            'Condiciones especiales para paquetes combinados',
          ],
        },
        {
          icon: 'compass',
          title: 'Asesoría 360°',
          points: [
            'Orientación personalizada previa al viaje (lista climática, etiqueta cultural)',
            'Soporte dedicado durante todo el recorrido vía WhatsApp',
            'Análisis post-viaje de la experiencia + consejos para su próxima aventura',
          ],
        },
        {
          icon: 'wifi',
          title: 'Conectividad Ininterrumpida',
          points: [
            'Atención 24/7 en portugués vía WhatsApp, Telegram y línea directa',
            'Desde emergencias médicas hasta recomendaciones de cafés en El Cairo',
            'Resolvemos cualquier desafío en hasta 2 horas, dondequiera que esté',
          ],
        },
        {
          icon: 'leaf',
          title: 'Un Legado que Regenera',
          points: [
            'Apoyo a acciones sociales en El Cairo',
            'Recursos a orfanatos locales y estudiantes de comunidades necesitadas',
            'Contribuciones a hospitales que atienden comunidades vulnerables',
            'La ayuda real no necesita publicidad, solo acción consistente',
          ],
        },
      ],
    },
    feedback: {
      title: 'Evaluaciones y Retroalimentación',
      subtitle: 'La Voz que Rige Nuestra Excelencia',
      intro: 'Su opinión no es solo bienvenida – es esencial. Al compartir experiencias reales, usted moldea el futuro de miles de viajes y fortalece proyectos sociales en Egipto.',
      points: [
        'Transformamos críticas en mejoras prácticas: rutas, seguridad y experiencias.',
        'Evalúe a través de múltiples canales (en línea, Trustpilot, correo electrónico o encuentros presenciales).',
        'Gane 5% DE DESCUENTO en su próximo viaje al compartir su travesía.',
        'Vea cambios reales en nuestro "Informe de Evolución" trimestral.',
      ],
    },
  },
  pt: {
    title: 'Nossa Filosofia',
    subtitle: 'Amor & Cuidado',
    intro: 'Nossa Filosofia na Girasol Egypt Travel é, em essência, Amor & Cuidado – a pedra angular que tem guiado cada decisão no turismo egípcio e combinado ao longo de 31 anos. Cultivamos uma cultura de ética inquebrantável, consciência social e respeito sagrado, onde valores intocáveis moldam nossa excelência:',
    values: [
      { title: 'Sabedoria Multicultural', description: 'Nossos diretores e especialistas egípcios e brasileiros fundem conhecimento ancestral a uma visão contemporânea, dominando cada detalhe técnico com sensibilidade única.' },
      { title: 'Respeito que Personaliza', description: 'Honramos a cultura, os gostos e os costumes individuais, criando soluções únicas para cada perfil de viajante.' },
      { title: 'Satisfação como Missão', description: 'Priorizamos permanentemente a felicidade e o conforto de nossos clientes e passageiros, transformando expectativas em realidade.' },
      { title: 'Excelência Operacional', description: 'Aplicamos padrões máximos de agilidade, cuidado e perfeição em todos os serviços, desde o planejamento até o pós-viagem.' },
      { title: 'Credibilidade Consciente', description: 'Alinhamos rentabilidade, sucesso profissional e ética para construir parcerias duradouras e um crescimento sólido.' },
      { title: 'Inovação com Raízes', description: 'Crescemos em harmonia com a comunidade global por meio de uma gestão ágil que preserva as tradições egípcias.' },
      { title: 'Legado Sustentável', description: 'Contribuímos ativamente para as comunidades locais e a preservação ambiental – cada viagem apoia projetos sociais no Egito.' },
      { title: 'Ambiente Acolhedor', description: 'Garantimos tratamento digno e respeito mútuo entre nossa equipe e colaboradores – porque jornadas incríveis nascem de times inspirados.' },
    ],
    vision: {
      title: 'Alma & Zelo',
      subtitle: 'Uma Visão Nascida de 31 Anos de Paixão pelo Egito',
      description: 'Nossa Visão é elevar sua jornada ao Egito a uma experiência inesquecível e profundamente rica, guiada por nosso princípio único de Alma & Zelo. Com 31 anos de expertise em turismo egípcio e roteiros combinados, criamos jornadas adaptadas onde segurança premium e qualidade excepcional desvendam histórias milenares com conforto absoluto.',
      legacy: 'Nosso legado? 31 anos de paixão pelo Egito, materializados em cada jornada de nossos viajantes.',
      logo: 'Nosso logo? Maat sentada com asas abertas — mitologicamente, a deusa que simboliza a justiça e a força cósmica para manter o equilíbrio universal com verdade, disciplina, harmonia e justiça.',
    },
    standard: {
      title: 'O Padrão AMOR & CUIDADO',
      subtitle: 'Nossa promessa viva: um ecossistema de benefícios exclusivos que transforma sua jornada no Egito em uma experiência sem igual.',
      sections: [
        {
          icon: 'shield',
          title: 'Compromisso Inquebrantável',
          points: [
            'Garantia tripla de responsabilidade integral',
            'Qualidade certificada e transparência radical',
            'Contratos claros e operações auditadas',
            'Solução imediata para qualquer imprevisto',
          ],
        },
        {
          icon: 'crown',
          title: 'Gestão Pessoal por Diretores',
          points: [
            'Especialistas egípcio-brasileiros tratam seu roteiro como uma obra-prima',
            'Sensibilidade cultural e precisão logística',
            'Detalhes personalizados de horários de visitas a restaurantes com vista para o Nilo',
          ],
        },
        {
          icon: 'gift',
          title: 'Vantagens Além da Viagem',
          points: [
            '5-10% de desconto em futuras viagens',
            'Descontos específicos em passagens internacionais (parceria EgyptAir)',
            'Até 10% de desconto em voos domésticos egípcios',
            'Possíveis upgrades surpreendentes (Hotéis 4★ → 5★, Cruzeiros 5★ → 5★ Deluxe)',
            'Cortesias VIP: Visto gratuito, transfers privativos, eventos exclusivos',
          ],
        },
        {
          icon: 'credit',
          title: 'Flexibilidade Financeira',
          points: [
            'Parcelamento em até 5x via cartão de crédito',
            'Plano de pagamento estendido até 4x via links seguros',
            'Desconto especial para pagamento integral em US$',
            'Condições especiais para pacotes combinados',
          ],
        },
        {
          icon: 'compass',
          title: 'Consultoria 360°',
          points: [
            'Orientação personalizada pré-viagem (checklist climático, etiqueta cultural)',
            'Suporte dedicado durante todo o percurso via WhatsApp',
            'Análise pós-viagem da experiência + dicas para sua próxima aventura',
          ],
        },
        {
          icon: 'wifi',
          title: 'Conectividade Ininterrupta',
          points: [
            'Atendimento 24h em português via WhatsApp, Telegram e linha direta',
            'Desde emergências médicas até recomendações de cafés no Cairo',
            'Resolvemos qualquer desafio em até 2 horas, onde quer que você esteja',
          ],
        },
        {
          icon: 'leaf',
          title: 'Um Legado que Regenera',
          points: [
            'Apoio a ações sociais no Cairo',
            'Recursos a orfanatos locais e estudantes de comunidades carentes',
            'Contribuições com hospitais que atendem comunidades vulneráveis',
            'Ajuda real não precisa de publicidade, apenas de ação consistente',
          ],
        },
      ],
    },
    feedback: {
      title: 'Avaliações & Feedback',
      subtitle: 'A Voz que Reina Nossa Excelência',
      intro: 'Sua opinião não é apenas bem-vinda – é essencial. Ao compartilhar experiências reais, você molda o futuro de milhares de jornadas e fortalece projetos sociais no Egito.',
      points: [
        'Transformamos críticas em melhorias práticas: rotas, segurança e experiências.',
        'Avalie por múltiplos canais (online, Trustpilot, e-mail ou encontros presenciais).',
        'Ganhe 5% DE DESCONTO na próxima viagem ao compartilhar sua jornada.',
        'Veja mudanças reais em nosso "Relatório de Evolução" trimestral.',
      ],
    },
  },
};

const iconMap: Record<string, React.ElementType> = {
  shield: Shield,
  crown: Crown,
  gift: Gift,
  credit: CreditCard,
  compass: Compass,
  wifi: Wifi,
  leaf: Leaf,
};

export default function OurPhilosophyPage() {
  const { language } = useLanguageStore();
  const t = content[language];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[50vh] min-h-[400px] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-red-900/90 to-orange-800/80 z-10" />
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
            <Heart className="w-16 h-16 mx-auto text-red-300" />
          </motion.div>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-red-200 text-lg mb-2"
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

      {/* Intro */}
      <section className="py-12 bg-white">
        <div className="container-custom">
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-lg text-gray-700 max-w-4xl mx-auto text-center leading-relaxed"
          >
            {t.intro}
          </motion.p>
        </div>
      </section>

      {/* Values Grid */}
      <section className="py-16 bg-gray-50">
        <div className="container-custom">
          <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6">
            {t.values.map((value, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.05 }}
                className="bg-white rounded-xl p-6 shadow-md hover:shadow-lg transition-shadow"
              >
                <div className="w-10 h-10 rounded-lg bg-primary-100 flex items-center justify-center mb-4">
                  <Star className="w-5 h-5 text-primary-600" />
                </div>
                <h3 className="font-bold text-gray-900 mb-2">{value.title}</h3>
                <p className="text-sm text-gray-600">{value.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Vision Section */}
      <section className="py-20 bg-gradient-to-br from-primary-600 to-primary-800 text-white">
        <div className="container-custom">
          <div className="max-w-4xl mx-auto text-center">
            <motion.h2
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              className="text-3xl md:text-4xl font-bold mb-2"
            >
              {t.vision.title}
            </motion.h2>
            <motion.p
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.1 }}
              className="text-xl text-primary-200 mb-8"
            >
              {t.vision.subtitle}
            </motion.p>
            <motion.p
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              transition={{ delay: 0.2 }}
              className="text-lg text-white/90 mb-8"
            >
              {t.vision.description}
            </motion.p>
            <div className="grid md:grid-cols-2 gap-6 text-left">
              <motion.div
                initial={{ opacity: 0, x: -20 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                className="bg-white/10 backdrop-blur-sm rounded-xl p-6"
              >
                <p className="text-white/90">{t.vision.legacy}</p>
              </motion.div>
              <motion.div
                initial={{ opacity: 0, x: 20 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                className="bg-white/10 backdrop-blur-sm rounded-xl p-6"
              >
                <p className="text-white/90">{t.vision.logo}</p>
              </motion.div>
            </div>
          </div>
        </div>
      </section>

      {/* Love & Care Standard */}
      <section className="py-20 bg-white">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-12"
          >
            <Heart className="w-12 h-12 text-red-500 mx-auto mb-4" />
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">{t.standard.title}</h2>
            <p className="text-xl text-gray-600 max-w-3xl mx-auto">{t.standard.subtitle}</p>
          </motion.div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {t.standard.sections.map((section, index) => {
              const Icon = iconMap[section.icon] || Shield;
              return (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: index * 0.1 }}
                  className="bg-gray-50 rounded-2xl p-6"
                >
                  <div className="w-12 h-12 rounded-xl bg-primary-100 flex items-center justify-center mb-4">
                    <Icon className="w-6 h-6 text-primary-600" />
                  </div>
                  <h3 className="text-xl font-bold text-gray-900 mb-4">{section.title}</h3>
                  <ul className="space-y-2">
                    {section.points.map((point, pIndex) => (
                      <li key={pIndex} className="flex items-start gap-2 text-sm text-gray-600">
                        <CheckCircle className="w-4 h-4 text-green-500 mt-0.5 flex-shrink-0" />
                        <span>{point}</span>
                      </li>
                    ))}
                  </ul>
                </motion.div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Feedback Section */}
      <section className="py-16 bg-gradient-to-br from-amber-50 to-orange-50">
        <div className="container-custom">
          <div className="max-w-4xl mx-auto">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              className="text-center mb-8"
            >
              <MessageCircle className="w-12 h-12 text-amber-500 mx-auto mb-4" />
              <h2 className="text-3xl font-bold text-gray-900 mb-2">{t.feedback.title}</h2>
              <p className="text-xl text-gray-600">{t.feedback.subtitle}</p>
            </motion.div>

            <motion.p
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              className="text-center text-gray-700 mb-8"
            >
              {t.feedback.intro}
            </motion.p>

            <div className="grid md:grid-cols-2 gap-4">
              {t.feedback.points.map((point, index) => (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, x: index % 2 === 0 ? -20 : 20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: index * 0.1 }}
                  className="flex items-start gap-3 bg-white rounded-lg p-4 shadow-sm"
                >
                  <CheckCircle className="w-5 h-5 text-green-500 mt-0.5 flex-shrink-0" />
                  <span className="text-gray-700">{point}</span>
                </motion.div>
              ))}
            </div>
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="py-16 bg-primary-600 text-white text-center">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
          >
            <h2 className="text-2xl md:text-3xl font-bold mb-6">
              {language === 'en' ? 'Your voice refines our Love & Care!' : language === 'es' ? '¡Su voz refina nuestro Amor y Cuidado!' : 'Sua voz refina nosso Amor & Cuidado!'}
            </h2>
            <Link href="/contact" className="btn bg-white text-primary-600 hover:bg-gray-100 btn-lg">
              {language === 'en' ? 'Contact Us' : language === 'es' ? 'Contáctenos' : 'Fale Conosco'}
            </Link>
          </motion.div>
        </div>
      </section>
    </div>
  );
}
