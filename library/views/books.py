from flask import render_template
from library import app
from flask_login import login_required

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