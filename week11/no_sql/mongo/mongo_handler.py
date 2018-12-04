import pymongo

if __name__ == "__main__":

    db_name = "lection"
    col_name = "redis"

    client = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = client[db_name]

    collection = mydb[col_name]

    our_first_row = {"key": "name",
                     "value": "Denis"}

    our_rows = [
        {"key": "name", "value": 1235},
        {"key": "Some Lisy", "value": [1, 2, 4, 5, 6, 8]},
        {"new_one": "Ups"}
    ]

    collection.insert_many(our_rows)


    # print(f"Lets see what we have {result}")

