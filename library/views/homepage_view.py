"""
Web application homepage views used, this module defines the following classes:
- `HomepageView`, class that defines homepage view
"""
from flask_login import login_required, current_user
from flask import render_template, abort
from library import app, db

@app.route('/', endpoint='homepage')
def homepage():
    """
    Returns rendered `start.html` template for url route `/` and endpoint
    `homepage`
    """
    title = 'Welcome to the library'
    return render_template('start.html', title=title)


@app.route('/admin/dashboard', endpoint='admin_dashboard')
@login_required
def admin_dashboard():
    # prevent non-admins from accessing the page
    if not current_user.role:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")

