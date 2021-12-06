
from library.models.author_models import Author
from library.models.book_models import Book
from library.models.order_models import Order
from library.models.user_models import User
from library.tests.test_init import TestBase


class TestModels(TestBase):
    """
    This class checks records added bt initial script
    """
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
