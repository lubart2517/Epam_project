from library import db
import datetime
from werkzeug.security import generate_password_hash,  check_password_hash
from flask_login import UserMixin


class User(db.Model, UserMixin):
    """
        This class represents an User. \n
        Attributes:
        -----------
        param name: Describes real name of the user
        type name: str max_length=20
        param last_name: Describes last name of the author
        type last_name: str max_length=20
        param middle_name: Describes middle name of the author
        type middle_name: str max_length=20
        """

    __tablename__ = 'users'
    # user id
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    # user real name
    first_name = db.Column(db.String(20))

    # user real name
    last_name = db.Column(db.String(20))

    # user nickname
    username = db.Column(db.String(20), nullable=False, unique=True)

    # user email address
    email = db.Column(db.String(100), nullable=False, unique=True)

    # user role type(0 - regular user, 1 - administrator)
    role = db.Column(db.Integer(), default=0)

    # field for storing hash of user password
    password_hash = db.Column(db.Text(), nullable=False)

    # date of user profile creation
    created_on = db.Column(db.DateTime(), default=datetime.datetime.now())

    # date of last update of user's profile
    updated_on = db.Column(db.DateTime(), default=datetime.datetime.now(),  onupdate=datetime.datetime.now())

    # string representation of user model
    def __repr__(self):
        return "<{}:{}>".format(self.id, self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @staticmethod
    def get(id):
        return db.session.query(User).filter_by(id=id).first()

    def __init__(self, first_name, last_name, username, email, password):

        # user real name
        self.first_name = first_name

        # user real name
        self.last_name = last_name

        # user nickname
        self.username = username

        # user email address
        self.email = email

        # field for storing hash of user password
        self.password_hash = generate_password_hash(password)
