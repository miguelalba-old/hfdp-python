"""
Classical implentation of singleton (non thread-safe)

Author: m1ge7
Date: 2014/03/27
"""


class Singleton(object):
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = object.__new__(cls)
        return cls.instance


if __name__ == '__main__':
    singleton1 = Singleton()
    singleton2 = Singleton()
    assert singleton1 == singleton2
