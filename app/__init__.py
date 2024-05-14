from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment



app = Flask(__name__, static_url_path='/static')
app.config['SECRET_KEY'] = Config.SECRET_KEY
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
moment = Moment(app)

from app import routes, models, forms

from .helper import add_dummy_data
   
@app.cli.command("add_data")
def add_data():
    add_dummy_data()

def create_app(config):
    flaskApp = Flask(__name__)
    flaskApp.config.from_object(config)

    db.init_app(flaskApp)

    from app.blueprints import main
    flaskApp.register_blueprint(main)

    #initialise routes

    return flaskApp

