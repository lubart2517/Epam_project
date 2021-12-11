"""
Author schema used to serialize/deserialize authors, this module
defines the following classes:
- `AuthorSchema`, author serialization/deserialization schema
"""


from marshmallow import validates_schema, ValidationError, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ..models.author_models import Author


class AuthorSchema(SQLAlchemyAutoSchema):
    """
    author serialization/deserialization schema
    """

    class Meta:
        """
        author schema metadata
        """
        #: model to automatically generate schema from
        model = Author

        #: fields excluded from schema
        exclude = ['id']

        #: deserialize to model instance
        load_instance = True

        #: include foreign keys into schema
        include_fk = True
