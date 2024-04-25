from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'THIS_IS_TERRIBLE_OP_SEC'
from app import routes
from app import forms

