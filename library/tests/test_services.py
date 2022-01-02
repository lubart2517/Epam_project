import json
import pandas as pd
from flask import abort, url_for, request
from library.tests.test_init import TestBase
from library.service.book_service import BookService
from library.service.author_service import AuthorService
from library.service.orders_service import OrderService

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

    def test_book_delete_author(self):
        """
        Test that we can delete author from the book authors list
        """
        BookService.delete_author(1, "admin admin2016")
        self.assertEqual(BookService.get_book_by_id(1).authors, [])

    def test_get_authors(self):
        """
        Test that author service accessible and returns authors from db
        """
        author = AuthorService.get_authors()[0]
        self.assertEqual(author.name, "admin")
        self.assertEqual(author.last_name, 'admin2016')

    def test_get_author_by_uuid(self):
        """
        Test that author by_uuid service accessible and returns author from db with given uuid
        """
        author = AuthorService.get_author_by_uuid("8d3fe6dd-d750-47be-91b5-c926c31ac7ff")
        self.assertEqual(author.name, "admin")
        self.assertEqual(author.last_name, 'admin2016')

    def test_get_author_by_id(self):
        """
        Test that author by_id service accessible and returns author from db with given id
        """
        author = AuthorService.get_author_by_id(1)
        self.assertEqual(author.name, "admin")
        self.assertEqual(author.last_name, 'admin2016')

    def test_get_author_by_name(self):
        """
        Test that author by_name service accessible and returns author from db with given name
        """
        author = AuthorService.get_author_by_name("admin")
        self.assertEqual(author.name, "admin")
        self.assertEqual(author.last_name, 'admin2016')

    def test_author_add(self):
        """
        Test that author add service accessible and add and returns author from db with given parameters
        """
        author = AuthorService.add_author(name='Henry', middle_name="The", last_name="Collins")
        self.assertEqual(author.name, "Henry")
        self.assertEqual(author.middle_name, 'The')

    def test_author_delete_success(self):
        """
        Test that author delete service accessible
        """
        author = AuthorService.add_author(name='Henry', middle_name="The", last_name="Collins")
        self.assertEqual(AuthorService.delete_author(author_id=2),
                         'Author successfully deleted')

    def test_get_orders(self):
        """
        Test that order service accessible and returns orders from db
        """
        order = OrderService.get_orders()[0]
        self.assertEqual(order.user_id, 1)
        self.assertEqual(order.book_id, 1)

    def test_get_order_by_id(self):
        """
        Test that order by_id service accessible and returns order from db with given id
        """
        order = OrderService.get_order_by_id(1)
        self.assertEqual(order.user_id, 1)
        self.assertEqual(order.book_id, 1)

    def test_get_orders_by_user(self):
        """
        Test that order by_user service accessible and returns orders from db with given user id
        """
        order = OrderService.get_orders_by_user(1)[0]
        self.assertEqual(order.user_id, 1)
        self.assertEqual(order.book_id, 1)

    def test_get_opened_orders_by_user(self):
        """
        Test that order open_by_user service accessible and returns open orders from db with given user id
        """
        order = OrderService.get_open_orders_by_user(1)[0]
        self.assertEqual(order.user_id, 1)
        self.assertEqual(order.book_id, 1)

    def test_get_orders_by_book(self):
        """
        Test that order by_book service accessible and returns orders from db with given book id
        """
        order = OrderService.get_orders_by_book(1)[0]
        self.assertEqual(order.user_id, 1)
        self.assertEqual(order.book_id, 1)

    def test_order_add(self):
        """
        Test that order add service accessible and add and returns order from db with given parameters
        """
        book = BookService.add_book(name='Harry', description="Harry the Potter", count=10, author="admin admin2016")
        order = OrderService.add_order(1, 2)
        self.assertEqual(order.user_id, 1)
        self.assertEqual(order.book_id, 2)

    def test_order_close(self):
        """
        Test that order close service accessible
        """
        order = OrderService.close_order(1)
        self.assertEqual(order.closed, True)
