from abc import ABCMeta, abstractmethod


class QuackBehavior:
    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self):
        pass


class Quack(QuackBehavior):
    def quack(self):
        print("Quack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("<< Silence >>")


class Squeak(QuackBehavior):
    def quack(self):
        print("Squeak")


class FakeQuack(QuackBehavior):
    def quack(self):
        print("Qwak")
