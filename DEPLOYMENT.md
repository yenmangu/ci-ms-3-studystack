# Deployment

This document outlines how **StudyStack** is deployed in production and how it can be run locally for development and testing.

The project uses a **split deployment strategy**:

- **Heroku** for the live Django application
- **GitHub Pages** for hosting project documentation and assessment assets

This separation ensures production security while keeping documentation publicly accessible.

---

## Application Deployment (Heroku)

StudyStack is deployed using **Heroku**, following Django production best practices.

The production environment includes:

- **PostgreSQL** as the primary database
- **Cloudinary** for user-uploaded media storage
- **Whitenoise** for serving static files
- **Environment variables** for secrets and environment-specific configuration

The application automatically detects whether it is running locally or on Heroku and adjusts settings such as `DEBUG`, database engine, and static file handling accordingly.

Key characteristics of the Heroku deployment:

- `DEBUG` is disabled in production
- Sensitive values (e.g. `SECRET_KEY`, Cloudinary credentials) are never committed to source control
- Static files are collected and served efficiently
- Media uploads are handled externally via Cloudinary

---

## Documentation Hosting (GitHub Pages)

**GitHub Pages** is used exclusively to host project documentation and static assessment assets.

This includes:

- README.md
- TESTING.md
- Deployment documentation
- Validation screenshots
- Lighthouse reports
- Agile planning evidence

The live Django application itself is **not** served via GitHub Pages.

This approach ensures:

- Production security is maintained
- Documentation remains publicly accessible
- No sensitive configuration is exposed

---

## Local Development

To run StudyStack locally, follow the steps below.

### Prerequisites

- Python 3.x
- pip
- Git
- A Cloudinary account (for media handling)

---

### Cloning the Repository

1. Navigate to the GitHub repository:
   https://github.com/yenmangu/ci-ms-3-studystack

2. Clone the repository:
   `git clone https://github.com/yenmangu/ci-ms-3-studystack.git`

3. Change into the project directory:
   `cd ci-ms-3-studystack`

---

### Local Setup

1. Create and activate a virtual environment:

`python -m venv .venv`

`source .venv/bin/activate`

1. Install dependencies:

   `pip install -r requirements.txt`

2. Create an `env.py` file in the project root and define the required environment variables, including:
   - SECRET_KEY
   - DATABASE_URL (optional for local SQLite)
   - CLOUDINARY_URL
   - TINY_MCE_KEY

3. Apply database migrations:

   `python manage.py migrate`

4. (Optional) Create a superuser for admin access:

   `python manage.py createsuperuser`

5. Run the development server:

   `python manage.py runserver`

---

## Environment Awareness

StudyStack distinguishes between **local development**, **remote development**, and **production** using environment variables provided by the hosting platform.

This ensures:

- Debug mode is disabled in production
- Secrets are never hard-coded
- Static and media handling behave correctly in each environment
- Local development closely mirrors production behaviour

---

## Forking the Repository

Forking allows you to create an independent copy of the project for experimentation or extension.

1. Navigate to the repository on GitHub.
2. Click the **Fork** button in the top-right corner.
3. Clone your fork locally using the same steps as above.

---

## Deployment Summary

- **Heroku** is used for the live Django application
- **GitHub Pages** is used for documentation only
- Environment variables control configuration securely
- Local development mirrors production structure where possible

This deployment strategy ensures reliability, security, and a clear separation of concerns.
