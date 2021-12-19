import json
import pandas as pd
from flask import abort, url_for, request
from library.tests.test_init import TestBase
from library.service.book_service import BookService
from library.service.author_service import AuthorService


class TestServices(TestBase):
    """
    Class for testing Services
    """
    def test_get_books(self):
        """
        Test that book service accessible and returns books from db
        """
        book = BookService.get_books()[0]
        self.assertEqual(book.count, 5)
        self.assertEqual(book.name, 'IT')

    def test_get_available_books(self):
        """
        Test that book available service accessible and returns books from db
        """
        book = BookService.get_available_books()[0]
        self.assertEqual(book.count, 5)
        self.assertEqual(book.available, 4)
        self.assertEqual(book.name, 'IT')

    def test_get_book_by_uuid(self):
        """
        Test that book by_uuid service accessible and returns book from db with given uuid
        """
        book = BookService.get_book_by_uuid("92a69ce8-13b4-4fe0-a4cc-d519e8fb7933")
        self.assertEqual(book.count, 5)
        self.assertEqual(book.name, 'IT')

    def test_get_book_by_id(self):
        """
        Test that book by_id service accessible and returns book from db with given id
        """
        book = BookService.get_book_by_id(1)
        self.assertEqual(book.count, 5)
        self.assertEqual(book.name, 'IT')

    def test_get_book_by_name(self):
        """
        Test that book by_name service accessible and returns book from db with given name
        """
        book = BookService.get_book_by_name("IT")
        self.assertEqual(book.count, 5)
        self.assertEqual(book.name, 'IT')

    def test_book_add(self):
        """
        Test that book add service accessible and add and returns book from db with given parameters
        """
        book = BookService.add_book(name='Harry', description="Harry the Potter", count=10, author="admin admin2016")
        self.assertEqual(book.count, 10)
        self.assertEqual(book.name, 'Harry')

    def test_book_delete_error(self):
        """
        Test that book delete service accessible and does not delete book which contains in opened orders
        """
        self.assertEqual(BookService.delete_book(book_id=1),
                         'Deleting books not fully returned to library is prohibited')

    def test_book_delete_success(self):
        """
        Test that book delete service accessible
        """
        BookService.add_book(name='Harry', description="Harry the Potter", count=10, author="admin admin2016")
        self.assertEqual(BookService.delete_book(book_id=2),
                         'Book successfully deleted')

    def test_book_add_author(self):
        """
        Test that we can add author to the book authors list
        """
        author = AuthorService.add_author(name="Miguel", middle_name='De', last_name="Servantes")
        BookService.add_author(1, author.name + ' ' + author.last_name)
        self.assertEqual(BookService.get_book_by_id(1).authors[1].id, 2)
