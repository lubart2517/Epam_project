# pylint: disable=wrong-import-position, protected-access, cyclic-import, import-outside-toplevel
"""This module initialize Flask app"""
import os
import sys
import logging
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_restful import Api
from flask_httpauth import HTTPBasicAuth
from config import DevelopmentConfig


MIGRATION_DIR = os.path.join('library', 'migrations')

db = SQLAlchemy()
auth = HTTPBasicAuth()


def create_app(config_class=DevelopmentConfig):
    """Creates main flask application"""
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config_class)

    # logging
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s: %(message)s')

    file_handler = logging.FileHandler(filename='app.log', mode='w+')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(logging.DEBUG)

    # pylint: disable=no-member
    logger = app.logger
    logger.handlers.clear()
    app.logger.addHandler(file_handler)
    app.logger.addHandler(console_handler)
    app.logger.setLevel(logging.DEBUG)
    werkzeug_logger = logging.getLogger('werkzeug')
    werkzeug_logger.handlers.clear()
    werkzeug_logger.addHandler(file_handler)
    werkzeug_logger.addHandler(console_handler)
    werkzeug_logger.setLevel(logging.DEBUG)

    Bootstrap(app)
    db.init_app(app)
    api = Api(app)
    from .models.user_models import User
    from .views.blueprint import home as home_blueprint
    from .views.blueprint import auth as auth_blueprint, user as user_blueprint, admin as admin_blueprint
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    app.register_blueprint(home_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

    from .rest.resources import register_resources
    register_resources(api)

    @app.errorhandler(403)
    def forbidden(error):
        return render_template('errors/403.html', title='Forbidden', error = error), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html', title='Page Not Found', error = error), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return render_template('errors/500.html', title='Server Error', error = error), 500
    return app
