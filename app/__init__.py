from flask import Flask
from flask_mako import MakoTemplates
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_whooshee import Whooshee
from flask_caching import Cache

mako = MakoTemplates()
db = SQLAlchemy()
whooshee = Whooshee()
login_manager = LoginManager()
cache = Cache(config={'CACHE_TYPE': 'simple'})
login_manager.login_view = 'login' 
login_manager.login_message_category = 'warning'


def create_app():
	app = Flask(__name__)
	app.template_folder = "templates"
	app.config.from_pyfile('config.py')
	mako.init_app(app)
	login_manager.init_app(app)
	db.init_app(app)
	whooshee.init_app(app)
	cache.init_app(app)
	#whooshee.reindex()

	from .admin import admin as admin_bp
	from .auth import auth as auth_bp
	from .user import user as user_bp
	from .api import api as api_bp
	app.register_blueprint(admin_bp)
	app.register_blueprint(user_bp)
	app.register_blueprint(auth_bp)
	app.register_blueprint(api_bp)

	return app
