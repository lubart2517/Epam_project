from flask import render_template
from library import app
from ..models.author_models import Author

@app.route('/authors/')
def authors_index():
    authors = Author.query.all()
    return render_template('authors_index.html', authors=authors)