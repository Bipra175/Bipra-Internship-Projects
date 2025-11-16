from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

def home(request):
    return render(request, 'books/home.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('books.urls')),
    path('', home),  # shows homepage
]
