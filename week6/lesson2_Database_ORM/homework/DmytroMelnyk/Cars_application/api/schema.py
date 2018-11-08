from week6.lesson2_Database_ORM.homework.DmytroMelnyk.Cars_application.db.app_database import ma


class CarSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('id', 'model', 'mark', 'horsepower', 'year', 'origin')


car_schema = CarSchema()
cars_schema = CarSchema(many=True)


# class NameSchema(ma.Schema):
#     class Meta:
#         # Fields to expose
#         fields = ('id', 'name')
#
#
# name_schema = NameSchema()
# names_schema = NameSchema(many=True)
#
#
# class PersonSchema(ma.Schema):
#     class Meta:
#         # Fields to expose
#         fields = ('id', 'name', 'name_id')
#
#
# person_schema = PersonSchema()
# persons_schema = PersonSchema(many=True)
