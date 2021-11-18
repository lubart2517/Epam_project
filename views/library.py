from flask import render_template


def index():
    books = [{'name': 'lol', 'count': '1'}]
    return render_template('index.html', books=books)