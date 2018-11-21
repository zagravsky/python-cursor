import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=5)
    TEST_VARIABLE = "Config"
    DEBUG = False
    TESTING = False
    PG_USER = "antonio"
    PG_PASSWORD = "1111"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "bikedb"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevConfig(Config):
    DEBUG = True
    TEST_VARIABLE = "Dev Config"



class TestConfig(Config):
    TEST_VARIABLE = "Test Config"
    TESTING = True


def runtime_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    if env == "TEST":
        return TestConfig
    else:
        return Config