from flask import Blueprint
user = Blueprint('user', __name__)
admin = Blueprint('admin', __name__)
home = Blueprint('home', __name__)
auth = Blueprint('auth', __name__)