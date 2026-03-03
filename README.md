# GreatKart

> A production-oriented e-commerce backend built with Django — covering the full purchase lifecycle from product discovery to PayPal payment capture, order management, and user account workflows.

![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-6.0.2-092E20?style=flat&logo=django&logoColor=white)
![Pillow](https://img.shields.io/badge/Pillow-12.1.1-lightgrey?style=flat)
![PayPal](https://img.shields.io/badge/PayPal-Sandbox-003087?style=flat&logo=paypal&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

---

## What Is This?

GreatKart is a full-featured e-commerce platform built entirely on Django. The focus is on **backend depth** — clean app separation, a real payment integration, a complete order lifecycle, and secure authentication flows. Frontend is functional but intentionally minimal; this is a backend-first project.

Built to reflect the kind of code and architecture a junior/mid backend developer would write in a real team environment.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.12 |
| Framework | Django 6.0.2 |
| Database | SQLite (dev) → PostgreSQL (planned) |
| Frontend | Bootstrap 5, jQuery, Vanilla JS |
| Payments | PayPal JS SDK (Sandbox) |
| Email | SMTP — Gmail App Password |
| Auth | Django Auth + Signed Token Email Verification |
| Image Handling | Pillow 12.1.1 |
| Config | `python-decouple` 3.8, `python-dotenv` 1.2.1 |
| Version Control | Git + GitHub (Conventional Commits) |

---

## Architecture

```
GreatKart/
│
├── Ecommerce/        # Project settings, root URLs, WSGI/ASGI
│
├── accounts/         # Registration, login, email verification,
│                     # password reset, profile management
│
├── store/            # Product listings, detail pages,
│                     # image gallery, reviews & ratings
│
├── carts/            # Session-based cart, quantity management,
│                     # stock validation
│
├── category/         # Product category model & filtering
│
├── orders/           # Order creation, PayPal capture,
│                     # payment persistence, order history
│
├── templates/        # App-scoped HTML templates + shared includes
└── static/           # CSS, JS, images
```

Each Django app owns its own models, views, URLs, and business logic — following the **separation of concerns** principle for maintainability and scalability.

---

## Core Features

### Authentication & Account Management
- Email verification — accounts are inactive until the link is clicked
- Signed token-based activation links (via Django's `default_token_generator`)
- Password reset + change with full validation
- Profile management: name, phone, address, profile photo
- All sensitive views protected with `@login_required`

### Store & Cart
- Product listing with category-based filtering
- Product detail page with multi-image gallery (jQuery-driven switcher)
- Cart with per-item quantity control
- Real-time stock validation — prevents overselling at add-to-cart and checkout
- Out-of-stock guard on product and cart level

### Payments & Order Lifecycle
- PayPal Sandbox integrated via the official JavaScript SDK
- Payment captured client-side, verified and persisted server-side
- Each order gets a unique generated order number
- Cart items migrate to `OrderProduct` table post-payment
- Stock automatically decremented on successful purchase
- Order confirmation email dispatched after payment
- Order statuses: `New` → `Accepted` → `Completed` / `Cancelled`

### Reviews & Ratings
- Star ratings from 0.5 to 5 with live average aggregation
- Only verified purchasers can submit reviews
- Anonymous user access handled gracefully

---

## Local Setup

### Prerequisites
- Python 3.12+
- pip
- Git

---

### 1. Clone the repo
```bash
git clone https://github.com/itesh-singh/ecommerce-django-backend.git
cd ecommerce-django-backend
```

### 2. Set up virtual environment
```bash
python -m venv .venv

source .venv/bin/activate       # macOS / Linux
.venv\Scripts\activate          # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
DJANGO_SECRET_KEY=your_secret_key_here
DEBUG=True

EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_gmail_app_password   # Not your Gmail password — use an App Password

PAYPAL_CLIENT_ID=your_paypal_sandbox_client_id
PAYPAL_RECEIVER_EMAIL=your_sandbox_business_email
```

> **Gmail App Password:** Go to Google Account → Security → 2-Step Verification → App Passwords. Generate one for "Mail".
>
> **PayPal Sandbox:** Create a developer account at [developer.paypal.com](https://developer.paypal.com), then use the sandbox app credentials.

### 5. Apply migrations
```bash
python manage.py migrate
```

### 6. Create a superuser
```bash
python manage.py createsuperuser
```

### 7. Run the dev server
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Security Practices

| Practice | Implementation |
|---|---|
| Secret management | All credentials in `.env`, excluded via `.gitignore` |
| Account activation | Email verification required before login |
| Activation links | Django signed token generator — time-limited and one-use |
| CSRF | Django's built-in CSRF middleware enabled globally |
| Payment credentials | PayPal keys loaded from environment, never hardcoded |

---

## Roadmap

- [ ] Migrate database to PostgreSQL
- [ ] Expose REST API using Django REST Framework
- [ ] Add JWT-based API authentication
- [ ] Write unit tests for order and payment flows
- [ ] Add CI/CD pipeline with GitHub Actions
- [ ] Containerize with Docker + docker-compose

---

## Commit Convention

This project follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):

```
feat(orders): add automatic stock reduction on payment capture
fix(cart): prevent quantity exceeding available stock
refactor(accounts): extract token logic into utility module
```

---

## Author

**Itesh Singh**
Backend Developer · Python & Django · Roorkee, India

[![GitHub](https://img.shields.io/badge/GitHub-itesh--singh-181717?style=flat&logo=github)](https://github.com/itesh-singh)
[![Email](https://img.shields.io/badge/Email-itesh5906@gmail.com-D14836?style=flat&logo=gmail&logoColor=white)](mailto:itesh5906@gmail.com)

---

## License

This project is open source under the [MIT License](LICENSE).