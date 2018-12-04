import argparse

from redis import Redis

from no_sql.redis.redis_handler import RedisHandler

dbs = {"redis" : RedisHandler}

if __name__ == "__main__":

    r = Redis()
    name = r.get("name")
    print(name)
