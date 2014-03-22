"""
Ducks problem with quack counts

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


###############################################################################
# QuackCounter
###############################################################################
class QuackCounter(Quackable):

    number_of_quacks = 0

    def __init__(self, duck):
        self.__duck = duck

    def quack(self):
        self.__duck.quack()
        QuackCounter.number_of_quacks += 1

    @staticmethod
    def get_quacks():
        return QuackCounter.number_of_quacks
    
    def __str__(self):
        return str(self.__duck)

    

class DuckSimulator:

    def simulate_factory(self):
        mallard_duck = QuackCounter(MallardDuck())
        redhead_duck = QuackCounter(RedheadDuck())
        duck_call = QuackCounter(DuckCall())
        rubber_duck = QuackCounter(RubberDuck())
        goose_duck = QuackCounter(GooseAdapter(Goose()))

        print "\nDuck Simulator: With Goose Decorator"

        self.simulate_duck(mallard_duck)
        self.simulate_duck(redhead_duck)
        self.simulate_duck(duck_call)
        self.simulate_duck(rubber_duck)
        self.simulate_duck(goose_duck)

        print "The ducks quacked " + str(QuackCounter.get_quacks()) + " times"

    def simulate_duck(self, duck):
        duck.quack()


if __name__ == '__main__':
    simulator = DuckSimulator()
    simulator.simulate_factory()
