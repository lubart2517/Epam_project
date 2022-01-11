from flask import request
from flask_restful import abort
from ..service.user_service import UserService


def authenticate(func):
    def wrapper(*args, **kwargs):
        user = UserService.get_user_by_username(request.authorization.username)
        if user:
            if user.check_password(request.authorization.password):
                return func(*args, **kwargs)

        return abort(403)
    return wrapper


def is_admin(func):
    def wrapper(*args, **kwargs):
        user = UserService.get_user_by_username(request.authorization.username)
        if user:
            if user.check_password(request.authorization.password):
                if user.role == 1:
                    return func(*args, **kwargs)

        return abort(403)
    return wrapper
