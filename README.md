# Django Blog Website

A fully-featured blog website built with Django, featuring user authentication, blog post management, comments, likes, and an admin panel.

## Features

- **User Authentication**: Registration, login, logout, and profile pages.
- **Blog Post Management**: Authenticated users can create, edit, and delete their own posts.
- **Comment System**: Users can add comments to blog posts.
- **Like Feature**: Users can like/unlike posts with real‑time updates.
- **Admin Panel**: Django admin interface for managing users, posts, comments, and likes.
- **Responsive Design**: Bootstrap‑based frontend with custom CSS.

## Requirements

- Python 3.8+
- Django 5.1+
- Pillow (for image handling, optional)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/django-blog-website.git
   cd django-blog-website
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and go to `http://127.0.0.1:8000/`

## Project Structure

```
blog_project/
├── blog/                 # Main blog app
│   ├── models.py        # Post, Comment, Like models
│   ├── views.py         # CRUD, like, comment views
│   ├── urls.py          # Blog URL routing
│   ├── forms.py         # Post and comment forms
│   ├── admin.py         # Admin panel configuration
│   └── templates/blog/  # Blog templates
├── users/               # User authentication app
│   ├── views.py         # Registration, profile views
│   ├── urls.py          # Auth URL routing
│   └── templates/users/ # Auth templates
├── blog_project/        # Project settings
├── templates/           # Base templates
├── static/              # Static files (CSS, JS)
├── media/               # Uploaded media (if any)
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Usage

- **Homepage**: Displays recent posts and site introduction.
- **All Posts**: Lists all blog posts with like counts and comment counts.
- **Post Detail**: Shows full post, comments, and like button.
- **Create/Edit Post**: Authenticated users can write or modify posts.
- **User Profile**: Displays user information.
- **Admin Panel**: Accessible at `/admin` for site management.

## Deployment

The project can be deployed on platforms like **PythonAnywhere**, **Render**, or **Heroku**.

### Steps for deployment:

1. Set `DEBUG = False` in `settings.py`.
2. Configure `ALLOWED_HOSTS` with your domain.
3. Set up a production database (PostgreSQL recommended).
4. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
5. Follow platform‑specific deployment guides.

## Reference Blog Site

A live example of a similar blog can be found at:  
[https://niloy47321.pythonanywhere.com/](https://niloy47321.pythonanywhere.com/)

## License

This project is open‑source and available under the MIT License.
