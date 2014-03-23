"""
Ducks problem with flocks of ducks

Author: m1ge7
Date: 2014/03/23
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


###############################################################################
# Flock
###############################################################################

class Flock(Quackable):

    def __init__(self):
        self.__quackers = []

    def add(self, quacker):
        self.__quackers.append(quacker)

    def quack(self):
        for quacker in self.__quackers:
            quacker.quack()

    def __str__(self):
        return "Flock of Quackers"


class DuckSimulator:

    def simulate_factory(self, duck_factory):
        print "\nDuck Simulator: With Composite - Flocks"

        flock_of_ducks = Flock()

        flock_of_ducks.add(duck_factory.create_redhead_duck())
        flock_of_ducks.add(duck_factory.create_duck_call())
        flock_of_ducks.add(duck_factory.create_rubber_duck())
        flock_of_ducks.add(GooseAdapter(Goose()))

        flock_of_mallards = Flock()

        for i in range(4):
            flock_of_mallards.add(duck_factory.create_mallard_duck())

        flock_of_ducks.add(flock_of_mallards)

        print "\nDuck Simulator: Whole Flock Simulation"
        self.simulate_duck(flock_of_ducks)

        print "\nDuck Simulator: Mallard Flock Simulation"
        self.simulate_duck(flock_of_mallards)

        print "The ducks quacked " + str(QuackCounter.get_quacks()) + " times"

    def simulate_duck(self, duck):
        duck.quack()


if __name__ == '__main__':
    simulator = DuckSimulator()
    duck_factory = CountingDuckFactory()
    simulator.simulate_factory(duck_factory)
