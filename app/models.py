from app import db, login_manager, whooshee
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

class User(UserMixin,db.Model):
	uid = db.Column(db.Integer,primary_key = True)
	username = db.Column(db.String(64), index=True, unique=True)
	password_hash = db.Column(db.String(120))
	email = db.Column(db.String(120), unique=True)
	create_time = db.Column(db.DateTime, default=datetime.now)

	def is_authenticated(self):
		return True

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def get_id(self):
		return str(self.uid)

	def __repr__(self):
		return '<User %r>' %self.username

	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self,password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(uid):
    return User.query.get(int(uid))



@whooshee.register_model('title', 'body')
class Book(db.Model):
	bookid = db.Column(db.Integer,primary_key = True)
	title = db.Column(db.String(64), index=True, unique=True)
	body = db.Column(db.String(64), index=True)
	cover_path = db.Column(db.String(120), unique=True)
	create_time = db.Column(db.DateTime, default=datetime.now)


