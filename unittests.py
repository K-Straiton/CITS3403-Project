import unittest
from app import create_app, db
import sqlalchemy as sa
from unittest import TestCase
from app.config import TestConfig
from app.models import *


class UnitTests(TestCase):
    
    def setUp(self):
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()
        self.client = testApp.test_client()

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
        post = Post(title="test title", body="test body", author=u)
        db.session.add(post)
        db.session.commit()
        posts = db.session.scalars(sa.select(Post).select_from(Post)).all()
        self.assertIn(post, posts)
    

    def test_addComment(self):
        u = User(username='sersangy', email='sersang@isawesome.com', pronouns="she/her", ThinkPads=0)
        db.session.add(u)
        db.session.commit()
        post = Post(title="test title", body="test body", author=u)
        db.session.add(post)
        db.session.commit()       
        comment = Comments(body="test comment", post_id=post.id, user_id=u.id)
        db.session.add(comment)
        db.session.commit()
        comments = db.session.scalars(sa.select(Comments).select_from(Comments)).all()
        self.assertIn(comment, comments)

    def test_login(self):
        u = User(username='sersangy', email='sersang@isawesome.com', pronouns="she/her", ThinkPads=0)
        u.set_password('cat')
        db.session.add(u)
        db.session.commit()
        response = self.client.post('/login', data={
            'username': u.username,
            'password': 'dog'
        })
        self.assertEqual(response.status_code, 200)  # Expect a redirect

if __name__ == '__main__':
    unittest.main(verbosity=5)
    
    