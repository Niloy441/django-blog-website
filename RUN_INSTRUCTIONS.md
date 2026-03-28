# Running the Django Blog Project

## Project Overview
This is a Django blog application with user authentication and blog post management.

## Project Structure
- `blog_project/` - Django project settings
- `blog/` - Blog application
- `users/` - User authentication application
- `templates/` - HTML templates
- `static/` - CSS and static files

## Requirements
- Python 3.11+
- Django 5.1.7+
- Pillow 10.0.0+

## Current Status
The project has been analyzed and is ready to run, but there's a system issue preventing Django installation:

### Issue Detected
The system's temporary directory configuration is causing pip installation to fail with error:
```
FileNotFoundError: [Errno 2] No usable temporary directory found
```

### Steps to Fix and Run the Project

#### Option 1: Fix Temp Directory Issue
1. Create a usable temp directory:
   ```cmd
   mkdir C:\temp
   ```
2. Set environment variables:
   ```cmd
   set TEMP=C:\temp
   set TMP=C:\temp
   ```
3. Install requirements:
   ```cmd
   pip install -r requirements.txt
   ```

#### Option 2: Use Virtual Environment
1. Create virtual environment:
   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```
2. Install requirements (may work with virtual env's temp directory):
   ```cmd
   pip install -r requirements.txt
   ```

#### Option 3: Manual Django Installation
1. Download Django wheel manually:
   ```cmd
   python -m pip download Django --no-deps -d .
   ```
2. Install from local file:
   ```cmd
   pip install Django-5.1.7-py3-none-any.whl
   ```

## Running the Project
Once dependencies are installed:

1. Apply database migrations:
   ```cmd
   python manage.py migrate
   ```
2. Create superuser (optional):
   ```cmd
   python manage.py createsuperuser
   ```
3. Run development server:
   ```cmd
   python manage.py runserver
   ```
4. Open browser to: http://127.0.0.1:8000/

## Project Features
- User registration and login
- Blog post creation, editing, deletion
- User profiles
- Static file serving
- SQLite database

## Notes
The project structure is complete and all necessary files are present:
- Django settings configured for development
- URL routing set up
- Templates for all pages
- Static CSS styling
- Models, views, and forms defined

To successfully run this project, the temporary directory issue needs to be resolved first.