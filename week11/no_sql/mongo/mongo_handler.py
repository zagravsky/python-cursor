import pymongo

if __name__ == "__main__":

    db_name = "lection"
    col_name = "redis"

    client = pymongo.MongoClient("mongodb://localhost:27017/")

    mydb = client[db_name]

    collection = mydb[col_name]

    our_first_row = {"key": "name",
                     "value": "Denis"}

    collection.insert(our_first_row)

    result = collection.find_one()

    print(f"Lets see what we have {result}")

