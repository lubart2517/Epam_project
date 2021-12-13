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
import pandas as pd


def filter_fn(row, word):
    for x in row['authors']:
        if word in x['name']:
            return True
    return False

class BookRestService:
    """
    Book rest service used to make api queries
    """
    @staticmethod
    def get_books(url=None):
        """
        Fetches all of the books from api
        :return: list of all books
        """
        if url:
            data = pd.json_normalize(pd.read_json(url))
        else:
            data = pd.json_normalize(requests.get(request.host_url + url_for('api_books')).json())
            # data = pd.json_normalize(pd.read_json(request.host_url + url_for('api_books')))
        return data
        #return jsonify(all_json)

    @classmethod
    def filter(cls, dataframe, query_filter, to_find):
        """
        Sort books according to
        filter parameter
        :return: filtered query of books
        """
        if query_filter == '1':
            # books = dataframe[dataframe['authors']['name'].contains(f'{to_find}')]
            books = dataframe[dataframe.iloc[:, 1:].apply(filter_fn, args=(to_find, ), axis=1)]
        elif query_filter == '2':
            books = dataframe[dataframe['count'] == int(to_find)]
        elif query_filter == '3':
            books = dataframe[dataframe['name'].str.contains(f'{to_find}')]
        elif query_filter == '4':
            books = dataframe[dataframe['description'].str.contains(f'{to_find}')]
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
            books = books.sort_values('name', ascending=True)
        elif query_sort == '2':
            books = books.sort_values('name', ascending=False)
        elif query_sort == '3':
            books = books.sort_values('count', ascending=True)
        elif query_sort == '4':
            books = books.sort_values('count', ascending=False)
        return books
