from .app_database import ma
from .model import BikeTable


class UserSchema(ma.ModelSchema):
    class Meta:
        # Fields to expose
        fields = ('id', 'username', 'email', 'age', 'password_hash')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class BikeSchema(ma.ModelSchema):
    class Meta:
        # fields = ('id', 'name', 'brand', 'bike_type', 'wheel_size','')
        model = BikeTable

bike_schema = BikeSchema()
bikes_schema = BikeSchema(many=True)


class BrandSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'name')

brand_schema = BrandSchema()
braands_schema = BrandSchema(many=True)
