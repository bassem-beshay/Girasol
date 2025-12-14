# دليل رفع المشروع على Bluehost VPS

## المتطلبات
- VPS من Bluehost مع وصول SSH
- دومين مربوط بالسيرفر
- بيانات SSH (IP, username, password)

---

## الخطوة 1: الاتصال بالسيرفر

```bash
ssh username@YOUR_SERVER_IP
```

---

## الخطوة 2: تثبيت المتطلبات الأساسية

```bash
# تحديث النظام
sudo apt update && sudo apt upgrade -y

# تثبيت Python
sudo apt install -y python3 python3-pip python3-venv

# تثبيت PostgreSQL
sudo apt install -y postgresql postgresql-contrib

# تثبيت Redis
sudo apt install -y redis-server

# تثبيت Nginx
sudo apt install -y nginx

# تثبيت Node.js 18
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# تثبيت Certbot (SSL)
sudo apt install -y certbot python3-certbot-nginx
```

---

## الخطوة 3: إعداد قاعدة البيانات

```bash
# الدخول لـ PostgreSQL
sudo -u postgres psql

# داخل PostgreSQL، نفذ:
CREATE DATABASE girasol_tours;
CREATE USER girasol_user WITH PASSWORD 'كلمة_سر_قوية';
ALTER ROLE girasol_user SET client_encoding TO 'utf8';
ALTER ROLE girasol_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE girasol_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE girasol_tours TO girasol_user;
\q
```

---

## الخطوة 4: رفع ملفات المشروع

### الطريقة 1: باستخدام SCP (من جهازك)
```bash
# من جهازك المحلي
scp -r C:\Users\Dell\Desktop\tourism username@YOUR_SERVER_IP:/var/www/girasol
```

### الطريقة 2: باستخدام FileZilla
1. افتح FileZilla
2. اتصل بالسيرفر (SFTP, port 22)
3. ارفع مجلد `tourism` إلى `/var/www/girasol`

### الطريقة 3: باستخدام Git
```bash
# على السيرفر
sudo mkdir -p /var/www/girasol
cd /var/www/girasol
git clone YOUR_REPO_URL .
```

---

## الخطوة 5: إعداد Backend (Django)

```bash
cd /var/www/girasol/backend

# إنشاء البيئة الافتراضية
python3 -m venv venv
source venv/bin/activate

# تثبيت المكتبات
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn

# نسخ ملف البيئة
cp /var/www/girasol/deploy/.env.production .env

# تعديل ملف .env بالقيم الصحيحة
nano .env
```

### تعديل ملف .env:
```
SECRET_KEY=اولد_مفتاح_سري_جديد
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DB_PASSWORD=كلمة_سر_قاعدة_البيانات
CORS_ALLOWED_ORIGINS=https://yourdomain.com
```

### لتوليد SECRET_KEY:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### تشغيل Migrations:
```bash
export DJANGO_SETTINGS_MODULE=config.settings.production
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser  # إنشاء مستخدم أدمن

deactivate
```

---

## الخطوة 6: إعداد Frontend (Next.js)

```bash
cd /var/www/girasol/frontend

# نسخ ملف البيئة
cp /var/www/girasol/deploy/.env.frontend .env.local

# تعديل الدومين
nano .env.local
# غير YOUR_DOMAIN.com إلى دومينك

# تثبيت المكتبات
npm install

# بناء المشروع
npm run build
```

---

## الخطوة 7: إعداد Systemd Services

### Gunicorn (Django):
```bash
# إنشاء مجلد اللوجات
sudo mkdir -p /var/log/gunicorn

# نسخ ملف الخدمة
sudo cp /var/www/girasol/deploy/gunicorn.service /etc/systemd/system/

# تفعيل وتشغيل
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn

# التحقق
sudo systemctl status gunicorn
```

### Next.js:
```bash
sudo cp /var/www/girasol/deploy/nextjs.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable nextjs
sudo systemctl start nextjs

# التحقق
sudo systemctl status nextjs
```

---

## الخطوة 8: إعداد Nginx

```bash
# نسخ إعدادات Nginx
sudo cp /var/www/girasol/deploy/nginx.conf /etc/nginx/sites-available/girasol

# تعديل الدومين
sudo nano /etc/nginx/sites-available/girasol
# استبدل YOUR_DOMAIN.com بدومينك

# تفعيل الموقع
sudo ln -sf /etc/nginx/sites-available/girasol /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default

# اختبار الإعدادات
sudo nginx -t

# إعادة تشغيل Nginx
sudo systemctl reload nginx
```

---

## الخطوة 9: شهادة SSL (HTTPS)

```bash
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
```

اتبع التعليمات وأدخل إيميلك.

---

## الخطوة 10: إعداد Firewall

```bash
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw enable
```

---

## الخطوة 11: الصلاحيات

```bash
sudo chown -R www-data:www-data /var/www/girasol
sudo chmod -R 755 /var/www/girasol
```

---

## أوامر مفيدة

### إعادة تشغيل الخدمات:
```bash
sudo systemctl restart gunicorn
sudo systemctl restart nextjs
sudo systemctl restart nginx
```

### عرض اللوجات:
```bash
# Django logs
sudo journalctl -u gunicorn -f

# Next.js logs
sudo journalctl -u nextjs -f

# Nginx logs
sudo tail -f /var/log/nginx/error.log
```

### تحديث المشروع:
```bash
cd /var/www/girasol

# Backend
cd backend
source venv/bin/activate
git pull  # أو ارفع الملفات الجديدة
pip install -r requirements.txt
python manage.py migrate --settings=config.settings.production
python manage.py collectstatic --noinput --settings=config.settings.production
deactivate
sudo systemctl restart gunicorn

# Frontend
cd ../frontend
git pull  # أو ارفع الملفات الجديدة
npm install
npm run build
sudo systemctl restart nextjs
```

---

## حل المشاكل الشائعة

### 1. خطأ 502 Bad Gateway
```bash
# تأكد من تشغيل Gunicorn
sudo systemctl status gunicorn

# تحقق من اللوجات
sudo journalctl -u gunicorn -n 50
```

### 2. الصور لا تظهر
```bash
# تأكد من صلاحيات مجلد media
sudo chown -R www-data:www-data /var/www/girasol/backend/media
```

### 3. خطأ في قاعدة البيانات
```bash
# تأكد من إعدادات .env
cat /var/www/girasol/backend/.env

# تحقق من اتصال PostgreSQL
sudo -u postgres psql -c "\l"
```

### 4. SSL لا يعمل
```bash
# أعد تشغيل certbot
sudo certbot --nginx -d yourdomain.com
```

---

## هيكل الملفات على السيرفر

```
/var/www/girasol/
├── backend/
│   ├── venv/
│   ├── .env
│   ├── media/
│   ├── staticfiles/
│   └── ...
├── frontend/
│   ├── .next/
│   ├── .env.local
│   └── ...
└── deploy/
    ├── nginx.conf
    ├── gunicorn.service
    └── nextjs.service
```

---

## روابط مفيدة

- Django Admin: `https://yourdomain.com/admin/`
- API Docs: `https://yourdomain.com/api/docs/`
- الموقع: `https://yourdomain.com/`
