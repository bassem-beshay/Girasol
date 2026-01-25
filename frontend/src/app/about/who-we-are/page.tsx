'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import { ArrowLeft, Award, Pyramid, Feather, Sun, Sparkles, Plane, Clock, Compass, Anchor, Heart, Users } from 'lucide-react';
import { useLanguageStore, Language } from '@/store/languageStore';

const content: Record<Language, {
  title: string;
  subtitle: string;
  intro: string[];
  yearsText: string;
  yearsDescription: string;
  logoSection: {
    title: string;
    subtitle: string;
    pyramid: { title: string; description: string };
    feather: { title: string; description: string };
    name: { title: string; description: string };
    gLetter: { title: string; description: string };
    conclusion: string;
  };
  howWeMaterialize: {
    title: string;
    operations: string;
    customerService: string;
    quote: string;
  };
  loveAndCare: {
    title: string;
    subtitle: string;
    points: string[];
    quote: string;
  };
  tripTypes: {
    title: string;
    subtitle: string;
    types: Array<{
      icon: string;
      title: string;
      idealFor: string;
      howItWorks: string;
      keyExperience: string;
    }>;
  };
  multiCultural: {
    title: string;
    combinations: Array<{ countries: string; description: string; note: string }>;
  };
  packages: {
    title: string;
    list: string[];
  };
  cta: string;
}> = {
  en: {
    title: 'Who We Are',
    subtitle: 'Our Story',
    intro: [
      'Who are we? We were born in the heart of Cairo, Egypt, as part of the experienced Girassol Viagens family. Girasol Egypt Travel and Tours is the fruit of a union between Egyptian experts, passionate about their homeland, and Tourism professionals who deeply understand the desires of travelers.',
      'This unique combination allows us to create authentic and immersive itineraries, Trips and Tour-packages not only through fascinating Egypt but also to integrated destinations across the Middle East, the Mediterranean, and Asia. Operating as your ground handler in Egypt, we rely on solid partnerships with the best hotel networks and luxurious Nile cruises, guaranteeing memorable experiences and excellent service, both for you, the traveler, and for the agencies that trust us.',
    ],
    yearsText: '31 years weaving a passion for Egypt into every step our travelers take.',
    yearsDescription: 'Three decades dedicated to transforming expectations into immersive experiences. With technical expertise and cultural sensitivity, we craft journeys that harmonize historical authenticity, comfort, and transformative discoveries.',
    logoSection: {
      title: 'The Symbol that Inspires Us',
      subtitle: 'Our Logo: A Symbol of Excellence, Built on Timeless Values',
      pyramid: {
        title: 'The Pyramid: The Foundation of Progress & Mastery',
        description: 'At its heart stands a stylized representation of the Step Pyramid of Sakkara—the world\'s first pyramid. This symbolizes our foundational commitment to progress, structure, and evolutionary mastery. Just as this ancient wonder marked a revolutionary step forward in architectural history, we see every journey as a purposeful, upward ascent.',
      },
      feather: {
        title: 'The Feather: The Pillar of Justice & Integrity',
        description: 'Enshrined within the pyramid\'s form is the Feather of Maat, the ancient Egyptian symbol of truth, balance, and moral order. This powerful symbol is our sacred commitment to justice, fairness, and ethical integrity in all our dealings.',
      },
      name: {
        title: 'The Name: Clarity, Warmth, and Guiding Light',
        description: '"Girasol" – the latin word for Sunflower – was chosen with deep intention. The sunflower is a universal emblem of positivity, warmth, and an unwavering orientation toward light. In the context of travel, this translates to clarity, optimism, and joyful discovery.',
      },
      gLetter: {
        title: 'The Stylized \'G\': Our Signature of Radiance',
        description: 'The first letter of our name, the \'G\', is artistically rendered as the blooming heart of a sunflower. This floral \'G\' visually communicates openness, radiant energy, and transparent service.',
      },
      conclusion: 'Together, these elements fuse into a single, powerful statement: We are a company built on the solid progress of expertise, guided by the ethical integrity of justice, and delivered with the transparent warmth of a guiding light.',
    },
    howWeMaterialize: {
      title: 'How We Materialize This Inspiration',
      operations: 'In Operations: Contractual clarity, detailed itineraries, proactive communication.',
      customerService: 'In Customer Service: Active listening, genuine personalization, respect for individualities.',
      quote: '"Love & Care are our golden threads – weaving harmony and discipline into every journey, balancing details like pyramids and hearts with eternal truth."',
    },
    loveAndCare: {
      title: 'The Love & Care Standard',
      subtitle: 'Our Inner Compass',
      points: [
        'Exclusive benefits born from excellence.',
        'Technical perfection honed over three decades.',
        'Human warmth that transforms deserts into a home.',
      ],
      quote: '"Traveling with us is feeling at home before the Great Pyramids and magical wonders – where every detail is an expression of Love & Care, every itinerary, a legacy of timeless harmony."',
    },
    tripTypes: {
      title: 'Types of Our Trips',
      subtitle: 'Find Your Perfect Experience',
      types: [
        {
          icon: 'rocket',
          title: 'Quick Trips (4-8 days)',
          idealFor: 'Those with few holiday days, a layover in Egypt, or who desire an unforgettable "taste."',
          howItWorks: 'Dynamic, well-structured itineraries carefully planned for you to experience the essence of Egypt.',
          keyExperience: 'Discover the most iconic wonders in a practical and memorable way.',
        },
        {
          icon: 'star',
          title: 'Classic Trips (9-14 nights)',
          idealFor: 'Travelers seeking a complete immersion in the country\'s history, culture, and natural beauty.',
          howItWorks: 'Programs with fixed dates throughout the year, covering main Egyptian destinations.',
          keyExperience: 'A comprehensive journey through Pharaonic wonders, the majestic Nile River, and the Red Sea.',
        },
        {
          icon: 'globe',
          title: 'Grand Expeditions (15-21 nights)',
          idealFor: 'Travelers seeking a deep connection with Egypt\'s essence or combined tours.',
          howItWorks: 'Extensive itineraries through Egypt or multicultural experiences integrating multiple countries.',
          keyExperience: 'Broaden your horizons with an epic journey uniting ancient civilizations.',
        },
        {
          icon: 'palette',
          title: 'Customized & Tailor-Made',
          idealFor: 'Those seeking total flexibility, intimate trips, or groups with specific interests.',
          howItWorks: 'Complete freedom! Choose duration, dates, destinations, and style.',
          keyExperience: 'The trip of your dreams, tailor-made for your pace and interests.',
        },
        {
          icon: 'crystal',
          title: 'Thematic & Special Trips',
          idealFor: 'Lovers of Egyptology, archaeology, mythology, spirituality, or diving.',
          howItWorks: 'Groups with pre-set dates focused on profound themes.',
          keyExperience: 'Go far beyond conventional tourism and connect with the soul of Ancient Egypt.',
        },
      ],
    },
    multiCultural: {
      title: 'Multicultural Combinations',
      combinations: [
        { countries: 'Egypt & Jordan', description: 'The Rose City of Petra & Wadi Rum Desert', note: 'Our most requested combination' },
        { countries: 'Egypt & UAE', description: 'Pharaohs & Dubai\'s Futurism', note: 'Where antiquity meets modernity' },
        { countries: 'Egypt & Turkey', description: 'Istanbul & Cappadocia', note: 'Entwined empires' },
        { countries: 'Egypt & Morocco', description: 'Marrakech & Fez/Rabat Heritage', note: 'From the Nile to the Atlas' },
        { countries: 'Egypt & India', description: 'Taj Mahal & Temples of the Nile', note: 'A journey of our specialty for 20 years' },
      ],
    },
    packages: {
      title: 'Explore Our Packages',
      list: [
        'Egypt Packages with Flights',
        'Egypt Packages 4-8 Days (Without flights)',
        'Egypt Packages 9-15 Days (Without flights)',
        'Multidestination Packages: Egypt + Another Country',
        'New Year\'s, Holiday, and Thematic Packages',
        'Diving and Beach Packages',
        'Daily Tours and Excursions (1-4 days)',
      ],
    },
    cta: 'Ready to live your Journey? Let us guide you on this unforgettable adventure!',
  },
  es: {
    title: 'Quiénes Somos',
    subtitle: 'Nuestra Historia',
    intro: [
      '¿Quiénes somos? Nacimos en el corazón de El Cairo, Egipto, como parte de la experimentada familia Girassol Viagens. Girasol Egypt Travel and Tours es el fruto de la unión entre expertos egipcios, apasionados por su tierra natal, y profesionales del turismo que comprenden profundamente los deseos de los viajantes.',
      'Esta combinación única nos permite crear itinerarios auténticos e inmersivos, viajes y paquetes turísticos que recorren no solo el fascinante Egipto, sino también destinos integrados en todo Oriente Medio, el Mediterráneo y Asia. Al actuar como su operadora receptiva en Egipto, contamos con sólidas alianzas con las mejores cadenas hoteleras y los lujosos cruceros por el Nilo, garantizando experiencias memorables y servicios de excelencia.',
    ],
    yearsText: '31 años entretejiendo pasión por Egipto en cada paso de nuestros viajeros.',
    yearsDescription: 'Tres décadas dedicadas a transformar expectativas en experiencias inmersivas. Con experiencia técnica y sensibilidad cultural, construimos travesías que armonizan autenticidad histórica, comodidad y descubrimientos transformadores.',
    logoSection: {
      title: 'El Símbolo que Nos Inspira',
      subtitle: 'Nuestro Logo: Un Símbolo de Excelencia, Construido sobre Valores Atemporales',
      pyramid: {
        title: 'La Pirámide: La Base del Progreso y la Maestría',
        description: 'En su centro hay una representación estilizada de la Pirámide Escalonada de Saqqara—la primera pirámide del mundo. Simboliza nuestro compromiso fundamental con el progreso, la estructura y la maestría evolutiva.',
      },
      feather: {
        title: 'La Pluma: El Pilar de la Justicia y la Integridad',
        description: 'Incrustada en la forma de la pirámide está la Pluma de Maat, el antiguo símbolo egipcio de la verdad, el equilibrio y el orden moral. Este poderoso símbolo es nuestro compromiso sagrado con la justicia, la equidad y la integridad ética.',
      },
      name: {
        title: 'El Nombre: Claridad, Calor y Luz Guía',
        description: '"Girasol" fue elegida con profunda intención. El girasol es un emblema universal de positividad, calor y una orientación inquebrantable hacia la luz.',
      },
      gLetter: {
        title: 'La \'G\' Estilizada: Nuestra Firma de Radiancia',
        description: 'La primera letra de nuestro nombre, la \'G\', es representada artísticamente como el corazón floreciente de un girasol. Comunica visualmente apertura, energía radiante y servicio transparente.',
      },
      conclusion: 'Juntos, estos elementos se fusionan en una sola y poderosa declaración: Somos una empresa construida sobre el progreso sólido de la experiencia, guiada por la integridad ética de la justicia y entregada con el calor transparente de una luz guía.',
    },
    howWeMaterialize: {
      title: 'Cómo Materializamos Esta Inspiración',
      operations: 'En Operaciones: Claridad contractual, itinerarios detallados, comunicación proactiva.',
      customerService: 'En Atención al Cliente: Escucha activa, personalización genuina, respeto a las individualidades.',
      quote: '"El Amor y el Cuidado son nuestros hilos de oro – tejiendo armonía y disciplina en cada travesía, equilibrando detalles como pirámides y corazones con verdad eterna."',
    },
    loveAndCare: {
      title: 'El Estándar Amor y Cuidado',
      subtitle: 'Nuestra Brújula Interior',
      points: [
        'Beneficios exclusivos nacidos de la excelencia.',
        'Perfección técnica pulida durante tres décadas.',
        'Calidez humana que transforma desiertos en hogar.',
      ],
      quote: '"Viajar con nosotros es sentirse como en casa frente a las Grandes Pirámides y maravillas mágicas – donde cada detalle es expresión de Amor y Cuidado, cada itinerario, legado de armonía inmemorial."',
    },
    tripTypes: {
      title: 'Tipos de Nuestros Viajes',
      subtitle: 'Encuentre Su Experiencia Perfecta',
      types: [
        {
          icon: 'rocket',
          title: 'Viajes Rápidos (4-8 días)',
          idealFor: 'Quien tiene pocos días de vacaciones o desea una "probadita" inolvidable.',
          howItWorks: 'Itinerarios dinámicos y bien estructurados para vivir lo esencial de Egipto.',
          keyExperience: 'Conozca las maravillas más icónicas de forma práctica y memorable.',
        },
        {
          icon: 'star',
          title: 'Viajes Clásicos (9-14 noches)',
          idealFor: 'Viajeros que buscan una inmersión completa en la historia y cultura del país.',
          howItWorks: 'Programas con fechas fijas cubriendo los principales destinos egipcios.',
          keyExperience: 'Un recorrido integral por las maravillas faraónicas y el Río Nilo.',
        },
        {
          icon: 'globe',
          title: 'Grandes Expediciones (15-21 noches)',
          idealFor: 'Viajeros que buscan una conexión profunda con Egipto o tours combinados.',
          howItWorks: 'Itinerarios extensos o experiencias multiculturales integrando varios países.',
          keyExperience: 'Amplíe sus horizontes con un viaje épico uniendo civilizaciones milenarias.',
        },
        {
          icon: 'palette',
          title: 'Viajes Personalizados',
          idealFor: 'Quien busca flexibilidad total, viajes íntimos o grupos con intereses específicos.',
          howItWorks: '¡Libertad total! Elija duración, fechas, destinos y estilo.',
          keyExperience: 'El viaje de sus sueños, creado a la medida de su ritmo e intereses.',
        },
        {
          icon: 'crystal',
          title: 'Viajes Temáticos y Especiales',
          idealFor: 'Amantes de la egiptología, arqueología, mitología, espiritualidad o buceo.',
          howItWorks: 'Grupos con fechas prefijadas enfocados en temas profundos.',
          keyExperience: 'Vaya mucho más allá del turismo convencional y conéctese con el alma del Antiguo Egipto.',
        },
      ],
    },
    multiCultural: {
      title: 'Combinaciones Multiculturales',
      combinations: [
        { countries: 'Egipto y Jordania', description: 'La Ciudad Rosa de Petra y el Desierto de Wadi Rum', note: 'Nuestra combinación más solicitada' },
        { countries: 'Egipto y Emiratos', description: 'Faraones y el Futurismo de Dubái', note: 'Donde la antigüedad se encuentra con la modernidad' },
        { countries: 'Egipto y Turquía', description: 'Estambul y Capadocia', note: 'Imperios entrelazados' },
        { countries: 'Egipto y Marruecos', description: 'Marrakech y Patrimonio de Fez/Rabat', note: 'Del Nilo al Atlas' },
        { countries: 'Egipto e India', description: 'Taj Mahal y Templos del Nilo', note: 'Travesía de nuestra especialidad desde hace 20 años' },
      ],
    },
    packages: {
      title: 'Explore Nuestros Paquetes',
      list: [
        'Paquetes a Egipto con Vuelo',
        'Paquetes a Egipto 4-8 Días (Sin vuelos)',
        'Paquetes a Egipto 9-15 Días (Sin vuelos)',
        'Paquetes Multidestino: Egipto + Otro País',
        'Paquetes de Año Nuevo, Feriados y Temáticos',
        'Paquetes de Buceo y Playa',
        'Tours Diarios y Excursiones (1-4 días)',
      ],
    },
    cta: '¿Listo para vivir su Travesía? ¡Permítanos guiarle en esta aventura inolvidable!',
  },
  pt: {
    title: 'Quem Somos',
    subtitle: 'Nossa História',
    intro: [
      'Quem somos? Nascemos no coração do Cairo, Egito, como parte da experiente família Girassol Viagens. A Girasol Egypt Travel and Tours é fruto da união entre especialistas egípcios, apaixonados por sua terra natal, e profissionais do turismo que compreendem profundamente os desejos dos viajantes.',
      'Essa combinação única nos permite criar roteiros autênticos e imersivos, viagens e pacotes turísticos que percorrem não apenas o Egito fascinante, mas também destinos integrados em todo o Oriente Médio, Mediterrâneo e Ásia. Atuando como sua operadora receptiva no Egito, contamos com sólidas parcerias com as melhores redes de hotéis e os luxuosos cruzeiros no Nilo, garantindo experiências memoráveis e serviços de excelência.',
    ],
    yearsText: '31 anos tecendo paixão pelo Egito em cada passo de nossos viajantes.',
    yearsDescription: 'Três décadas dedicadas a transformar expectativas em experiências imersivas. Com expertise técnica e sensibilidade cultural, construímos jornadas que harmonizam autenticidade histórica, conforto e descobertas transformadoras.',
    logoSection: {
      title: 'O Símbolo que Nos Inspira',
      subtitle: 'Nosso Logo: Um Símbolo de Excelência, Construído sobre Valores Atemporais',
      pyramid: {
        title: 'A Pirâmide: A Base do Progresso & Maestria',
        description: 'Em seu centro está uma representação estilizada da Pirâmide de Degraus de Sakkara—a primeira pirâmide do mundo. Ela simboliza nosso compromisso fundamental com progresso, estrutura e maestria evolutiva.',
      },
      feather: {
        title: 'A Pena: O Pilar da Justiça & Integridade',
        description: 'Inserida na forma da pirâmide está a Pena de Maat, o antigo símbolo egípcio da verdade, equilíbrio e ordem moral. Este símbolo poderoso é nosso compromisso sagrado com justiça, equidade e integridade ética.',
      },
      name: {
        title: 'O Nome: Clareza, Calor e Luz Guia',
        description: '"Girasol" – a palavra latina para Girassol – foi escolhida com profunda intenção. O girassol é um emblema universal de positividade, calor e uma orientação inabalável em direção à luz.',
      },
      gLetter: {
        title: 'O \'G\' Estilizado: Nossa Assinatura de Radiância',
        description: 'A primeira letra do nosso nome, o \'G\', é artisticamente renderizada como o coração florescente de um girassol. Este \'G\' floral comunica visualmente abertura, energia radiante e serviço transparente.',
      },
      conclusion: 'Juntos, esses elementos se fundem em uma única e poderosa declaração: Somos uma empresa construída sobre o progresso sólido da expertise, guiada pela integridade ética da justiça e entregue com o calor transparente de uma luz guia.',
    },
    howWeMaterialize: {
      title: 'Como Materializamos Esta Inspiração',
      operations: 'Nas Operações: Clareza contratual, itinerários detalhados, comunicação proativa.',
      customerService: 'No Atendimento ao Cliente: Escuta ativa, personalização genuína, respeito às individualidades.',
      quote: '"O Amor & Cuidado são nossos fios de ouro – tecendo harmonia e disciplina em cada jornada, equilibrando detalhes como pirâmides e corações com verdade eterna."',
    },
    loveAndCare: {
      title: 'O Padrão Amor & Cuidado',
      subtitle: 'Nosso Compasso Interior',
      points: [
        'Benefícios exclusivos nascidos da excelência.',
        'Perfeição técnica lapidada por três décadas.',
        'Acolhimento humano que transforma desertos em lar.',
      ],
      quote: '"Viajar conosco é sentir-se em casa diante das Grandes Pirâmides e maravilhas mágicas – onde cada detalhe é expressão de Amor & Cuidado, cada roteiro, legado de harmonia imemorial."',
    },
    tripTypes: {
      title: 'Tipos de Nossas Viagens',
      subtitle: 'Encontre Sua Experiência Perfeita',
      types: [
        {
          icon: 'rocket',
          title: 'Viagens Rápidas (4-8 dias)',
          idealFor: 'Quem tem poucos dias de férias ou deseja um "gostinho" inesquecível.',
          howItWorks: 'Roteiros dinâmicos e bem estruturados para viver o essencial do Egito.',
          keyExperience: 'Conheça as maravilhas mais icônicas de forma prática e memorável.',
        },
        {
          icon: 'star',
          title: 'Viagens Clássicas (9-14 noites)',
          idealFor: 'Viajantes que buscam uma imersão completa na história e cultura do país.',
          howItWorks: 'Programas com datas fixas cobrindo os principais destinos egípcios.',
          keyExperience: 'Uma jornada abrangente pelas maravilhas faraônicas e o Rio Nilo.',
        },
        {
          icon: 'globe',
          title: 'Grandes Expedições (15-21 noites)',
          idealFor: 'Viajantes que buscam conexão profunda com o Egito ou combinados.',
          howItWorks: 'Roteiros extensos ou experiências multiculturais integrando vários países.',
          keyExperience: 'Amplie seus horizontes com uma jornada épica unindo civilizações milenares.',
        },
        {
          icon: 'palette',
          title: 'Viagens Personalizadas',
          idealFor: 'Quem busca flexibilidade total, viagens íntimas ou grupos com interesses específicos.',
          howItWorks: 'Liberdade total! Escolha duração, datas, destinos e estilo.',
          keyExperience: 'A viagem dos seus sonhos, criada sob medida para seu ritmo e interesses.',
        },
        {
          icon: 'crystal',
          title: 'Viagens Temáticas e Especiais',
          idealFor: 'Amantes de egiptologia, arqueologia, mitologia, espiritualidade ou mergulho.',
          howItWorks: 'Grupos com datas prefixadas focados em temas profundos.',
          keyExperience: 'Vá muito além do turismo convencional e conecte-se com a alma do Egito Antigo.',
        },
      ],
    },
    multiCultural: {
      title: 'Combinações Multiculturais',
      combinations: [
        { countries: 'Egito & Jordânia', description: 'A Cidade Rosa de Petra & o Deserto de Wadi Rum', note: 'Nossa combinação mais requisitada' },
        { countries: 'Egito & Emirados', description: 'Faraós & o Futurismo de Dubai', note: 'Onde a antiguidade encontra a modernidade' },
        { countries: 'Egito & Turquia', description: 'Istambul & Capadócia', note: 'Impérios entrelaçados' },
        { countries: 'Egito & Marrocos', description: 'Marrakesh & Patrimônio de Fez/Rabat', note: 'Do Nilo ao Atlas' },
        { countries: 'Egito & Índia', description: 'Taj Mahal & Templos do Nilo', note: 'Jornada de nossa especialidade há 20 anos' },
      ],
    },
    packages: {
      title: 'Explore Nossos Pacotes',
      list: [
        'Pacotes para o Egito com Aéreo',
        'Pacotes para o Egito 4-8 Dias (Sem voos)',
        'Pacotes para o Egito 9-15 Dias (Sem voos)',
        'Pacotes Multidestino: Egito + Outro País',
        'Pacotes de Réveillon, Feriados e Temáticos',
        'Pacotes de Mergulho e Praia',
        'Passeios Diários e Excursões (1-4 dias)',
      ],
    },
    cta: 'Pronto para viver sua Jornada? Deixe-nos guiar você nesta aventura inesquecível!',
  },
};

