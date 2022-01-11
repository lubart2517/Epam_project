"""This module defines function register_resources"""
from .import books_api, authors_api


def register_resources(api):
    """This function receives one arg api from library init ang register all
    resources defined in the function into api"""
    api.add_resource(
        books_api.BookListApi,
        '/api/books/',
        strict_slashes=False, endpoint='api_books'
    )
    api.add_resource(
        books_api.BookListUserApi,
        '/api/user_books/',
        strict_slashes=False, endpoint='api_user_books'
    )
    api.add_resource(
        books_api.BookApi,
        '/api/book/<uuid>',
        strict_slashes=False, endpoint='api_book_uuid'
    )
    api.add_resource(
        books_api.BooksQueryApi,
        '/api/books/<name>',
        '/api/books/<name>/<sort>',
        strict_slashes=False, endpoint='api_book_filter'
    )
    api.add_resource(
        authors_api.AuthorApi,
        '/api/author/<uuid>',
        strict_slashes=False, endpoint='api_author_uuid'
    )
    api.add_resource(
        authors_api.AuthorListApi,
        '/api/authors',
        strict_slashes=False, endpoint='api_authors'
    )
