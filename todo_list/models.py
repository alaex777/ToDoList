from todo_list import db

class Task(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	content = db.Column(db.String(128))
	urgency = db.Column(db.String(20))
	status = db.Column(db.String(20), default="Work in progress")
	username = db.Column(db.String(128), db.ForeignKey("user.username"), nullable=False)

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(128), unique=True, nullable=False)
	email = db.Column(db.String(128), unique=True, nullable=False)
	password = db.Column(db.String(128), nullable=False)
