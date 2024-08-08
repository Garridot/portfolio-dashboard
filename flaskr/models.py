from . import db, bcrypt
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)


class Project(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    skills      = db.Column(db.String(250), nullable=True)
    url_github  = db.Column(db.String(80), nullable=False)
    url_project = db.Column(db.String(80), nullable=False)

        