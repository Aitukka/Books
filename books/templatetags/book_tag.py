from django import template

import books
from books.models import Book

register = template.Library()


@register.inclusion_tag('books/tags/last_book.html')
def get_last_books(count=5):
    books = Book.objects.order_by("id")[:count]
    return {"last_books": books}
