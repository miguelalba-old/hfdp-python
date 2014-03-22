"""
Ducks base problem.

Author: m1ge7
Date: 2014/03/22
"""

from abc import ABCMeta, abstractmethod


class Quackable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self):
        pass


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


class DuckSimulator:

    def simulate_factory(self):
        mallard_duck = MallardDuck()
        redhead_duck = RedheadDuck()
        duck_call = DuckCall()
        rubber_duck = RubberDuck()

        print "\nDuck Simulator"

        self.simulate_duck(mallard_duck)
        self.simulate_duck(redhead_duck)
        self.simulate_duck(duck_call)
        self.simulate_duck(rubber_duck)

    def simulate_duck(self, duck):
        duck.quack()


if __name__ == '__main__':
    simulator = DuckSimulator()
    simulator.simulate_factory()
