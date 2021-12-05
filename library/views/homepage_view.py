"""
Web application homepage views used, this module defines the following classes:
- `HomepageView`, class that defines homepage view
"""
from flask_login import login_required, current_user
from flask import render_template, abort
from . import home


@home.route('/', endpoint='homepage')
def homepage():
    """
    Returns rendered `start.html` template for url route `/` and endpoint
    `homepage`
    """
    title = 'Welcome to the library'
    return render_template('start.html', title=title)




