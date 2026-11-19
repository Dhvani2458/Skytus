# Task 3: Django Views and Templates

## Overview
This task explores Django's Function-Based Views (FBVs) and Class-Based Views (CBVs) to retrieve database records, display book listings, create new records, and pass additional context to HTML templates.

## Topics Covered
- **Function-Based Views:** Retrieved all Book records and rendered them using an HTML template.
- **Generic ListView:** Implemented `BookListView` to display book records.
- **CreateView:** Created `BookCreateView` with specified model fields and a form template.
- **Redirects:** Used `reverse_lazy()` to redirect users after successful form submission.
- **Context Customization:** Overrode `get_context_data()` to pass the total number of books to the template.
- **HTML Templates:** Designed an attractive book listing page and book creation form using HTML and CSS.

## Technologies Used
- Python
- Django
- Django ORM
- HTML5
- CSS3
- SQLite

## How to Run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Open the following URLs in your browser:

- Book listing: `http://127.0.0.1:8000/books/`
- Add a book: `http://127.0.0.1:8000/books/add/`
- Function-Based View: `http://127.0.0.1:8000/books/fbv/`

## Learning Outcome
Gained practical experience in implementing FBVs and CBVs, working with Django generic views, handling form submissions and redirects, customizing template context, and presenting database records through styled HTML pages.
