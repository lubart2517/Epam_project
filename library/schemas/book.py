# pylint: disable=no-member
"""
Book schema used to serialize/deserialize books, this module
defines the following classes:
- `BookSchema`, book serialization/deserialization schema
"""


from marshmallow import validates_schema, ValidationError, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from .author import AuthorSchema
from ..models.book_models import Book
from library import db


class Nested(fields.Nested):
    """Nested field that inherits the session from its parent."""

    def _deserialize(self, *args, **kwargs):
        if hasattr(self.schema, "session"):
            self.schema.session = db.session  # overwrite session here
            self.schema.transient = self.root.transient
        return super()._deserialize(*args, **kwargs)


class BookSchema(SQLAlchemyAutoSchema):
    """
    Book serialization/deserialization schema
    """

    class Meta:
        """
        Book schema metadata
        """
        #: model to automatically generate schema from
        model = Book

        load_instance = True
        include_fk = True
        #: fields to provide only on serialization
        # dump_only = ('authors',)

    authors = fields.List(Nested(AuthorSchema))
