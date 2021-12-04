from flask import Flask, render_template, abort
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap
from flask_restful import Api

# write your code here
app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)

Bootstrap(app)

MIGRATION_DIR = os.path.join('library', 'migrations')


db = SQLAlchemy(app)
api = Api(app)
migrate = Migrate(app, db, directory=MIGRATION_DIR)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

from .models.user_models import User


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

from .models import author_models, book_models, user_models, order_models
from .rest import init_api
init_api()


@app.errorhandler(403)
def forbidden(error):
    return render_template('errors/403.html', title='Forbidden'), 403


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', title='Page Not Found'), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('errors/500.html', title='Server Error'), 500


from .views import *


