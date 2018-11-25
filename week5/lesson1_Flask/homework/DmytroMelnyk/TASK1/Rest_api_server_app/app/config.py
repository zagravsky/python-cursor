import os


class Config:
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = "powerful_key"


class TestConfig(Config):
    DEBUG = True
    TESTING = True


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = "5f31c532e88134d18c12517d3c70a80a"

def runtime_config():
    env = os.environ.get("FLASK_ENV")
    if env == "DEV":
        return DevConfig
    if env == "TEST":
        return TestConfig
    if env == "PROD":
        return ProductionConfig
    else:
        return Config
