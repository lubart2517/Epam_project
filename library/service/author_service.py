
from sqlalchemy.orm import lazyload
from library import db

from ..models.author_models import Author


class AuthorService:
    """
    Author service used to make database queries
    """
    @staticmethod
    def get_author_by_uuid(uuid):
        author = db.session.query(Author).filter_by(uuid=uuid).first()
        if author is None:
            raise ValueError('Invalid author uuid')
        return author

