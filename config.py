import os

class Config():
    SECRET_KEY = os.urandom(32)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///photoblog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True