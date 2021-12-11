"""
author service used to make database queries, this module defines the
following classes:
- `authorService`, author service
"""

from library import db
from ..models.author_models import Author


class AuthorService:
    """
    author service used to make database queries
    """
    @staticmethod
    def get_authors():
        """
        Fetches all of the authors from database
        :return: list of all authors
        """

        return Author.query.all()

    @staticmethod
    def get_author_by_uuid(uuid):
        """
        Fetches the author with given UUID from database, raises
        ValueError if such author is not found
        :param uuid: UUID of the author to be fetched
        :raise ValueError: in case of author with given UUID being absent
        in the database
        :return: author with given UUID
        """
        author = db.session.query(Author).filter_by(uuid=uuid).first()
        if author is None:
            raise ValueError('Invalid author uuid')
        return author

    @staticmethod
    def get_author_by_id(author_id):
        """
        Fetches the author with given ID from database, raises
        ValueError if such author is not found
        :param author_id: ID of the author to be fetched
        :raise ValueError: in case of author with given ID being absent
        in the database
        :return: author with given ID
        """
        author = Author.query.get_or_404(author_id)
        if author is None:
            raise ValueError('Invalid author id')
        return author

    @staticmethod
    def get_author_by_name(name):
        """
        Fetches the author with given name   from database,
        raises ValueError if such author is not found
        :param name: name of the author to be fetched
        :return: author with given name
        """
        return db.session.query(Author).filter_by(
            name=name).first()

    @staticmethod
    def add_author_from_json(schema, author_json):
        """
        Deserializes author and adds it to the database
        :param schema: schema to be used to deserialize the author
        :param author_json: data to deserialize the author from
        :return: author that was added
        """
        author = schema.load(author_json, session=db.session)
        db.session.add(author)
        db.session.commit()
        return author

    @classmethod
    def update_author_from_json(cls, schema, uuid, author_json):
        """
        Deserializes author and updates author with given UUID using
        latter, raises ValueError if author with given UUID is not found
        :param schema: schema to be used to deserialize the author
        :param uuid: UUID of the author to be updated
        :param author_json: data to deserialize the author from
        :raise ValueError: in case of author with given UUID being absent
        in the database
        :return: author that was updated
        """
        author = cls.get_author_by_uuid(uuid)
        if author is None:
            raise ValueError('Invalid author uuid')
        author = schema.load(
            data=author_json, session=db.session, instance=author
        )
        db.session.add(author)
        db.session.commit()
        return author

    @classmethod
    def delete_author(cls, author_id):
        """
        Deletes the author with given ID from database, raises
        ValueError if such author is not found
        :param author_id: ID of the author to be deleted
        :raise ValueError: in case of author with given ID being absent
        in the database
        :return: None
        """
        author = cls.get_author_by_id(author_id)
        db.session.delete(author)
        db.session.commit()

    @classmethod
    def delete_author_by_uuid(cls, uuid):
        """
        Deletes the author with given UUID from database, raises
        ValueError if such author is not found
        :param uuid: UUID of the author to be deleted
        :raise ValueError: in case of author with given ID being absent
        in the database
        :return: None
        """
        author = cls.get_author_by_uuid(uuid)
        db.session.delete(author)
        db.session.commit()

    @classmethod
    def update(cls, author_id, name, middle_name, last_name):
        """
        Update author with given id
        :return: None
        """
        author = cls.get_author_by_id(author_id)
        author.name = name
        author.middle_name = middle_name
        author.last_name = last_name
        db.session.commit()

    @staticmethod
    def add_author(name, middle_name, last_name):
        """
        Adds author to the database
        :param name: author name
        :param middle_name: author middle_name
        :param last_name: author last_name
        :return: author that was added
        """
        author = Author(name, middle_name, last_name)
        db.session.add(author)
        db.session.commit()
        return author




