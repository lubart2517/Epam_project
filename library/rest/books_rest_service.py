""" Books REST service, this module defines the following classes:
- `BookRestService`, which provides methods for operations with books by api
"""
import requests
from marshmallow import EXCLUDE
from sqlalchemy.orm import scoped_session, sessionmaker
from flask import url_for, redirect, request, jsonify
from ..schemas.book import BookSchema
from ..models.book_models import Book
from library import db

class BookRestService:
    """
    Book rest service used to make api queries
    """
    @staticmethod
    def get_books():
        """
        Fetches all of the books from api
        :return: list of all books
        """
        all_json = requests.get(request.host_url + url_for('api_books')).json()
        return all_json
        #return jsonify(all_json)
