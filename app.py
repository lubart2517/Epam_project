from flask import Flask, render_template, request, redirect, flash
import sys
import requests
import datetime
from flask_sqlalchemy import SQLAlchemy
from views.library import index
from views.books import books_index
from views.orders import orders_index
# write your code here
api_key = '5972f433a1e0715a50a114b14cf611a6'
app = Flask(__name__)


app.add_url_rule("/", view_func=index, methods=['GET'])
app.add_url_rule("/books/", view_func=books_index, methods=['GET', 'POST'])
app.add_url_rule("/orders/", view_func=orders_index, methods=['GET', 'POST'])
if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()