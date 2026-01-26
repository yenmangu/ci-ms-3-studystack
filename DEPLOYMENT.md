# Deployment

This document outlines how **StudyStack** is deployed in production and how it can be run locally for development and testing.

The project uses a **split deployment strategy**:

- **Heroku** for the live Django application
- **GitHub Pages** for hosting project documentation and assessment assets

This separation ensures production security while keeping documentation publicly accessible.

---

## Deploying StudyStack to Heroku

This document provides a complete, step-by-step guide for deploying the **StudyStack** Django application to **Heroku**.
It is intended for assessment, documentation, and reproducibility purposes.

The deployment process follows Django production best practices.

---

### Overview

StudyStack uses a **split deployment strategy**:

- **Heroku** hosts the live Django application
- **GitHub Pages** hosts documentation and assessment assets only

This document covers **Heroku deployment only**.

---

### Prerequisites

Before deploying, ensure you have:

- A **Heroku account**
- A **GitHub account**
- The StudyStack repository pushed to GitHub
- A **Cloudinary account** (for media uploads)
- Python dependencies listed in `requirements.txt`
- A valid `Procfile` in the project root

---

### Create a Heroku App

1. Log in to the Heroku dashboard.
2. Click **New → Create new app**.
3. Enter a unique application name.
4. Select the appropriate region (e.g. Europe).
5. Click **Create app**.

---

### Configure Environment Variables

In the Heroku dashboard:

1. Navigate to **Settings → Reveal Config Vars**.
2. Add the following environment variables:

| Key                   | Description                            |
| --------------------- | -------------------------------------- |
| SECRET_KEY            | Django secret key                      |
| CLOUDINARY_URL        | Cloudinary API connection string       |
| DATABASE_URL          | Automatically set by Heroku Postgres   |
| TINY_MCE_KEY          | TinyMCE API key                        |
| DISABLE_COLLECTSTATIC | `1` (temporary, optional during setup) |

> [!IMPORTANT]
> Remove `DISABLE_COLLECTSTATIC` when ready to push production, otherwise static files will not be collected.

Sensitive values are never committed to source control and are managed exclusively through Heroku’s environment configuration.

---

### Attach a PostgreSQL Database

1. In the Heroku dashboard, go to the **Resources** tab.
2. Add **Heroku Postgres**.
3. Select the free or appropriate tier.
4. Heroku automatically provisions the database and sets `DATABASE_URL`.

---

### Prepare the Project for Deployment

Ensure the following files and settings are present:

#### `requirements.txt`

Contains all Python dependencies required for the project.

#### `Procfile`

Defines the application entry point for Heroku.

Example:

```
web: gunicorn studystack.wsgi
```

#### `settings.py` (Production Configuration)

Confirm that:

- `DEBUG` is disabled in production
- `ALLOWED_HOSTS` includes the Heroku app domain
- Database configuration reads from `DATABASE_URL`
- Whitenoise is enabled for static file handling
- Cloudinary is configured for media storage
- Secrets are loaded from environment variables

---

### Connect GitHub to Heroku

1. Open the Heroku app dashboard.
2. Navigate to the **Deploy** tab.
3. Select **GitHub** as the deployment method.
4. Authorise Heroku to access your GitHub account.
5. Search for and connect the StudyStack repository.

---

### Deploy the Application

1. Select the branch to deploy (typically `main`).
2. Click **Deploy Branch**.
3. Wait for the build process to complete.

A successful deployment will display a **“Build succeeded”** message.

---

### Apply Database Migrations

After deployment:

1. Open the **Heroku CLI** or use the dashboard console.
2. Run the following command:
   ```
   python manage.py migrate
   ```
3. (Optional) Create a superuser:
   ```
   python manage.py createsuperuser
   ```

---

### Collect Static Files

If static files are not automatically collected during deployment, run:

```
python manage.py collectstatic
```

Whitenoise serves static files directly in the production environment.

---

### Verify the Deployment

Visit the deployed Heroku URL and confirm:

- Pages load without errors
- Static assets (CSS, JS) are served correctly
- Media uploads function via Cloudinary
- Authentication works as expected
- CRUD functionality behaves correctly
- `DEBUG` is disabled and no sensitive error information is exposed

---

### Deployment Notes

- Heroku is used exclusively for the live Django application
- GitHub Pages is used only for documentation and assessment evidence
- Secrets and credentials are never committed to the repository
- Environment variables control all sensitive configuration
- Local development mirrors production behaviour where possible

---

The deployment was tested during development to ensure consistency between local and production environments.

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
