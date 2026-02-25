🛒 Django Ecommerce Website

A production-style Ecommerce Web Application built using Django, implementing secure authentication, email verification, product management, and shopping cart functionality.
This project focuses on backend architecture, authentication workflows, and scalable Django app design.

🚀 Features
🔐 Authentication System

User registration with email verification

Account activation via secure token link

Login & logout system

Protected routes using authentication decorators

🛍️ Ecommerce Core

Product listing and categorization

Product detail pages

Shopping cart management

Add / remove items from cart

Quantity handling

📧 Email Functionality

Email-based account activation

Secure token generation using Django auth system

🧱 Project Architecture
Ecommerce/
│
├── accounts/      # User authentication & profile management
├── store/         # Product models and product views
├── carts/         # Cart and cart item logic
├── category/      # Product categorization
├── templates/     # HTML templates
├── static/        # CSS, JS, images
└── Ecommerce/     # Django project settings

The project follows modular Django app architecture to keep business logic separated and maintainable.

🛠️ Tech Stack

Backend: Python, Django

Database: SQLite (Development)

Frontend: HTML, CSS, JavaScript

Authentication: Django Authentication System

Email Service: SMTP Email Backend

⚙️ Installation & Setup
1️⃣ Clone repository
git clone https://github.com/itesh-singh/Ecommerce-Website---Django.git
cd Ecommerce-Website---Django
2️⃣ Create virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux / Mac
3️⃣ Install dependencies
pip install -r requirements.txt
4️⃣ Configure environment variables

Create a .env file and add:

SECRET_KEY=your_secret_key
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASSWORD=your_app_password
5️⃣ Apply migrations
python manage.py migrate
6️⃣ Run development server
python manage.py runserver

Open:

http://127.0.0.1:8000/
🔒 Security Notes

Sensitive credentials are stored using environment variables.

Email verification required before account activation.

Django token generator used for secure activation links.

📈 Future Improvements

Password reset via email

Order & payment integration

User dashboard

REST API using Django REST Framework

Deployment (Docker + Production Database)

👨‍💻 Author

Itesh Singh

Backend Developer (Python & Django)

⭐ Purpose of This Project

This project is built to demonstrate real-world Django backend development practices, including authentication workflows, modular architecture, and clean Git history suitable for internship and junior backend roles.