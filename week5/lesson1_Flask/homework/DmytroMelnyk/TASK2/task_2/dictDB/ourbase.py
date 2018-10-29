import json


def get_db():
    with open('task_2/dictDB/ourbase.json', 'r') as db:
        data = json.load(db)
    return data


def rewrite_db(data: list):
    with open('task_2/dictDB/ourbase.json', 'w') as db:
        json.dump(data, db)


def get_users_db():
    with open('task_2/dictDB/users.json', 'r') as db:
        data = json.load(db)
        return data


def rewrite_users_db(data: list):
    with open('task_2/dictDB/users.json', 'w') as db:
        json.dump(data, db)