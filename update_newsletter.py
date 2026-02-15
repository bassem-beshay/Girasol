import paramiko, sys
sys.stdout.reconfigure(encoding='utf-8')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('50.6.250.81', username='bassem', password='852456312002Bassem**')
sftp = ssh.open_sftp()
with sftp.open('/home/bassem/Girasol/frontend/src/components/home/Newsletter.tsx', 'r') as f:
    content = f.read().decode('utf-8')

# 1. Add imports after toast import
content = content.replace(
    "import toast from 'react-hot-toast';",
    "import toast from 'react-hot-toast';\nimport { useLanguageStore } from '@/store/languageStore';\nimport { newsletterT, t } from '@/lib/translations';"
)

# 2. Add language hook after status useState
content = content.replace(
    "const [status, setStatus] = useState<SubscriptionStatus>('idle');",
    "const [status, setStatus] = useState<SubscriptionStatus>('idle');\n  const { language } = useLanguageStore();"
)

# 3. Replace title
content = content.replace('Get Exclusive Deals & Travel Tips', "{t(newsletterT, language, 'title')}")

# 4. Replace description (multi-line)
old_desc = "Subscribe to our newsletter and be the first to know about special\n                  offers, new tours, and insider travel tips."
content = content.replace(old_desc, "{t(newsletterT, language, 'description')}")

# 5. Replace placeholder
content = content.replace('placeholder="Enter your email"', "placeholder={t(newsletterT, language, 'placeholder')}")

# 6. Replace Subscribing...
content = content.replace('Subscribing...', "{t(newsletterT, language, 'subscribing')}")

# 7. Replace Subscribe button text
content = content.replace(
    '>\n                        Subscribe\n                        <Send',
    ">{t(newsletterT, language, 'subscribe')}\n                        <Send"
)

# 8. Replace no spam
content = content.replace('No spam, unsubscribe anytime', "{t(newsletterT, language, 'noSpam')}")

# 9. Success states - pending_confirmation
content = content.replace('Check Your Email!', "{t(newsletterT, language, 'checkEmail')}")
content = content.replace("We&apos;ve sent a confirmation link to your email.", "{t(newsletterT, language, 'confirmationSent')}")
content = content.replace('Click the link to complete your subscription.', "{t(newsletterT, language, 'clickToConfirm')}")
content = content.replace('Subscribe with a different email', "{t(newsletterT, language, 'differentEmail')}")

# already_subscribed
content = content.replace("You&apos;re Already Subscribed!", "{t(newsletterT, language, 'alreadySubscribed')}")
content = content.replace("Great news - you&apos;re already on our list!", "{t(newsletterT, language, 'alreadyOnList')}")
content = content.replace('Keep an eye on your inbox for exclusive offers.', "{t(newsletterT, language, 'keepEye')}")
content = content.replace('Try another email', "{t(newsletterT, language, 'tryAnother')}")

# reactivated
content = content.replace('>Welcome Back!</h3>', ">{t(newsletterT, language, 'welcomeBack')}</h3>")
content = content.replace('Your subscription has been reactivated.', "{t(newsletterT, language, 'reactivated')}")
content = content.replace("You&apos;ll start receiving our updates again!", "{t(newsletterT, language, 'startReceiving')}")

with sftp.open('/home/bassem/Girasol/frontend/src/components/home/Newsletter.tsx', 'w') as f:
    f.write(content)
print('Newsletter.tsx updated successfully')

# Verify
checks = ['useLanguageStore', 'newsletterT', "language, 'title'", "language, 'description'", "language, 'placeholder'", "language, 'subscribe'", "language, 'noSpam'", "language, 'checkEmail'"]
for c in checks:
    if c in content:
        print(f'  OK: {c} found')
    else:
        print(f'  MISSING: {c} NOT found')

sftp.close()
ssh.close()
