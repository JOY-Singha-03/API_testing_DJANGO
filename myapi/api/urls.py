from django.urls import path
from .views import BookListCreate, BookRetrieveUpdateDelete

urlpatterns = [
    path('books/', BookListCreate.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDelete.as_view(), name='book-detail'),
]
