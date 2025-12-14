#!/bin/bash
# ===========================================
# Girasol Tours - Deployment Script
# ===========================================
# Run this script on your VPS server

set -e

echo "=========================================="
echo "  Girasol Tours - Deployment Script"
echo "=========================================="

# Configuration
APP_DIR="/var/www/girasol"
DOMAIN="YOUR_DOMAIN.com"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Step 1: Update System
print_status "Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Step 2: Install Dependencies
print_status "Installing required packages..."
sudo apt install -y python3 python3-pip python3-venv nginx postgresql postgresql-contrib redis-server nodejs npm certbot python3-certbot-nginx

# Install Node.js 18+ (if needed)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Step 3: Create Application Directory
print_status "Creating application directory..."
sudo mkdir -p $APP_DIR
sudo chown -R $USER:$USER $APP_DIR

# Step 4: Setup PostgreSQL
print_status "Setting up PostgreSQL database..."
sudo -u postgres psql <<EOF
CREATE DATABASE girasol_tours;
CREATE USER girasol_user WITH PASSWORD 'YOUR_DB_PASSWORD';
ALTER ROLE girasol_user SET client_encoding TO 'utf8';
ALTER ROLE girasol_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE girasol_user SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE girasol_tours TO girasol_user;
EOF

# Step 5: Setup Backend
print_status "Setting up Django backend..."
cd $APP_DIR/backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install gunicorn

# Run migrations
python manage.py migrate --settings=config.settings.production
python manage.py collectstatic --noinput --settings=config.settings.production

deactivate

# Step 6: Setup Frontend
print_status "Setting up Next.js frontend..."
cd $APP_DIR/frontend
npm install
npm run build

# Step 7: Setup Gunicorn Service
print_status "Configuring Gunicorn service..."
sudo mkdir -p /var/log/gunicorn
sudo cp $APP_DIR/deploy/gunicorn.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable gunicorn
sudo systemctl start gunicorn

# Step 8: Setup Next.js Service
print_status "Configuring Next.js service..."
sudo cp $APP_DIR/deploy/nextjs.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable nextjs
sudo systemctl start nextjs

# Step 9: Setup Nginx
print_status "Configuring Nginx..."
sudo cp $APP_DIR/deploy/nginx.conf /etc/nginx/sites-available/girasol
sudo ln -sf /etc/nginx/sites-available/girasol /etc/nginx/sites-enabled/
sudo rm -f /etc/nginx/sites-enabled/default
sudo nginx -t
sudo systemctl reload nginx

# Step 10: Setup SSL with Let's Encrypt
print_status "Setting up SSL certificate..."
sudo certbot --nginx -d $DOMAIN -d www.$DOMAIN --non-interactive --agree-tos -m your-email@example.com

# Step 11: Setup Firewall
print_status "Configuring firewall..."
sudo ufw allow 'Nginx Full'
sudo ufw allow OpenSSH
sudo ufw --force enable

# Step 12: Start Redis
print_status "Starting Redis..."
sudo systemctl enable redis-server
sudo systemctl start redis-server

echo ""
echo "=========================================="
echo -e "${GREEN}  Deployment Complete!${NC}"
echo "=========================================="
echo ""
echo "Your site should now be available at:"
echo "  https://$DOMAIN"
echo ""
echo "Useful commands:"
echo "  - Check Django: sudo systemctl status gunicorn"
echo "  - Check Next.js: sudo systemctl status nextjs"
echo "  - Check Nginx: sudo systemctl status nginx"
echo "  - View logs: sudo journalctl -u gunicorn -f"
echo ""
