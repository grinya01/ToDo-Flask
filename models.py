from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    password = db.Column(db.String())

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return f""


class TaskModel(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String())
    description = db.Column(db.String())
    task_owner = db.Column(db.String())

    def __init__(self, task_name, description, task_owner):
        self.task_name = task_name
        self.description = description
        self.task_owner = task_owner

    def __repr__(self):
        return f""