from flask import Flask, render_template, redirect, url_for
from todo_list import app, db
from todo_list.models import Task
from todo_list.forms import TaskForm

@app.route("/", methods=["GET", "POST"])
def home():
	form = TaskForm()
	tasks = Task.query.all()
	if form.is_submitted():
		print(form.task.data)
		task = Task(content=str(form.task.data))
		db.session.add(task)
		db.session.commit()
		print("Fuuuuck")
		return redirect(url_for("home"))
	return render_template("home.html", tasks=tasks, form=form)