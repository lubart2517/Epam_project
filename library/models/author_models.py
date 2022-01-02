# pylint: disable=no-member
import uuid as new_uuid
from library import db


class Author(db.Model):
    """
        This class represents an Author. \n
        Attributes:
        -----------
        param name: Describes name of the author
        type name: str max_length=20
        param last_name: Describes last name of the author
        type last_name: str max_length=20
        param middle_name: Describes middle name of the author
        type middle_name: str max_length=20

    """
    #: Name of the database table storing authors
    __tablename__ = 'Author'

    #: Database id of the author
    id = db.Column(db.Integer, primary_key=True)

    # Name of the author
    name = db.Column(db.String(20))

    # Last name of the author
    last_name = db.Column(db.String(20))

    # Middle name of the author
    middle_name = db.Column(db.String(20))

    #: UUID of the author
    uuid = db.Column(db.String(36), unique=True)

    def __init__(self, name, middle_name, last_name, uuid=None):
        #: Name of the author
        self.name = name

        # Middle name of the author
        self.middle_name = middle_name

        # Last name of the author
        self.last_name = last_name

        #: UUID of the author
        if uuid:
            self.uuid = uuid
        else:
            self.uuid = str(new_uuid.uuid4())

    def __repr__(self):
        """
        Returns string representation of author
        """
        return f'{self.name} {self.last_name}'
