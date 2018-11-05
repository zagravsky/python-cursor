from db_config import ma

class BookSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('title','id')

book_schema = BookSchema()
books_schema = BookSchema(many=True)