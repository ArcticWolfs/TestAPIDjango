from django.urls import path, include
from rest_framework.permissions import IsAuthenticated

import Account
from API import views

app_name = "API"

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('author', views.getData),
    path('books', views.get_books),
    path('book/<int:author_id>', views.GetBook.as_view(), name="Get book by id"),
    path('book/add', views.add_book),
    path('book/update/<int:book_id>', views.update_book),
    path('book/delete/<int:book_id>', views.delete_book),
]
