""" This module initialize Base class for all tests"""
import unittest
from flask_testing import TestCase

from library import create_app, db
from library.models.author_models import Author
from library.models.user_models import User
from library.models.book_models import Book
from library.models.order_models import Order
from config import TestingConfig


class TestBase(TestCase):
    """
    Base class for all tests
    """
    def create_app(self):
        """ Creates test Flask app"""
        app = create_app(TestingConfig)
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.create_all()

        # create test author
        author = Author(name="admin", last_name="admin2016", middle_name='True')


        # save author to database
        db.session.add(author)
        admin = User(first_name='Eric', last_name='Smit',username="admin", email='123@gmail.com',
                     password="admin2016", role=1)

        # create test non-admin user
        user = User(first_name='John', last_name='Lennon',username="user", email='789@gmail.com',
                     password="admin2016")
        # create test book
        book = Book(name="IT", description="The IT Department", count=5, authors=[Author.query.first()])

        # save book to database
        db.session.add(book)
        db.session.add(admin)
        db.session.add(user)
        db.session.commit()
        order = Order(user_id=User.query.first().id, book_id=Book.query.first().id)

        # save order to database
        db.session.add(order)

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
