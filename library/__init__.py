"""
Sources root package.
Initializes web application and web service, contains following subpackages and
modules:
Subpackages:
- `sql`: contains modules used to populate database
- `migrations`: contains migration files used to manage database schema
- `models`: contains modules with Python classes describing database models
- `rest`: contains modules with RESTful service implementation
- `schemas`: contains modules with serialization/deserialization schemas for \
models
- `service`: contains modules with classes used to work with database
- `static`: contains web application static files (scripts, styles, images)
- `templates`: contains web application html templates
- `views`: contains modules with web controllers/views
- `tests`: contains modules with unit tests
"""
# pylint: disable=wrong-import-position, protected-access, cyclic-import, wrong-import-order
from flask import Flask, render_template
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import DevelopmentConfig
from flask_bootstrap import Bootstrap
from flask_restful import Api
MIGRATION_DIR = os.path.join('library', 'migrations')

db = SQLAlchemy()


def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(config_class)

    Bootstrap(app)
    db.init_app(app)
    api = Api(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .models.user_models import User
    from .views import home as home_blueprint

    app.register_blueprint(home_blueprint)

    from.views import auth as auth_blueprint, user as user_blueprint, admin as admin_blueprint

    app.register_blueprint(auth_blueprint)

    app.register_blueprint(user_blueprint)

    app.register_blueprint(admin_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

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



