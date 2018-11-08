import os


class Config:
    MODE = 'Config'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/site.db'
    SECRET_KEY = "5f31c532e88134d18c12517d3c70a80a"


class DevConfig(Config):
    MODE = 'DevConfig'
    DEBUG = True


class TestConfig(Config):
    MODE = 'TestConfig'
    DEBUG = False


def run_config():
    env = os.environ.get('ENV')
    if env == 'DEV':
        return DevConfig
    if env == 'TEST':
        return TestConfig
    else:
        return Config
