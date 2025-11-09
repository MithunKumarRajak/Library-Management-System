from django.contrib import admin
from .models import Book

# Search enhnacement and appearness
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')


admin.site.register(Book, BookAdmin)
