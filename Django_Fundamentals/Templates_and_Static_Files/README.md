# Task 4: Django Templates and Static Files

## Overview
This task focuses on Django's template system, reusable layouts, dynamic content rendering, static file management, and custom template filters. It demonstrates how to create structured and maintainable web pages using Django templates, HTML, and CSS.

## Questions Covered

### Q1. Layout and Template Inheritance
- Created a reusable `base.html` template with common header, navigation, content, and footer sections.
- Used `{% block %}` tags to define customizable template sections.
- Created child templates using `{% extends 'base.html' %}`.

### Q2. Dynamic Template Logic
- Used `{% for %}` loops to display a list of items.
- Applied `{% if %}` and `{% else %}` conditions to display item availability.
- Used `{% empty %}` to handle cases where the list contains no items.

### Q3. Static File Asset Linking
- Configured `STATIC_URL` and `STATICFILES_DIRS` in `settings.py`.
- Created an external CSS stylesheet at `static/css/style.css`.
- Used `{% load static %}` and `{% static 'css/style.css' %}` to link CSS files.
- Applied custom styling, responsive layouts, gradients, and hover effects.

### Q4. Custom Template Filters
- Created a `templatetags` package inside the application.
- Implemented a custom `truncate_words` filter in `custom_filters.py`.
- Registered the filter using `template.Library()`.
- Loaded and applied the custom filter in a template to shorten text dynamically.

## Technologies Used
- Python
- Django
- HTML5
- CSS3
- SQLite
- Visual Studio Code

## Project Structure

```text
Django_Fundamentals/
├── myapp/
│   ├── templates/
│   │   ├── base.html
│   │   └── myapp/
│   │       ├── home.html
│   │       ├── item_list.html
│   │       └── description.html
│   ├── templatetags/
│   │   ├── __init__.py
│   │   └── custom_filters.py
│   ├── views.py
│   └── models.py
├── static/
│   └── css/
│       └── style.css
├── myproject/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## How to Run the Project

1. Open the project directory in the terminal.
2. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

3. Open the following URLs in your browser:

   - **Home Page:** `http://127.0.0.1:8000/`
   - **Dynamic Items:** `http://127.0.0.1:8000/items/`
   - **Custom Template Filter:** `http://127.0.0.1:8000/description/`

## Learning Outcomes
- Understood Django template inheritance and reusable layouts.
- Implemented dynamic rendering using loops and conditional statements.
- Configured and linked static CSS assets.
- Created and used custom Django template filters.
- Improved webpage appearance using responsive CSS and modern styling.

## Conclusion
This practical provided hands-on experience with Django templates and static files, demonstrating how reusable layouts, dynamic content, custom filters, and CSS styling work together to build organized and visually appealing web applications.
