from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField, RadioField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, InputRequired, Length
import sqlalchemy as sa
from app import db
from app.models import User


class SignInForm(FlaskForm):
	username = StringField("Username",validators=[DataRequired()])
	password = StringField("Password",validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	logIn = SubmitField("Log In")

class SignUpForm(FlaskForm):
	username = StringField("Username",validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	password = PasswordField("Password",validators=[DataRequired()])
	password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password', "Passwords must match.")])
	signUp = SubmitField("Sign Up")
	pronouns = RadioField("Pronouns:", validators=[InputRequired(message=None)], choices=[("She/Her", "She/Her"), ("He/Him", "He/Him"), ("They/Them","They/Them")])
	
	def validate_username(self, username):
		user = db.session.scalar(sa.select(User).where(
			User.username == username.data))
		if user is not None:
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):
		user = db.session.scalar(sa.select(User).where(
			User.email == email.data))
		
		if user is not None:
			raise ValidationError('Please use a different email address.')

class newPost(FlaskForm):
    title = TextAreaField('Write Title Placeholder', validators=[DataRequired(), Length(min=1, max=140)])
    post = TextAreaField('Write Post Placeholder', validators=[DataRequired(), Length(min=1, max=1400)])
    submit = SubmitField('Post!')

class newComment(FlaskForm):
	commentBody = TextAreaField('Write comment placeholder', validators=[DataRequired(), Length(min=1, max=1400)])
	submit = SubmitField('Reply!')
