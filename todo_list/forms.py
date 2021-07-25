from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
	task = StringField("Task", validators=[DataRequired()])
	submit = SubmitField("Add")
