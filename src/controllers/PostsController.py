from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from src.models.PostsModel import Post, db
from src.models.UsersModel import User
import os, random
import boto3

BUCKET = "flaviophotoblog"


def upload_file(file_name, bucket):
    """
    Function to upload a file to an S3 bucket
    """
    object_name = file_name
    s3_client = boto3.client('s3')
    response = s3_client.upload_file(file_name, bucket, object_name)
    os.remove(file_name)

    return response

@login_required
def create():
    if request.method == 'POST':
        # return str(current_user.id)
        f = request.files['file']
        filename, file_extension = os.path.splitext(f.filename)
        filename = str(current_user.user_account)+str(current_user.id)+str(random.randrange(1,999999999))+file_extension
        f.save(f.filename)
        os.rename(f.filename, filename)
        upload_file(f"{filename}", BUCKET)

        id = current_user.id
        description = request.form['description']
        media_type = file_extension
        media_filename = filename
        media_path = None

        post = Post(user_id=id,
                          post_description=description,
                          post_media_type=media_type,
                          post_media_filename=media_filename,
                          post_media_path=media_path
                          )
        db.session.add(post)
        db.session.commit()

        return redirect('/'+current_user.user_account)
    
    if current_user.is_authenticated == True:
        account_data = db.one_or_404(db.select(User).filter_by(user_account=current_user.user_account))
        return render_template('/posts/create.html',
                               account_data = account_data
                               )

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