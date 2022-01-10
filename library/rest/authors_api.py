"""
Authors REST API, this module defines the following classes:
- `AuthorApiBase`, author API base class
- `AuthorListApi`, author list API class
- `AuthorApi`, author API class
"""

from flask import request
from flask_restful import Resource, abort
from marshmallow import ValidationError
from library import auth

from ..schemas.author import AuthorSchema
from ..service.author_service import AuthorService
from ..service.user_service import UserService


def authenticate(func):
    def wrapper(*args, **kwargs):
        user = UserService.get_user_by_username(request.authorization.username)
        if user:
            if user.check_password(request.authorization.password):
                return func(*args, **kwargs)

        return abort(403)
    return wrapper


class AuthorApiBase(Resource):
    """
    Author API base class
    """
    #: Marshmallow schema used for author serialization/deserialization
    schema = AuthorSchema

    #: author database service
    service = AuthorService
    method_decorators = [authenticate]


class AuthorListApi(AuthorApiBase):
    """
    author list API class
    """
    def get(self):

        """
        GET request handler of author list API
        Fetches all authors via service and returns them in a JSON format
        with a status code 200(OK)
        :return: a tuple of all authors JSON and a status code 200
        """
        authors = self.service.get_authors()
        return self.schema().dump(obj=authors, many=True), 200

    def post(self):
        """
        POST request handler of author list API
        Deserializes request data, uses service to add the author to the
        database and returns newly added author in a JSON format with a
        status code 201(Created), or returns error messages with a status code
        400(Bad Request) in case of validation error during deserialization
        :return: a tuple of newly added author JSON and status code 201 or a
        tuple of error messages and status code 400 in case of validation error
        """
        try:
            author = self.service.add_author_from_json(self.schema(), request.json)
        except ValidationError as error:
            return error.messages, 400
        return self.schema().dump(author), 201


class AuthorApi(AuthorApiBase):
    """
    author API class
    """
    #: message to be returned in case of author not being found
    NOT_FOUND_MESSAGE = 'Author not found'

    #: message to be returned in case of author being successfully deleted
    NO_CONTENT_MESSAGE = 'Author deleted successfully'

    def get(self, uuid: str):
        """
        GET request handler of author API
        Fetches the author with given uuid via service and returns it in a
        JSON format with a status code 200(OK), or returns an error message
        with a status code 404(Not Found) in case of author with given
        uuid not being found
        :return: a tuple of the author with given uuid in JSON and a status
        code 200, or a tuple of an error message and a status code 404 in
        case of author with given uuid not being found
        """
        try:
            author = self.service.get_author_by_uuid(uuid)
        except ValueError:
            return self.NOT_FOUND_MESSAGE, 404
        return self.schema().dump(author), 200

    def put(self, uuid):
        """
        PUT request handler of author API
        Uses service to deserialize request data and find the author with
        given uuid and update it with deserialized instance, returns updated
        author in a JSON format with a status code 201(Created), or returns
        error messages with a status code 400(Bad Request) in case of
        validation error during deserialization, or returns an error message
        with a status code 404(Not Found) in case of author with given uuid
        not being found
        :return: a tuple of updated author JSON and status code 200, or a
        tuple of error messages and status code 400 in case of validation
        error, or a tuple of an error message and a status code 404 in case of
        author with given uuid not being found
        """
        try:
            author = self.service.update_author_from_json(
                self.schema(), uuid, request.json
            )
        except ValidationError as error:
            return error.messages, 400
        except ValueError:
            return self.NOT_FOUND_MESSAGE, 404
        return self.schema().dump(author), 200

    def delete(self, uuid):
        """
        DELETE request handler of author API
        Uses service to delete the author with given uuid, returns no
        content message with a status code 204(No Content), or returns an error
        message with a status code 404(Not Found) in case of author with
        given uuid not being found
        :return: a tuple no content message and status code 204, or a tuple of
        an error message and a status code 404 in case of author with given
        uuid not being found
        """
        try:
            self.service.delete_author_by_uuid(uuid)
        except ValueError:
            return self.NOT_FOUND_MESSAGE, 404
        return self.NO_CONTENT_MESSAGE, 204
