from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from src.models.UsersModel import User, db

def create():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        account = request.form['account']
        user = User(user_first_name=firstname,
                          user_last_name=lastname,
                          user_email=email,
                          user_account=account,
                          user_password=password
                          )
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('users_routes.read'))

    return render_template('/users/create.html')

@login_required
def read(account = None):
    if(account == None):
        users = db.session.execute(db.select(User).order_by(User.user_account)).scalars()
    else:
        user = db.one_or_404(db.select(User).filter_by(user_account=account))
        return render_template(
            "/users/user.html",
            user = user
        )

    return render_template(
        "/users/read.html",
        users = users
    )
    

def update(account = None):
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        user = db.one_or_404(db.select(User).filter_by(user_account=account))
        user.user_first_name = firstname
        user.user_last_name = lastname
        db.session.commit()
        return redirect(url_for('users_routes.read'))
    else:
        user = db.one_or_404(db.select(User).filter_by(user_account=account))
        return render_template('/users/update.html',
                               user = user)

def delete(account = None):
    user = db.one_or_404(db.select(User).filter_by(user_account=account))
    db.session.delete(user)
    db.session.commit()

    return redirect(url_for('users_routes.read'))