import paramiko, sys
sys.stdout.reconfigure(encoding='utf-8')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('50.6.250.81', username='bassem', password='852456312002Bassem**')
sftp = ssh.open_sftp()
with sftp.open('/home/bassem/Girasol/frontend/src/components/home/Testimonials.tsx', 'r') as f:
    content = f.read().decode('utf-8')

# 1. Add imports - after useInView import
content = content.replace(
    "import { useInView } from '@/hooks/useInView';",
    "import { useInView } from '@/hooks/useInView';\nimport { useLanguageStore } from '@/store/languageStore';\nimport { testimonialsT, t } from '@/lib/translations';"
)

# 2. Add language hook after useInView hook
content = content.replace(
    "const [ref, isInView] = useInView<HTMLElement>({ rootMargin: '200px' });",
    "const [ref, isInView] = useInView<HTMLElement>({ rootMargin: '200px' });\n  const { language } = useLanguageStore();"
)

# 3. Replace 'Testimonials' heading
content = content.replace(
    '>\n            Testimonials\n          </motion.span>',
    ">\n            {t(testimonialsT, language, 'testimonials')}\n          </motion.span>"
)

# 4. Replace 'What Our Travelers Say'
content = content.replace(
    'What Our Travelers Say',
    "{t(testimonialsT, language, 'whatTravelersSay')}"
)

# 5. Replace description
old_desc = "Don&apos;t just take our word for it. Here&apos;s what our guests have to say\n            about their Egyptian adventures."
content = content.replace(old_desc, "{t(testimonialsT, language, 'description')}")

# 6. Replace 'out of 5 based on'
# The original: <span className="font-bold text-gray-900">{avgRating}</span> out of 5 based on
content = content.replace(
    '</span> out of 5 based on',
    "</span> {t(testimonialsT, language, 'outOf5')}"
)

# 7. Replace 'reviews' - the part after the count
content = content.replace(
    '+ reviews</span>',
    "+ {t(testimonialsT, language, 'reviews')}</span>"
)

# 8. Replace loading message
content = content.replace(
    'Loading testimonials...',
    "{t(testimonialsT, language, 'loadingTestimonials')}"
)

# 9. Replace error message
content = content.replace(
    'Unable to load testimonials. Please try again later.',
    "{t(testimonialsT, language, 'unableToLoad')}"
)

# 10. Replace empty state
content = content.replace(
    'No testimonials available at the moment.',
    "{t(testimonialsT, language, 'noTestimonials')}"
)

with sftp.open('/home/bassem/Girasol/frontend/src/components/home/Testimonials.tsx', 'w') as f:
    f.write(content)
print('Testimonials.tsx updated successfully')

# Verify
checks = ['useLanguageStore', 'testimonialsT', "language, 'testimonials'", "language, 'whatTravelersSay'", "language, 'description'", "language, 'outOf5'", "language, 'reviews'", "language, 'loadingTestimonials'", "language, 'unableToLoad'", "language, 'noTestimonials'"]
for c in checks:
    if c in content:
        print(f'  OK: {c} found')
    else:
        print(f'  MISSING: {c} NOT found')

sftp.close()
ssh.close()
