Django REST Framework Authentication API

A production-oriented Backend Authentication API built with Python, Django, Django REST Framework (DRF), PostgreSQL, and JWT authentication.

This project is being developed incrementally from the ground up as both a practical authentication system and a structured learning project. Each feature is implemented and tested step-by-step using Django and DRF best practices.

The goal is not only to build a secure authentication API, but also to understand how Django's authentication system, serializers, token-based authentication, email verification, permissions, and security mechanisms work internally.



Project Goals

This project aims to build a complete, production-oriented authentication system supporting:

User registration
Email verification
JWT authentication
Login
Logout
Refresh tokens
Password reset
Change password
User profile management
Role-based authorization
Token blacklisting
Account activation and deactivation
Security hardening
Production deployment

The project is being developed in structured phases to make the implementation easy to understand and maintain.


Technologies Used
Python 3.x
Django 6.0.7
Django REST Framework 3.17.1
PostgreSQL
Psycopg 3
Simple JWT 5.5.1
PyJWT 2.13.0
python-decouple 3.8
UUID Primary Keys
Custom Django User Model
Django ORM
SMTP / Gmail
Git & GitHub
Postman
Environment Variables



Features
Completed

Django project setup
Django REST Framework installation and configuration
PostgreSQL database integration
Environment variable configuration using python-decouple
Custom User Model using AbstractBaseUser
PermissionsMixin integration
UUID primary keys
Email-based authentication
Custom User Manager
Password hashing using Django's password utilities
Django Admin integration
Database migrations
Registration Serializer
Password confirmation validation
Django password strength validation
Registration API View
Registration URL configuration
Registration API testing with Postman
SMTP email configuration
Test email successfully sent from Django
Email verification token generator
Email verification URL generation
Verification email delivery
Email verification API
Account activation after successful email verification
Email verification API testing
Simple JWT installation and configuration groundwork
Login Serializer implementation


In Progress

Login API View
Login API testing
JWT access token generation
JWT refresh token generation
Logout
Token blacklisting
Forgot password
Password reset
Change password
User profile API
Profile update
Permissions and roles
Security hardening
Production deployment


Current Progress

The project is currently in the JWT Authentication and Login phase.

Completed milestones
Django project setup
PostgreSQL integration
Django REST Framework configuration
Custom User Model
Custom User Manager
UUID primary keys
Email-based authentication
Registration Serializer
Password validation
Registration API View
Registration URL configuration
Registration API testing
SMTP configuration
Verification email delivery
Email verification token generation
Email verification endpoint
Email verification testing
Simple JWT dependency installation
Login Serializer


Current milestone

Login API / JWT Authentication

The next objective is to complete and test the LoginAPIView, including:

Validating user credentials
Checking account activation
Authenticating the user
Generating JWT access tokens
Generating JWT refresh tokens
Returning the authenticated user's information

The next milestone is connecting the registration endpoint through URL routing and testing it with Postman.



user_authentication_api/
│
├── config/
│   │
│   ├── accounts/
│   │   ├── migrations/
│   │   │   ├── __init__.py
│   │   │   └── 0002_alter_user_is_active.py
│   │   │
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── emails.py
│   │   ├── managers.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tests.py
│   │   ├── tokens.py
│   │   ├── urls.py
│   │   └── views.py
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   │
│   └── manage.py
│
├── auth/
│   └── # Python virtual environment
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt


API Base URL
During Local development:
http://127.0.0.1:8000/


Authenication API base Path:
http://127.0.0.1:8000/api/v1/auth/


Current API Endpoints
User Registration

POST /api/v1/auth/register/ - 
# Registers new user


Example Request:
{
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "password": "StrongPassword123!",
    "password_confirm": "StrongPassword123!"
}

# A successful registration creates the user account and sends an email verification link.


Email Verification
GET /api/v1/auth/verify-email/<uid>/<token>/

# The endpoint verifies the user's email address and activates the account.


Successful Response:
{
    "message": "Email verified successfully. Your account is now active."
}

Login
POST /api/v1/auth/login/

# Status: In progress

# The login endpoint will authenticate users using their email address and password and return JWT credentials.


Expected response structure:
{
    "message": "Login successful.",
    "user": {
        "id": "uuid",
        "email": "user@example.com",
        "first_name": "John",
        "last_name": "Doe"
    },
    "tokens": {
        "refresh": "refresh-token",
        "access": "access-token"
    }
}

# The exact response will be updated after the Login API is fully implemented and tested.


Authentication Flow

The authentication system is being designed around the following flow:

                    ┌─────────────────┐
                    │  User Registers │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Account Created │
                    │ is_active=False │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Verification    │
                    │ Email Sent      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ User Clicks     │
                    │ Verification   │
                    │ Link            │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Email Verified  │
                    │ is_active=True  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │     Login       │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ JWT Access +    │
                    │ Refresh Tokens  │
                    └─────────────────┘


Development Roadmap

# Phase 1 — Project Planning
 Project planning
 Authentication requirements
 API architecture planning

# Phase 2 — Development Environment
 Python environment
 Virtual environment
 Django installation
 Git configuration
 GitHub repository


# Phase 3 — Django Project Setup
 Django project creation
 Django REST Framework installation
 DRF configuration
 PostgreSQL configuration

