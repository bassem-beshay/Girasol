import paramiko, sys
sys.stdout.reconfigure(encoding='utf-8')

HOST = '50.6.250.81'
USER = 'bassem'
PASS = '852456312002Bassem**'
BASE = '/home/bassem/Girasol/frontend/src/components/home/'

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, username=USER, password=PASS)
print("Connected to server")

sftp = ssh.open_sftp()

def read_file(name):
    with sftp.open(BASE + name, 'r') as f:
        return f.read().decode('utf-8')

def write_file(name, content):
    with sftp.open(BASE + name, 'w') as f:
        f.write(content.encode('utf-8'))
    print(f"  Written: {name}")

def verify(name, checks):
    with sftp.open(BASE + name, 'r') as f:
        c = f.read().decode('utf-8')
    for check in checks:
        if check in c:
            print(f"    [OK] {check[:60]}")
        else:
            print(f"    [MISSING] {check[:60]}")

# ============================================
# 1. HeroSection.tsx
# ============================================
print("\n=== HeroSection.tsx ===")
c = read_file('HeroSection.tsx')

# Add imports
c = c.replace(
    "import { contactApi } from '@/lib/api';",
    "import { contactApi } from '@/lib/api';\nimport { useLanguageStore } from '@/store/languageStore';\nimport { heroT, t } from '@/lib/translations';"
)

# Add language hook
c = c.replace(
    "const videoRef = useRef<HTMLVideoElement>(null);",
    "const videoRef = useRef<HTMLVideoElement>(null);\n  const { language } = useLanguageStore();"
)

# Trust badges - replace the array
c = c.replace(
    "{ icon: Shield, label: 'IATA Certified' },",
    "{ icon: Shield, label: t(heroT, language, 'iataCertified') },"
)
c = c.replace(
    "{ icon: Award, label: isLoaded ? `${yearsExperience} Years Experience` : '' },",
    "{ icon: Award, label: isLoaded ? `${yearsExperience} ${t(heroT, language, 'yearsExperience')}` : '' },"
)
c = c.replace(
    "{ icon: Clock, label: '24/7 Support' },",
    "{ icon: Clock, label: t(heroT, language, 'support247') },"
)

# Badge text
c = c.replace(
    "{isLoaded ? <>Trusted by <AnimatedCounter value={travelersCount} className=\"tabular-nums\" /> travelers worldwide</> : 'Your Trusted Travel Partner'}",
    "{isLoaded ? <>{t(heroT, language, 'trustedBy')} <AnimatedCounter value={travelersCount} className=\"tabular-nums\" /> {t(heroT, language, 'travelersWorldwide')}</> : t(heroT, language, 'trustedBy')}"
)

# Title
c = c.replace(
    "{isLoaded ? <>Discover Egypt with{' '}\n            <span className=\"text-primary-400\"><AnimatedCounter value={yearsExperience} className=\"inline tabular-nums\" /> Years</span> of Excellence</> : <>Discover Egypt with{' '}\n            <span className=\"text-primary-400\">Decades</span> of Excellence</>}",
    "{isLoaded ? <>{t(heroT, language, 'discoverEgyptWith')}{' '}\n            <span className=\"text-primary-400\"><AnimatedCounter value={yearsExperience} className=\"inline tabular-nums\" /> {t(heroT, language, 'yearsOfExcellence')}</span></> : <>{t(heroT, language, 'discoverEgyptWith')}{' '}\n            <span className=\"text-primary-400\">{t(heroT, language, 'yearsOfExcellence')}</span></>}"
)

# Subtitle
c = c.replace(
    "Tailor-made tours, Nile cruises & unforgettable experiences.\n            Let us craft your perfect Egyptian adventure.",
    "{t(heroT, language, 'subtitle')}"
)

# CTA buttons
c = c.replace(
    "              Explore Tours\n              <ChevronRight",
    "              {t(heroT, language, 'exploreTours')}\n              <ChevronRight"
)
c = c.replace(
    "              Get Free Quote\n",
    "              {t(heroT, language, 'getFreeQuote')}\n"
)

# Scroll text
c = c.replace(
    ">Scroll</span>", ">{t(heroT, language, 'scroll')}</span>"
)
# Alternative: exact match
c = c.replace(
    "            Scroll\n",
    "            {t(heroT, language, 'scroll')}\n"
)

