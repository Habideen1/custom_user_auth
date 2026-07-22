Django REST Framework Authentication API

A production-ready **Backend Authentication API** built with Python, Django, Django REST Framework (DRF), and PostgreSQL.

This project is being developed as a beginner-to-advanced learning project, where every concept is implemented and explained step-by-step using industry best practices.

The goal is not only to build a secure authentication system but also to understand how Django's authentication framework works internally.



Project Goals

This project aims to build a complete authentication system that supports modern REST API authentication while teaching the underlying concepts behind every implementation.

The project is being developed in phases to make it easy for beginners to follow and understand.



Technologies Used

* Python 3.x
* Django
* Django REST Framework (DRF)
* PostgreSQL
* JWT Authentication
* Simple JWT
* UUID Primary Keys
* Custom User Model
* Git & GitHub
* Postman
* Environment Variables
* Django ORM



Features

✅ Completed

* Django Project Setup
* Django REST Framework Installation & Configuration
* PostgreSQL Database Configuration
* Custom User Model (`AbstractBaseUser`)
* Custom User Manager
* UUID Primary Keys
* Email-Based Authentication
* Django Admin Integration
* Database Migrations
* Production-Ready Registration Serializer
* Password Confirmation Validation
* Django Password Strength Validation
* Registration API View (`CreateAPIView`)

🚧 In Progress
Registration Endpoint URL Configuration
Registration API Testing with Postman
Email Verification
JWT Authentication
Login API
Logout API
Refresh Token
Forgot Password
Password Reset
Change Password
User Profile API
Role-Based Permissions
Token Blacklisting
Production Deployment


Current Progress

This project is being built incrementally as part of a comprehensive Django REST Framework learning series.

Current Phase: Phase 7.3 – Registration API View

Completed so far:

* Project setup
* PostgreSQL integration
* Django REST Framework configuration
* Custom User Model
* Custom User Manager
* UUID primary keys
* Registration Serializer
* Password validation
* Registration API View

The next milestone is connecting the registration endpoint through URL routing and testing it with Postman.



Project Structure

authentication-api/
│
├── accounts/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── managers.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py          # To be created in Phase 7.4
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── auth/                # Virtual Environment (ignored by Git)
├── .gitignore
├── README.md
├── manage.py
└── requirements.txt


Development Roadmap

* [x] Project Planning
* [x] Development Environment Setup
* [x] Django Project Creation
* [x] Django REST Framework Configuration
* [x] PostgreSQL Configuration
* [x] Custom User Model
* [x] Custom User Manager
* [x] Registration Serializer
* [x] Registration View
* [ ] Registration URL Configuration
* [ ] Registration API Testing (Postman)
* [ ] Email Verification
* [ ] JWT Authentication
* [ ] Login API
* [ ] Logout API
* [ ] Forgot Password
* [ ] Password Reset
* [ ] Change Password
* [ ] User Profile API
* [ ] Permissions & Roles
* [ ] Security Hardening
* [ ] Deployment


Authentication Features (Planned)

* User Registration
* Email Verification
* Login
* Logout
* JWT Authentication
* Refresh Tokens
* Forgot Password
* Password Reset
* Change Password
* User Profile
* Update Profile
* Role-Based Authorization
* Token Blacklisting
* Account Activation
* Account Deactivation



Learning Objectives

This project is designed to teach:

* Django Fundamentals
* Django REST Framework
* Authentication vs Authorization
* JWT Authentication
* Custom User Models
* Django ORM
* PostgreSQL Integration
* API Development
* Serializer Validation
* Permissions
* Error Handling
* Security Best Practices
* REST API Design
* Git & GitHub Workflow
* Postman API Testing



Setup Instructions

1. Clone the Repository

bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git


2. Navigate into the Project

bash
cd YOUR_REPOSITORY


3. Create a Virtual Environment

Windows

bash
python -m venv auth


macOS/Linux

bash
python3 -m venv auth


4. Activate the Virtual Environment

Windows

bash
auth\Scripts\activate


macOS/Linux

bash
source auth/bin/activate


5. Install Dependencies

bash
pip install -r requirements.txt


6. Configure PostgreSQL

Create a PostgreSQL database and update your database configuration in `settings.py` (or your future `.env` file).

7. Apply Migrations

bash
python manage.py migrate


8. Create a Superuser

bash
python manage.py createsuperuser


9. Run the Development Server

bash
python manage.py runserver


The application will be available at:


http://127.0.0.1:8000/




API Testing

All API endpoints will be tested using Postman.

A Postman Collection will be added as the project progresses.


Best Practices Followed

* Custom User Model
* UUID Primary Keys
* Email Authentication
* Password Hashing
* Django ORM
* PostgreSQL
* Modular Project Structure
* RESTful API Design
* Clean Code Principles
* Production-Oriented Development



Author

Abideen Adenekan

Backend Developer | Django & Django REST Framework Enthusiast | AI/ML Learner



License

This project is intended for educational and portfolio purposes.
