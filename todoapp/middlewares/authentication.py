from flask import jsonify, request
from todoapp.configs.constants import SECRET_KEY
import jwt

def token_required(f):
	def decorated(*args, **kwargs):
		if 'Authorization' not in request.headers :
			return jsonify({'message': 'token is missing'})
		else:
			token = request.headers['Authorization']

		try:
			jwt.decode(token, SECRET_KEY)
		except Exception as e:
			return jsonify({'message': 'token is invalid'})
			
		return f(*args, **kwargs)

	return decorated