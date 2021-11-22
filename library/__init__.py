from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# write your code here
api_key = '5972f433a1e0715a50a114b14cf611a6'
app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/Epam'
MIGRATION_DIR = os.path.join('library', 'migrations')


db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
migrate = Migrate(app, db, directory=MIGRATION_DIR)

from .views import init_views
init_views()
from .models import author_models, book_models, user_models, order_models



