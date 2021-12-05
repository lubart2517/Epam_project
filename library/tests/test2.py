
import os,sys,inspect

import logging
import unittest, os, sys
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir2 = os.path.dirname(parentdir)
sys.path.insert(0,parentdir2)
from library.models.author_models import Author
from library.tests.test import TestBase
class TestModels(TestBase):

    def test_user_model(self):
        """
        Test number of records in Employee table
        """
        self.assertEqual(Author.query.count(), 1)