import argparse

from no_sql.redis.redis_handler import RedisHandler

dbs = {"redis": RedisHandler}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Our first script')
    # parser.add_argument('-st', '--storage', help='Name of storage', required=True)
    parser.add_argument('-ht', '--host', dest="host")
    parser.add_argument('-pt', '--port', dest="port")
    parser.add_argument('-db', '--db', dest="db")

    args = parser.parse_args()

    r = RedisHandler(host=args.host, port=args.port, db=args.db)

    print(r.conn.get("name"))
