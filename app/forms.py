from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField, RadioField
from wtforms.validators import DataRequired, InputRequired

class SignInForm(FlaskForm):
	username = StringField("Username",validators=[DataRequired()])
	password = StringField("Password",validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	logIn = SubmitField("Log In")

class SignUpForm(FlaskForm):
	username = StringField("Username",validators=[DataRequired()])
	password = StringField("Password",validators=[DataRequired()])
	signUp = SubmitField("Sign Up")
	pronouns = RadioField("Pronouns:", validators=[InputRequired(message=None)], choices=[("She/Her", "She/Her"), ("He/Him", "He/Him"), ("They/Them","They/Them")])
