"""
Script to add default FAQs to all tours with translations.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.base')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

from apps.tours.models import Tour, TourFAQ

# Default FAQs for tours (English, Spanish, Portuguese)
DEFAULT_FAQS = [
    {
        'question': 'What is included in the tour price?',
        'question_es': '¿Qué está incluido en el precio del tour?',
        'question_pt': 'O que está incluído no preço do passeio?',
        'answer': 'The tour price includes accommodation, transportation, guided tours, entrance fees to attractions mentioned in the itinerary, and meals as specified. Please check the "What\'s Included" section for complete details.',
        'answer_es': 'El precio del tour incluye alojamiento, transporte, visitas guiadas, tarifas de entrada a las atracciones mencionadas en el itinerario y comidas según se especifica. Por favor, consulte la sección "Qué está incluido" para obtener detalles completos.',
        'answer_pt': 'O preço do passeio inclui hospedagem, transporte, passeios guiados, taxas de entrada para as atrações mencionadas no itinerário e refeições conforme especificado. Por favor, verifique a seção "O que está incluído" para detalhes completos.',
    },
    {
        'question': 'What is the cancellation policy?',
        'question_es': '¿Cuál es la política de cancelación?',
        'question_pt': 'Qual é a política de cancelamento?',
        'answer': 'Free cancellation up to 30 days before the tour start date. Cancellations made 15-29 days before receive a 50% refund. Cancellations less than 15 days before the tour are non-refundable. We recommend travel insurance for added protection.',
        'answer_es': 'Cancelación gratuita hasta 30 días antes de la fecha de inicio del tour. Las cancelaciones realizadas entre 15 y 29 días antes reciben un reembolso del 50%. Las cancelaciones con menos de 15 días de anticipación no son reembolsables. Recomendamos un seguro de viaje para mayor protección.',
        'answer_pt': 'Cancelamento gratuito até 30 dias antes da data de início do passeio. Cancelamentos feitos de 15 a 29 dias antes recebem reembolso de 50%. Cancelamentos com menos de 15 dias de antecedência não são reembolsáveis. Recomendamos seguro de viagem para proteção adicional.',
    },
    {
        'question': 'What should I pack for the tour?',
        'question_es': '¿Qué debo empacar para el tour?',
        'question_pt': 'O que devo levar para o passeio?',
        'answer': 'We recommend comfortable walking shoes, sunscreen, a hat, sunglasses, light and breathable clothing, and a camera. For temple visits, modest clothing covering shoulders and knees is required. Don\'t forget any personal medications and a reusable water bottle.',
        'answer_es': 'Recomendamos zapatos cómodos para caminar, protector solar, sombrero, gafas de sol, ropa ligera y transpirable, y una cámara. Para visitas a templos, se requiere ropa modesta que cubra hombros y rodillas. No olvide sus medicamentos personales y una botella de agua reutilizable.',
        'answer_pt': 'Recomendamos sapatos confortáveis para caminhar, protetor solar, chapéu, óculos de sol, roupas leves e respiráveis e uma câmera. Para visitas a templos, é necessário usar roupas modestas que cubram ombros e joelhos. Não esqueça seus medicamentos pessoais e uma garrafa de água reutilizável.',
    },
    {
        'question': 'Is this tour suitable for children?',
        'question_es': '¿Este tour es adecuado para niños?',
        'question_pt': 'Este passeio é adequado para crianças?',
        'answer': 'Yes, this tour is family-friendly and suitable for children of all ages. We can arrange child-friendly activities and adjust the pace as needed. Child discounts are available for children under 12 years old. Please inform us of any specific requirements when booking.',
        'answer_es': 'Sí, este tour es apto para familias y adecuado para niños de todas las edades. Podemos organizar actividades aptas para niños y ajustar el ritmo según sea necesario. Hay descuentos para niños menores de 12 años. Por favor, infórmenos de cualquier requisito específico al reservar.',
        'answer_pt': 'Sim, este passeio é adequado para famílias e crianças de todas as idades. Podemos organizar atividades adequadas para crianças e ajustar o ritmo conforme necessário. Descontos para crianças estão disponíveis para menores de 12 anos. Por favor, informe-nos sobre quaisquer requisitos específicos ao fazer a reserva.',
    },
    {
        'question': 'What type of accommodation is provided?',
        'question_es': '¿Qué tipo de alojamiento se proporciona?',
        'question_pt': 'Que tipo de hospedagem é fornecida?',
        'answer': 'We provide 4-5 star hotels with comfortable rooms, air conditioning, and private bathrooms. All hotels are carefully selected for their quality, location, and service. Upgrades to luxury hotels are available upon request for an additional fee.',
        'answer_es': 'Proporcionamos hoteles de 4-5 estrellas con habitaciones cómodas, aire acondicionado y baños privados. Todos los hoteles están cuidadosamente seleccionados por su calidad, ubicación y servicio. Las mejoras a hoteles de lujo están disponibles bajo petición por un cargo adicional.',
        'answer_pt': 'Fornecemos hotéis de 4-5 estrelas com quartos confortáveis, ar condicionado e banheiros privativos. Todos os hotéis são cuidadosamente selecionados pela qualidade, localização e serviço. Upgrades para hotéis de luxo estão disponíveis mediante solicitação por uma taxa adicional.',
    },
    {
        'question': 'Do I need a visa to visit Egypt?',
        'question_es': '¿Necesito una visa para visitar Egipto?',
        'question_pt': 'Preciso de visto para visitar o Egito?',
        'answer': 'Most nationalities require a visa to enter Egypt. You can obtain a visa on arrival at Egyptian airports or apply for an e-visa online before your trip. We can assist you with the visa process and provide the necessary documentation for your application.',
        'answer_es': 'La mayoría de las nacionalidades requieren una visa para entrar a Egipto. Puede obtener una visa a su llegada en los aeropuertos egipcios o solicitar una e-visa en línea antes de su viaje. Podemos ayudarle con el proceso de visa y proporcionar la documentación necesaria para su solicitud.',
        'answer_pt': 'A maioria das nacionalidades requer visto para entrar no Egito. Você pode obter o visto na chegada aos aeroportos egípcios ou solicitar um e-visa online antes da viagem. Podemos ajudá-lo com o processo de visto e fornecer a documentação necessária para sua solicitação.',
    },
    {
        'question': 'What is the best time to visit Egypt?',
        'question_es': '¿Cuál es la mejor época para visitar Egipto?',
        'question_pt': 'Qual é a melhor época para visitar o Egito?',
        'answer': 'The best time to visit Egypt is from October to April when temperatures are milder and more comfortable for sightseeing. Summer months (May-September) can be very hot, especially in Upper Egypt. However, beach destinations like Hurghada and Sharm El Sheikh are enjoyable year-round.',
        'answer_es': 'La mejor época para visitar Egipto es de octubre a abril, cuando las temperaturas son más suaves y cómodas para hacer turismo. Los meses de verano (mayo-septiembre) pueden ser muy calurosos, especialmente en el Alto Egipto. Sin embargo, destinos de playa como Hurghada y Sharm El Sheikh son agradables todo el año.',
        'answer_pt': 'A melhor época para visitar o Egito é de outubro a abril, quando as temperaturas são mais amenas e confortáveis para passeios turísticos. Os meses de verão (maio-setembro) podem ser muito quentes, especialmente no Alto Egito. No entanto, destinos de praia como Hurghada e Sharm El Sheikh são agradáveis o ano todo.',
    },
    {
        'question': 'Are the guides licensed and English-speaking?',
        'question_es': '¿Los guías están licenciados y hablan inglés?',
        'question_pt': 'Os guias são licenciados e falam inglês?',
        'answer': 'Yes, all our guides are professionally licensed Egyptologists who are fluent in English. They have extensive knowledge of Egyptian history, culture, and archaeology. Guides speaking Spanish, Portuguese, and other languages are also available upon request.',
        'answer_es': 'Sí, todos nuestros guías son egiptólogos profesionalmente licenciados que hablan inglés con fluidez. Tienen un amplio conocimiento de la historia, cultura y arqueología egipcia. También hay guías que hablan español, portugués y otros idiomas disponibles bajo petición.',
        'answer_pt': 'Sim, todos os nossos guias são egiptólogos profissionalmente licenciados e fluentes em inglês. Eles têm amplo conhecimento da história, cultura e arqueologia egípcia. Guias que falam espanhol, português e outros idiomas também estão disponíveis mediante solicitação.',
    },
]


def add_faqs_to_tours():
    """Add default FAQs to all tours that don't have any."""
    tours = Tour.objects.all()
    total = tours.count()
    added = 0

    print("="*60)
    print("ADDING FAQs TO TOURS")
    print("="*60)

    for i, tour in enumerate(tours, 1):
        existing_faqs = tour.faqs.count()
        print(f"\n[{i}/{total}] {tour.name[:50]}")

        if existing_faqs > 0:
            print(f"  Already has {existing_faqs} FAQs, skipping...")
            continue

        # Add default FAQs
        for idx, faq_data in enumerate(DEFAULT_FAQS):
            TourFAQ.objects.create(
                tour=tour,
                question=faq_data['question'],
                question_es=faq_data['question_es'],
                question_pt=faq_data['question_pt'],
                answer=faq_data['answer'],
                answer_es=faq_data['answer_es'],
                answer_pt=faq_data['answer_pt'],
                sort_order=idx
            )

        print(f"  Added {len(DEFAULT_FAQS)} FAQs")
        added += 1

    print(f"\n{'='*60}")
    print(f"COMPLETED! Added FAQs to {added} tours")
    print(f"Total FAQs created: {added * len(DEFAULT_FAQS)}")
    print("="*60)


if __name__ == '__main__':
    add_faqs_to_tours()
