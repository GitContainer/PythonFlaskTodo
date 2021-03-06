from flask import Blueprint, request, abort, jsonify, Response

# import db instance for database control
from todoapp.models import db

# import models
from todoapp.models.task import Task

# import controllers
from todoapp.controllers.todo_controller import TodoController

# import middlewares
from todoapp.middlewares.authentication import token_required


api = Blueprint('api', __name__)

@api.route('/', methods=['GET'])
@token_required 
def api_index():
	return 'index here'

@api.route('/todos', methods=['GET'])
def api_todos():
	return TodoController.index()

@api.route('/todos', methods=['POST'])
def create_todo():
	return TodoController.create(request)
