
from django.urls import path, include
from books.views import *
urlpatterns = [
    path('', home, name='home'),
    path('books/', books, name='books'),
]
