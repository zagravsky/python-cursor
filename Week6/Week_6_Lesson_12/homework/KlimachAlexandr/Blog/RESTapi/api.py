from flask import Blueprint, jsonify, request
from Blog.database.db import MovieTable, movie_schema, movies_schema, db

API = Blueprint('api', __name__)


@API.route('/api', methods=['GET'])
def get_all_data():
    movies = MovieTable.query.all()
    if not movies:
        return jsonify({"status": "ERROR", "result": "DB is empty"})
    return jsonify(movies_schema.dump(movies).data)


@API.route('/api/<int:id>', methods=['GET'])
def get_movie(id):
    movie = MovieTable.query.filter_by(id=id).first()
    if not movie:
        return jsonify({"status": "ERROR", "result": "Not found id %s" % id})
    return jsonify(movie_schema.dump(movie).data)


@API.route('/api', methods=['POST'])
def post_new_movie():
    data = request.get_json()
    if data.get('movie_title') is not None:
        movie = MovieTable.query.filter_by(movie_title=data['movie_title']).first()
        if movie:
            return jsonify({"status": "ERROR", "result": "Movie is already in the DB"})
        try:
            new_movie = MovieTable(**data)
            db.session.add(new_movie)
            db.session.commit()
            return jsonify(movie_schema.dump(new_movie).data)
        except TypeError:
            return jsonify({"status": "ERROR", "result": "Not correct params"})
    else:
        return jsonify({"status": "ERROR", "result": "Not correct params"})


@API.route('/api/<int:id>', methods=['PUT'])
def update_movie(id):
    data = request.get_json()
    movie = MovieTable.query.filter_by(id=id).first()
    if movie:
        movie.movie_title = data.get('movie_title', movie.movie_title)
        movie.year = data.get('year', movie.year)
        movie.country = data.get('country', movie.country)

        db.session.commit()
        return jsonify(movie_schema.dump(movie).data)
    else:
        return jsonify({"status": "ERROR", "result": "Not found id %s" % id})


@API.route('/api/<string:movie_title>', methods=['DELETE'])
def delete_movie(movie_title):
    movie = MovieTable.query.filter_by(movie_title=movie_title).first()
    if movie:
        db.session.delete(movie)
        db.session.commit()
        return jsonify({"status": "OK", "result": "Movie %s successful deleted" % movie_title})
    else:
        return jsonify({"status": "ERROR", "result": "Movie %s not found" % movie_title})