write_file('HeroSection.tsx', c)
verify('HeroSection.tsx', ['useLanguageStore', 'heroT', "language, 'iataCertified'", "language, 'exploreTours'", "language, 'subtitle'"])

# ============================================
# 2. WhyChooseUs.tsx
# ============================================
print("\n=== WhyChooseUs.tsx ===")
c = read_file('WhyChooseUs.tsx')

# Add imports
c = c.replace(
    "import { contactApi } from '@/lib/api';",
    "import { contactApi } from '@/lib/api';\nimport { useLanguageStore } from '@/store/languageStore';\nimport { whyChooseUsT, t } from '@/lib/translations';"
)

# Add language hook (inside WhyChooseUs function)
c = c.replace(
    "const { data: statisticsData } = useQuery<StatisticsResponse>({",
    "const { language } = useLanguageStore();\n\n  const { data: statisticsData } = useQuery<StatisticsResponse>({"
)

# Replace getFeatures to use translations
old_features = """const getFeatures = (yearsExperience: string) => [
  {
    icon: Award,
    title: 'Experts in Egypt',
    description: `When traveling with Girasol Egypt Travel and Tours, you choose a team of professionals and experts in Egypt with over ${yearsExperience} years of experience. We care for every detail of your journey to ensure an unforgettable experience.`,
    link: '/about/who-we-are',
  },
  {
    icon: MapPin,
    title: 'Privileges & Facilities',
    description: 'With local offices in Cairo, Luxor, Aswan, Sharm El Sheikh, Hurghada, and partners in various countries worldwide. You will receive high-quality services and on-ground support wherever you travel.',
    link: '/about/booking',
  },
  {
    icon: Headphones,
    title: '24/7 Dedicated Support',
    description: 'We care about all your requirements, making your reservations quick and efficient. Our dedicated team is available around the clock via WhatsApp, phone, or email to serve you whenever and wherever you are.',
    link: '/about/service-quality',
  },
  {
    icon: Heart,
    title: 'Our Working Style',
    description: 'Love and care for your needs and requests is our working style with all our clients. Our professional team realizes and advises on all your requirements with personalized attention and genuine hospitality.',
    link: '/about/our-philosophy',
  },
];"""

new_features = """const getFeatures = (yearsExperience: string, lang: string) => [
  {
    icon: Award,
    title: t(whyChooseUsT, lang, 'expertsTitle'),
    description: `${t(whyChooseUsT, lang, 'expertsPrefix')}${yearsExperience} ${t(whyChooseUsT, lang, 'expertsSuffix')}`,
    link: '/about/who-we-are',
  },
  {
    icon: MapPin,
    title: t(whyChooseUsT, lang, 'privilegesTitle'),
    description: t(whyChooseUsT, lang, 'privilegesDesc'),
    link: '/about/booking',
  },
  {
    icon: Headphones,
    title: t(whyChooseUsT, lang, 'supportTitle'),
    description: t(whyChooseUsT, lang, 'supportDesc'),
    link: '/about/service-quality',
  },
  {
    icon: Heart,
    title: t(whyChooseUsT, lang, 'styleTitle'),
    description: t(whyChooseUsT, lang, 'styleDesc'),
    link: '/about/our-philosophy',
  },
];"""

c = c.replace(old_features, new_features)

# Update getFeatures call to pass language
c = c.replace(
    "const features = getFeatures(yearsExperience);",
    "const features = getFeatures(yearsExperience, language);"
)

# Header text
c = c.replace(
    "            Why Choose Us\n",
    "            {t(whyChooseUsT, language, 'mainTitle').split(' ').slice(0, 3).join(' ')}\n"
)

# Actually, let me keep it simpler - replace the full badge text
# Undo
c = c.replace(
    "            {t(whyChooseUsT, language, 'mainTitle').split(' ').slice(0, 3).join(' ')}\n",
    "            Why Choose Us\n"
)

# Main title
c = c.replace(
    "            Why Girasol Egypt Travel and Tours\n",
    "            {t(whyChooseUsT, language, 'mainTitle')}\n"
)

# Subtitle
c = c.replace(
    "            Your Trusted Partner in Egyptian Tourism\n",
    "            {t(whyChooseUsT, language, 'subtitle')}\n"
)

# Description
c = c.replace(
    "            We combine deep local knowledge with international service standards\n            to deliver experiences that exceed expectations.\n",
    "            {t(whyChooseUsT, language, 'description')}\n"
)

# Read More button
c = c.replace(
    "                      Read More\n",
    "                      {t(whyChooseUsT, language, 'readMore')}\n"
)

