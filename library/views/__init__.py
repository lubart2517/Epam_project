"""
This package contains modules defining department and employee services:
Modules:
- `department_view.py`: defines department views
- `employee_view.py`: defines employee views
- `homepage_view.py`: defines homepage views
"""

from library import app

from . import books_view
from . import auth_views
from . import homepage_view
from ..auth.forms import RegistrationForm


def init_views():
    """
    Register views
    :return: None
    """
    books_view.BookIndexView.register(app)
    #auth_views.register.register(app)
    # department_view.DepartmentView.register(app)
    homepage_view.HomepageView.register(app)