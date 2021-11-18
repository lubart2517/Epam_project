from flask import render_template

def books_index():
    books = [{'name': 'lol', 'count': '2'}]
    return render_template('index.html', books=books)