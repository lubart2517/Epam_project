import json
import pandas as pd
from flask import abort, url_for, request
from library.tests.test_init import TestBase
from library.service.book_service import BookService


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
        Test that book by_name service accessible and returns book from db with given name
        """
        book = BookService.add_book(name='Harry', description="Harry the Potter", count=10, author="admin admin2016")
        self.assertEqual(book.count, 10)
        self.assertEqual(book.name, 'Harry')