write_file('WhyChooseUs.tsx', c)
verify('WhyChooseUs.tsx', ['useLanguageStore', 'whyChooseUsT', "language, 'mainTitle'", "language, 'subtitle'", "language, 'readMore'"])

# ============================================
# 3. Destinations.tsx
# ============================================
print("\n=== Destinations.tsx ===")
c = read_file('Destinations.tsx')

# Add imports
c = c.replace(
    "import { useInView } from '@/hooks/useInView';",
    "import { useInView } from '@/hooks/useInView';\nimport { useLanguageStore } from '@/store/languageStore';\nimport { destinationsHomeT, t } from '@/lib/translations';"
)

# Add language hook
c = c.replace(
    "const [ref, isInView] = useInView<HTMLElement>({ rootMargin: '200px' });",
    "const [ref, isInView] = useInView<HTMLElement>({ rootMargin: '200px' });\n  const { language } = useLanguageStore();"
)

# Header text
c = c.replace(">Explore Egypt</", ">{t(destinationsHomeT, language, 'exploreEgypt')}</")
# The actual text is just the content
c = c.replace(
    "            Explore Egypt\n",
    "            {t(destinationsHomeT, language, 'exploreEgypt')}\n"
)
c = c.replace(
    "            Popular Destinations\n",
    "            {t(destinationsHomeT, language, 'popularDestinations')}\n"
)
c = c.replace(
    "            From ancient temples to pristine beaches, discover the diverse\n            wonders of Egypt.\n",
    "            {t(destinationsHomeT, language, 'description')}\n"
)

# Loading
c = c.replace(
    "<span className=\"ml-3 text-gray-600\">Loading destinations...</span>",
    "<span className=\"ml-3 text-gray-600\">{t(destinationsHomeT, language, 'loadingDestinations')}</span>"
)

# Error
c = c.replace(
    "<p className=\"text-gray-500\">Unable to load destinations. Please try again later.</p>",
    "<p className=\"text-gray-500\">{t(destinationsHomeT, language, 'unableToLoad')}</p>"
)

# Tours count
c = c.replace(
    "                        {destination.tour_count} Tours\n",
    "                        {destination.tour_count} {t(destinationsHomeT, language, 'tours')}\n"
)

# Explore link
c = c.replace(
    "                        Explore\n",
    "                        {t(destinationsHomeT, language, 'explore')}\n"
)

# Discover fallback
c = c.replace(
    "{destination.tagline || 'Discover'}",
    "{destination.tagline || t(destinationsHomeT, language, 'discover')}"
)

# Empty state
c = c.replace(
    "<p className=\"text-gray-500\">No destinations available at the moment.</p>",
    "<p className=\"text-gray-500\">{t(destinationsHomeT, language, 'noDestinations')}</p>"
)

# View All
c = c.replace(
    "              View All Destinations\n",
    "              {t(destinationsHomeT, language, 'viewAllDestinations')}\n"
)

write_file('Destinations.tsx', c)
verify('Destinations.tsx', ['useLanguageStore', 'destinationsHomeT', "language, 'exploreEgypt'", "language, 'popularDestinations'", "language, 'viewAllDestinations'"])

# ============================================
# 4. PopularTours.tsx
# ============================================
print("\n=== PopularTours.tsx ===")
c = read_file('PopularTours.tsx')

# Add imports
c = c.replace(
    "import { useInView } from '@/hooks/useInView';",
    "import { useInView } from '@/hooks/useInView';\nimport { useLanguageStore } from '@/store/languageStore';\nimport { popularToursT, t } from '@/lib/translations';"
)

# Add language hook
c = c.replace(
    "const [ref, isInView] = useInView<HTMLElement>({ rootMargin: '200px' });",
    "const [ref, isInView] = useInView<HTMLElement>({ rootMargin: '200px' });\n  const { language } = useLanguageStore();"
)

# Header text
c = c.replace(
    "              Popular Tours\n",
    "              {t(popularToursT, language, 'popularTours')}\n"
)
c = c.replace(
    "              Most Loved Tour Packages\n",
    "              {t(popularToursT, language, 'mostLoved')}\n"
)
c = c.replace(
    "              View All Tours\n",
    "              {t(popularToursT, language, 'viewAllTours')}\n"
)

