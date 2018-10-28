from flask import Blueprint, jsonify, request, json
from Blog.database.db import get_db, write_db

API = Blueprint('api', __name__)


@API.route('/api', methods=['GET'])
def get_all_data():
    data = get_db()
    return jsonify(data)


@API.route('/api/<int:id>', methods=['GET'])
def get_movie(id):
    data = get_db()
    for movie, info in data['data'].items():
        if info.get('id') == id:
            return jsonify({movie: info})
    else:
        return json.dumps({"status": "error", "result": "ID %s not found" % id})


@API.route('/api', methods=['POST'])
def post_new_movie():
    data = get_db()
    r_data: dict = json.loads(request.data.decode('utf-8'))
    movie_title = r_data.get('movie_title')
    if movie_title is None:
        return json.dumps({"status": "error", "result": "Not correct request"})
    elif data["data"].get(movie_title) is not None:
        return json.dumps({"status": "error", "result": "The movie is already in DB"})
    else:
        new_movie = {r_data.get('movie_title'): {"genre": r_data.get("genre", []),
                                                 "year": r_data.get("year"),
                                                 "country": r_data.get("country"),
                                                 "id": data["id_counter"]}}
    data["id_counter"] += 1
    data["data"].update(new_movie)
    write_db(data)
    return json.dumps({"status": "OK", "result": "You added new movie"})


@API.route('/api/<string:movie>', methods=['DELETE'])
# Removes a movie from the database by title.
def delete_movie(movie):
    data = get_db()
    if data['data'].get(movie) is not None:
        data['data'].pop(movie)
        write_db(data)
        return json.dumps({"status": "OK", "result": "Movie %s deleted" % movie})

    else:
        return json.dumps({"status": "error", "result": "Movie %s not found" % movie})
