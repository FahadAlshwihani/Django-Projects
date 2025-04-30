from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, ReviewViewSet, UserRegistrationView

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'books/(?P<book_id>[^/.]+)/reviews', ReviewViewSet, basename='book-reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-register'),  # User registration endpoint
]