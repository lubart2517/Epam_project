import os,sys,inspect

import logging
import unittest, os, sys
from flask_testing import TestCase
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir2 = os.path.dirname(parentdir)
sys.path.insert(0,parentdir2)
from library import create_app, db
from library.models.author_models import Author
from library.models.user_models import User


class TestBase(TestCase):

    def create_app(self):
        app = create_app('testing')
        return app

    def setUp(self):
        """
        Will be called before every test
        """

        db.create_all()

        # create test author
        author = Author(name="admin", last_name="admin2016", middle_name='True')


        # save author to database
        db.session.add(author)
        admin = User(first_name='Eric', last_name='Smit',username="admin", email='123@gmail.com',
                     password="admin2016", role=1)

        # create test non-admin user
        user = User(first_name='John', last_name='Lennon',username="user", email='789@gmail.com',
                     password="admin2016")
        db.session.add(admin)
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestModels(TestBase):

    def test_user_model(self):
        """
        Test number of records in Employee table
        """
        self.assertEqual(User.query.count(), 2)
if __name__ == '__main__':
    unittest.main()

