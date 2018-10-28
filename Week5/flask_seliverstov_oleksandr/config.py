import os


class Config:
    TEST_VARIABLE = "Config"
    DEBUG = True
    KEY = "password"

class DevConfig(Config):
    TEST_VARIABLE = "Dev Config"
    KEY = "j2n@02DNP@82hep[@)(u;290jd"


class TestConfig(Config):
    TEST_VARIABLE = "Test Config"
    KEY = "JFH@00002jojk"


def configuration():
    env = os.environ.get("ENV")
    if env == "DEV":
        return DevConfig
    if env == "TEST":
        return TestConfig
    else:
        return Config