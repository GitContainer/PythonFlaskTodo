from flask import Blueprint, request
from todoapp.controllers.user_authorization_controller import UserAuthorizationController
auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
	return UserAuthorizationController.login(request)
	


@auth.route('/register', methods=['POST'])
def register():
	return UserAuthorizationController.register(request)
	