# Loading
c = c.replace(
    "<span className=\"ml-3 text-gray-600\">Loading tours...</span>",
    "<span className=\"ml-3 text-gray-600\">{t(popularToursT, language, 'loadingTours')}</span>"
)

# Error
c = c.replace(
    "<p className=\"text-gray-500\">Unable to load tours. Please try again later.</p>",
    "<p className=\"text-gray-500\">{t(popularToursT, language, 'unableToLoad')}</p>"
)

# Best Seller badge
c = c.replace(
    "<span className=\"badge bg-primary-500 text-white\">Best Seller</span>",
    "<span className=\"badge bg-primary-500 text-white\">{t(popularToursT, language, 'bestSeller')}</span>"
)

# New badge
c = c.replace(
    "<span className=\"badge bg-green-500 text-white\">New</span>",
    "<span className=\"badge bg-green-500 text-white\">{t(popularToursT, language, 'new')}</span>"
)

# Early Bird in badge
c = c.replace(
    "{tour.early_booking_badge || 'Early Bird'}",
    "{tour.early_booking_badge || t(popularToursT, language, 'earlyBird')}"
)

# Reviews
c = c.replace(
    "<span className=\"text-gray-400 text-sm\">({tour.review_count || 0} reviews)</span>",
    "<span className=\"text-gray-400 text-sm\">({tour.review_count || 0} {t(popularToursT, language, 'reviews')})</span>"
)

# Price label
c = c.replace(
    "                          {tour.is_early_booking ? 'Early Bird' : 'From'}",
    "                          {tour.is_early_booking ? t(popularToursT, language, 'earlyBird') : t(popularToursT, language, 'from')}"
)

# Details
c = c.replace(
    "                        Details\n",
    "                        {t(popularToursT, language, 'details')}\n"
)

# Empty state
c = c.replace(
    "<p className=\"text-gray-500\">No tours available at the moment.</p>",
    "<p className=\"text-gray-500\">{t(popularToursT, language, 'noTours')}</p>"
)

write_file('PopularTours.tsx', c)
verify('PopularTours.tsx', ['useLanguageStore', 'popularToursT', "language, 'popularTours'", "language, 'mostLoved'", "language, 'viewAllTours'", "language, 'details'"])

# ============================================
# 5. MultiDestinationTours.tsx
# ============================================
print("\n=== MultiDestinationTours.tsx ===")
c = read_file('MultiDestinationTours.tsx')

# Add imports
c = c.replace(
    "import { useInView } from '@/hooks/useInView';",
    "import { useInView } from '@/hooks/useInView';\nimport { useLanguageStore } from '@/store/languageStore';\nimport { multiDestT, t } from '@/lib/translations';"
)

# Add language hook
c = c.replace(
    "const [ref, isInView] = useInView<HTMLElement>({ rootMargin: '200px' });",
    "const [ref, isInView] = useInView<HTMLElement>({ rootMargin: '200px' });\n  const { language } = useLanguageStore();"
)

# Header
c = c.replace(
    "              Multi-Destination Tours\n",
    "              {t(multiDestT, language, 'multiDestTours')}\n"
)
c = c.replace(
    "              Explore Multiple Countries\n",
    "              {t(multiDestT, language, 'exploreMultiple')}\n"
)
c = c.replace(
    "              Combine the wonders of Egypt with Jordan, Dubai, and more in one unforgettable journey\n",
    "              {t(multiDestT, language, 'description')}\n"
)
c = c.replace(
    "              View All Multi-Destination Tours\n",
    "              {t(multiDestT, language, 'viewAll')}\n"
)

# Loading
c = c.replace(
    "<span className=\"ml-3 text-gray-600\">Loading tours...</span>",
    "<span className=\"ml-3 text-gray-600\">{t(multiDestT, language, 'loadingTours')}</span>"
)

# Error
c = c.replace(
    "<p className=\"text-gray-500\">Unable to load tours. Please try again later.</p>",
    "<p className=\"text-gray-500\">{t(multiDestT, language, 'unableToLoad')}</p>"
)

# Multi-Country badge
c = c.replace(
    "                        Multi-Country\n",
    "                        {t(multiDestT, language, 'multiCountry')}\n"
)

# Best Seller
c = c.replace(
    "<span className=\"badge bg-amber-500 text-white\">Best Seller</span>",
    "<span className=\"badge bg-amber-500 text-white\">{t(multiDestT, language, 'bestSeller')}</span>"
)

