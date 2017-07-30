# utils import
import datetime
import jwt

from flask import request, jsonify

# parent class imports
from todoapp.controllers.base_controller import BaseController
from todoapp.models import db
from todoapp.models.user import User

# constants
from todoapp.configs.constants import SECRET_KEY

class UserAuthorizationController(BaseController):

	@staticmethod
	def login(request):
		username = request.form['username'] if 'username' in request.form else None
		password = request.form['password'] if 'password' in request.form else None
		# if User.authenticate(username, password):
		if username and password:
			# check for user in token table later
			user = User(username, password)
			if user.authenticate(username, password):		
				token = jwt.encode({'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)				
				''' 
				token string should be replaced by token variable: somehow documentation said 
				jwt.encode() return string
				but can't be pass to jsonify here
				'''
				return BaseController.send_response({'access_token': 'token'}, 'logged in successfully')
			else:
				return BaseController.send_response(None, 'wrong credential')
			# save token
		return BaseController.send_response(None, 'Could not verify users')

	@staticmethod
	def register(request):
		first_name = request.form['first_name'] if 'first_name' in request.form else None
		last_name = request.form['last_name'] if 'last_name' in request.form else None
		email = request.form['email'] if 'email' in request.form else None
		username = request.form['username'] if 'username' in request.form else None
		password = request.form['password'] if 'password' in request.form else None
		
		# prior checking user request body
		if(first_name and last_name and email and username and password):
			# create new user instance
			user = User.new_user(first_name, last_name, email, username, password)
			db.session.add(user)
			db.session.commit()
		else:
			return BaseController.send_response(None, 'invalid forms submitted')

		return BaseController.send_response(user.as_dict(), 'user saved')