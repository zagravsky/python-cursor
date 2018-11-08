import os


class Config:
    TEST_VARIABLE = "Config"
    SECRET_KEY = 'b\xaa;\x0b\x12\x8a\xa1V+\x16\xc5'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/lesson_db.db'

class DevConfig(Config):
    TEST_VARIABLE = "Dev Config"
    SECRET_KEY = os.urandom(16)


class TestConfig(Config):
    TEST_VARIABLE = "Test Config"
    SECRET_KEY = 'b\xaa;\x0b\x12'


def runtime_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    if env == "TEST":
        return TestConfig
    else:
        return Config