# Reviews
c = c.replace(
    "<span className=\"text-gray-400 text-sm\">({tour.review_count || 0} reviews)</span>",
    "<span className=\"text-gray-400 text-sm\">({tour.review_count || 0} {t(multiDestT, language, 'reviews')})</span>"
)

# From
c = c.replace(
    "                        <span className=\"text-gray-500 text-sm\">From</span>",
    "                        <span className=\"text-gray-500 text-sm\">{t(multiDestT, language, 'from')}</span>"
)

# Details
c = c.replace(
    "                        Details\n                        <ChevronRight",
    "                        {t(multiDestT, language, 'details')}\n                        <ChevronRight"
)

write_file('MultiDestinationTours.tsx', c)
verify('MultiDestinationTours.tsx', ['useLanguageStore', 'multiDestT', "language, 'multiDestTours'", "language, 'exploreMultiple'", "language, 'details'"])

# ============================================
# 6. EarlyBookingSlider.tsx
# ============================================
print("\n=== EarlyBookingSlider.tsx ===")
c = read_file('EarlyBookingSlider.tsx')

# Add imports
c = c.replace(
    "import { useInView } from '@/hooks/useInView';",
    "import { useInView } from '@/hooks/useInView';\nimport { useLanguageStore } from '@/store/languageStore';\nimport { earlyBookingT, t } from '@/lib/translations';"
)

# Add language hook inside EarlyBookingSlider
c = c.replace(
    "const [currentSlide, setCurrentSlide] = useState(0);",
    "const { language } = useLanguageStore();\n  const [currentSlide, setCurrentSlide] = useState(0);"
)

# Countdown timer labels - Days, Hours, Mins, Secs
# These are inside the CountdownTimer component which doesn't have access to language store
# Need to pass language as prop or use the store in CountdownTimer too
# Simplest: use the store in CountdownTimer component too
old_countdown_func = "function CountdownTimer({ endDate }: { endDate: string }) {"
new_countdown_func = "function CountdownTimer({ endDate }: { endDate: string }) {\n  const { language } = useLanguageStore();"
c = c.replace(old_countdown_func, new_countdown_func)

# Replace countdown labels
c = c.replace(
    ">Days</span>",
    ">{t(earlyBookingT, language, 'days')}</span>"
)
c = c.replace(
    ">Hours</span>",
    ">{t(earlyBookingT, language, 'hours')}</span>"
)
c = c.replace(
    ">Mins</span>",
    ">{t(earlyBookingT, language, 'mins')}</span>"
)
c = c.replace(
    ">Secs</span>",
    ">{t(earlyBookingT, language, 'secs')}</span>"
)

# Offer Ends In
c = c.replace(
    "<span>Offer Ends In</span>",
    "<span>{t(earlyBookingT, language, 'offerEndsIn')}</span>"
)

# Tours available
c = c.replace(
    "{currentOffer.tours_with_early_price.length} tours available",
    "{currentOffer.tours_with_early_price.length} {t(earlyBookingT, language, 'toursAvailable')}"
)

# View Early Bird Tours button
c = c.replace(
    "                  View Early Bird Tours\n",
    "                  {t(earlyBookingT, language, 'viewEarlyBird')}\n"
)

# Early Bird Offer badge
c = c.replace(
    "{currentOffer.badge_text || 'Early Bird Offer'}",
    "{currentOffer.badge_text || t(earlyBookingT, language, 'earlyBirdOffer')}"
)

write_file('EarlyBookingSlider.tsx', c)
verify('EarlyBookingSlider.tsx', ['useLanguageStore', 'earlyBookingT', "language, 'days'", "language, 'offerEndsIn'", "language, 'viewEarlyBird'"])

sftp.close()
print("\n\nAll 6 files translated successfully!")
print("Now building...")

stdin, stdout, stderr = ssh.exec_command(
    'cd /home/bassem/Girasol/frontend && rm -rf .next && npm run build',
    timeout=300
)
for line in stdout:
    line = line.strip()
    if line:
        try: print(line)
        except: pass

exit_code = stdout.channel.recv_exit_status()
print(f"\nBuild exit code: {exit_code}")

if exit_code == 0:
    print("Restarting pm2...")
    stdin, stdout, stderr = ssh.exec_command('pm2 restart all')
    stdout.channel.recv_exit_status()
    print("PM2 restarted successfully!")
else:
    err = stderr.read().decode('utf-8', errors='replace')
    print(f"Build failed! Error:\n{err}")

ssh.close()
print("Done!")
