from flask import Flask
from flask_login import LoginManager
from src.models.UsersModel import User, db

from config import Config

from database import db

from src.routes.PostsRoutes import PostsRoutes
from src.routes.UsersRoutes import UserRoutes
from src.routes.AppRoutes import AppRoutes

import datetime

def create_app(config_class=Config):
    app = Flask(__name__,template_folder="views/")
    app.config.from_object(config_class)
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'app_routes.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.one_or_404(db.select(User).filter_by(id=user_id))

    app.register_blueprint(UserRoutes, url_prefix='/users')
    app.register_blueprint(AppRoutes, url_prefix='/')
    app.register_blueprint(PostsRoutes, url_prefix='/posts')

    @app.template_filter()
    def format_datetime(value):
        date_formated = datetime.datetime.date(value)
        return date_formated
        

    return app

