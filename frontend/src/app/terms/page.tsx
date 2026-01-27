'use client';

import { motion } from 'framer-motion';
import Link from 'next/link';
import { FileText, ArrowLeft, Shield, BookOpen, Plane, Hotel, Ship, Bus, Baby, XCircle, CreditCard, Calendar, ShoppingCart, Lock, Scale, FileCheck } from 'lucide-react';
import { useLanguageStore, Language } from '@/store/languageStore';

const content: Record<Language, {
  title: string;
  subtitle: string;
  intro: string;
  backToHome: string;
  sections: Array<{
    icon: string;
    title: string;
    content: string[];
  }>;
}> = {
  en: {
    title: 'Terms & Conditions',
    subtitle: 'Check details about our general rules and conditions, from booking guarantee and documentation to safety standards.',
    intro: 'We present to you the general rules and conditions, from booking guarantee and documentation to health standards. These rules and conditions cover all topics a traveler wishes to know. Please read carefully and contact us if you have any questions.',
    backToHome: 'Back to Home',
    sections: [
      {
        icon: 'shield',
        title: 'Booking Guarantee',
        content: [
          'Tour reservations are subject to availability and are only guaranteed after purchase is completed upon payment.'
        ]
      },
      {
        icon: 'passport',
        title: 'Travel Documentation',
        content: [
          'The passport is a personal and non-transferable document. The passport must be valid for at least 6 months from the date of entry into the destination country; it must also contain the requested visa (for countries requiring prior visa issuance).',
          'Unaccompanied minors, or those accompanied only by a father, mother, or legal guardian, will require special authorization for travel abroad, even with a passport and prior visa (where applicable).'
        ]
      },
      {
        icon: 'visa',
        title: 'Egypt Entry Visa',
        content: [
          'A visa is necessary to enter Egypt. There are 3 ways to obtain an Egypt Visa:',
          '• Electronic Visa online via the Egyptian government portal (Egypt e-Visa Portal). Brazil and Portugal are among the countries permitted to obtain an e-Visa.',
          '• On arrival at Cairo International Airport - not conditioned on obtaining a consular visa beforehand.',
          '• Consular visa requested through the Embassy/Consulate of the Arab Republic of Egypt.'
        ]
      },
      {
        icon: 'airport',
        title: 'Formalities at Airports',
        content: [
          'If the traveler fills out and signs forms at airports regarding their medical condition, it is the passenger\'s exclusive responsibility.',
          'Passengers must follow and respect all entry and exit formalities and Customs, as well as the measures and sanitary regulations applied at airports, hotels, restaurants, and tourist sites.'
        ]
      },
      {
        icon: 'insurance',
        title: 'Travel Insurance',
        content: [
          'Travel insurance is not included in the package, however, the traveler, if desired, can purchase one of the Travel Health Insurance plans we offer.'
        ]
      },
      {
        icon: 'voucher',
        title: 'Vouchers and Air Tickets',
        content: [
          'Vouchers with final service confirmations and Domestic Air Tickets are sent approximately 30 to 15 days before the departure date to the destination.',
          'The International Air ticket will be delivered at the time of purchase when the acquisition is made through our services.'
        ]
      },
      {
        icon: 'tours',
        title: 'Tours and Services in the Itinerary',
        content: [
          'The Agency undertakes to fulfill all items and services mentioned as included, the only authentic interpretation of the travel itinerary that is presented by the organizing agency in its descriptive itinerary.',
          'For the execution of the trip or even during it, for technical or operational reasons, the order or logistics of the described tours may eventually undergo changes in sequence without prior notice, however preserving all previously agreed tours.',
          'Occasionally, services such as hotels may undergo changes due to availability, contractual breach, overbooking, tariff disagreements, or other aspects. They will be replaced by other hotels of the same initially planned category.'
        ]
      },
      {
        icon: 'unused',
        title: 'Services Provided and Not Enjoyed',
        content: [
          'If an included service is provided and the participant does not enjoy it, there will be no financial refund, no charges or reimbursement, and no substitution or exchange of services due to the participant\'s decision not to use that service during the trip.'
        ]
      },
      {
        icon: 'optional',
        title: 'Complementary or Optional Services',
        content: [
          'Complementary or Optional Services are not included in the final price of the itinerary and will be included upon extra request and acquisition.',
          'In case of any service or tour organized by the participant themselves, outside the services or knowledge of the organizing agency, it will be the sole responsibility of the participant.'
        ]
      },
      {
        icon: 'reschedule',
        title: 'Rescheduling of Dates and Changes',
        content: [
          'For rescheduling the travel date and/or service times that include programming and/or prior reservations, applicable fees and penalties will be considered, according to the specific policy of each respective supplier.',
          'Requests for possible changes must be communicated in writing to this Agency; requests of a purely verbal nature will not be accepted.'
        ]
      },
      {
        icon: 'plane',
        title: 'Air Service',
        content: [
          'Once the air ticket(s) is issued, any date change, schedule change, cancellation, refund request will be carried out through the specific procedure of each airline and is subject to the fare rule policy.',
          'Air tickets are nominal, non-transferable, and non-re-routable.',
          'Special airfares with promotional values and/or group travel have their own fare policy and there is no refund in case of no-show.'
        ]
      },
      {
        icon: 'baggage',
        title: 'Baggage Limits',
        content: [
          'The baggage allowance on air segments follows special rules of the Airlines responsible and may vary depending on the airline, fare, flight class, and throughout the trip.',
          'The Agency is not responsible for baggage loss/delay under the custody of Airlines.',
          'On domestic flights or internal flights in Egypt, the limit for checked baggage is 01 piece of up to 23 Kg.'
        ]
      },
      {
        icon: 'hotel',
        title: 'Hotel Service',
        content: [
          'The Agency undertakes to provide the hotel mentioned in the itinerary presentation or a similar hotel in category.',
          'Check-in with room release occurs at 3:00 PM. Check-out is until 12:00 PM. Cruises have differentiated check-in and check-out times.',
          'Possible early check-in and/or late check-out generate additional expenses of the sole and exclusive responsibility of the participants.',
          'The Agency and its partners do not guarantee the reservation of rooms with double beds, or connecting rooms for families. Meeting the requests is subject to hotel availability at the time of check-in.'
        ]
      },
      {
        icon: 'accommodation',
        title: 'Types of Accommodation',
        content: [
          'SGL: 1 person single in the room.',
          'DBL: 2 people sharing the same room.',
          'TPL: 3 people sharing the same room.',
          'Note: In the case of triple room sharing, the third accommodation is an extra bed and may present a layout different from the standard room layout.'
        ]
      },
      {
        icon: 'star',
        title: 'Hotel and Cruise Classification',
        content: [
          'Our packages use a star rating standard: from 4-star standard, 4-star superior, 5-star standard, 5-star Luxury, and 5-star Superluxury.',
          'The boats that operate the Nile cruises we offer are from category 5-star Standard, 5-star Luxury, and 5-star Superluxury.',
          'We do not work with 3-star hotels or lower.',
          'We do not work with 4-star cruises or lower.'
        ]
      },
      {
        icon: 'bus',
        title: 'Transportation',
        content: [
          'Transfers and tours included in a package/itinerary will be made by car, van/minibus, or bus, modern model with air conditioning, according to the number of travelers.',
          'The arrival and departure transfer at the airport, in case of groups or when the participant arrives/departs at a different time from the standard, generates an adjustment for an exclusive transfer service.'
        ]
      },
      {
        icon: 'tax',
        title: 'Tourism Taxes',
        content: [
          'In general, in Egypt, the price of the land package or itinerary includes the resort fee, tour fees, and tourism tax.',
          'It does not include service charges, tips, restaurants, bars, and other related fees.',
          'In some destinations, there is a Tourism Tax and Resort/Hotel Fees to be paid by the participant.'
        ]
      },
      {
        icon: 'child',
        title: 'Child Policy in Land Packages',
        content: [
          'Child WITHOUT extra bed:',
          '• Under 2 years (traveling on lap): involved fees according to each itinerary.',
          '• From 2 to under 7 years: 50% DISCOUNT ON THE DOUBLE VALUE, PER PERSON.',
          '• From 7 to under 12 years: 25% DISCOUNT ON THE DOUBLE VALUE, PER PERSON.',
          '',
          'Child WITH extra bed:',
          '• Under 2 years (traveling on lap): involved fees according to each itinerary.',
          '• From 2 to under 7 years: 30% DISCOUNT ON THE DOUBLE VALUE, PER PERSON.',
          '• From 7 to under 12 years: 15% DISCOUNT ON THE DOUBLE VALUE, PER PERSON.'
        ]
      },
      {
        icon: 'cancel',
        title: 'Cancellation and Refund',
        content: [
          'According to these Terms and Conditions, all cancellations must be requested in writing and verbal-only requests will not be validated.',
          'According to the participants\' withdrawal period, in relation to the travel execution date, penalties and cancellation fees for reservations are applied, as well as administrative expenses and services involved.'
        ]
      },
      {
        icon: 'refund',
        title: 'Rules and Conditions Regarding Refund',
        content: [
          'The amount to be refunded considers the difference between the amount paid by the participant and the penalties and fees applied due to the withdrawal period.',
          'The agency will have a period of up to 45 business days to affect the financial refund, counted from the date of withdrawal communication.',
          'For purchases made by credit card, the refund follows the procedures, rules, and deadlines of the credit card administrator.'
        ]
      },
      {
        icon: 'shared',
        title: 'Shared Accommodations without Prior Companion',
        content: [
          'Passengers without a prior companion who wish to share a room will be conditionally accepted upon signature of a knowledge term.',
          'If it is not possible to find a companion to share the room, passengers must supplement the payment according to the room type, with payment made up to 7 days before the trip.',
          'The agency disclaims any responsibility regarding affinities and/or possible incompatibilities among passengers during the trip.'
        ]
      },
      {
        icon: 'notincluded',
        title: 'Services Not Included',
        content: [
          'All services not expressly listed in the program are considered not included.',
          'Examples: personal expenses, embarkation/port fees, optional tours, additional services, additional overnight stays, documentation expenses, consular visas, excess baggage fees, phone calls, tips, porters, laundry, fines for air ticket reissuance and/or date changes.'
        ]
      },
      {
        icon: 'money',
        title: 'Financial Values',
        content: [
          'The financial values disclosed are presented per person and in US dollars, according to the chosen accommodation.',
          'All fares and conditions published in our price tables are subject to change without prior notice, according to availability, exchange rate variations, tax adjustments, fare adjustments, fuel adjustments, etc.'
        ]
      },
      {
        icon: 'validity',
        title: 'Itinerary Validity and Value Update',
        content: [
          'Each itinerary operates with specific departure dates within a determined period.',
          'The published prices are valid only for the listed dates. Requests outside these dates require a new quote (variation of up to 40%).',
          'Published values may vary due to: Season (high/low/medium), Hotel availability, Promotional airfares, Monetary exchange (USD/EUR/EGP).',
          'Customization of standard itinerary, number of travelers, and additional services generate a new quote with its own validity.',
          'Average blocking period for customized packages: 72h after confirmation.'
        ]
      },
      {
        icon: 'payment',
        title: 'Acquisition Facilities',
        content: [
          'We have several acquisition facilities:',
          '1. Down payment + fixed installments in Brazilian Reais on VISA or MASTERCARD credit cards without interest.',
          '2. Full amount with DISCOUNT via PIX or bank TED transfer.',
          '3. Full amount via Link in US Dollars on VISA or MASTERCARD credit card.'
        ]
      },
      {
        icon: 'safety',
        title: 'Safety Standards',
        content: [
          'Due to safety standards from the Ministry of Tourism, when the participant undertakes tours involving some risk or extra demand on physical capacity (deep-sea diving, hot air balloon ride in Luxor, entry into the Great Pyramid galleries, ascent to Mount Sinai, etc.), a liability waiver will be requested.',
          'The participant is aware of the possible risks and physical demands involved.'
        ]
      },
      {
        icon: 'responsibility',
        title: 'Responsibility',
        content: [
          'The Agency is responsible for the planning, organization, and execution of the program.',
          'The Agency is not responsible for delays, advancements, or changes in schedules and cancellation of excursions due to weather conditions, natural disasters, government decisions, acts of terrorism, robberies, thefts, and other reasons of force majeure.',
          'Any personal expenses motivated by such circumstances are the passenger\'s responsibility.'
        ]
      },
      {
        icon: 'claims',
        title: 'Rules and Conditions Regarding Claims',
        content: [
          'In cases of services proven not to be provided due to the organizers\' responsibility, the amounts corresponding to the specific service not provided will be refunded.',
          'All claims must be presented in writing with applicable supporting documentation within 30 days from the arrival date.',
          'The refund, when applicable, must occur within up to 45 days after the consumer\'s written request.',
          'After this period, the contractual relationship will be considered perfect and finalized.'
        ]
      }
    ]
  },
  es: {
    title: 'Términos y Condiciones',
    subtitle: 'Consulte detalles sobre nuestras reglas y condiciones generales, desde la garantía de reserva y documentación hasta normas de seguridad.',
    intro: 'Presentamos para usted reglas y condiciones generales desde la garantía de reserva y documentación hasta normas sanitarias. Estas reglas y condiciones tratan todos los temas que un viajero desea conocer. Por favor, lea con atención y si tiene dudas, contáctenos.',
    backToHome: 'Volver al Inicio',
    sections: [
      {
        icon: 'shield',
        title: 'Garantía de Reserva',
        content: [
          'Las reservas del circuito están sujetas a disponibilidad y solo están garantizadas después de la adquisición efectuada mediante la realización del pago.'
        ]
      },
      {
        icon: 'passport',
        title: 'Documentación para el Viaje',
        content: [
          'El Pasaporte es un documento personal e intransferible. El Pasaporte deberá estar válido por mínimo 6 meses de validez a contar de la fecha de entrada en el país de destino; también debe contener el visado solicitado (para los países que soliciten emisión de visado previamente).',
          'Los menores desacompañados, o en compañía solo del padre o de la madre o de un responsable, necesitarán autorización especial para viajar al exterior, aun teniendo pasaporte y visado previo (cuando aplique).'
        ]
      },
      {
        icon: 'visa',
        title: 'Visado de entrada en Egipto',
        content: [
          'Es necesario para entrar en Egipto obtener el Visado. Existen 3 maneras de obtener el Visado de Egipto:',
          '• Visado Electrónico en línea por el portal del gobierno de Egipto (Egypt e-Visa Portal). Brasil y Portugal están entre los países permitidos para obtener un e-Visado.',
          '• Al llegar al aeropuerto Internacional de El Cairo - no está condicionado a la obtención previa del visado consular.',
          '• Visado consular solicitado por el consulado de la República Árabe de Egipto.'
        ]
      },
      {
        icon: 'airport',
        title: 'Formalidades en los Aeropuertos',
        content: [
          'Si el viajero llena y firma formularios en los aeropuertos sobre su caso médico, es de exclusiva responsabilidad del pasajero.',
          'Los pasajeros deben seguir y respetar todas las formalidades de entrada y salida y Aduana, además de las medidas y regulaciones sanitarias aplicadas en aeropuertos, hoteles, restaurantes y lugares turísticos.'
        ]
      },
      {
        icon: 'insurance',
        title: 'Seguro de Viaje',
        content: [
          'El Seguro de viaje no está incluido en el paquete, sin embargo, el viajero, si lo desea, puede comprar uno de los planes de Seguro de Salud de Viaje que ofrecemos.'
        ]
      },
      {
        icon: 'voucher',
        title: 'Vouchers y Billetes Aéreos',
        content: [
          'Los vouchers con las confirmaciones finales de los servicios y los Billetes Aéreos Internos se envían aproximadamente 30 a 15 días antes de la fecha de embarque al destino.',
          'El billete aéreo Internacional será entregado en el acto de la compra cuando la adquisición se realice a través de nuestros servicios.'
        ]
      },
      {
        icon: 'tours',
        title: 'Excursiones y Servicios en el circuito',
        content: [
          'La Agencia se compromete a cumplir todos los ítems y servicios citados como incluidos, siendo que la única interpretación auténtica del circuito del viaje será aquella presentada por la agencia organizadora, en su circuito descriptivo.',
          'Para la ejecución del viaje o incluso durante el mismo, por razones técnicas u operacionales, el orden o la logística de realización de las excursiones descritas puede, eventualmente, sufrir modificaciones en la secuencia sin aviso previo, sin embargo preservando todas las excursiones previamente acordadas.',
          'Eventualmente, servicios como hoteles pueden sufrir alteraciones por motivos de disponibilidad, quiebra contractual, overbooking, desacuerdo sobre tarifas u otros aspectos. Serán sustituidos por otros hoteles de la misma categoría inicialmente prevista.'
        ]
      },
      {
        icon: 'unused',
        title: 'Servicios disponibles y no usufructuados',
        content: [
          'En caso de que un servicio incluido sea disponible y el participante no lo usufructúe, no habrá devolución financiera, ningún gravamen o resarcimiento, ni sustitución o cambio de servicios, en función de la desistencia del participante de utilizar aquel servicio durante el viaje.'
        ]
      },
      {
        icon: 'optional',
        title: 'Servicios Complementarios u Opcionales',
        content: [
          'Los Servicios Complementarios u Opcionales no están incluidos en el valor final del circuito y serán incluidos mediante solicitud y adquisición extra.',
          'En caso de cualquier servicio o excursión organizado por el propio participante, fuera de los servicios o del conocimiento de la agencia organizadora, será de entera responsabilidad del participante.'
        ]
      },
      {
        icon: 'reschedule',
        title: 'Remarcaciones de Fechas y Alteraciones',
        content: [
          'Para remarcación de fecha del viaje y/o horarios de servicios que incluyan programación y/o reservas previas, serán consideradas tasas y multas involucradas, conforme la política específica de cada respectivo proveedor.',
          'La solicitud de posibles alteraciones debe ser comunicada por escrito a esta Agencia, no siendo aceptadas solicitudes solo de carácter verbal.'
        ]
      },
      {
        icon: 'plane',
        title: 'Servicio Aéreo',
        content: [
          'Una vez emitido(s) el(los) billete(s) aéreo(s), cualquier cambio de fecha, cambio de horario, cancelación, pedido de reembolso será realizado a través del procedimiento específico de cada compañía aérea y está sujeto a la política de la regla tarifaria.',
          'Los billetes aéreos son nominales, intransferibles y no re-intinerables.',
          'Tarifas aéreas especiales con valores de ofertas y/o de viajes en grupo poseen su política propia de tarifas y no hay resarcimiento en caso de no comparecencia.'
        ]
      },
      {
        icon: 'baggage',
        title: 'Límites de Equipaje',
        content: [
          'La franquicia de equipaje en los tramos aéreos obedece a reglas especiales de las Cías Aéreas involucradas y puede variar en función de la compañía aérea, de la tarifa, de la clase del vuelo y a lo largo del viaje.',
          'La Agencia no es responsable por el extravío de equipajes custodiados por las Cías. Aéreas.',
          'En los vuelos domésticos o internos en Egipto, el límite para despachar es 01 pieza de hasta 23 Kg.'
        ]
      },
      {
        icon: 'hotel',
        title: 'Servicio de Hotelería',
        content: [
          'La Agencia se compromete a disponibilizar el hotel citado en la presentación del circuito o hotel similar en la categoría.',
          'El Check-in con liberación para entrada en las habitaciones ocurre a las 15:00h. El Check-out ocurre hasta las 12:00h. Los cruceros tienen horarios de Check-in y check-out diferenciados.',
          'La posible anticipación del check-in y/o postergación en el Check-out generan gastos adicionales de única y exclusiva responsabilidad de los participantes.',
          'La Agencia y sus socias no garantizan la reserva de apartamentos con camas de matrimonio, o habitaciones conectadas para familias. La atención a las solicitudes se encuentra sujeta a disponibilidad de los hoteles en el acto del Check-in.'
        ]
      },
      {
        icon: 'accommodation',
        title: 'Tipos de Alojamiento',
        content: [
          'SGL: 1 persona individual en la habitación.',
          'DBL: 2 personas compartiendo la misma habitación.',
          'TPL: 3 personas compartiendo la misma habitación.',
          'Nota: En el caso del alojamiento triple, la tercera acomodación es una cama extra y puede presentar un layout diferente del layout estándar de la habitación.'
        ]
      },
      {
        icon: 'star',
        title: 'Clasificación de Hoteles y Cruceros',
        content: [
          'Nuestros paquetes utilizan el estándar de número de estrellas: a partir de 4 estrellas estándar, 4 estrellas superior, 5 estrellas estándar, 5 estrellas Lujo y 5 estrellas superlujo.',
          'Los barcos que realizan los cruceros en el Nilo que ofrecemos son a partir de categoría 5 estrellas Estándar, 5 estrellas Lujo y 5 estrellas superlujo.',
          'No trabajamos con hoteles categoría 3 estrellas o inferior.',
          'No trabajamos con cruceros categoría 4 estrellas o inferior.'
        ]
      },
      {
        icon: 'bus',
        title: 'Transporte',
        content: [
          'Los traslados y excursiones incluidos en un paquete/circuito se harán en auto, van/microbús o autobús, de modelo moderno con aire acondicionado, conforme al número de viajantes.',
          'El traslado de llegada y salida en el aeropuerto, en caso de grupos o cuando el participante llegue/salga en horario diferente del estándar, genera ajuste en el servicio exclusivo de traslado.'
        ]
      },
      {
        icon: 'tax',
        title: 'Impuestos de turismo',
        content: [
          'En general, en Egipto, el precio del paquete terrestre o circuito incluye la tasa de resort, tasas de tours y tasa de turismo.',
          'No incluye tasas de propinas, servicios, restaurantes, bares y otras afines.',
          'En algunos destinos existe Impuesto de turismo y Tasas de resort y/o de hotel a ser pagados por el participante.'
        ]
      },
      {
        icon: 'child',
        title: 'Política de Niños en los paquetes terrestres',
        content: [
          'Niño SIN cama adicional:',
          '• Menos de 2 años (viajando en el regazo): tasas involucradas conforme cada circuito.',
          '• De 2 a menores de 7 años: 50% DE DESCUENTO EN EL VALOR DOBLE, POR PERSONA.',
          '• De 7 a menores de 12 años: 25% DE DESCUENTO EN EL VALOR DOBLE, POR PERSONA.',
          '',
          'Niño CON cama adicional:',
          '• Menos de 2 años (viajando en el regazo): tasas involucradas conforme cada circuito.',
          '• De 2 a menores de 7 años: 30% DE DESCUENTO EN EL VALOR DOBLE, POR PERSONA.',
          '• De 7 a menores de 12 años: 15% DE DESCUENTO EN EL VALOR DOBLE, POR PERSONA.'
        ]
      },
      {
        icon: 'cancel',
        title: 'De la Cancelación y Reembolso',
        content: [
          'Conforme estos Términos y Condiciones, todas las cancelaciones deberán ser solicitadas por escrito y no serán validadas solicitudes solo verbales.',
          'Conforme el plazo de desistencia del participante, en relación a la fecha de realización del viaje se aplican multas y tarifas de cancelaciones de reservas, así como gastos administrativos y servicios involucrados.'
        ]
      },
      {
        icon: 'refund',
        title: 'Reglas y Condiciones Sobre Devolución y Reembolso',
        content: [
          'El valor a ser devuelto considera la diferencia entre el valor pagado por el participante y las penalidades de multa y tarifas aplicadas en función del plazo de desistencia.',
          'La agencia tendrá un plazo de hasta 45 días útiles para efectuar la devolución del valor financiero, contado de la fecha de comunicación de la desistencia.',
          'Para compras realizadas por tarjeta de crédito, la devolución sigue los procedimientos, las normas y plazos de la administradora de la tarjeta de crédito.'
        ]
      },
      {
        icon: 'shared',
        title: 'Alojamientos compartidos sin acompañante previo',
        content: [
          'Pasajeros sin acompañante previo y que desean compartir la habitación serán aceptados condicionalmente y mediante firma de un término de conocimiento.',
          'Si no fuese posible conseguir compañía para compartir la habitación, los pasajeros deberán complementar el pago de acuerdo con el tipo de habitación, con el pago realizado hasta 7 días antes del viaje.',
          'La agencia se exime de cualquier responsabilidad en relación a afinidades y/o posibles incompatibilidades entre los pasajeros durante el viaje.'
        ]
      },
      {
        icon: 'notincluded',
        title: 'Servicios no Incluidos',
        content: [
          'Son considerados no incluidos todos los servicios que no constaren expresamente en el programa.',
          'Ejemplos: gastos personales, tasas de embarque/portuarias, excursiones opcionales, servicios adicionales, pernoctes adicionales, gastos con documentación, visados consulares, tasas por exceso de equipaje, llamadas telefónicas, propinas, maleteros, lavandería, multas por reemisión de billetes aéreos y/o alteraciones de fechas.'
        ]
      },
      {
        icon: 'money',
        title: 'Valores Financieros',
        content: [
          'Los valores financieros divulgados son presentados por persona y en dólares americanos, conforme alojamiento escogido.',
          'Todas las tarifas y condiciones publicadas en nuestras tablas de precios están sujetas a alteraciones sin aviso previo, conforme disponibilidad, variaciones cambiarias, ajustes de impuestos, ajustes de tarifas, ajuste de combustibles, etc.'
        ]
      },
      {
        icon: 'validity',
        title: 'Validez del Circuito y Actualización de Valores',
        content: [
          'Cada circuito opera con fechas de salida específicas dentro de un período determinado.',
          'Los precios publicados son válidos solo para las fechas listadas. Solicitudes fuera de esas fechas exigen nuevo presupuesto (variación de hasta 40%).',
          'Los valores publicados pueden variar por: Temporada (alta/baja/media), Disponibilidad hotelera, Tarifas aéreas promocionales, Cambio monetario (USD/EUR/EGP).',
          'Personalización del circuito estándar, número de viajeros y servicios adicionales generan nuevo presupuesto con validez propia.',
          'Plazo medio de bloqueo para paquetes personalizados: 72h después de confirmación.'
        ]
      },
      {
        icon: 'payment',
        title: 'Facilidades de adquisición',
        content: [
          'Tenemos varias facilidades de adquisición:',
          '1. Entrada + cuotas fijas en reales brasileños en tarjetas de crédito VISA o MASTERCARD sin intereses.',
          '2. Integral con DESCUENTO vía PIX o transferencia bancaria TED.',
          '3. Integral vía Link en dólares americanos en tarjeta de crédito VISA o MASTERCARD.'
        ]
      },
      {
        icon: 'safety',
        title: 'Normas de Seguridad',
        content: [
          'Por normas de seguridad del Ministerio de Turismo, cuando el participante realice excursiones que involucren algún riesgo o solicitud extra de la capacidad física (buceo en alta mar, paseo panorámico de globo en Luxor, entrada al interior de las galerías de la Gran Pirámide, subida al Monte Sinaí, etc.), será solicitada firma del término de responsabilidad.',
          'El participante está consciente de los posibles riesgos y solicitudes físicas involucradas.'
        ]
      },
      {
        icon: 'responsibility',
        title: 'Responsabilidad',
        content: [
          'La Agencia es responsable por la planificación, organización y ejecución de la programación.',
          'La Agencia no responde por atrasos, anticipaciones o cambios de horarios y cancelación de las excursiones debido a condiciones atmosféricas, catástrofes naturales, decisiones gubernamentales, actos de terrorismo, robos, hurtos y otros motivos de fuerza mayor.',
          'Los eventuales gastos personales motivados por tales circunstancias son de responsabilidad del pasajero.'
        ]
      },
      {
        icon: 'claims',
        title: 'Reglas y Condiciones sobre Solicitudes',
        content: [
          'En los casos de servicios comprobadamente no prestados por responsabilidad de los organizadores, serán devueltas las importancias al servicio específico no prestado.',
          'Todas las solicitudes deben ser presentadas por escrito con documentaciones comprobatorias pertinentes dentro de 30 días contados de la fecha de la llegada.',
          'La devolución, cuando pertinente, deberá ocurrir en el plazo de hasta 45 días después de solicitud escrita del consumidor.',
          'Después de este plazo, la relación contractual será considerada perfecta y finalizada.'
        ]
      }
    ]
  },
  pt: {
    title: 'Termos e Condições',
    subtitle: 'Confira detalhes sobre nossas regras e condições gerais, desde a garantia de reserva e documentação até normas de segurança.',
    intro: 'Apresentamos para você as regras e condições gerais que abrangem desde a garantia de reserva e documentação até normas sanitárias. Essas regras e condições abordam todos os tópicos que um viajante deseja conhecer. Por gentileza, leia com atenção e entre em contato conosco se tiver qualquer dúvida.',
    backToHome: 'Voltar ao Início',
    sections: [
      {
        icon: 'shield',
        title: 'Garantia de Reserva',
        content: [
          'As reservas dos roteiros estão sujeitas à disponibilidade e ficam garantidas somente após a aquisição efetivada mediante a realização do pagamento.'
        ]
      },
      {
        icon: 'passport',
        title: 'Documentação para a Viagem',
        content: [
          'O Passaporte é um documento pessoal e intransferível. O Passaporte deverá possuir validade de pelo menos 6 meses a contar da data de entrada no país de destino; também deve conter o visto solicitado (para os países que exijam emissão de visto antecipadamente).',
          'Menores desacompanhados, ou na companhia apenas do pai ou da mãe ou de um responsável, necessitarão de autorização especial para viagem ao exterior, mesmo portando passaporte e visto prévio (quando aplicável).',
          'Para o passageiro brasileiro ou de América Latina é necessário o Certificado Internacional da Vacina contra Febre Amarela emitido pela ANVISA.'
        ]
      },
      {
        icon: 'visa',
        title: 'Visto de entrada no Egito',
        content: [
          'É necessário para entrar no Egito obter o Visto. Existem 3 maneiras de obter o Visto para o Egito:',
          '• Visto Eletrônico online pelo portal do governo do Egito (Egypt e-Visa Portal). Brasil e Portugal estão entre os países permitidos para obter um e-Visto.',
          '• Na chegada ao Aeroporto Internacional do Cairo - não estando condicionado à obtenção prévia do visto consular.',
          '• Visto consular solicitado junto ao consulado da República Árabe do Egito.'
        ]
      },
      {
        icon: 'airport',
        title: 'Formalidades nos Aeroportos',
        content: [
          'Se o viajante preencher e assinar formulários nos Aeroportos acerca de sua condição médica, é da exclusiva responsabilidade do passageiro.',
          'Os passageiros devem seguir e respeitar todas as formalidades de entrada e saída e da Alfândega, além das medidas e regulamentos sanitários aplicados nos aeroportos, hotéis, restaurantes e locais turísticos.'
        ]
      },
      {
        icon: 'insurance',
        title: 'Seguro Viagem',
        content: [
          'O Seguro Viagem não está incluso no pacote, porém o viajante, se desejar, pode adquirir um dos planos de Seguro Saúde Viagem que oferecemos.'
        ]
      },
      {
        icon: 'voucher',
        title: 'Vouchers e Passagens Aéreas',
        content: [
          'Os vouchers com as confirmações finais dos serviços e as Passagens Aéreas Internas são enviados cerca de 30 a 15 dias antes da data de embarque para o destino.',
          'A passagem aérea Internacional será entregue no ato da compra quando a aquisição for realizada através dos nossos serviços.'
        ]
      },
      {
        icon: 'tours',
        title: 'Passeios e Serviços no roteiro',
        content: [
          'A Agência compromete-se a cumprir todos os itens e serviços mencionados como inclusos, sendo que a única interpretação autêntica do roteiro da viagem será aquela apresentada pela agência organizadora, no seu roteiro descritivo.',
          'Para a execução da viagem ou mesmo durante a mesma, por razões técnicas ou operacionais, a ordem ou a logística de realização dos passeios descritos pode, eventualmente, sofrer modificações na sequência sem aviso prévio, preservando, no entanto, todos os passeios previamente acordados.',
          'Eventualmente, serviços como hospedagem em hotéis podem sofrer alterações por motivos de disponibilidade, quebra contratual, overbooking, desacordo sobre tarifas ou outros aspectos. Os mesmos serão substituídos por outros hotéis da mesma categoria inicialmente prevista.'
        ]
      },
      {
        icon: 'unused',
        title: 'Serviços disponibilizados e não usufruídos',
        content: [
          'No caso de um serviço incluso ser disponibilizado e o participante não usufruir do mesmo, não haverá devolução financeira, nenhum ônus ou ressarcimento e nem substituição ou troca de serviços, em função da desistência do participante de utilizar aquele serviço durante a viagem.'
        ]
      },
      {
        icon: 'optional',
        title: 'Serviços Complementares ou Opcionais',
        content: [
          'Serviços Complementares ou Opcionais não estão inclusos no valor final do roteiro e serão incluídos mediante solicitação e aquisição extra.',
          'No caso de qualquer serviço ou passeio organizado pelo próprio participante, fora dos serviços ou do conhecimento da agência organizadora, será de inteira responsabilidade do participante.'
        ]
      },
      {
        icon: 'reschedule',
        title: 'Remarcações de Datas e Alterações',
        content: [
          'Para remarcação da data da viagem e/ou horários de serviços que incluam programação e/ou reservas prévias, serão consideradas as taxas e multas envolvidas, conforme a política específica de cada respectivo fornecedor.',
          'A solicitação de possíveis alterações devem ser comunicada por escrito a esta Agência, não sendo aceitas solicitações apenas de caráter verbal.'
        ]
      },
      {
        icon: 'plane',
        title: 'Serviço Aéreo',
        content: [
          'Uma vez emitido(s) o(s) bilhete(s) aéreo(s), qualquer mudança de data, mudança de horário, cancelamento, pedido de reembolso será realizado através do procedimento específico de cada companhia aérea e está sujeito à política da regra tarifária.',
          'Os bilhetes aéreos são nominais, intransferíveis e não reembolsáveis.',
          'Tarifas aéreas especiais com valores promocionais e/ou de viagens em grupo possuem política própria de tarifas e não há ressarcimento em caso de não comparecimento.'
        ]
      },
      {
        icon: 'baggage',
        title: 'Limites de Bagagem',
        content: [
          'A franquia de bagagem nos trechos aéreos obedece a regras especiais das Cias Aéreas envolvidas, podendo variar em função da companhia aérea, da tarifa, da classe do voo e ao longo da viagem.',
          'A Agência não é responsável pelo extravio de bagagens custodiadas pelas Cias. Aéreas.',
          'Nos voos domésticos ou internos no Egito, o limite para bagagem despachada é de 01 peça de até 23 Kg.'
        ]
      },
      {
        icon: 'hotel',
        title: 'Serviço de Hotelaria',
        content: [
          'A Agência compromete-se a disponibilizar o hotel citado na apresentação do roteiro ou hotel similar na categoria.',
          'O Check-in com liberação para entrada nos quartos acontece às 15:00h. O Check-out acontece até às 12:00h. Os cruzeiros têm horários de Check-in e check-out diferenciados.',
          'A possível antecipação do check-in e/ou postergação no Check-out geram despesas adicionais de única e exclusiva responsabilidade dos participantes.',
          'A Agência e suas parceiras não garantem a reserva de apartamentos com camas de casal, ou quartos conectados para famílias. O atendimento às solicitações está sujeito à disponibilidade dos hotéis no ato do Check-in.'
        ]
      },
      {
        icon: 'accommodation',
        title: 'Tipos de Acomodação',
        content: [
          'SGL: 1 pessoa em quarto individual.',
          'DBL: 2 pessoas compartilhando o mesmo quarto.',
          'TPL: 3 pessoas compartilhando o mesmo quarto.',
          'Observação: No caso do compartilhamento de quarto triplo, a terceira acomodação é uma cama extra e pode apresentar layout diferente do layout padrão do quarto.'
        ]
      },
      {
        icon: 'star',
        title: 'Classificação de Hotéis e Cruzeiros',
        content: [
          'Nossos pacotes utilizam o padrão de número de estrelas: a partir de 4 estrelas standard, 4 estrelas superior, 5 estrelas standard, 5 estrelas Luxo e 5 estrelas superluxo.',
          'Os barcos que realizam os cruzeiros no Nilo que oferecemos são a partir da categoria 5 estrelas Standard, 5 estrelas Luxo e 5 estrelas superluxo.',
          'Não trabalhamos com hotéis de categoria 3 estrelas ou inferior.',
          'Não trabalhamos com cruzeiros de categoria 4 estrelas ou inferior.'
        ]
      },
      {
        icon: 'bus',
        title: 'Transporte',
        content: [
          'Os traslados e passeios inclusos em um pacote/roteiro serão feitos em carro, van/microônibus ou ônibus, de modelo moderno com ar-condicionado, conforme o número de viajantes.',
          'O traslado de chegada e saída do aeroporto, em caso de grupos ou quando o participante chegar/sair em horário diferente do padrão, gera ajuste para serviço de traslado exclusivo.'
        ]
      },
      {
        icon: 'tax',
        title: 'Impostos de turismo',
        content: [
          'Em geral, no Egito, o preço do pacote terrestre ou roteiro inclui a taxa de resort, taxas de tours e taxa de turismo.',
          'Não inclui taxas de gorjetas, serviços, restaurantes, bares e outras afins.',
          'Em alguns destinos, existe Imposto de turismo e Taxas de resort e/ou de hotel a serem pagos pelo participante.'
        ]
      },
      {
        icon: 'child',
        title: 'Política de Crianças nos pacotes terrestres',
        content: [
          'Criança SEM cama adicional:',
          '• Menos de 2 anos (viajando ao colo): taxas envolvidas conforme cada roteiro.',
          '• De 2 a menores de 7 anos: 50% DE DESCONTO NO VALOR DO DUPLO, POR PESSOA.',
          '• De 7 a menores de 12 anos: 25% DE DESCONTO NO VALOR DO DUPLO, POR PESSOA.',
          '',
          'Criança COM cama adicional:',
          '• Menos de 2 anos (viajando ao colo): taxas envolvidas conforme cada roteiro.',
          '• De 2 a menores de 7 anos: 30% DE DESCONTO NO VALOR DO DUPLO, POR PESSOA.',
          '• De 7 a menores de 12 anos: 15% DE DESCONTO NO VALOR DO DUPLO, POR PESSOA.'
        ]
      },
      {
        icon: 'cancel',
        title: 'Do Cancelamento e Reembolso',
        content: [
          'Conforme estes Termos e Condições, todos os cancelamentos deverão ser solicitados por escrito e não serão validadas solicitações apenas verbais.',
          'Conforme o prazo de desistência do participante, em relação à data de realização da viagem, são aplicadas multas e tarifas de cancelamento de reservas, bem como despesas administrativas e serviços envolvidos.'
        ]
      },
      {
        icon: 'refund',
        title: 'Regras e Condições Sobre Devolução e Reembolso',
        content: [
          'O valor a ser devolvido considera a diferença entre o valor pago pelo participante e as penalidades de multa e tarifas aplicadas em função do prazo de desistência.',
          'A agência terá um prazo de até 45 dias úteis para efetuar a devolução do valor financeiro, contado da data de comunicação da desistência.',
          'Para compras realizadas por cartão de crédito, a devolução segue os procedimentos, as normas e prazos da administradora do cartão de crédito.'
        ]
      },
      {
        icon: 'shared',
        title: 'Acomodações compartilhadas sem acompanhante prévio',
        content: [
          'Passageiros sem acompanhante prévio e que desejam compartilhar o quarto serão aceitos condicionalmente e mediante assinatura de termo de ciência.',
          'Se não for possível conseguir companhia para compartilhar o quarto, os passageiros deverão complementar o pagamento de acordo com o tipo de quarto, com o pagamento realizado até 7 dias antes da viagem.',
          'A agência isenta-se de qualquer responsabilidade em relação a afinidades e/ou possíveis incompatibilidades entre os passageiros durante a viagem.'
        ]
      },
      {
        icon: 'notincluded',
        title: 'Serviços não Incluídos',
        content: [
          'São considerados não incluídos todos os serviços que não constarem expressamente no programa.',
          'Exemplos: despesas pessoais, taxas de embarque/portuárias, passeios opcionais, serviços adicionais, pernoites adicionais, despesas com documentação, vistos consulares, taxas por excesso de bagagem, telefonemas, gorjetas, maleteiros, lavanderia, multas por reemissão de bilhetes aéreos e/ou alterações de datas.'
        ]
      },
      {
        icon: 'money',
        title: 'Valores Financeiros',
        content: [
          'Os valores financeiros divulgados são apresentados por pessoa e em dólares americanos, conforme a acomodação escolhida.',
          'Todas as tarifas e condições publicadas em nossas tabelas de preços estão sujeitas a alterações sem aviso prévio, conforme a disponibilidade, variações cambiais, ajustes de impostos, ajustes de tarifas, ajuste de combustíveis, etc.'
        ]
      },
      {
        icon: 'validity',
        title: 'Validade do Roteiro e Atualização de Valores',
        content: [
          'Cada roteiro opera com datas de saída específicas dentro de um período determinado.',
          'Os preços publicados são válidos apenas para as datas listadas. Solicitações fora dessas datas exigem novo orçamento (variação de até 40%).',
          'Os valores publicados podem variar devido a: Temporada (alta/baixa/média estação), Disponibilidade hoteleira, Tarifas aéreas promocionais, Câmbio monetário (USD/EUR/EGP).',
          'Personalização do roteiro padrão, número de viajantes e serviços adicionais geram novo orçamento com validade própria.',
          'Prazo médio de bloqueio para pacotes personalizados: 72h após confirmação.'
        ]
      },
      {
        icon: 'payment',
        title: 'Facilidades de aquisição',
        content: [
          'Temos várias facilidades de aquisição:',
          '1. Entrada + parcelas fixas em reais brasileiros nos cartões de crédito VISA ou MASTERCARD sem juros.',
          '2. Integral com DESCONTO via PIX ou TED bancário.',
          '3. Integral via Link em dólares americanos no cartão de crédito VISA ou MASTERCARD.'
        ]
      },
      {
        icon: 'safety',
        title: 'Normas de Segurança',
        content: [
          'Por normas de segurança do Ministério do Turismo, quando o participante realizar passeios que envolvam algum risco ou exigência extra da capacidade física (mergulho em alto mar, passeio panorâmico de balão em Luxor, entrada no interior das galerias da Grande Pirâmide, subida ao Monte Sinai, etc.), será solicitada a assinatura de termo de responsabilidade.',
          'O participante está ciente dos possíveis riscos e exigências físicas envolvidas.'
        ]
      },
      {
        icon: 'responsibility',
        title: 'Responsabilidade',
        content: [
          'A Agência é responsável pelo planejamento, organização e execução da programação.',
          'A Agência não responde por atrasos, antecipações ou mudanças de horários e cancelamento das excursões decorrentes de condições atmosféricas, catástrofes naturais, decisões governamentais, atos de terrorismo, roubos, furtos e outros motivos de força maior.',
          'Os eventuais gastos pessoais motivados por tais circunstâncias são de responsabilidade do passageiro.'
        ]
      },
      {
        icon: 'claims',
        title: 'Regras e Condições sobre Solicitações',
        content: [
          'Nos casos de serviços comprovadamente não prestados por responsabilidade dos organizadores, serão devolvidas as importâncias referentes ao serviço específico não prestado.',
          'Todas as solicitações devem ser apresentadas por escrito com documentações comprobatórias cabíveis no prazo de 30 dias contados da data da chegada.',
          'A devolução, quando cabível, deverá ocorrer no prazo de até 45 dias após solicitação escrita do consumidor.',
          'Após este prazo, a relação contratual será considerada perfeita e finalizada.'
        ]
      }
    ]
  }
};

