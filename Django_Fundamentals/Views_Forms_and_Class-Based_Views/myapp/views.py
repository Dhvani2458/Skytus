from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import Avg
from myapp.models import Student
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .models import Book


# Create your views here.
def home(request):
    return HttpResponse("Welcome to Django!")


def student_detail(request, student_id):
    return HttpResponse(f"Student ID: {student_id}")

students = Student.objects.filter(age__gte=18)

print(students)

students = Student.objects.filter(
    Q(age__gte=18) | Q(name="Dhvani")
)

print(students)

students = Student.objects.filter(
    Q(age__gte=18) & Q(name="Dhvani")
)

print(students)

result = Student.objects.aggregate(average_age=Avg('age'))

print(result)
print(result['average_age'])

def book_list(request):
    books = Book.objects.all()
    return render(request, 'myapp/book_list.html', {
        'books': books
    })

class BookListView(ListView):
    model = Book
    template_name = 'myapp/book_list.html'
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_books'] = self.get_queryset().count()
        return context

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'author', 'price']
    template_name = 'myapp/book_form.html'
    success_url = reverse_lazy('book_list')