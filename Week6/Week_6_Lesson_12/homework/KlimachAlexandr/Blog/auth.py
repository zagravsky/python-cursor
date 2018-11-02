from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import check_password_hash, generate_password_hash
from Blog.database.db import UserTable, db

auth = Blueprint('auth', __name__)


@auth.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        age = request.form['age']
        email = request.form['email']
        error = None

        user = UserTable.query.filter_by(name=username).first()

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        elif user:
            error = 'User %s is already registered.' % username
        if error is None:
            new_user = UserTable(username,
                                 generate_password_hash(password),
                                 age,
                                 email)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        flash(error)
    return render_template('auth/register.html')


@auth.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = UserTable.query.filter_by(name=username).first()
        error = None
        if user is None:
            error = 'Incorrect username'
        elif not check_password_hash(user.password, password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('blog.home_page'))
        flash(error)
    return render_template('auth/login.html')


@auth.before_app_request
def user_logged_load():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        user = UserTable.query.filter_by(id=user_id).first()
        if user.id:
            g.user = user
            session.permanent = True


@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('blog.home_page'))
