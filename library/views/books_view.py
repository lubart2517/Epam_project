
"""
Web application homepage views used, this module defines the following classes:
- `HomepageView`, class that defines homepage view
"""

from flask import render_template
from flask_classy import route, FlaskView
from library import app, db
from flask_login import login_required
from ..models.book_models import Book


class BookIndexView(FlaskView):
    """
    Web application books views
    """

    #: base url route for all books routes
    route_base = '/books/'

    @route('/', endpoint='index')
    def index(self):
        """
        Returns rendered `books_index.html` template for url route `/books` and endpoint
        `index`
        """
        books = db.session.query(Book).first()
        return render_template('books_index.html', books=books)
"""
@app.route('/books/')
def books_index():
    books = [{'name': 'lol', 'count': '2'}]
    return render_template('books_index.html', books=books)


@app.route('/books/author/')
def books_author():
    books = [{'name': 'lol', 'count': '2'}]
    return render_template('books_author.html', books=books)


@app.route('/books/user/')
def books_user():
    books = [{'name': 'lol', 'count': '2'}]
    return render_template('books_user.html', books=books)


@app.route('/books/detail/')
def books_detail():
    books = [{'name': 'lol', 'count': '2'}]
    return render_template('books_detail.html', books=books)


@login_required
@app.route('/books/unordered/')
def books_unordered():
    books = [{'name': 'lol', 'count': '2'}]
    return render_template('books_unordered.html', books=books)
"""""