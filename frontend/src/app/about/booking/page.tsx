'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import { ArrowLeft, CreditCard, CheckCircle, Percent, Building, Plane, DollarSign, Clock, Shield } from 'lucide-react';
import { useLanguageStore, Language } from '@/store/languageStore';

const content: Record<Language, {
  title: string;
  subtitle: string;
  intro: string;
  paymentMethods: {
    title: string;
    methods: Array<{
      icon: string;
      title: string;
      description: string;
    }>;
  };
  flightPolicy: {
    title: string;
    items: Array<{
      title: string;
      description: string;
    }>;
  };
  localPayment?: string;
}> = {
  en: {
    title: 'Booking Convenience & Flexible Payment Options',
    subtitle: 'Easy & Secure Booking',
    intro: 'At Girasol Egypt Travel and Tours, we offer a flexible and customer-friendly booking system designed for your convenience. You can easily acquire any of our services whether as part of a complete travel package or as individual services arranged by our agency.',
    paymentMethods: {
      title: 'Payment Methods',
      methods: [
        {
          icon: 'credit',
          title: 'Secure Credit Card Payment via Link',
          description: 'Instant and secure online payment.',
        },
        {
          icon: 'clock',
          title: 'Installment Plans',
          description: 'For purchases over 800 USD, we offer installment plans via Visa and Mastercard. You can split your payment into 2, 3, 4, or 5 installments, with predetermined dates tailored to your specific package.',
        },
        {
          icon: 'percent',
          title: 'Early Bird Discount',
          description: 'Book well in advance (minimum 8-10 months before travel) and receive a 3% to 5% discount, depending on the package type.',
        },
        {
          icon: 'building',
          title: 'International Bank Transfer',
          description: 'We accept wire transfers in USD or EUR via SWIFT/IBAN.',
        },
        {
          icon: 'split',
          title: 'Split Payment for Select Packages',
          description: 'For specific longer packages (minimum 9 days and valued over 1500 USD), we offer a convenient split: 50% deposit via credit card link upon booking, and the remaining 50% in USD cash upon your arrival in Egypt.',
        },
      ],
    },
    flightPolicy: {
      title: 'Flight Ticket Payment Policy',
      items: [
        {
          title: 'Domestic Egyptian Flights',
          description: 'Full payment in advance via our secure credit card link.',
        },
        {
          title: 'International Flights',
          description: 'Installment plans are available for tickets valued at a minimum of 800 USD. Depending on the total fare and travel date, payments can be split into 2, 3, or 4 installments.',
        },
      ],
    },
    localPayment: 'For our Egyptian clients, we accept payment in Egyptian Pounds (EGP) through multiple convenient methods: credit card, bank transfer, or cash at our office.',
  },
  es: {
    title: 'Facilidad en la Reserva y Opciones de Pago Flexibles',
    subtitle: 'Reserva Fácil y Segura',
    intro: 'En Girasol Egypt Travel and Tours, ofrecemos un sistema de reserva flexible y centrado en el cliente, diseñado para su conveniencia. Puede adquirir fácilmente cualquiera de nuestros servicios, ya sea como parte de un paquete de viaje completo o como servicios individuales organizados por nuestra agencia.',
    paymentMethods: {
      title: 'Métodos de Pago',
      methods: [
        {
          icon: 'credit',
          title: 'Pago Seguro con Tarjeta de Crédito vía Enlace',
          description: 'Pago en línea instantáneo y seguro.',
        },
        {
          icon: 'clock',
          title: 'Planes de Pago a Plazos',
          description: 'Para compras superiores a 800 USD, ofrecemos planes de pago a plazos con Visa y Mastercard. Puede dividir su pago en 2, 3, 4 o 5 cuotas, con fechas predeterminadas adaptadas a su paquete específico.',
        },
        {
          icon: 'percent',
          title: 'Descuento por Reserva Anticipada',
          description: 'Reserve con suficiente antelación (mínimo 8-10 meses antes del viaje) y reciba un descuento del 3% al 5%, según el tipo de paquete.',
        },
        {
          icon: 'building',
          title: 'Transferencia Bancaria Internacional',
          description: 'Aceptamos transferencias en USD o EUR vía SWIFT/IBAN.',
        },
        {
          icon: 'split',
          title: 'Pago Dividido para Paquetes Selectos',
          description: 'Para paquetes específicos más largos (mínimo 9 días y valor superior a 1500 USD), ofrecemos una división conveniente: 50% de depósito vía enlace de tarjeta de crédito al reservar, y el 50% restante en efectivo (USD) a su llegada a Egipto.',
        },
      ],
    },
    flightPolicy: {
      title: 'Política de Pago para Boletos Aéreos',
      items: [
        {
          title: 'Vuelos Domésticos en Egipto',
          description: 'Pago completo por adelantado a través de nuestro enlace seguro de tarjeta de crédito.',
        },
        {
          title: 'Vuelos Internacionales',
          description: 'Los planes de pago a plazos están disponibles para boletos con un valor mínimo de 800 USD. Dependiendo de la tarifa total y la fecha del viaje, los pagos pueden dividirse en 2, 3 o 4 cuotas.',
        },
      ],
    },
    localPayment: 'Para nuestros clientes egipcios, aceptamos pago en Libras Egipcias (EGP) a través de múltiples métodos convenientes: tarjeta de crédito, transferencia bancaria o efectivo en nuestra oficina.',
  },
  pt: {
    title: 'Facilidade na Reserva e Aquisição',
    subtitle: 'Opções Flexíveis de Pagamento',
    intro: 'Na Girasol Egypt Travel and Tours, oferecemos um sistema de reserva flexível e centrado no cliente, projetado para sua conveniência. Você pode adquirir facilmente qualquer um de nossos serviços, seja como parte de um pacote de viagem completo ou como serviços individuais organizados por nossa agência.',
    paymentMethods: {
      title: 'Métodos de Pagamento',
      methods: [
        {
          icon: 'credit',
          title: 'Pagamento Seguro por Cartão de Crédito via Link',
          description: 'Pagamento online instantâneo e seguro.',
        },
        {
          icon: 'clock',
          title: 'Planos de Parcelamento',
          description: 'Para compras acima de 800 USD, oferecemos parcelamento via Visa e Mastercard. Você pode dividir seu pagamento em 2, 3, 4 ou 5 parcelas, com datas predeterminadas ajustadas ao seu pacote específico.',
        },
        {
          icon: 'percent',
          title: 'Desconto Early Bird (Antecipado)',
          description: 'Reserve com bastante antecedência (mínimo de 8 a 10 meses antes da viagem) e receba um desconto de 3% a 5%, dependendo do tipo de pacote.',
        },
        {
          icon: 'building',
          title: 'Transferência Bancária Internacional',
          description: 'Aceitamos transferências em USD ou EUR via SWIFT/IBAN.',
        },
        {
          icon: 'split',
          title: 'Pagamento Dividido para Pacotes Selecionados',
          description: 'Para pacotes específicos mais longos (mínimo de 9 dias e valor superior a 1500 USD), oferecemos uma divisão conveniente: entrada de 50% via link de cartão de crédito no ato da reserva, e os 50% restantes em dinheiro (USD) na sua chegada ao Egito.',
        },
      ],
    },
    flightPolicy: {
      title: 'Política de Pagamento para Passagens Aéreas',
      items: [
        {
          title: 'Voos Domésticos no Egito',
          description: 'Pagamento integral antecipado via nosso link seguro de cartão de crédito.',
        },
        {
          title: 'Voos Internacionais',
          description: 'Planos de parcelamento estão disponíveis para passagens com valor mínimo de 800 USD. Dependendo da tarifa total e da data da viagem, os pagamentos podem ser divididos em 2, 3 ou 4 parcelas.',
        },
      ],
    },
    localPayment: 'Para nossos clientes egípcios, aceitamos pagamento em Libra Egípcia (EGP) através de múltiplos métodos convenientes: cartão de crédito, transferência bancária ou dinheiro em nosso escritório.',
  },
};

