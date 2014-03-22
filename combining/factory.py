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

    
###############################################################################
# Factories
###############################################################################

class AbstractDuckFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_mallard_duck(self):
        pass

    @abstractmethod
    def create_redhead_duck(self):
        pass

    @abstractmethod
    def create_duck_call(self):
        pass

    @abstractmethod
    def create_rubber_duck(self):
        pass


class DuckFactory(AbstractDuckFactory):

    def create_mallard_duck(self):
        return MallardDuck()

    def create_redhead_duck(self):
        return RedheadDuck()
    
    def create_duck_call(self):
        return DuckCall()

    def create_rubber_duck(self):
        return RubberDuck()


class CountingDuckFactory(AbstractDuckFactory):

    def create_mallard_duck(self):
        return QuackCounter(MallardDuck())

    def create_redhead_duck(self):
        return QuackCounter(RedheadDuck())

    def create_duck_call(self):
        return QuackCounter(DuckCall())

    def create_rubber_duck(self):
        return QuackCounter(RubberDuck())


class DuckSimulator:

    def simulate_factory(self, duck_factory):
        mallard_duck = duck_factory.create_mallard_duck()
        redhead_duck = duck_factory.create_redhead_duck()
        duck_call = duck_factory.create_duck_call()
        rubber_duck = duck_factory.create_rubber_duck()
        goose_duck = GooseAdapter(Goose())

        print "\nDuck Simulator: With Abstract Factory"

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
    duck_factory = CountingDuckFactory()
    simulator.simulate_factory(duck_factory)
