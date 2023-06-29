from flask import Blueprint

from src.controllers.UsersController import create, read, update, delete

#                                           C       R     U       D

UserRoutes = Blueprint('users_routes', __name__)

# UserRoutes.route('/', methods=['GET'])(index)
UserRoutes.route('/create/', methods=['GET','POST'])(create)
UserRoutes.route('/read/', methods=['GET'])(read)
UserRoutes.route('/read/<account>', methods=['GET'])(read)
UserRoutes.route('/update/', methods=['GET'])(update)
UserRoutes.route('/update/<account>', methods=['GET','POST'])(update)
UserRoutes.route('/delete/<account>', methods=['GET','POST'])(delete)
