# pylint: disable=no-member
import uuid
from sqlalchemy.ext.hybrid import hybrid_property
from library import db


book_authors = db.Table(
    'book_authors',
    db.Column('book_id', db.Integer(), db.ForeignKey('Book.id')),
    db.Column('author_id', db.Integer(), db.ForeignKey('Author.id'))
)


class Book(db.Model):
    """
        This class represents an Book. \n
        Attributes:
        -----------
        param name: Describes name of the book
        type name: str max_length=128
        param description: Describes description of the book
        type description: str
        param count: Describes count of the book
        type count: int default=10
        param authors: list of Authors
        type authors: list[Author] or None
    """
    #: Name of the database table storing books
    __tablename__ = 'Book'

    #: Database id of the book
    id = db.Column(db.Integer, primary_key=True)

    #: Name of the book
    name = db.Column(db.String(128))

    #: Description of the book
    description = db.Column(db.Text())

    #: Initial amount  of the book in the library
    count = db.Column(db.Integer, default=10)

    #: UUID of the book
    uuid = db.Column(db.String(36), unique=True)

    #: Authors of the book
    authors = db.relationship('Author', secondary=book_authors, backref=db.backref('Book', lazy='dynamic'))

    def __init__(self, name, description, count, authors=None, book_uuid=None):
        #: Name of the book
        self.name = name

        #: Description of the book
        self.description = description

        #: Initial amount  of the book in the library
        self.count = count

        if authors is None:
            authors = []
            #: Authors of the book
        self.authors = authors

        #: UUID of the book
        if book_uuid:
            self.uuid = book_uuid
        else:
            self.uuid = str(uuid.uuid4())

    def __repr__(self):
        """
        This magic method is redefined to show class and id of Book object.
        :return: class, id
        """
        return f'{self.name}'

    @hybrid_property
    def available(self):
        # pylint: disable=import-outside-toplevel
        from .order_models import Order
        return self.count - Order.query.filter(Order.book_id == self.id, Order.closed is False).count()
