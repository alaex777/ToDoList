from todo_list import db
from todo_list.models import Task, User
db.drop_all()
db.create_all()
db.session.commit()

