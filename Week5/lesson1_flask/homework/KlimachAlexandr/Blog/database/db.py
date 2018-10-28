import json


def get_db():
    with open('Blog/database/db.json', 'r') as db:
        data = json.load(db)
    return data


def write_db(data: dict):
    with open('Blog/database/db.json', 'w') as db:
        json.dump(data, db)


def get_user_db():
    with open('Blog/database/db_user.json', 'r') as db:
        data = json.load(db)
    return data


def write_user_db(data: dict):
    with open('Blog/database/db_user.json', 'w') as db:
        json.dump(data, db)
