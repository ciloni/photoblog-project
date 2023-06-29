from flask import Blueprint

from src.controllers.PostsController import create, read, update, delete

#                                           C       R     U       D

PostsRoutes = Blueprint('posts_routes', __name__)

# UserRoutes.route('/', methods=['GET'])(index)
PostsRoutes.route('/create/', methods=['GET','POST'])(create)
PostsRoutes.route('/read/', methods=['GET'])(read)
PostsRoutes.route('/read/<account>', methods=['GET'])(read)
PostsRoutes.route('/update/', methods=['GET'])(update)
PostsRoutes.route('/update/<account>', methods=['GET','POST'])(update)
PostsRoutes.route('/delete/<account>', methods=['GET','POST'])(delete)
