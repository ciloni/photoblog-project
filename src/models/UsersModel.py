from database import db, metadata_obj
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
import datetime

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    metadata_obj
    id = db.Column(db.Integer, primary_key=True)
    user_first_name = db.Column(db.String(25))
    user_last_name = db.Column(db.String(65))
    user_email = db.Column(db.String(255), unique=True)
    user_account = db.Column(db.String(18), unique=True)
    user_password = db.Column(db.String(255))
    user_date_created = db.Column(db.DateTime())

    def __repr__(self):
        return f'<User "{self.user_account}">'

    def __init__(self, user_first_name, user_last_name, user_account, user_email, user_password):
        self.user_first_name = user_first_name
        self.user_last_name = user_last_name
        self.user_account = user_account
        self.user_email = user_email
        self.user_password = generate_password_hash(user_password)
        self.user_date_created = datetime.datetime.now()

    # código util para outras implementacoes
    # def as_dict(self):
    #    return {c.name: str(getattr(self, c.name)) for c in self.__table__.columns}

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_first_name': self.user_first_name,
            'user_last_name': self.user_last_name,
            'user_account': self.user_account,
            'user_email': self.user_email,
            'user_date_created': self.user_date_created
        }