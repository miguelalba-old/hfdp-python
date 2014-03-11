from abc import ABCMeta, abstractmethod
import random


class Duck:
    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self):
        pass

    def fly(self):
        pass


class MallardDuck(Duck):
    def quack(self):
        print "Quack"

    def fly(self):
        print "I'm flying"


class Turkey:
    __metaclass__ = ABCMeta

    @abstractmethod
    def gobble(self):
        pass

    @abstractmethod
    def fly(self):
        pass


class WildTurkey(Turkey):
    __metaclass__ = ABCMeta

    def gobble(self):
        print "Gobble gobble"

    def fly(self):
        print "I'm flying a short distance"


class TurkeyAdapter(Duck):

    def __init__(self, turkey):
        self._turkey = turkey

    def quack(self):
        self._turkey.gobble()

    def fly(self):
        for i in range(5):
            self._turkey.fly()


class DuckAdapter(Turkey):

    def __init__(self, duck):
        self._duck = duck

    def gobble(self):
        self._duck.quack()

    def fly(self):
        if random.randint(0, 5) == 0:
            self._duck.fly()


def turkey_test_drive():
    # Turkey Test Drive
    duck = MallardDuck()
    duckAdapter = DuckAdapter(duck)

    for i in range(10):
        print "The DuckAdapter says..."
        duckAdapter.gobble()
        duckAdapter.fly()


def duck_test_drive():
    def test_duck(duck):
        duck.quack()
        duck.fly()

    # Duck Test Drive
    duck = MallardDuck()
    turkey = WildTurkey()
    turkeyAdapter = TurkeyAdapter(turkey)

    print "The Turkey says..."
    turkey.gobble()
    turkey.fly()

    print "\nThe Duck says..."
    test_duck(duck)

    print "\nThe TurkeyAdapter says..."
    test_duck(turkeyAdapter)


if __name__ == '__main__':
    turkey_test_drive()
    duck_test_drive()
