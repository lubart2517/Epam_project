# pylint: disable=no-member
"""
Book schema used to serialize/deserialize books, this module
defines the following classes:
- `BookSchema`, book serialization/deserialization schema
"""


from marshmallow import validates_schema, ValidationError, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ..models.book_models import Book


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
        dump_only = ('authors',)

    authors = fields.Nested(
        'AuthorSchema', many=True
    )