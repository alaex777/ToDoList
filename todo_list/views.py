from flask import Flask, render_template, redirect, url_for
from todo_list import app, db
from todo_list.models import Task
from todo_list.forms import TaskForm

@app.route("/", methods=["GET", "POST"])
def home():
	form = TaskForm()
	tasks = Task.query.all()
	if form.is_submitted():
		task = Task(content=str(form.task.data))
		db.session.add(task)
		db.session.commit()
		return redirect(url_for("home"))
	return render_template("home.html", tasks=tasks, form=form)

@app.route("/delete/<int:id>")
def delete(id):
	task = Task.query.get_or_404(id)
	try:
		db.session.delete(task)
		db.session.commit()
		return redirect("/")
	except:
		return "Error in deleting"
