from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
	task = StringField("Task", validators=[DataRequired()])
	submit = SubmitField("Add")
	urgency = BooleanField("Importance")