# Phase 4 — Custom User System
 Custom User Model
 AbstractBaseUser
 PermissionsMixin
 Custom User Manager
 Email authentication
 UUID primary key
 Django Admin integration
 Database migrations

# Phase 5 — Environment Configuration
 python-decouple
 .env configuration
 Secret key configuration
 Database environment variables
 SMTP environment variables
 .env added to .gitignore

# Phase 6 — Registration
 Registration Serializer
 Password confirmation
 Password validation
 User creation
 Registration API View
 Registration URL
 Postman testing

# Phase 7 — Email Verification
 SMTP configuration
 Test email
 Email verification token generator
 Verification URL
 Verification email utility
 Verification endpoint
 Account activation
 Verification testing

# Phase 8 — JWT Authentication
 Install Simple JWT
 Verify Simple JWT installation
 Login Serializer
 Login API View
 Login API testing
 Access token generation
 Refresh token generation
 Protected API testing

# Phase 9 — Logout
 Logout API
 Refresh token invalidation
 Token blacklisting
 Logout testing

# Phase 10 — Password Management
 Forgot password
 Password reset email
 Password reset token
 Password reset API
 Change password API
 Password management testing

# Phase 11 — User Profile
 Current user profile
 Update profile
 Authentication permissions
 Profile testing

# Phase 12 — Authorization
 User roles
 Permissions
 Role-based authorization
 Protected endpoints
 Authorization testing

# Phase 13 — Security Hardening
 Production security settings
 CORS configuration
 CSRF considerations
 Rate limiting
 Secure cookies where applicable
 JWT security configuration
 Password security review
 Environment variable review
 Error handling
 API security audit

# Phase 14 — Testing & Deployment
 Automated tests
 API integration tests
 Postman collection
 Production PostgreSQL configuration
 Production environment variables
 Deployment
 Production verification
 API documentation


Authentication Features

The completed system is intended to support:

User registration
Email verification
Account activation
Login
JWT access tokens
JWT refresh tokens
Logout
Token blacklisting
Forgot password
Password reset
Change password
User profile
Profile update
Role-based authorization
Account deactivation


Database

The project uses PostgreSQL as its primary database.

Database configuration is stored in environment variables rather than directly in settings.py.
DB_NAME=authentication_db
DB_USER=postgres
DB_PASSWORD=********
DB_HOST=localhost
DB_PORT=5432


Environment Variables

The project uses python-decouple to load environment variables.

The .env file contains configuration such as:
SECRET_KEY=your-secret-key
DEBUG=True

DB_NAME=authentication_db
DB_USER=postgres
DB_PASSWORD=your-database-password
DB_HOST=localhost
DB_PORT=5432

EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
EMAIL_USE_TLS=True
DEFAULT_FROM_EMAIL=your-email@gmail.com


API Testing

The API is tested using Postman.

Testing currently covers:

User registration
Validation errors
Password confirmation
Password strength validation
Email verification
Account activation

JWT login and protected endpoint testing will be added as the authentication system progresses.


Learning Objectives

This project is designed to provide practical understanding of:

Django fundamentals
Django REST Framework
Custom User Models
Authentication vs Authorization
Django ORM
PostgreSQL
Serializers
API Views
JWT Authentication
Access and Refresh Tokens
Email verification
Password hashing
Password validation
Permissions
Role-based authorization
Token blacklisting
Environment variables
SMTP
REST API design
Error handling
API security
Git and GitHub
Postman API testing
Production deployment



Best Practices Followed

The project follows several production-oriented practices:

Custom User Model
Email-based authentication
UUID primary keys
Password hashing
Django password validation
Environment-based configuration
.env excluded from Git
PostgreSQL
Modular application structure
Django ORM
RESTful API design
Serializer-level validation
Token-based authentication
Email verification before account activation
Separation of email functionality from views
Git version control
Incremental development and testing


Setup Instructions

Setup Instructions
1. Clone the Repository

git clone https://github.com/Habideen1/custom_user_auth.git


2. Navigate into the Project

cd custom_user_auth


3. Create a Virtual Environment

python -m venv auth


macOS/Linux

python3 -m venv auth


4. Activate the Virtual Environment

Windows

auth\Scripts\activate


macOS/Linux

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

python manage.py createsuperuser


9. Run the Development Server

python manage.py runserver


The application will be available at:

http://127.0.0.1:8000/

Requirements

Current Python dependencies are maintained in requirements.txt.

Key dependencies include:
Django==6.0.7
djangorestframework==3.17.1
djangorestframework_simplejwt==5.5.1
psycopg==3.3.4
psycopg-binary==3.3.4
PyJWT==2.13.0
python-decouple==3.8

Install all dependencies with:
pip install -r requirements.txt

Git & GitHub

The project uses Git for version control and GitHub for remote repository management.

Repository:
https://github.com/Habideen1/custom_user_auth.git


Future Improvements

Potential future improvements include:

API documentation with Swagger/OpenAPI
Automated unit and integration testing
Rate limiting
Refresh token rotation
More granular permission classes
User account deletion
Account recovery
Audit logging
Production email provider
Docker containerization
CI/CD
Production deployment
Monitoring and logging


Author

Abideen Adenekan
Backend Developer | Django & Django REST Framework Enthusiast | AI/ML Learner



License

This project is intended for educational, portfolio, and backend engineering learning purposes.
