from django.contrib import admin
from .models import Author, Books, Chapter


# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    search_fields = ['book_title']


admin.site.register(Books, BooksAdmin)
admin.site.register(Author)
