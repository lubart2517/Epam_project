"""
Books REST API, this module defines the following classes:
- `BookApiBase`, book API base class
- `BookListApi`, book list API class
- `bookApi`, book API class
"""

from flask import request
from flask_restful import Resource
from marshmallow import ValidationError

from ..schemas.book import BookSchema, BookWithAvailableCountSchema
from ..service.book_service import BookService
from ..rest.decorators import authenticate, is_admin


class BookApiBase(Resource):
    """
    book API base class
    """
    #: Marshmallow schema used for book serialization/deserialization
    schema = BookSchema

    #: book database service
    service = BookService


class BookListApi(BookApiBase):
    """
    book list API class
    """

    @authenticate
    def get(self):
        """
        GET request handler of book list API
        Fetches all books via service and returns them in a JSON format
        with a status code 200(OK)
        :return: a tuple of all books JSON and a status code 200
        """
        books = self.service.get_books()
        return self.schema().dump(obj=books, many=True), 200

    @is_admin
    def post(self):
        """
        POST request handler of book list API
        Deserializes request data, uses service to add the book to the
        database and returns newly added book in a JSON format with a
        status code 201(Created), or returns error messages with a status code
        400(Bad Request) in case of validation error during deserialization
        :return: a tuple of newly added book JSON and status code 201 or a
        tuple of error messages and status code 400 in case of validation error
        """
        try:
            book = self.service.add_book_from_json(self.schema, request.json)
        except ValidationError as error:
            return error.messages, 400
        return self.schema().dump(book), 201


class BookApi(BookApiBase):
    """
    book API class
    """
    #: message to be returned in case of book not being found
    NOT_FOUND_MESSAGE = 'Book not found'

    #: message to be returned in case of book being successfully deleted
    NO_CONTENT_MESSAGE = 'Book deleted successfully'

    @authenticate
    def get(self, uuid: str):
        """
        GET request handler of book API
        Fetches the book with given uuid via service and returns it in a
        JSON format with a status code 200(OK), or returns an error message
        with a status code 404(Not Found) in case of book with given
        uuid not being found
        :return: a tuple of the book with given uuid in JSON and a status
        code 200, or a tuple of an error message and a status code 404 in
        case of book with given uuid not being found
        """
        try:
            book = self.service.get_book_by_uuid(uuid)
        except ValueError:
            return self.NOT_FOUND_MESSAGE, 404
        return self.schema().dump(book), 200

    @is_admin
    def put(self, uuid):
        """
        PUT request handler of book API
        Uses service to deserialize request data and find the book with
        given uuid and update it with deserialized instance, returns updated
        book in a JSON format with a status code 201(Created), or returns
        error messages with a status code 400(Bad Request) in case of
        validation error during deserialization, or returns an error message
        with a status code 404(Not Found) in case of book with given uuid
        not being found
        :return: a tuple of updated book JSON and status code 200, or a
        tuple of error messages and status code 400 in case of validation
        error, or a tuple of an error message and a status code 404 in case of
        book with given uuid not being found
        """
        try:
            book = self.service.update_book_from_json(
                self.schema(), uuid, request.json
            )
        except ValidationError as error:
            return error.messages, 400
        #except ValueError:
            #return self.NOT_FOUND_MESSAGE, 404
        return self.schema().dump(book), 200

    @is_admin
    def delete(self, uuid):
        """
        DELETE request handler of book API
        Uses service to delete the book with given uuid, returns no
        content message with a status code 204(No Content), or returns an error
        message with a status code 404(Not Found) in case of book with
        given uuid not being found
        :return: a tuple no content message and status code 204, or a tuple of
        an error message and a status code 404 in case of book with given
        uuid not being found
        """
        try:
            self.service.delete_book(uuid)
        except ValueError:
            return self.NOT_FOUND_MESSAGE, 404
        return self.NO_CONTENT_MESSAGE, 204


class BooksQueryApi(BookApiBase):
    """
    This class allows make rest calls with filtering for Book model
    """

    @authenticate
    def get(self, name, sort=None):
        """
        GET request handler of book list API
        Fetches all books via service, filters them by containing name arg in book description
         and returns them in a JSON format
        with a status code 200(OK)
        :return: a tuple of all books JSON and a status code 200
        """
        books = self.service.filter(query_filter='4', to_find=name)
        if sort:
            books = self.service.sort(books, query_sort=sort)
        return self.schema().dump(obj=books, many=True), 200


class BookListUserApi(BookApiBase):
    """
    book list for user API class
    """
    schema = BookWithAvailableCountSchema

    @authenticate
    def get(self):
        """
        GET request handler of book list API for users
        Fetches all books available books via service and returns them in a JSON format
        with a status code 200(OK)
        :return: a tuple of all available books JSON and a status code 200
        """
        books = self.service.get_available_books()
        return self.schema().dump(obj=books, many=True), 200
