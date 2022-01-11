from dotenv import load_dotenv
import os
# load environment variables
load_dotenv()
user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
server = os.environ.get('POSTGRES_SERVER')
database = os.environ.get('POSTGRES_DATABASE')
database_test = os.environ.get('POSTGRES_DATABASE_TEST')
api_key = os.environ.get('API_KEY')
secret_key = os.environ.get('SECRET_KEY')
user_username = os.environ.get('USER_USERNAME')
user_password = os.environ.get('USER_PASSWORD')


class Config(object):
    """
    Base configurations
    """
    DEBUG = True
    SECRET_KEY = secret_key
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@localhost:{server}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    api_key = api_key
    # SESSION_COOKIE_NAME = "my_session"


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@localhost:{server}/{database}'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """
    Production configurations
    """

    DEBUG = False


class TestingConfig(Config):
    """
    Testing configurations
    """
    SECRET_KEY = os.urandom(32)
    TESTING = True
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@localhost:{server}/{database_test}'

