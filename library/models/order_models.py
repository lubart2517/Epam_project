from library import db
import datetime
from ..service.book_service import BookService
from ..service.user_service import UserService


class Order(db.Model):
    """
        This class represents an Order. \n
        Attributes:
        -----------
        param user_id: Describes user which placed an order
        type name: User instance
        param book: Describes book in this order
        type book: Book instance
        param created_at: Describes when user placed this order
        type created_at: date
    """

    #: Name of the database table storing books
    __tablename__ = 'Order'

    #: Database id of the order
    id = db.Column(db.Integer, primary_key=True)

    # user which placed an order
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id'))

    # book in this order
    book_id = db.Column(db.Integer(), db.ForeignKey('Book.id'))

    # when user placed this order
    created_at = db.Column(db.DateTime(), default=datetime.datetime.now())

    # when user returned this order
    end_at = db.Column(db.DateTime(), default=(datetime.datetime.now() + datetime.timedelta(days=365)))

    # when user must return this order
    planed_end_at = db.Column(db.DateTime(), default=(datetime.datetime.now() + datetime.timedelta(days=30)))

    # Set to true when user will return the book
    closed = db.Column(db.Boolean, default=False)

    def __init__(self, user_id, book_id, planed_end_at=None):
        #: id of the user
        self.user_id = user_id

        #: id of the book
        self.book_id = book_id

        if planed_end_at is not None:
            self.planed_end_at = planed_end_at

    def __repr__(self):
        """
        This magic method is redefined to show user_id and book_id of Order object.

        """
        return f'Order({self.user_id}, {self.book_id})'

    def get_bookname(self):
        """ Returns name of this order book"""
        return BookService.get_book_by_id(self.book_id).name

    def get_username(self):
        """ Returns first and last name of this order user"""
        user = UserService.get_user_by_id(self.user_id)
        return f"{user.first_name} {user.last_name}"

