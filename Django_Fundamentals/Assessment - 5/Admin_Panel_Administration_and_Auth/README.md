# Task 5: Django Admin and Authentication

## Overview
This task demonstrates Django's administration panel, model registration, admin interface customization, and authentication-based access control. It provides practical experience in managing database records through Django Admin and protecting views from unauthorized access.

## Questions Covered

### Q1. Superuser Creation
- Created a Django superuser using the `createsuperuser` management command.
- Accessed the Django administration panel at `/admin/`.
- Logged in using the administrator credentials.

### Q2. Basic Model Registration
- Registered the `Book` model in `myapp/admin.py`.
- Enabled authorized administrators to add, view, update, and delete book records through Django Admin.

### Q3. Admin UI Customization
- Created a custom `BookAdmin` class using `admin.ModelAdmin`.
- Configured `list_display` to show the book ID, title, author, and price.
- Added `search_fields` to search by book title and author.
- Configured `list_filter` to filter books by author.
- Added book records and verified the customized administration interface.

### Q4. View Authorization Guards
- Applied Django's `@login_required` decorator to the `item_list` Function-Based View.
- Redirected unauthenticated users to the login page.
- Tested access to the protected endpoint after authentication.

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
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── myproject/
│   ├── settings.py
│   └── urls.py
├── db.sqlite3
└── manage.py
```

*Note: The structure above highlights the main files relevant to this task. Other files and folders from previous tasks remain in the project.*

## Commands Used

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

## How to Test

1. Start the Django development server.
2. Open `http://127.0.0.1:8000/admin/`.
3. Log in using the superuser credentials.
4. Open the Books section to add, edit, search, filter, or delete book records.
5. Open `http://127.0.0.1:8000/items/` in a logged-out browser session to verify the login protection.
6. Log in and verify that the protected page becomes accessible.

## Learning Outcomes
- Learned how to create a Django superuser.
- Understood model registration and CRUD operations in Django Admin.
- Customized the admin list display, search, and filtering options.
- Implemented authentication-based view protection.
- Practiced testing administrator access and protected endpoints.

## Conclusion
This practical provided hands-on experience with Django Admin and authentication. It demonstrated how to manage database records through a customized administration interface and restrict access to protected views using Django's authentication system.
