from flask import Blueprint, request, abort, jsonify, Response

# import db instance for database control
from todoapp.models import db

# import models
from todoapp.models.task import Task

# import controllers
from todoapp.controllers.todo_controller import TodoController

api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
def api_index():
	return 'index here'

@api.route('/todos', methods=['GET'])
def api_todos():
	return jsonify({'todo': 'routes'})

@api.route('/todos', methods=['POST'])
def create_todo():
	return TodoController.create(request)