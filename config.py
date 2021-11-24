from dotenv import load_dotenv
load_dotenv()
import os


user = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
server = os.environ.get('POSTGRES_SERVER')
database = os.environ.get('POSTGRES_DATABASE')


class Config:
    DEBUG = True
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = f'postgresql://{user}:{password}@localhost:{server}/{database}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_I18N_ENABLED = True