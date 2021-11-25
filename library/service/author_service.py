
from sqlalchemy.orm import lazyload
from library import db

from ..models.author_models import Author


class AuthorService:
    """
    Author service used to make database queries
    """
    @staticmethod
    def get_first():
        author = db.session.query(Author).filter_by(id=1).first()
        if author is None:
            raise ValueError('Invalid author id')
        return author