export default function WhoWeArePage() {
  const { language } = useLanguageStore();
  const t = content[language];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[50vh] min-h-[400px] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-primary-900/90 to-primary-800/80 z-10" />
        <div
          className="absolute inset-0 bg-cover bg-center"
          style={{ backgroundImage: "url('/images/about-hero.jpg')" }}
        />
        <div className="relative z-20 text-center text-white max-w-4xl mx-auto px-4">
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-primary-300 text-lg mb-2"
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
      <section className="py-12 bg-white">
        <div className="container-custom">
          <div className="max-w-4xl mx-auto space-y-6 text-gray-700 text-lg leading-relaxed">
            {t.intro.map((paragraph, index) => (
              <motion.p
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
              >
                {paragraph}
              </motion.p>
            ))}
          </div>
        </div>
      </section>

      {/* 31 Years Banner */}
      <section className="py-16 bg-gradient-to-r from-primary-600 to-primary-800 text-white">
        <div className="container-custom text-center">
          <motion.div
            initial={{ opacity: 0, scale: 0.9 }}
            whileInView={{ opacity: 1, scale: 1 }}
            viewport={{ once: true }}
          >
            <div className="text-6xl md:text-7xl font-bold mb-4">31+</div>
            <h2 className="text-2xl md:text-3xl font-bold mb-4">{t.yearsText}</h2>
            <p className="text-white/80 max-w-2xl mx-auto text-lg">{t.yearsDescription}</p>
          </motion.div>
        </div>
      </section>

      {/* Logo Section */}
      <section className="py-20 bg-gray-50">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-12"
          >
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">{t.logoSection.title}</h2>
            <p className="text-xl text-gray-600">{t.logoSection.subtitle}</p>
          </motion.div>

          <div className="grid md:grid-cols-2 gap-8 max-w-5xl mx-auto">
            {[
              { icon: Pyramid, ...t.logoSection.pyramid },
              { icon: Feather, ...t.logoSection.feather },
              { icon: Sun, ...t.logoSection.name },
              { icon: Sparkles, ...t.logoSection.gLetter },
            ].map((item, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                className="bg-white rounded-2xl p-8 shadow-lg"
              >
                <div className="w-14 h-14 rounded-xl bg-primary-100 flex items-center justify-center mb-4">
                  <item.icon className="w-7 h-7 text-primary-600" />
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-3">{item.title}</h3>
                <p className="text-gray-600">{item.description}</p>
              </motion.div>
            ))}
          </div>

          <motion.p
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center text-lg text-gray-700 mt-12 max-w-3xl mx-auto"
          >
            {t.logoSection.conclusion}
          </motion.p>
        </div>
      </section>

      {/* How We Materialize */}
      <section className="py-16 bg-white">
        <div className="container-custom">
          <div className="max-w-4xl mx-auto">
            <motion.h2
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              className="text-3xl font-bold text-gray-900 mb-8 text-center flex items-center justify-center gap-2"
            >
              <Heart className="w-8 h-8 text-red-500" />
              {t.howWeMaterialize.title}
            </motion.h2>
            <div className="space-y-4 text-gray-700">
              <p className="text-lg">{t.howWeMaterialize.operations}</p>
              <p className="text-lg">{t.howWeMaterialize.customerService}</p>
              <blockquote className="border-l-4 border-primary-500 pl-6 py-4 my-8 bg-primary-50 rounded-r-lg italic text-primary-800">
                {t.howWeMaterialize.quote}
              </blockquote>
            </div>
          </div>
        </div>
      </section>

      {/* Love & Care Standard */}
      <section className="py-16 bg-gradient-to-br from-red-50 to-orange-50">
        <div className="container-custom">
          <div className="max-w-4xl mx-auto text-center">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
            >
              <Heart className="w-16 h-16 text-red-500 mx-auto mb-4" />
              <h2 className="text-3xl font-bold text-gray-900 mb-2">{t.loveAndCare.title}</h2>
              <p className="text-xl text-gray-600 mb-8">{t.loveAndCare.subtitle}</p>
            </motion.div>
            <ul className="space-y-4 text-left max-w-xl mx-auto mb-8">
              {t.loveAndCare.points.map((point, index) => (
                <motion.li
                  key={index}
                  initial={{ opacity: 0, x: -20 }}
                  whileInView={{ opacity: 1, x: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: index * 0.1 }}
                  className="flex items-start gap-3"
                >
                  <Sparkles className="w-5 h-5 text-primary-500 mt-1 flex-shrink-0" />
                  <span className="text-gray-700">{point}</span>
                </motion.li>
              ))}
            </ul>
            <blockquote className="text-lg italic text-gray-700 border-l-4 border-red-400 pl-6 py-4 bg-white rounded-r-lg text-left">
              {t.loveAndCare.quote}
            </blockquote>
          </div>
        </div>
      </section>

      {/* Trip Types */}
      <section className="py-20 bg-white">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-center mb-12"
          >
            <h2 className="text-3xl md:text-4xl font-bold text-gray-900 mb-4">{t.tripTypes.title}</h2>
            <p className="text-xl text-gray-600">{t.tripTypes.subtitle}</p>
          </motion.div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {t.tripTypes.types.map((type, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                className="bg-gray-50 rounded-2xl p-6 hover:shadow-lg transition-shadow"
              >
                <div className="w-12 h-12 rounded-xl bg-primary-100 flex items-center justify-center mb-4">
                  {type.icon === 'rocket' && <Clock className="w-6 h-6 text-primary-600" />}
                  {type.icon === 'star' && <Award className="w-6 h-6 text-primary-600" />}
                  {type.icon === 'globe' && <Plane className="w-6 h-6 text-primary-600" />}
                  {type.icon === 'palette' && <Users className="w-6 h-6 text-primary-600" />}
                  {type.icon === 'crystal' && <Compass className="w-6 h-6 text-primary-600" />}
                </div>
                <h3 className="text-xl font-bold text-gray-900 mb-3">{type.title}</h3>
                <div className="space-y-2 text-sm text-gray-600">
                  <p><strong>{language === 'en' ? 'Ideal for:' : language === 'es' ? 'Ideal para:' : 'Ideal para:'}</strong> {type.idealFor}</p>
                  <p><strong>{language === 'en' ? 'How it works:' : language === 'es' ? 'Cómo funciona:' : 'Como funciona:'}</strong> {type.howItWorks}</p>
                  <p className="text-primary-600 font-medium">{type.keyExperience}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Multicultural Combinations */}
      <section className="py-16 bg-gradient-to-r from-blue-600 to-indigo-700 text-white">
        <div className="container-custom">
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-3xl font-bold text-center mb-12"
          >
            {t.multiCultural.title}
          </motion.h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
            {t.multiCultural.combinations.map((combo, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.1 }}
                className="bg-white/10 backdrop-blur-sm rounded-xl p-6"
              >
                <div className="flex items-center gap-2 mb-2">
                  <Plane className="w-5 h-5" />
                  <h3 className="font-bold text-lg">{combo.countries}</h3>
                </div>
                <p className="text-white/80 mb-2">{combo.description}</p>
                <p className="text-sm text-primary-300">{combo.note}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Packages */}
      <section className="py-16 bg-gray-50">
        <div className="container-custom">
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-3xl font-bold text-gray-900 text-center mb-8"
          >
            {t.packages.title}
          </motion.h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4 max-w-4xl mx-auto">
            {t.packages.list.map((pkg, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: -20 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                transition={{ delay: index * 0.05 }}
                className="flex items-center gap-3 bg-white rounded-lg p-4 shadow-sm"
              >
                <Anchor className="w-5 h-5 text-primary-500 flex-shrink-0" />
                <span className="text-gray-700">{pkg}</span>
              </motion.div>
            ))}
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
            <h2 className="text-2xl md:text-3xl font-bold mb-6">{t.cta}</h2>
            <Link href="/tours" className="btn bg-white text-primary-600 hover:bg-gray-100 btn-lg">
              {language === 'en' ? 'Explore Our Tours' : language === 'es' ? 'Explorar Tours' : 'Explorar Passeios'}
            </Link>
          </motion.div>
        </div>
      </section>
    </div>
  );
}
