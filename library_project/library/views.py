from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Book, Author, Member, Loan  # Import your models

class BookListView(View):
    def get(self, request):
        books = Book.objects.all()
        authors = Author.objects.all()
        return render(request, 'library/book_list.html', {'books': books, 'authors': authors})

    def post(self, request):
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        published_date = request.POST.get('published_date')
        isbn = request.POST.get('isbn')

        try:
            Book.objects.create(
                title=title,
                author_id=author_id,
                published_date=published_date,
                isbn=isbn
            )
            return redirect('book_list')
        except IntegrityError:
            return render(request, 'library/book_list.html', {
                'books': Book.objects.all(),
                'authors': Author.objects.all(),
                'error': 'A book with that ISBN already exists.'
            })

class BookDetailView(View):
    def get(self, request, pk):
        book = get_object_or_404(Book, pk=pk)  # Fetch the book by primary key
        return render(request, 'library/book_detail.html', {'book': book})

    def post(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()  # Delete the book
        return redirect('book_list')

class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')  # Redirect to book list after registration
        return render(request, 'registration/register.html', {'form': form})