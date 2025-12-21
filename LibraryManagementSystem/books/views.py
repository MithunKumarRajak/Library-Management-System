from venv import create
from django.shortcuts import render
from .models import Book
# Create your views here.


def home(request):
    return render(request, 'books/home.html')


def books(request):
    data = Book.objects.all()  # like gathering all data from database
    # putting data in dictionary or label for passing to template
    books = {'details': data}
    '''
    lunchbox = {'fruit': 'apple'}
    Here:
    - 'fruit' is the label on the box.
    - 'apple' is the actual item inside.
    - we’ll use {{ fruit }} to access it
    '''
    return render(request, 'books/books.html', books)

def pricing(request):
    return render(request, 'books/pricing.html')