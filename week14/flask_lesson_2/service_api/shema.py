from service_api.app_database import ma


class AuthorSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)


class BookSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'author_id')


book_schema = BookSchema()
books_schema = BookSchema(many=True)


class CharacterSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


character_schema = CharacterSchema()
characters_schema = CharacterSchema(many=True)


class GenreSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


class IdCardSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user_id')


id_card_schema = IdCardSchema()
id_cards_schema = IdCardSchema(many=True)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name')


user_schema = UserSchema()
users_schema = UserSchema(many=True)