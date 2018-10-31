from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self,user):
        self.username = user['username']
        self.password_hash = user['password_hash']
        self.email = user['email']
        self.age = user['age']

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
