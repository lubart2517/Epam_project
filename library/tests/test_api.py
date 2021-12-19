"""This module contains tests of correct CRUD operations with db by API"""
import json
import pandas as pd
from flask import abort, url_for, request
from library.models.user_models import User
from library.tests.test_init import TestBase


class TestApi(TestBase):
    """
    Class for testing Api
    """
    def test_books(self):
        """
        Test that books_api accessible and returns books from db
        """
        response = self.client.get(url_for('api_books'))
        self.assertEqual(response.status_code, 200)
        books = pd.json_normalize(response.get_json())
        self.assertEqual(books['count'][0], 5)
        self.assertEqual(books['name'][0], 'IT')

    def test_user_books(self):
        """
        Test that books_api accessible and returns books from db
        """
        response = self.client.get(url_for('api_user_books'))
        self.assertEqual(response.status_code, 200)
        books = pd.json_normalize(response.get_json())
        self.assertEqual(books['available'][0], 4)
        self.assertEqual(books['name'][0], 'IT')

    def test_book_get_uuid(self):
        """
        Test that book_api accessible and returns book with given uuid from db
        """
        response = self.client.get(url_for('api_book_uuid', uuid = '92a69ce8-13b4-4fe0-a4cc-d519e8fb7933'))
        self.assertEqual(response.status_code, 200)
        book = pd.json_normalize(response.get_json())
        self.assertEqual(book['count'][0], 5)
        self.assertEqual(book['name'][0], 'IT')

    def test_book_desc_contains(self):
        """
        Test that book_api accessible and returns books with description contains 'part'
        """
        response = self.client.get(url_for('api_book_filter', name='part'))
        self.assertEqual(response.status_code, 200)
        book = pd.json_normalize(response.get_json())
        self.assertEqual(book['count'][0], 5)
        self.assertEqual(book['name'][0], 'IT')

    def test_book_desc_contains_sort(self):
        """
        Test that book_api accessible and returns books with description contains 'part' sorted
        """
        response = self.client.get(url_for('api_book_filter', name='part', sort='1'))
        self.assertEqual(response.status_code, 200)
        book = pd.json_normalize(response.get_json())
        self.assertEqual(book['count'][0], 5)
        self.assertEqual(book['name'][0], 'IT')

    def test_author_get_uuid(self):
        """
        Test that author_api accessible and returns author with given uuid from db
        """
        response = self.client.get(url_for('api_author_uuid', uuid = '8d3fe6dd-d750-47be-91b5-c926c31ac7ff'))
        self.assertEqual(response.status_code, 200)
        author = pd.json_normalize(response.get_json())
        self.assertEqual(author['last_name'][0], "admin2016")
        self.assertEqual(author['name'][0], 'admin')

    def test_authors(self):
        """
        Test that authors_api accessible and returns authors from db
        """
        response = self.client.get(url_for('api_authors'))
        self.assertEqual(response.status_code, 200)
        author = pd.json_normalize(response.get_json())
        self.assertEqual(author['last_name'][0], "admin2016")
        self.assertEqual(author['name'][0], 'admin')

    def test_author_put_uuid(self):
        """
        Test that author_api accessible and changes author with given uuid in db
        """
        resp = {'last_name': 'admin2016', 'name': 'admin', 'middle_name': 'de',
                'uuid': '8d3fe6dd-d750-47be-91b5-c926c31ac7ff'}
        response = self.client.put(url_for('api_author_uuid', uuid='8d3fe6dd-d750-47be-91b5-c926c31ac7ff'),
                                   data=json.dumps(resp),
                       content_type='application/json')
        self.assertEqual(response.status_code, 200)
        author = pd.json_normalize(response.get_json())
        self.assertEqual(author['last_name'][0], "admin2016")
        self.assertEqual(author['name'][0], 'admin')

    def test_author_add(self):
        """
        Test that author_api accessible and adds author in db
        """
        author = {'last_name': 'Derec', 'name': 'John', 'middle_name': 'de',
                'uuid': '8d3fe6dd-d443-47be-91b5-c926c31ac7ff'}
        response = self.client.post(url_for('api_authors'),
                                   data=json.dumps(author),
                       content_type='application/json')
        self.assertEqual(response.status_code, 201)
        author = pd.json_normalize(response.get_json())
        self.assertEqual(author['last_name'][0], "Derec")
        self.assertEqual(author['name'][0], 'John')

    def test_author_del_uuid(self):
        """
        Test that author_api accessible and deletes author with given uuid from db
        """
        response = self.client.delete(url_for('api_author_uuid', uuid='8d3fe6dd-d750-47be-91b5-c926c31ac7ff'))
        self.assertEqual(response.status_code, 204)
