from django.contrib import admin
from .models import Author, Book, Genre, Publisher


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Publisher)
