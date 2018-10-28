from flask import Blueprint, render_template, request, url_for, redirect, flash, session, g
from werkzeug.security import check_password_hash, generate_password_hash
from Blog.database.db import get_user_db, write_user_db

auth = Blueprint('auth', __name__)


@auth.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        age = request.form['age']
        email = request.form['email']
        db = get_user_db()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        for user in db['data']:
            if username == user['name']:
                error = 'User %s is already registered.' % username
                break
        if error is None:
            new_user = {"id": db["id_counter"],
                        "name": username,
                        "password": generate_password_hash(password),
                        "age": age,
                        "email": email}
            db["id_counter"] += 1
            db["data"].append(new_user)
            write_user_db(db)
            return redirect(url_for('auth.login'))
        flash(error)

    return render_template('auth/register.html')


@auth.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_user_db()
        error = None
        user = None
        user_password = ''
        user_id = None
        for usr in db['data']:
            if username == usr['name']:
                user_password = usr['password']
                user_id = usr['id']
                user = usr['name']
        if user is None:
            error = 'Incorrect username'
        elif not check_password_hash(user_password, password):
            error = 'Incorrect password'

        if error is None:
            session.clear()
            session['user_id'] = user_id
            return redirect(url_for('blog.home_page'))

        flash(error)

    return render_template('auth/login.html')


@auth.before_app_request
def user_logged_load():
    db = get_user_db()
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        for user in db['data']:
            if user['id'] == user_id:
                g.user = user
                session.permanent = True


@auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('blog.home_page'))
