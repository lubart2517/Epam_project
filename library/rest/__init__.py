"""
This package contains modules defining department and employee REST APIs and
functions to initialize respective API endpoints:
Modules:
- `department_api.py`: defines model representing departments
- `employee_api.py`: defines model representing employees
Functions:
- `init_api`: register REST API endpoints
"""

from . import books_api
from . import authors_api


def init_api():
    """
    Register REST Api endpoints
    :return: None
    """
    api.add_resource(
        books_api.BookListApi,
        '/api/books',
        strict_slashes=False
    )
    api.add_resource(
        books_api.BookApi,
        '/api/book/<uuid>',
        strict_slashes=False
    )
    api.add_resource(
        authors_api.AuthorListApi,
        '/api/authors',
        strict_slashes=False
    )
    api.add_resource(
        authors_api.AuthorApi,
        '/api/author/<uuid>',
        strict_slashes=False
    )

