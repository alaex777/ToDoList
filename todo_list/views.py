from flask import Flask, render_template, redirect, url_for
from todo_list import app, db
from todo_list.models import Task, User
from todo_list.forms import TaskForm, LoginForm, RegisterForm

@app.route("/")
def start():
	return redirect("/login")

@app.route("/home/admin", methods=["GET", "POST"])
def admin():
	form = TaskForm()
	tasks = Task.query.all()
	if form.is_submitted():
		task = Task(content=str(form.task.data), urgency=str(form.urgency.data), username=str(form.username.data))
		db.session.add(task)
		db.session.commit()
		return redirect("/home/admin")
	return render_template("home.html", tasks=tasks, form=form, users=User.query.all())

@app.route("/home/<username>", methods=["GET", "POST"])
def user(username):
	tasks = Task.query.filter_by(username=username)
	return render_template("user.html", tasks=tasks, username=username)

@app.route("/complete/<username>/<int:id>")
def complete(id, username):
	task = Task.query.get_or_404(id)
	task.status = "Complete"
	db.session.commit()
	address = "/home/" + str(username)
	return redirect(address)

@app.route("/delete/<int:id>")
def delete(id):
	task = Task.query.get_or_404(id)
	try:
		db.session.delete(task)
		db.session.commit()
		return redirect("/home/admin")
	except:
		return "Error in deleting"

@app.route("/edit/<int:id>",  methods=["GET", "POST"])
def edit(id):
	form = TaskForm()
	if form.is_submitted():
		task = Task.query.get(id)
		task.content = str(form.task.data)
		db.session.commit()
		return redirect("/home/admin")
	return render_template("edit.html", form=form)

@app.route("/login", methods=["POST", "GET"])
def login():
	form = LoginForm()
	if form.is_submitted():
		if form.username.data in [i[0] for i in User.query.with_entities(User.username)]:
			user = User.query.filter_by(username=form.username.data).all()[0]
			if user.username == "admin" and user.password == "root":
				return redirect("/home/admin")
			if user.password == form.password.data:
				address = "/home/" + str(form.username.data)
				return redirect(address)
			else:
				return "Incorrect password"
		else:
			return "Incorrect username"
	return render_template("login.html", form=form)

@app.route("/register", methods=["GET", "POST"])
def register():
	form = RegisterForm()
	if form.is_submitted():
		if form.password.data == form.repeat_password.data:
			user = User(username=form.username.data, password=form.password.data, email=form.email.data)
			db.session.add(user)
			db.session.commit()
			address = "/home/" + str(form.username.data)
			return redirect(address)
		else:
			return "Passwords do not match"
	return render_template("register.html", form=form)
