from flask import Flask
from todoapp.models import db
from todoapp.services import oauth
# constants
from todoapp.configs import constants

# routes
from todoapp.routes.main import main
from todoapp.routes.api import api

def create_app(configuration):
	app = Flask(__name__)

	# set configuration
	app.config.from_object(configuration)

	# database
	db.init_app(app)

	# oauth
	oauth.init_app(app)

	# register blueprints
	app.register_blueprint(main)
	app.register_blueprint(api, url_prefix=constants.BASE_API_URL)

	return app
