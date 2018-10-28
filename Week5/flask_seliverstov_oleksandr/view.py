from app import app
from flask import render_template, request, abort, session, redirect, url_for
from data.db import movies, users


@app.route("/")
@app.route("/home")
def home():
    return  render_template("home.html")

@app.route("/movies", methods=['GET'])
def movies_all():
    if session.get('logged', 'false') == 'true':
        return render_template("Movies.html" , data=movies)
    else:
        return redirect(url_for('login'))


@app.route("/movies/<string:movie>", methods=['GET'])
def movies_show(movie):
    if len(list(filter(lambda x: x['title']==movie, movies)))==0:
        abort(404)
    return render_template("Show_above.html", data=filter(lambda x: x['title']==movie, movies))


@app.route("/movies/", methods=['POST'])
def movies_add():
    movies.append(request.json)
    print (request.json)
    return render_template("home.html" , data=movies)


@app.route("/movies/<string:movie>", methods=['DELETE'])
def movies_del(movie):
    for i, elem in enumerate(movies):
        if elem['title'] == movie:
            movies.pop(i)
        else:
            abort(404)
    return render_template("home.html", data=movies)


@app.route('/registration', methods=['GET','POST'])
def registration():
    if request.method == 'GET':
        return render_template('Registration.html')
    if request.method == 'POST':
        new_user={}
        new_user['name']=request.form['name']
        new_user['age'] = request.form['age']
        new_user['password'] = str(request.form['password'])
        new_user['email'] = request.form['email']
        users.append(new_user)
        print(users)
        return render_template("home.html")


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'GET':
        return render_template('Login.html')
    if request.method == 'POST':
        user_mail = request.form['email']
        user_password= request.form['password']
        for user in users:
            if user['email']== user_mail and user['password']==user_password:
                session['logged'] = 'true'
                session['username'] = user['name']
            else:
                pass

        return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('logged', None)
    return redirect(url_for('login'))



@app.errorhandler(404)
def error_404_handler(error):
    return render_template("error_404.html")