from library import db
from ..models.user_models import User


class UserService:
    """
    user service used to make database queries
    """
    @staticmethod
    def get_users():
        """
        Fetches all of the users from database
        :return: list of all users
        """

        return User.query.all()

    @staticmethod
    def get_user_by_id(user_id):
        """
        Fetches the user with given ID from database, raises
        ValueError if such user is not found
        :param user_id: ID of the user to be fetched
        :raise ValueError: in case of user with given ID being absent
        in the database
        :return: user with given ID
        """
        user = User.query.get_or_404(user_id)
        if user is None:
            raise ValueError('Invalid user id')
        return user

    @staticmethod
    def get_user_by_username(username):
        """
        Fetches the user with given username   from database,
        raises ValueError if such user is not found
        :param username: username of the user to be fetched
        :return: user with given username
        """
        return db.session.query(User).filter_by(
            username=username).first()

    @staticmethod
    def add_user_from_json(schema, user_json):
        """
        Deserializes user and adds it to the database
        :param schema: schema to be used to deserialize the user
        :param user_json: data to deserialize the user from
        :return: user that was added
        """
        user = schema.load(user_json, session=db.session)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def update_user_from_json(cls, schema, user_id, user_json):
        """
        Deserializes user and updates user with given ID using
        latter, raises ValueError if user with given ID is not found
        :param schema: schema to be used to deserialize the user
        :param uuid: ID of the user to be updated
        :param user_json: data to deserialize the user from
        :raise ValueError: in case of user with given ID being absent
        in the database
        :return: user that was updated
        """
        user = cls.get_user_by_id(user_id)
        if user is None:
            raise ValueError('Invalid user id')
        user = schema.load(
            user_json, session=db.session, instance=user
        )
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def delete_user(cls, user_id):
        """
        Deletes the user with given ID from database, raises
        ValueError if such user is not found
        :param user_id: ID of the user to be deleted
        :raise ValueError: in case of user with given ID being absent
        in the database
        :return: None
        """
        user = cls.get_user_by_id(user_id)
        db.session.delete(user)
        db.session.commit()

    @classmethod
    def update(cls, user_id, first_name, last_name, username, email, password):
        """
        Update user with given id
        :param user_id: user id
        :param first_name: user first_name
        :param last_name: user last_name
        :param username: user username
        :param email: user email
        :param password: user password
        :return: user that was added
        """
        user = cls.get_user_by_id(user_id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.password_hash = user.set_password(password)
        db.session.commit()
        return user

    @staticmethod
    def add_user(first_name, last_name, username, email, password):
        """
        Adds user to the database
        :param first_name: user first_name
        :param last_name: user last_name
        :param username: user username
        :param email: user email
        :param password: user password
        :return: user that was added
        """
        user = User(first_name, last_name, username, email, password)
        db.session.add(user)
        db.session.commit()
        return user