const getIcon = (iconName: string) => {
  const icons: Record<string, React.ComponentType<{ className?: string }>> = {
    shield: Shield,
    passport: BookOpen,
    visa: FileText,
    airport: Plane,
    insurance: Shield,
    voucher: FileText,
    tours: FileText,
    unused: XCircle,
    optional: FileText,
    reschedule: Calendar,
    plane: Plane,
    baggage: FileText,
    hotel: Hotel,
    accommodation: Hotel,
    star: FileText,
    bus: Bus,
    tax: CreditCard,
    child: Baby,
    cancel: XCircle,
    refund: CreditCard,
    shared: Hotel,
    notincluded: XCircle,
    money: CreditCard,
    validity: Calendar,
    payment: ShoppingCart,
    safety: Lock,
    responsibility: Scale,
    claims: FileCheck
  };
  return icons[iconName] || FileText;
};

export default function TermsPage() {
  const { language } = useLanguageStore();
  const t = content[language];

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
              {t.title}
            </h1>
            <p className="text-xl text-white/80 max-w-3xl mx-auto">
              {t.subtitle}
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
            {t.backToHome}
          </Link>

          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className="prose prose-lg max-w-none"
          >
            <p className="text-gray-500 mb-8">
              {language === 'en' ? 'Last updated: January 2025' : language === 'es' ? 'Última actualización: Enero 2025' : 'Última atualização: Janeiro 2025'}
            </p>

            <div className="bg-primary-50 rounded-xl p-6 mb-10">
              <p className="text-gray-700 text-lg leading-relaxed m-0">
                {t.intro}
              </p>
            </div>

            <div className="space-y-8">
              {t.sections.map((section, index) => {
                const IconComponent = getIcon(section.icon);
                return (
                  <motion.div
                    key={index}
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ delay: index * 0.05 }}
                    className="bg-white rounded-xl border border-gray-100 shadow-sm overflow-hidden"
                  >
                    <div className="bg-gray-50 px-6 py-4 border-b border-gray-100">
                      <div className="flex items-center gap-3">
                        <div className="w-10 h-10 rounded-lg bg-primary-100 flex items-center justify-center">
                          <IconComponent className="w-5 h-5 text-primary-600" />
                        </div>
                        <h2 className="text-xl font-bold text-gray-900 m-0">
                          {section.title}
                        </h2>
                      </div>
                    </div>
                    <div className="px-6 py-4">
                      {section.content.map((paragraph, pIndex) => (
                        <p key={pIndex} className={`text-gray-600 ${paragraph === '' ? 'h-2' : ''} ${pIndex === section.content.length - 1 ? 'm-0' : 'mb-3'}`}>
                          {paragraph}
                        </p>
                      ))}
                    </div>
                  </motion.div>
                );
              })}
            </div>

            {/* Quality Standards Highlight */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              className="mt-12 bg-gradient-to-r from-primary-600 to-primary-700 rounded-xl p-8 text-white"
            >
              <h3 className="text-2xl font-bold mb-4 text-white">
                {language === 'en' ? 'Our Quality Standards' : language === 'es' ? 'Nuestros Estándares de Calidad' : 'Nossos Padrões de Qualidade'}
              </h3>
              <p className="text-white/90 mb-4">
                {language === 'en'
                  ? 'We rigorously select partners that reflect our commitment to excellence:'
                  : language === 'es'
                  ? 'Seleccionamos rigurosamente socios que reflejen nuestro compromiso con la excelencia:'
                  : 'Selecionamos rigorosamente parceiros que refletem nosso compromisso com a excelência:'}
              </p>
              <div className="grid md:grid-cols-2 gap-4">
                <div className="bg-white/10 rounded-lg p-4">
                  <div className="flex items-center gap-2 mb-2">
                    <Hotel className="w-5 h-5" />
                    <span className="font-semibold">
                      {language === 'en' ? 'Hotels' : language === 'es' ? 'Hoteles' : 'Hotéis'}
                    </span>
                  </div>
                  <p className="text-white/80 text-sm m-0">
                    {language === 'en'
                      ? 'We work exclusively with establishments from 4 stars or higher, ensuring comfort and premium services.'
                      : language === 'es'
                      ? 'Trabajamos exclusivamente con establecimientos a partir de 4 estrellas, garantizando confort y servicios premium.'
                      : 'Trabalhamos exclusivamente com estabelecimentos a partir de 4 estrelas, garantindo conforto e serviços premium.'}
                  </p>
                </div>
                <div className="bg-white/10 rounded-lg p-4">
                  <div className="flex items-center gap-2 mb-2">
                    <Ship className="w-5 h-5" />
                    <span className="font-semibold">
                      {language === 'en' ? 'Cruises' : language === 'es' ? 'Cruceros' : 'Cruzeiros'}
                    </span>
                  </div>
                  <p className="text-white/80 text-sm m-0">
                    {language === 'en'
                      ? 'We operate only luxury category (5-star) vessels, ensuring memorable experiences on the Nile and Red Sea.'
                      : language === 'es'
                      ? 'Operamos solo embarcaciones de categoría lujo (5 estrellas), asegurando experiencias memorables en el Nilo y Mar Rojo.'
                      : 'Operamos apenas embarcações de categoria luxo (5 estrelas), assegurando experiências memoráveis no Nilo e Mar Vermelho.'}
                  </p>
                </div>
              </div>
            </motion.div>

            {/* Contact Section */}
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              whileInView={{ opacity: 1, y: 0 }}
              viewport={{ once: true }}
              className="mt-12 text-center"
            >
              <h3 className="text-2xl font-bold text-gray-900 mb-4">
                {language === 'en' ? 'Questions about these terms?' : language === 'es' ? '¿Preguntas sobre estos términos?' : 'Dúvidas sobre estes termos?'}
              </h3>
              <p className="text-gray-600 mb-6">
                {language === 'en'
                  ? 'Contact us and we will be happy to help you.'
                  : language === 'es'
                  ? 'Contáctenos y estaremos encantados de ayudarle.'
                  : 'Entre em contato conosco e teremos prazer em ajudá-lo.'}
              </p>
              <Link
                href="/contact"
                className="inline-flex items-center gap-2 bg-primary-600 text-white px-6 py-3 rounded-lg font-medium hover:bg-primary-700 transition-colors"
              >
                {language === 'en' ? 'Contact Us' : language === 'es' ? 'Contáctenos' : 'Fale Conosco'}
              </Link>
            </motion.div>
          </motion.div>
        </div>
      </section>
    </main>
  );
}
