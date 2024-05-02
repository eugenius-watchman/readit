"""
URL configuration for readit project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from books.views import (AuthorDetail, AuthorList, BookDetail, CreateAuthor, list_books, 
							ReviewList ,review_book) 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', list_books, name='books'),
    path('authors', AuthorList.as_view(), name='authors'),
    path('books/(P<pk>[-\w]+)/', BookDetail.as_view(), name='book-detail'),
    path('authors/add/', CreateAuthor.as_view(), name='add-author'),
    path('authors/(P<pk>[-\w]+)/', AuthorDetail.as_view(), name='author-detail'),
    path('review/', ReviewList.as_view(), name='review-books'),
    path('review/(P<pk>[-\w]+)/', review_book, name='review-book'),
]
