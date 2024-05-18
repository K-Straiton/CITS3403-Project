from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login = LoginManager()
login.login_view = 'login'
moment = Moment()


from .helper import add_dummy_data


def create_app(config):
    flaskApp = Flask(__name__, static_url_path='/static')
    flaskApp.config['SECRET_KEY'] = Config.SECRET_KEY
    flaskApp.config.from_object(Config)

    # db.init_app(flaskApp)
    migrate.init_app(flaskApp, db)
    login.init_app(flaskApp)
    moment.init_app(flaskApp)

    from app.blueprints import main
    flaskApp.register_blueprint(main)
    db.init_app(flaskApp)
    login.init_app(flaskApp)

    # CLI command to add dummy data
    @flaskApp.cli.command("add_data")
    def add_data():
        from app.helper import add_dummy_data
        add_dummy_data()
    return flaskApp

# from app import routes, models, forms

   