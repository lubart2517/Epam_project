"""
Web application homepage views used, this module defines the following classes:
- `HomepageView`, class that defines homepage view
"""

from flask import render_template
from flask_classy import route, FlaskView


class HomepageView(FlaskView):
    """
    Web application homepage views
    """

    #: base url route for all homepage routes
    route_base = '/'

    @route('/', endpoint='homepage')
    def homepage(self):
        """
        Returns rendered `index.html` template for url route `/` and endpoint
        `homepage`
        """
        books = [{'name': 'lol', 'count': '2'}]
        return render_template('index.html', books=books)