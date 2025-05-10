from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    RegisterView,
    # Add any other views you have
)

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('register/', RegisterView.as_view(), name='register'),
]