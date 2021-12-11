# pylint: disable=wrong-import-position, protected-access, cyclic-import,
"""This module initialize Flask app"""
import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_restful import Api
from config import DevelopmentConfig


MIGRATION_DIR = os.path.join('library', 'migrations')

db = SQLAlchemy()


def create_app(config_class=DevelopmentConfig):
    """Creates main flask application"""
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config_class)
    Bootstrap(app)
    db.init_app(app)
    api = Api(app)
    from .models.user_models import User
    from .views.blueprint import home as home_blueprint
    from .views.blueprint import auth as auth_blueprint, user as user_blueprint, admin as admin_blueprint
    # migrate = Migrate(app, db, directory=MIGRATION_DIR)
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
    # from library import models, forms
    # from .models import author_models, book_models, user_models, order_models

    from .rest import books_api, authors_api
    api.add_resource(
        books_api.BookListApi,
        '/api/books',
        strict_slashes=False
    )
    api.add_resource(
        books_api.BookApi,
        '/api/book/<uuid>',
        strict_slashes=False
    )
    api.add_resource(
        authors_api.AuthorListApi,
        '/api/authors',
        strict_slashes=False
    )
    api.add_resource(
        authors_api.AuthorApi,
        '/api/author/<uuid>',
        strict_slashes=False
    )

    @app.errorhandler(403)
    def forbidden():
        return render_template('errors/403.html', title='Forbidden'), 403

    @app.errorhandler(404)
    def page_not_found():
        return render_template('errors/404.html', title='Page Not Found'), 404

    @app.errorhandler(500)
    def internal_server_error():
        return render_template('errors/500.html', title='Server Error'), 500
    return app



