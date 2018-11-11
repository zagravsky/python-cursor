from database.data import ma


class MySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'model', 'car_body', 'fuel', 'price', 'date')


car_schema = MySchema()
cars_schema = MySchema(many=True)
