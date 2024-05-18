# from app import app
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, create_app
from app.models import User, Post, Comments
from app.config import DeploymentConfig
from flask_migrate import Migrate

flaskApp = create_app(DeploymentConfig)
migrate = Migrate(flaskApp, db)

@flaskApp.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post, 'Comments':Comments}
