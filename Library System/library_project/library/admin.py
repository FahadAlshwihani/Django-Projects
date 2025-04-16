from django.contrib import admin
from .models import Author, Book, Member, Loan, Review, Category, BookCategory

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Member)
admin.site.register(Loan)
admin.site.register(Review)
admin.site.register(Category)
admin.site.register(BookCategory)