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
    flaskApp.config['SECRET_KEY'] = config.SECRET_KEY
    flaskApp.config.from_object(config)
    db.init_app(flaskApp)
    login.init_app(flaskApp)
    moment.init_app(flaskApp)

    from app.blueprints import main
    flaskApp.register_blueprint(main)
    # CLI command to add dummy data
    @flaskApp.cli.command("add_data")
    def add_data():
        from app.helper import add_dummy_data
        add_dummy_data()
    
    # Pass Stuff to Navbar
    @flaskApp.context_processor
    def base():
        searchform = forms.SearchForm()
        return dict(searchform=searchform)
    
    # Ensure tables are created before the first request
    with flaskApp.app_context():
        db.create_all()
    
    return flaskApp

from app import routes, models, forms


   