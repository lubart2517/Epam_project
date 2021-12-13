"""
Book service used to make database queries, this module defines the
following classes:
- `BookService`, book service
"""

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

        return Book.query.all()

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
        Fetches the book with given name   from database,
        raises ValueError if such book is not found
        :param name: name of the book to be fetched
        :return: book with given name
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
    def delete_book(cls, book_id):
        """
        Deletes the book with given ID from database, raises
        ValueError if such book is not found
        :param book_id: ID of the book to be deleted
        :raise ValueError: in case of book with given ID being absent
        in the database
        :return: None
        """
        book = cls.get_book_by_id(book_id)
        db.session.delete(book)
        db.session.commit()

    @classmethod
    def add_author(cls, book_id, author):
        """
        Add author to the list of book authors
        :param book_id: ID of the book
        :param author: Author's name and lastname
        :raise ValueError: in case of book with given ID being absent
        in the database
        :return: None
        """
        book = cls.get_book_by_id(book_id)
        author = db.session.query(Author).filter_by(name=author.split()[0], last_name=author.split()[1]).first()
        book.authors.append(author)
        db.session.commit()

    @classmethod
    def delete_author(cls, book_id, author):
        """
        Delete author from the list of book authors
        :param book_id: ID of the book
        :param author: Author's name and lastname
        :raise ValueError: in case of book with given ID being absent
        in the database
        :return: None
        """
        book = cls.get_book_by_id(book_id)
        author = db.session.query(Author).filter_by(name=author.split()[0], last_name=author.split()[1]).first()
        book.authors.remove(author)
        db.session.commit()

    @classmethod
    def get_free_authors(cls, book_id):
        """
        Return list of authors available for adding to the book authors
        :param book_id: ID of the book
        :raise ValueError: in case of book with given ID being absent
        in the database
        :return: None
        """
        book = cls.get_book_by_id(book_id)
        free_authors = [x for x in db.session.query(Author) if x.id not in [y.id for y in book.authors]]
        return free_authors

    @classmethod
    def get_authors(cls, book_id):
        """
        Return list of authors of the book
        :param book_id: ID of the book
        :raise ValueError: in case of book with given ID being absent
        in the database
        :return: None
        """
        book = cls.get_book_by_id(book_id)
        authors = [x for x in db.session.query(Author) if x.id in [y.id for y in book.authors]]
        return authors

    @classmethod
    def update(cls, book_id, name, description, count):
        """
        Update book with given id
        :return: None
        """
        book = cls.get_book_by_id(book_id)
        book.name = name
        book.description = description
        book.count = count
        db.session.commit()

    @classmethod
    def filter(cls, query_filter, to_find):
        """
        Sort books according to
        filter parameter
        :return: filtered query of books
        """
        if query_filter == '1':
            books = Book.query.filter(Book.authors.any(Author.name.contains(to_find))).all()
        elif query_filter == '2':
            books = Book.query.filter(Book.count == int(to_find)).all()
        elif query_filter == '3':
            books = Book.query.filter(Book.name.contains(to_find)).all()
        elif query_filter == '4':
            books = Book.query.filter(Book.description.contains(to_find)).all()
        else:
            books = cls.get_books()
        return books

    @staticmethod
    def sort(books, query_sort):
        """
        Sort list with books according to
        sort parameter
        :return: sorted list of books
        """
        if query_sort == '1':
            books.sort(key=lambda x: x.name, reverse=False)
        elif query_sort == '2':
            books.sort(key=lambda x: x.name, reverse=True)
        elif query_sort == '3':
            books.sort(key=lambda x: x.count, reverse=False)
        elif query_sort == '4':
            books.sort(key=lambda x: x.count, reverse=True)
        return books

