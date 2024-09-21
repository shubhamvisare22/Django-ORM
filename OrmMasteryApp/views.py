from django.http import JsonResponse
from .models import Author, Book, Genre, Publisher
from datetime import datetime


def list_view(request):

    # get all the books
    all_books = Book.objects.all().values()

    # get perticular book
    book = Book.objects.get(id=1)

    # filter all book of the same authors
    books_by_author = Book.objects.filter(authors=3).values()

    # filter first book of the same authors
    books_by_author_first = Book.objects.filter(authors=3).first()

    # filter last book of the same authors
    books_by_author_last = Book.objects.filter(authors=3).last()

    # filter book by title
    books_by_title = Book.objects.filter(title__icontains="commercial").values()

    # filter book by publish date
    books_by_publish_date = Book.objects.filter(publication_date__gte=datetime.today()).values()

    # filter book by genre
    books_by_genre = Book.objects.filter(genre=1).values()

    # exclude book by genre
    exlude_books_by_genre = Book.objects.exclude(genre=1).values()

    # books by multiple authors
    books_by_multiple_authors = Book.objects.filter(authors__in=[1, 2]).values()

    # book count by publisher
    publisher = Publisher.objects.get(id=1)
    book_count_by_publisher = Book.objects.filter(publisher=publisher).count()

    # books published in year
    year = 2023
    books_published_in_year = Book.objects.filter(publication_date__year=year).values()
    
    # books ordered by publish date asc
    books_ordered_by_publish_date_asc = Book.objects.order_by('publication_date').values()
    
    # books ordered by publish date desc
    books_ordered_by_publish_date_desc = Book.objects.order_by('-publication_date').values()

    # latest book
    latest_book = Book.objects.latest('publication_date')
    print(latest_book)

    return JsonResponse({
        "all_books": list(all_books),
        "perticular_book": {"id": book.id, "title": book.title},
        "books_by_author": list(books_by_author),
        "books_by_author_first": books_by_author_first.title,
        "books_by_author_last": books_by_author_last.title,
        "books_by_title": list(books_by_title),
        "books_by_publish_date": list(books_by_publish_date),
        "books_by_genre": list(books_by_genre),
        "exlude_books_by_genre": list(exlude_books_by_genre),
        "books_by_multiple_authors": list(books_by_multiple_authors),
        f"book_count_by_publisher:{publisher.id}": book_count_by_publisher,
        f"books_published_in_year: {year}": list(books_published_in_year), 
        "books_ordered_by_publish_date_asc":list(books_ordered_by_publish_date_asc), 
        "books_ordered_by_publish_date_desc" : list(books_ordered_by_publish_date_desc), 
        "latest_book":latest_book.title,
    })
