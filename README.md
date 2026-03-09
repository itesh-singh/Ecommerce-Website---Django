<div align="center">

# 🛒 GreatKart — Django Ecommerce Platform

*A backend-focused ecommerce system built with Django, covering the full purchase lifecycle — product discovery, cart management, PayPal payment capture, and order processing.*

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=flat&logo=django&logoColor=white)
![PayPal](https://img.shields.io/badge/PayPal-Sandbox-003087?style=flat&logo=paypal&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat&logo=bootstrap&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat)

</div>

---

## Highlights

- Complete ecommerce order lifecycle
- PayPal Sandbox payment integration
- Email-based account activation with signed tokens
- Session-based shopping cart with stock validation
- Admin honeypot with IP-based login attempt logging
- Automatic session expiry for inactive users
- Modular multi-app Django architecture
- Secure environment-based configuration

---

## What Is This?

GreatKart is a full-featured ecommerce platform built with **Django**. The focus is on **backend architecture** rather than frontend design.

The project demonstrates how a real ecommerce backend handles authentication flows, cart management, payment verification, order persistence, user account management, and inventory updates.

Frontend UI is intentionally simple so the **business logic and backend structure remain the focus**.

---

## Live Demo

> Deployment coming soon — will be hosted on Render.

---

## System Flow

```
User Request
    │
    ▼
Django Views  ──►  Business Logic  ──►  Models  ──►  Database
                        │
                        ▼
                   PayPal JS SDK
                   (client-side capture)
                        │
                        ▼
                   Server Verification
                   + Order Persistence
                        │
                        ▼
                   Confirmation Email
```

---

## Screenshots

### Home
![Homepage Top](screenshots/homepage_top.png)
![Homepage Bottom](screenshots/homepage_bottom.png)

---

### Store
![Store](screenshots/store.png)

---

### Authentication

| Sign In | Sign Up | Forgot Password |
|:---:|:---:|:---:|
| ![Sign In](screenshots/sign_in.png) | ![Sign Up](screenshots/sign_up.png) | ![Forgot Password](screenshots/forgot_password.png) |

---

### Checkout & Payment

| Checkout | Place Order | PayPal Sandbox |
|:---:|:---:|:---:|
| ![Checkout](screenshots/checkout.png) | ![Place Order](screenshots/place_order.png) | ![PayPal](screenshots/paypal_sandbox_payment.png) |

<div align="center">

![Payment Successful](screenshots/payment_successful.png)

</div>

---

### Orders

| My Orders | Order Detail | Confirmation Email |
|:---:|:---:|:---:|
| ![My Orders](screenshots/my_order.png) | ![Order Detail](screenshots/order_detail.png) | ![Email](screenshots/order_confirm_mail.png) |

---

### User Dashboard

| Dashboard | Edit Profile | Change Password |
|:---:|:---:|:---:|
| ![Dashboard](screenshots/dashboard.png) | ![Edit Profile](screenshots/edit_profile.png) | ![Change Password](screenshots/change_password.png) |

---

### Reviews

<div align="center">

![Review Order](screenshots/review_order.png)

</div>

---

## Tech Stack

| Category | Technology |
|:---|:---|
| Language | Python |
| Framework | Django |
| Database | SQLite (dev) → PostgreSQL (planned) |
| Frontend | Bootstrap 5, jQuery, Vanilla JS |
| Payments | PayPal JavaScript SDK (Sandbox) |
| Email | Gmail SMTP — App Password |
| Auth | Django Auth + Signed Token Email Verification |
| Image Processing | Pillow |
| Configuration | python-decouple, python-dotenv |
| Version Control | Git + GitHub (Conventional Commits) |

---

## Architecture

```
GreatKart/
│
├── Ecommerce/        # Project configuration (settings, urls, wsgi/asgi)
│
├── accounts/         # Authentication, email verification, profiles
│
├── store/            # Products, galleries, reviews, ratings
│
├── carts/            # Session-based cart and quantity management
│
├── category/         # Product categories
│
├── orders/           # Order creation, PayPal capture, order history
│
├── screenshots/      # README screenshots
├── templates/        # Django templates
└── static/           # CSS, JS, images
```

Each Django app manages its own models, views, and URLs — following the **separation of concerns** principle for maintainability and scalability.

---

## Core Features

### Authentication & Accounts
- Email verification — accounts inactive until the link is clicked
- Signed token-based activation links via Django's `default_token_generator`
- Password reset + change with full validation
- Profile management: name, phone, address, profile photo upload
- Protected views using `@login_required`
- Automatic session expiry via `django-session-timeout`

### Store & Cart
- Product catalog with category-based filtering
- Product detail pages with jQuery-driven image gallery
- Star rating display on product cards with live average aggregation
- Cart quantity management with totals and tax calculation
- Real-time stock validation — prevents overselling at add-to-cart and checkout

### Payments & Orders
- PayPal Sandbox integration via the official JavaScript SDK
- Payment captured client-side, verified and persisted server-side
- Unique order number generation per order
- Order confirmation email dispatched after payment
- Order history and detail pages
- Automatic stock reduction after successful purchase
- Order statuses: `New` → `Accepted` → `Completed` / `Cancelled`

### Reviews & Ratings
- Star ratings from 0.5 to 5 with live average aggregation
- Reviews restricted to verified purchasers only
- Anonymous user access handled gracefully

### Security & Admin
- Admin honeypot at `/admin/` — captures unauthorized login attempts with IP logging
- Real admin panel moved off the default URL
- All credentials in `.env`, excluded via `.gitignore`
- CSRF middleware enabled globally
- PayPal keys loaded from environment, never hardcoded

---

## Local Setup

### Requirements
- Python 3.12+
- pip
- Git

### 1. Clone the repo
```bash
git clone https://github.com/itesh-singh/ecommerce-django-backend.git
cd ecommerce-django-backend
```

### 2. Create virtual environment
```bash
python -m venv .venv
```

Activate:
```bash
source .venv/bin/activate    # Linux / macOS
.venv\Scripts\activate       # Windows
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
EMAIL_HOST_PASSWORD=your_gmail_app_password

PAYPAL_CLIENT_ID=your_paypal_sandbox_client_id
PAYPAL_RECEIVER_EMAIL=your_sandbox_business_email
```

> **Gmail App Password:** Google Account → Security → 2-Step Verification → App Passwords.
>
> **PayPal Sandbox:** Create a developer account at [developer.paypal.com](https://developer.paypal.com).

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Create superuser
```bash
python manage.py createsuperuser
```

### 7. Start development server
```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Security Practices

| Practice | Implementation |
|:---|:---|
| Secret management | All credentials in `.env`, excluded via `.gitignore` |
| Email verification | Accounts inactive until activation link is clicked |
| Activation links | Django signed token — time-limited and one-use |
| CSRF protection | Django CSRF middleware enabled globally |
| Payment credentials | PayPal keys loaded from environment, never hardcoded |
| Admin protection | Honeypot with IP-based login attempt logging |
| Session security | Automatic session expiry |

---

## Roadmap

- [ ] Migrate database to PostgreSQL
- [ ] Deploy to Render
- [ ] Expose REST API using Django REST Framework
- [ ] Add JWT-based API authentication
- [ ] Write unit tests for order and payment flows
- [ ] Add CI/CD pipeline with GitHub Actions
- [ ] Containerize with Docker + docker-compose

---

## Commit Convention

This project follows [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):

```
feat(orders): add stock reduction after payment capture
fix(cart): prevent quantity exceeding available stock
refactor(accounts): simplify activation token logic
feat(security): add admin honeypot with login attempt monitoring
```

---

## Author

<div align="center">

**Itesh Singh**
<br>
Backend Developer · Python & Django · Roorkee, Uttrakhand, India
<br><br>

[![GitHub](https://img.shields.io/badge/GitHub-itesh--singh-181717?style=flat&logo=github)](https://github.com/itesh-singh)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Itesh%20Singh-0A66C2?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/itesh-singh-113b55323)
[![Email](https://img.shields.io/badge/Email-itesh5906@gmail.com-D14836?style=flat&logo=gmail&logoColor=white)](mailto:itesh5906@gmail.com)

</div>

---

## License

This project is open source under the [MIT License](LICENSE).