from django.shortcuts import render, redirect
from .models import Book

# View 1 — Show all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/list_books.html', {'books': books})

# View 2 — Add a new book
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        price = request.POST.get('price')
        published_date = request.POST.get('published_date')

        # Save new book record
        Book.objects.create(
            title=title,
            author=author,
            price=price,
            published_date=published_date
        )
        return redirect('book_list')  # redirect to list after saving

    # For GET request → show the form
    return render(request, 'books/add_book.html')

# View 3 — Edit book
def edit_book(request, id):
    book = Book.objects.get(id=id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.price = request.POST.get('price')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('book_list')
    return render(request, 'books/edit_book.html', {'book': book})

# View 4 — Delete book
def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('book_list')
