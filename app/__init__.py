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
    app = Flask(__name__, static_url_path='/static')
    app.config['SECRET_KEY'] = Config.SECRET_KEY
    app.config.from_object(Config)

    from app.blueprints import main

    db.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)
    app.register_blueprint(main)


    # CLI command to add dummy data
    @app.cli.command("add_data")
    def add_data():
        from app.helper import add_dummy_data
        add_dummy_data()
    # Pass Stuff to Navbar
    @app.context_processor
    def base():
        searchform = forms.SearchForm()
        return dict(searchform=searchform)
    
    return app

    

from app import routes, models, forms


   