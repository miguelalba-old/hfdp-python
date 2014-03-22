"""
Ducks problem with support for gooses (adapter).

Author: m1ge7
Date: 2014/03/22
"""

from abc import ABCMeta, abstractmethod


class Quackable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self):
        pass


###############################################################################
# Duck concrete classes
###############################################################################

class DecoyDuck(Quackable):
    def quack(self):
        print "<< Silence >>"


class DuckCall(Quackable):
    def quack(self):
        print "Kwak"


class MallardDuck(Quackable):
    def quack(self):
        print "Quack"


class RedheadDuck(Quackable):
    def quack(self):
        print "Quack"


class RubberDuck(Quackable):
    def quack(self):
        print "Squeak"


###############################################################################
# Goose classes
###############################################################################

class Goose:
    def honk(self):
        print "Honk"


class GooseAdapter(Quackable):

    def __init__(self, goose):
        self.__goose = goose

    def quack(self):
        self.__goose.honk()

    def __str__(self):
        return "Goose pretending to be a Duck"


class DuckSimulator:

    def simulate_factory(self):
        mallard_duck = MallardDuck()
        redhead_duck = RedheadDuck()
        duck_call = DuckCall()
        rubber_duck = RubberDuck()
        goose_duck = GooseAdapter(Goose())

        print "\nDuck Simulator: With Goose Adapter"

        self.simulate_duck(mallard_duck)
        self.simulate_duck(redhead_duck)
        self.simulate_duck(duck_call)
        self.simulate_duck(rubber_duck)
        self.simulate_duck(goose_duck)

    def simulate_duck(self, duck):
        duck.quack()


if __name__ == '__main__':
    simulator = DuckSimulator()
    simulator.simulate_factory()
