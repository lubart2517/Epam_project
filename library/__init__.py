from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap

# write your code here
api_key = '5972f433a1e0715a50a114b14cf611a6'
app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)

Bootstrap(app)
MIGRATION_DIR = os.path.join('library', 'migrations')


db = SQLAlchemy(app)

migrate = Migrate(app, db, directory=MIGRATION_DIR)

from .views import init_views
init_views()
from .models import author_models, book_models, user_models, order_models



