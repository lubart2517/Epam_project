"""
This package contains modules defining department and employee services:
Modules:
- `department_view.py`: defines department views
- `employee_view.py`: defines employee views
- `homepage_view.py`: defines homepage views
"""
from . import auth_views
from . import homepage_view
from . import admin_views
from . import user_views

from flask import Blueprint
user = Blueprint('user', __name__)
admin = Blueprint('admin', __name__)
home = Blueprint('home', __name__)
auth = Blueprint('auth', __name__)
