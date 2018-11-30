from __future__ import annotations


class Config:
    __instance: Config = None

    def __new__(cls, *args, **kwargs):
        print("Method __new__ is calling")
        if Config.__instance is None:
            print("We have no inst yet")
            cls.__instance = super().__new__(cls)
        else:
            print("Return old one")
        return cls.__instance

    def __init__(self):
        print("Method init is calling")

class OrdinaryConfig:
    pass


if __name__ == "__main__":
    first_conf = Config()
    second_conf = Config()
    # ord_conf_first = OrdinaryConfig()
    # ord_conf_second = OrdinaryConfig()
    # print(first_conf is second_conf)
    # print(id(first_conf) == id(second_conf))
    # print(id(first_conf))
    # print(id(second_conf))

    # nd_conf)
    # print(id(ord_conf_first) == id(ord_conf_second))
    # print(id(ord_conf_first))
    # print(id(ord_conf_second))