# Girasol Tours - Egypt Tourism Platform

A comprehensive tourism management platform for Girasol Tours Egypt.

## Project Structure

```
tourism/
├── backend/           # Django REST API
│   ├── config/        # Project configuration
│   ├── apps/          # Django applications
│   │   ├── tours/     # Tours & packages
│   │   ├── destinations/  # Destinations
│   │   ├── bookings/  # Booking system
│   │   ├── users/     # User management
│   │   ├── blog/      # Blog & articles
│   │   ├── reviews/   # Reviews & testimonials
│   │   └── contact/   # Contact & inquiries
│   ├── media/         # Uploaded files
│   └── static/        # Static files
│
├── frontend/          # Next.js Frontend
│   ├── src/
│   │   ├── app/       # App router pages
│   │   ├── components/# React components
│   │   ├── lib/       # Utilities & API
│   │   ├── hooks/     # Custom hooks
│   │   └── types/     # TypeScript types
│   └── public/        # Static assets
│
└── docker/            # Docker configuration
```

## Tech Stack

### Backend
- Python 3.11+
- Django 5.0
- Django REST Framework
- PostgreSQL
- Redis (caching)
- Celery (async tasks)

### Frontend
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- React Query
- Zustand (state management)

## Getting Started

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## API Documentation

API documentation available at: `http://localhost:8000/api/docs/`

## License

Copyright © 2024 Girasol Tours. All rights reserved.
