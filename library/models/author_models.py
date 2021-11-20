from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from library import db
# sqlalchemy instance

class Author(db.Model):
    """
        This class represents an Author. \n
        Attributes:
        -----------
        param name: Describes name of the author
        type name: str max_length=20
        param surname: Describes last name of the author
        type surname: str max_length=20
        param patronymic: Describes middle name of the author
        type patronymic: str max_length=20

    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    surname = db.Column(db.String(128))
    patronymic = db.Column(db.String(128))

    def __init__(self, **kwargs):
        super(Author, self).__init__(**kwargs)