from flask_migrate import Migrate
from app import app
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db, create_app
from app.models import User, Post, Comments
from config import DeploymentConfig

flaskApp = create_app(DeploymentConfig)
migrate = Migrate(db, flaskApp)

@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post, 'Comments':Comments}
