from flask import Flask
from todoapp.models import db

# constants
from todoapp.configs import constants

# routes
from todoapp.routes.main import main
from todoapp.routes.api import api
from todoapp.routes.auth import auth

def create_app(configuration):
	app = Flask(__name__)

	# set configuration
	app.config.from_object(configuration)

	# database
	db.init_app(app)

	# oauth
	# jwt.init_app(app)

	# register blueprints
	app.register_blueprint(main)
	app.register_blueprint(auth)
	app.register_blueprint(api, url_prefix=constants.BASE_API_URL)

	return app
