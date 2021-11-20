from flask import Flask
import os


# write your code here
api_key = '5972f433a1e0715a50a114b14cf611a6'
app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/Epam'

import library.views.index
