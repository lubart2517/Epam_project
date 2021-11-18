from flask import Flask, render_template, request, redirect, flash
import sys
import requests
import datetime
from flask_sqlalchemy import SQLAlchemy
import string
# write your code here
api_key = '5972f433a1e0715a50a114b14cf611a6'
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    books = [{'name': 'lol', 'count': '1'}]
    return render_template('index.html', books=books)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg_host, arg_port = sys.argv[1].split(':')
        app.run(host=arg_host, port=arg_port)
    else:
        app.run()