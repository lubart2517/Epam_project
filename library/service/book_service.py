"""
Book service used to make database queries, this module defines the
following classes:
- `BookService`, book service
"""
# pylint: disable=cyclic-import

from sqlalchemy.orm import lazyload

from library import db
from ..models.book_models import Book
from ..models.author_models import Author


class BookService:
    """
    Book service used to make database queries
    """
    @staticmethod
    def get_books():
        """
        Fetches all of the books from database
        :return: list of all books
        """

        return db.session.query(Book).all()

    @staticmethod
    def get_book_by_uuid(uuid):
        """
        Fetches the book with given UUID from database, raises
        ValueError if such book is not found
        :param uuid: UUID of the book to be fetched
        :raise ValueError: in case of book with given UUID being absent
        in the database
        :return: book with given UUID
        """
        book = db.session.query(Book).filter_by(uuid=uuid).first()
        if book is None:
            raise ValueError('Invalid book uuid')
        return book

    @staticmethod
    def get_book_by_id(book_id):
        """
        Fetches the book with given ID from database, raises
        ValueError if such book is not found
        :param book_id: ID of the book to be fetched
        :raise ValueError: in case of book with given ID being absent
        in the database
        :return: book with given ID
        """
        book = Book.query.get_or_404(book_id)
        if book is None:
            raise ValueError('Invalid book id')
        return book

    @staticmethod
    def get_book_by_name(name):
        """
        Fetches the book with given name and organisation  from database,
        raises ValueError if such book is not found
        :param name: name of the book to be fetched
        :param organisation: organisation of the book to be fetched
        :return: book with given name and organisation
        """
        return db.session.query(Book).filter_by(
            name=name).first()

    @staticmethod
    def add_book_from_json(schema, book_json):
        """
        Deserializes book and adds it to the database
        :param schema: schema to be used to deserialize the book
        :param book_json: data to deserialize the book from
        :return: book that was added
        """
        book = schema.load(book_json, session=db.session)
        db.session.add(book)
        db.session.commit()
        return book

    @staticmethod
    def add_book(name, description, count, author):
        """
        Adds book to the database
        :param name: book name
        :param description: book description
        :param count: book count
        :param author: book author
        :return: book that was added
        """
        author = db.session.query(Author).filter_by(name=author.split()[0], last_name=author.split()[1]).first()
        book = Book(name, description, count, [author])
        db.session.add(book)
        db.session.commit()
        return book


    @classmethod
    def update_book_from_json(cls, schema, uuid, book_json):
        """
        Deserializes book and updates book with given UUID using
        latter, raises ValueError if book with given UUID is not found
        :param schema: schema to be used to deserialize the book
        :param uuid: UUID of the book to be updated
        :param book_json: data to deserialize the book from
        :raise ValueError: in case of book with given UUID being absent
        in the database
        :return: book that was updated
        """
        book = cls.get_book_by_uuid(uuid)
        if book is None:
            raise ValueError('Invalid book uuid')
        book = schema.load(
            book_json, session=db.session, instance=book
        )
        db.session.add(book)
        db.session.commit()
        return book

    @classmethod
    def delete_book(cls, id):
        """
        Deletes the book with given UUID from database, raises
        ValueError if such book is not found
        :param uuid: UUID of the book to be deleted
        :raise ValueError: in case of book with given UUID being absent
        in the database
        :return: None
        """
        book = cls.get_book_by_id(id)
        if book is None:
            raise ValueError('Invalid book id')
        db.session.delete(book)
        db.session.commit()

    @classmethod
    def add_author(cls, id, author):
        """
        Deletes the book with given UUID from database, raises
        ValueError if such book is not found
        :param uuid: UUID of the book to be deleted
        :raise ValueError: in case of book with given UUID being absent
        in the database
        :return: None
        """
        book = cls.get_book_by_id(id)
        if book is None:
            raise ValueError('Invalid book id')
        author = db.session.query(Author).filter_by(name=author.split()[0], last_name=author.split()[1]).first()
        book.authors.append(author)
        db.session.commit()

    @classmethod
    def get_free_authors(cls, id):
        """
        Deletes the book with given UUID from database, raises
        ValueError if such book is not found
        :param uuid: UUID of the book to be deleted
        :raise ValueError: in case of book with given UUID being absent
        in the database
        :return: None
        """
        book = cls.get_book_by_id(id)
        if book is None:
            raise ValueError('Invalid book id')
        free_authors = db.session.query(Author).filter(Author.id not in [x.id for x in book.authors])
        return free_authors