from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
	task = StringField("Task", validators=[DataRequired()])
	username = StringField("Username", validators=[DataRequired()])
	submit = SubmitField("Add")
	urgency = BooleanField("Importance")

class LoginForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	submit = SubmitField("Log In")

class RegisterForm(FlaskForm):
	username = StringField("Username", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	password = PasswordField("Password", validators=[DataRequired()])
	repeat_password = PasswordField("Repeat Password", validators=[DataRequired()])
	submit = SubmitField("Register")
