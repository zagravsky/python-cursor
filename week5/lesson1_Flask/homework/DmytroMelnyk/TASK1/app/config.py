# import os
#
#
# class Configuration():
#     TEST_VARIABLE = "Config"
#     DEBUG = None
#     HOST = "127.0.0.1"
#     PORT = 8080
#
#
# class DevConfiguration(Configuration):
#     TEST_VARIABLE = "Dev Config"
#     DEBUG = True
#     HOST = "127.0.0.1"
#     PORT = 5001
#
# class TestConfiguration(Configuration):
#     TEST_VARIABLE = "Test Config"
#     DEBUG = True
#     HOST = "127.0.0.1"
#     PORT = 5000
#
#
# def runtime_config():
#     env = os.environ.get("ENV")
#     if env == "DEV":
#         return DevConfiguration
#     if env == "TEST":
#         return TestConfiguration
#     else:
#         return Configuration
class Configuration():
    DEBUG = True