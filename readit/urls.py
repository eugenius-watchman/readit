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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from books.views import (AuthorDetail, AuthorList, BookDetail, CreateAuthor, list_books, 
																	ReviewList ,review_book) 

urlpatterns = [
	# Auth
	# path('logout/', auth_views.logout, name='logout'),
    path('logout/', auth_views.LogoutView.as_view(next_page='books'), name='logout'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    
    # Admin
    path('admin/', admin.site.urls),
    
    # Custom
    path('', list_books, name='books'),
    path('authors', AuthorList.as_view(), name='authors'),
    path('books/(P<pk>[-\w]+)/', BookDetail.as_view(), name='book-detail'),
    path('authors/add/', login_required(CreateAuthor.as_view()), name='add-author'),
    path('authors/(P<pk>[-\w]+)/', AuthorDetail.as_view(), name='author-detail'),
    path('review/', login_required(ReviewList.as_view()), name='review-books'),
    path('review/(P<pk>[-\w]+)/', review_book, name='review-book'),
]
