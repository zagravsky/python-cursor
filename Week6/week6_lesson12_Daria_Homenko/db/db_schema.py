from db.db_app import ma


class NewsSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'create_date', 'author')


news_schema = NewsSchema()
newses_schema = NewsSchema(many=True)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'age', 'email', 'password' )


user_schema = UserSchema()
users_schema = UserSchema(many=True)


class FlowerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'flower_name', 'flower_description', 'flower_image')


flower_schema = FlowerSchema()
flowers_schema = FlowerSchema(many=True)
