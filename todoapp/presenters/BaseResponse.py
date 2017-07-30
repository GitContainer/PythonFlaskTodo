from flask import jsonify

class BaseResponse(object):

	def __init__(self, data=None):
		self.data = data

	def __decorates(self):
		return self.data

	def response(self):
		message = self.__decorates()
		return jsonify(message)