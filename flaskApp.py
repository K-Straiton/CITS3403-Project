from flask_migrate import Migrate
from app import app
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import app, db
from app.models import User, Post, Comments


@app.shell_context_processor
def make_shell_context():
    return {'sa': sa, 'so': so, 'db': db, 'User': User, 'Post': Post, 'Comments':Comments}
