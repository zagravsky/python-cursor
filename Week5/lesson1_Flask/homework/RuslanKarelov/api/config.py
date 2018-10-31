import os


class BaseConfig:
    MODE = 'BaseConfig'
    DEBUG = False
    TESTING = False


class DevConfig(BaseConfig):
    MODE = 'DevConfig'
    DEBUG = True
    TESTING = False


class TestConfig(BaseConfig):
    MODE = 'TestConfig'
    DEBUG = False
    TESTING = True


def my_config():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig()
    elif env == "TEST":
        return TestConfig()
    else:
        return BaseConfig()
