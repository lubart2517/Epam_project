"""
Web application homepage views used, this module defines the following functions:
- `homepage`, that defines homepage view
"""
from flask import render_template
from .blueprint import home


@home.route('/', endpoint='homepage')
def homepage():
    """
    Returns rendered `start.html` template for url route `/` and endpoint
    `homepage`
    """
    title = 'Welcome to the library'
    return render_template('start.html', title=title)
