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
        

#     def createPost():
#         post = Post(title=form.title        post = Post(title=form.title.data, body=form.post.data, author=u.posts)
# .data, body=form.post.data, author=u.posts)

if __name__ == '__main__':
    unittest.main(verbosity=5)
    
    