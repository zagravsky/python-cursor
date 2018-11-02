from factory.flask_db import ma


class PlayerSchema(ma.Schema):
    class Meta:
        fields = ('id', 'full_name', 'age', 'club')


player_schema = PlayerSchema()
players_schema = PlayerSchema(many=True)
