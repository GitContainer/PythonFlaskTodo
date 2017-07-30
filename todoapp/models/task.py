import datetime
from todoapp.models import db

# import parent class
from todoapp.models.base_model import BaseModel


class Task(db.Model, BaseModel):
	__tablename__ = 'tasks'

	readable = ['id', 'task', 'created_at', 'updated_at']

	id = db.Column(db.Integer, primary_key=True)
	task = db.Column(db.String)
	created_at = db.Column(db.DateTime)
	updated_at = db.Column(db.DateTime)

	def __init__(self, task):
		self.task = task
		self.created_at = datetime.datetime.now()
		self.updated_at = datetime.datetime.now()