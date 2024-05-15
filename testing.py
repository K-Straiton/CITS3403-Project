import os
os.environ['DATABASE_URL'] = 'sqlite://'

from datetime import datetime, timezone, timedelta
import unittest
from app import app, db
import sqlalchemy as sa

from app.models import *


class UserModelCase(unittest.TestCase):
    
    def setUp(self):
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_password_hashing(self):
        u = User(username='sersangy', email='sersang@isawesome.com', pronouns="she/her", ThinkPads=0)
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))

    def test_addUserToDB(self):
        user = User(username='sersangy', email='sersang@isawesome.com', pronouns="she/her", ThinkPads=0)
        db.session.add(user)
        db.session.commit()
        users =  db.session.scalars(sa.select(User).select_from(User)).all()
        self.assertIn(user, users)
        
    def test_createPost(self):
        # u =  db.session.scalars(sa.select(User).select_from(User)).first()
        u = User(username='sersangy', email='sersang@isawesome.com', pronouns="she/her", ThinkPads=0)
        db.session.add(u)
        db.session.commit()
        post = Post(id = 1, title="test title", body="test body", author=u, user_id=u.id)
        db.session.add(post)
        db.session.commit()
        posts = db.session.scalars(sa.select(Post).select_from(Post)).all()
        self.assertIn(post, posts)
    
    # def test_addComment(self):
    #     u = db.session.scalar(sa.select(Comments).select_from(User)).first()


if __name__ == '__main__':
    unittest.main(verbosity=5)
    
    