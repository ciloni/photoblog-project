from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user
from src.models.UsersModel import User, db
from src.models.PostsModel import Post
from werkzeug.security import check_password_hash 

def index():
    return render_template('index.html')

# from flask_login import current_user name=current_user.name
def login():
    # login code goes here
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        # remember = True if request.form.get('remember') else False

        user = db.one_or_404(db.select(User).filter_by(user_email=email))
        # check if the user actually exists
        # take the user-supplied password, hash it, and compare it to the hashed password in the database
        if not user or not check_password_hash(user.user_password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('app_routes.login')) # if the user doesn't exist or password is wrong, reload the page

        # if the above check passes, then we know the user has the right credentials
        login_user(user)
        return redirect('/'+user.user_account)
    else:
        return render_template('/login.html')

def logout():
    logout_user()
    return redirect(url_for('app_routes.index'))

def profile(account = None):
    count = User.query.filter_by(user_account=account).count()
    if count == 0:
        return redirect(url_for('app_routes.index'))
    
    is_owner =  False
    if current_user.is_authenticated == True:
        if current_user.user_account == account:
            is_owner = True

    account_data = db.one_or_404(db.select(User).filter_by(user_account=account))

    count2 = Post.query.filter_by(user_id=account_data.id).count()
    posts = Post.query.filter_by(user_id=account_data.id)
    # posts = db.session.execute(db.select(Post).filter_by(user_id=account_data.id).order_by(Post.post_date_created))

    return render_template(
        "profile.html",
        is_owner = is_owner,
        account = account,
        account_data = account_data,
        posts = posts,
        count2 = count2                   
    )