import os,sys,inspect

# move to two level above for correct load library app
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir2 = os.path.dirname(parentdir)
sys.path.insert(0,parentdir2)

from library.models.author_models import Author
from library.models.book_models import Book
from library.models.order_models import Order
from library.models.user_models import User
from library.tests.test_init import TestBase
from library import db


class TestModels(TestBase):

    def test_author_model(self):
        """
        Test number of records in Author table
        """
        self.assertEqual(Author.query.count(), 1)

    def test_user_model(self):
        """
        Test number of records in Author table
        """
        self.assertEqual(User.query.count(), 2)

    def test_book_model(self):
        """
        Test number of records in Book table
        """

        self.assertEqual(Book.query.count(), 1)

    def test_order_model(self):
        """
        Test number of records in Order table
        """

        self.assertEqual(Order.query.count(), 1)
