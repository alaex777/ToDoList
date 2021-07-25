from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SECRET_KEY"] = "e69d631c52ef7ac79c9f279472fbf00e"

db = SQLAlchemy(app)

from todo_list import views
