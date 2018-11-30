from __future__ import annotations


class Config:
    __instance: Config = None

    def __new__(cls, *args, **kwargs):
        if Config.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance


if __name__ == "__main__":
    first_conf = Config()
    second_conf = Config()
    print(first_conf is second_conf)
    print(id(first_conf))
    print(id(second_conf))