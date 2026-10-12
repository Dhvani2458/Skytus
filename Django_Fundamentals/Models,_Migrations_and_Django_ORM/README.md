# Task 2: Django Models and ORM

## Overview
This task focuses on defining database models, establishing relationships, managing migrations, performing complex queries, and calculating aggregate values using Django's Object-Relational Mapper (ORM).

## Topics Covered
- **Schema Definition:** Created `Course` and `Student` models.
- **Relationships:** Established a ForeignKey relationship between students and courses.
- **Migration Lifecycle:** Used `makemigrations` and `migrate` to apply database schema changes.
- **Complex Filtering:** Used QuerySets and `Q` objects with AND and OR conditions.
- **Aggregation:** Calculated the average student age using `Avg`.

## Technologies Used
- Python
- Django ORM
- SQLite
- VS Code

## Commands Used
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py shell
```

## Learning Outcome
Learned to design relational models, manage database migrations, retrieve filtered records, and perform aggregate calculations using Django ORM.
