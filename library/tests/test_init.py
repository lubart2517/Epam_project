""" This module initialize Base class for all tests"""
import unittest, base64
from requests.auth import _basic_auth_str
from flask_testing import TestCase
from flask.testing import FlaskClient

from library import create_app, db
from library.models.author_models import Author
from library.models.user_models import User
from library.models.book_models import Book
from library.models.order_models import Order
from config import TestingConfig


class CustomClient(FlaskClient):
    def open(self, *args, **kwargs):
        headers = kwargs.setdefault("headers", {})
        headers.setdefault('Authorization', _basic_auth_str('user', "admin2016"))
        return super().open(*args, **kwargs)


class TestBase(TestCase):
    """
    Base class for all tests
    """
    def create_app(self):
        """ Creates test Flask app"""
        app = create_app(TestingConfig)
        app.test_client_class = CustomClient
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.create_all()

        # create test author
        author = Author(name="admin", last_name="admin2016", middle_name='True',
                        uuid="8d3fe6dd-d750-47be-91b5-c926c31ac7ff")

        # save author to database
        db.session.add(author)
        admin = User(first_name='Eric', last_name='Smit',username="admin", email='123@gmail.com',
                     password="admin2016", role=1)

        # create test non-admin user
        user = User(first_name='John', last_name='Lennon',username="user", email='789@gmail.com',
                     password="admin2016")
        # create test book
        book = Book(name="IT", description="The IT Department", count=5, authors=[Author.query.first() ],
                    uuid='92a69ce8-13b4-4fe0-a4cc-d519e8fb7933')

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
