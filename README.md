# Django Course App 🎓

A simple course management system built with Django as part of a tutorial series.  
This project demonstrates core Django features such as models, views, templates, admin customization, and user authentication.

## 🚀 Features

- List of courses with detail pages
- Instructor and category relations
- User authentication (login / register)
- Django admin interface customization
- Responsive UI with Bootstrap (optional)

## 🛠️ Tech Stack

- Python 3.x
- Django 4.x
- SQLite3 (default)
- HTML, CSS (Bootstrap)

## 📦 Setup Instructions

```bash
git clone https://github.com/yourusername/django-course-app.git
cd django-course-app
python -m venv env
source env/bin/activate  # or .\env\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
