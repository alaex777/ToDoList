from todo_list import db

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(100))
	urgency = db.Column(db.String(20))
