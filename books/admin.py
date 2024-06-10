from django.contrib import admin

# Register your models here.
from .models import Book, Reviews, RatingStar, Rating



admin.site.register(Book)
admin.site.register(Reviews)
admin.site.register(Rating)
admin.site.register(RatingStar)
