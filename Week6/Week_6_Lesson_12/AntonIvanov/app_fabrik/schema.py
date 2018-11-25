from .app_database import ma


class UserSchema(ma.ModelSchema):
    class Meta:
        # Fields to expose
        fields = ('id', 'username', 'email', 'age', 'password_hash')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class BikeSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'name', 'brand', 'type', 'wheel_size')

bike_schema = BikeSchema()
bikes_schema = BikeSchema(many=True)