const iconMap: Record<string, React.ElementType> = {
  credit: CreditCard,
  clock: Clock,
  percent: Percent,
  building: Building,
  split: DollarSign,
};

export default function BookingPage() {
  const { language } = useLanguageStore();
  const t = content[language];

  return (
    <div className="min-h-screen">
      {/* Hero Section */}
      <section className="relative h-[50vh] min-h-[400px] flex items-center justify-center overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-r from-green-900/90 to-emerald-800/80 z-10" />
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
            <CreditCard className="w-16 h-16 mx-auto text-green-300" />
          </motion.div>
          <motion.p
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="text-green-200 text-lg mb-2"
          >
            {t.subtitle}
          </motion.p>
          <motion.h1
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.1 }}
            className="text-3xl md:text-4xl lg:text-5xl font-display font-bold"
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

      {/* Payment Methods */}
      <section className="py-16 bg-gray-50">
        <div className="container-custom">
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-3xl md:text-4xl font-bold text-gray-900 text-center mb-12"
          >
            {t.paymentMethods.title}
          </motion.h2>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
            {t.paymentMethods.methods.map((method, index) => {
              const Icon = iconMap[method.icon] || CreditCard;
              return (
                <motion.div
                  key={index}
                  initial={{ opacity: 0, y: 20 }}
                  whileInView={{ opacity: 1, y: 0 }}
                  viewport={{ once: true }}
                  transition={{ delay: index * 0.1 }}
                  className="bg-white rounded-2xl p-6 shadow-lg hover:shadow-xl transition-shadow"
                >
                  <div className="w-14 h-14 rounded-xl bg-gradient-to-br from-green-500 to-emerald-600 flex items-center justify-center mb-4">
                    <Icon className="w-7 h-7 text-white" />
                  </div>
                  <h3 className="text-lg font-bold text-gray-900 mb-2">{method.title}</h3>
                  <p className="text-gray-600 text-sm">{method.description}</p>
                </motion.div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Flight Policy */}
      <section className="py-16 bg-white">
        <div className="container-custom">
          <motion.h2
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="text-3xl font-bold text-gray-900 text-center mb-12"
          >
            {t.flightPolicy.title}
          </motion.h2>

          <div className="grid md:grid-cols-2 gap-8 max-w-4xl mx-auto">
            {t.flightPolicy.items.map((item, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: index === 0 ? -30 : 30 }}
                whileInView={{ opacity: 1, x: 0 }}
                viewport={{ once: true }}
                className="bg-gradient-to-br from-blue-50 to-indigo-50 rounded-2xl p-8"
              >
                <div className="flex items-center gap-3 mb-4">
                  <Plane className="w-8 h-8 text-blue-600" />
                  <h3 className="text-xl font-bold text-gray-900">{item.title}</h3>
                </div>
                <p className="text-gray-600">{item.description}</p>
              </motion.div>
            ))}
          </div>

          {t.localPayment && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              className="mt-12 max-w-3xl mx-auto"
            >
              <div className="bg-amber-50 border border-amber-200 rounded-xl p-6 flex items-start gap-4">
                <Building className="w-6 h-6 text-amber-600 flex-shrink-0 mt-1" />
                <p className="text-amber-800">{t.localPayment}</p>
              </div>
            </motion.div>
          )}
        </div>
      </section>

      {/* Security Badge */}
      <section className="py-16 bg-gradient-to-r from-primary-600 to-primary-800 text-white">
        <div className="container-custom">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            className="max-w-3xl mx-auto text-center"
          >
            <Shield className="w-16 h-16 mx-auto mb-6 text-green-300" />
            <h2 className="text-2xl md:text-3xl font-bold mb-4">
              {language === 'en' ? 'Secure & Trusted Payments' : language === 'es' ? 'Pagos Seguros y Confiables' : 'Pagamentos Seguros e Confiáveis'}
            </h2>
            <p className="text-white/80 text-lg mb-8">
              {language === 'en'
                ? 'All our payment methods are secured with industry-standard encryption. Your financial information is always protected.'
                : language === 'es'
                  ? 'Todos nuestros métodos de pago están protegidos con cifrado estándar de la industria. Su información financiera siempre está protegida.'
                  : 'Todos os nossos métodos de pagamento são protegidos com criptografia padrão da indústria. Suas informações financeiras estão sempre protegidas.'
              }
            </p>
            <div className="flex flex-wrap justify-center gap-4">
              <Link href="/tours" className="btn bg-white text-primary-600 hover:bg-gray-100 btn-lg">
                {language === 'en' ? 'Browse Tours' : language === 'es' ? 'Ver Tours' : 'Ver Passeios'}
              </Link>
              <Link href="/contact" className="btn btn-outline border-white text-white hover:bg-white/10 btn-lg">
                {language === 'en' ? 'Get a Quote' : language === 'es' ? 'Solicitar Cotización' : 'Solicitar Orçamento'}
              </Link>
            </div>
          </motion.div>
        </div>
      </section>
    </div>
  );
}
