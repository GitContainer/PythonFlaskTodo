from pprint import pprint

from flask import request, jsonify

# import parent class
from todoapp.controllers.base_controller import BaseController

# import db instance for database control
from todoapp.models import db

# import models
from todoapp.models.task import Task

class TodoController(BaseController):

	@staticmethod
	def index():
		tasks = Task.query.all()
		result = []
		for task in tasks:
			result.append(task.as_dict())
		return BaseController.send_response(result, 'todos retrieved successfully')

	@staticmethod
	def create(request):
		payload = request.form['task']
		todo = Task(payload)
		db.session.add(todo)
		db.session.commit()
		return BaseController.send_response(todo.as_dict(), 'recorded successfully')
		# return super(TodoController, TodoController).send_response(list(todo), 'record inserted successfully');
