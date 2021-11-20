from flask import render_template
from library import app

@app.route('/')
def index():
    books = [{'name': 'lol', 'count': '1'}]
    return render_template('books_index.html', books=books)