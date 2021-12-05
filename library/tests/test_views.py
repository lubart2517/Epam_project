from flask import abort, url_for
from flask_login import current_user, login_user
import os,sys,inspect

# move to two level above for correct load library app
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
parentdir2 = os.path.dirname(parentdir)
sys.path.insert(0,parentdir2)

from library.models.author_models import Author
from library.models.book_models import Book
from library.models.order_models import Order
from library.models.user_models import User
from library.tests.test_init import TestBase
from library import db


class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        response = self.client.get(url_for('home.homepage'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        """
        Test that login page is accessible without login
        """
        response = self.client.get(url_for('auth.login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view(self):
        """
        Test that logout link is inaccessible without login
        and redirects to login page then to logout
        """
        target_url = url_for('auth.logout')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)


    def test_admin_dashboard_view(self):
        """
        Test that dashboard is inaccessible without login
        and redirects to login page then to dashboard
        """
        target_url = url_for('admin.dashboard')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_books_view(self):
        """
        Test that books page is inaccessible without login
        and redirects to login page then to books page
        """
        target_url = url_for('admin.books')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_authors_view(self):
        """
        Test that authors page is inaccessible without login
        and redirects to login page then to authors page
        """
        target_url = url_for('admin.authors')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_orders_view(self):
        """
        Test that orders page is inaccessible without login
        and redirects to login page then to orders page
        """
        target_url = url_for('admin.orders')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_success_login(self):
        """
        Testing the possibility of user logging in
        """
        target_url = url_for('auth.login')
        with self.client as client:
            response = client.post(target_url, data={
                'email': '123@gmail.com',
                'password': 'admin2016',
            }, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertTrue(User.is_authenticated)

    def test_book_edit(self):
        with self.client as client:
            user = User.query.filter_by(id=1).first()
            login_user(user, remember=True)
            target = url_for('admin.edit_book', id=1)
            self.assertEqual(current_user.role, 1)
            resp =client.get(target)
            self.assertEqual(resp.status_code, 200)


    def test_success_register(self):
        """
        Testing the possibility of user register
        """
        target_url = url_for('auth.register')
        response = self.client.post(target_url, data={
            'first_name':'Eric_Prime', 'last_name':'Smit&Vesson','username':"Erick_P", 'email':'12367@gmail.com',
                     'password':"admin2020"
        }, follow_redirects=True)

        self.assertEqual(response.status_code, 200)

        self.assertTrue(User.is_authenticated)

    def test_user_orders_view(self):
        """
        Test that user orders page is inaccessible without login
        and redirects to login page then to orders page
        """
        target_url = url_for('user.orders')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_user_books_view(self):
        """
        Test that user books page is inaccessible without login
        and redirects to login page then to books page
        """
        target_url = url_for('user.books')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_user_authors_view(self):
        """
        Test that user authors page is inaccessible without login
        and redirects to login page then to authors page
        """
        target_url = url_for('user.authors')
        redirect_url = url_for('auth.login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)


class TestErrorPages(TestBase):

    def test_403_forbidden(self):
        # create route to abort the request with the 403 Error
        @self.app.route('/403')
        def forbidden_error():
            abort(403)

        response = self.client.get('/403')
        self.assertEqual(response.status_code, 403)
        self.assertTrue("403 Error" in response.get_data(as_text=True))

    def test_404_not_found(self):
        response = self.client.get('/nothinghere')
        self.assertEqual(response.status_code, 404)
        self.assertTrue("404 Error" in response.get_data(as_text=True))

    def test_500_internal_server_error(self):
        # create route to abort the request with the 500 Error
        @self.app.route('/500')
        def internal_server_error():
            abort(500)

        response = self.client.get('/500')
        self.assertEqual(response.status_code, 500)
        self.assertTrue("500 Error" in response.get_data(as_text=True))