from .app_database import ma


class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'username', 'email', 'age', 'password_hash')

user_schema = UserSchema()
users_schema = UserSchema(many=True)
