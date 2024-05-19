from datetime import datetime, timezone
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

## Lots of the table models were inspired by https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database however they were modified/more tables made to suit our needs

#User table
class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)	#ID of the user, must be unique
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,unique=True)	#Username, must be unique
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)	#Email, must be unique
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    pronouns: so.Mapped[str] = so.mapped_column(sa.String(20))
    ThinkPads: so.Mapped[int] = so.mapped_column()	#Number of thinkpads
    posts: so.WriteOnlyMapped['Post'] = so.relationship(back_populates='author')	#Links User to Post table
    userComments: so.WriteOnlyMapped['Comments'] = so.relationship(back_populates='commentPoster')	#Links User to Comments table

    def set_password(self, password):	#Generates the password hash
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):	#Checks the password entered against the hash
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

#Post table
class Post(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)	#post ID, must be unique
    title: so.Mapped[str] = so.mapped_column(sa.String(140))	#Tite of the post
    body: so.Mapped[str] = so.mapped_column(sa.String(1400))	#Body of the post
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)	#User ID of the author of the post
    author: so.Mapped[User] = so.relationship(back_populates='posts')	#Links Post to User table (with the creator of the post being linked to the user)
    def __repr__(self):
        return '<Post {}>'.format(self.title, self.body)

#Comments table
class Comments(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)	#comment ID, must be unique
    post_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(Post.id), index=True)	#id of the post the comment is responding to
    body: so.Mapped[str] = so.mapped_column(sa.String(1400))	#Body of the comment
    timestamp: so.Mapped[datetime] = so.mapped_column(index=True, default=lambda: datetime.now(timezone.utc))
    user_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey(User.id), index=True)	#User ID of the author of the comment
    commentPoster: so.Mapped[User] = so.relationship(back_populates='userComments')	#Links comment to the author

    def __repr__(self):
        return '<Comments {}>'.format(self.body)


@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))
