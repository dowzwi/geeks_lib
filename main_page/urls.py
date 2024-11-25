from django.urls import path
from . import views

urlpatterns = [
    path('', views.books_list, name='book_list_view'),
    path('book_detail/<int:id>/', views.books_detail, name='detail'),
]