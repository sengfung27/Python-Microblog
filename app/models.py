from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

@login.user_loader
def load_user(id):
	return User.query.get(int(id))
	


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(64), index=True, unique=True)
	email = db.Column(db.String(120), index=True, unique=True)
	urole = db.Column(db.Integer, index=True)
	password_hash = db.Column(db.String(128))
	about_me = db.Column(db.String(140))
	last_seen = db.Column(db.DateTime, default=datetime.utcnow)
	
	def __repr__(self):
		return '<User {} {}>'.format(self.username, self.urole)
	
	def get_id(self):
		return self.id

	def get_username(self):
		return self.username
		
	def get_email(self):
		return self.email
		
	def get_urole(self):
		return self.urole

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)
	
	def check_password(self, password):
		return check_password_hash(self.password_hash,password)

	def avatar(self,size):
		digest = md5(self.email.lower().encode('utf-8')).hexdigest()
		return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

#u = User(username='seng',email='@wsd',urole=4)
#u.set_password('666')
#db.session.add(u)
#db.session.commit()
