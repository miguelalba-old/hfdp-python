"""
Ducks problem with quackologists (observers)

Author: m1ge7
Date: 2014/03/24
"""

from abc import ABCMeta, abstractmethod


###############################################################################
# 
###############################################################################

class QuackObservable:
    __metaclass__ = ABCMeta

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Quackable(QuackObservable):
    __metaclass__ = ABCMeta

    @abstractmethod
    def quack(self):
        pass


class Observable(QuackObservable):

    def __init__(self, duck):
        self.__observers = []
        self.__duck = duck

    def register_observer(self, observer):
        self.__observers.append(observer)

    def notify_observers(self):
        for obs in self.__observers:
            obs.update(self.__duck)

    def get_observers(self):
        return self.__observers


class Observer:
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, duck):
        pass


class Quackologist(Observer):

    def update(self, duck):
        print "Quackologist: " + str(duck) + " just quacked."

    def __str__(self):
        return "Quackologist"




###############################################################################
# Duck concrete classes
###############################################################################

class DecoyDuck(Quackable):

    def __init__(self):
        self.__observable = Observable(self)

    def quack(self):
        print "<< Silence >>"
        self.notify_observers()
    
    def register_observer(self, observer):
        self.__observable.register_observer(observer)

    def notify_observers(self):
        self.__observable.notify_observers()

    def __str__(self):
        return "Decoy Duck"


class DuckCall(Quackable):

    def __init__(self):
        self.__observable = Observable(self)

    def quack(self):
        print "Kwak"
        self.notify_observers()

    def register_observer(self, observer):
        self.__observable.register_observer(observer)

    def notify_observers(self):
        self.__observable.notify_observers()

    def __str__(self):
        return "Duck Call"


class MallardDuck(Quackable):

    def __init__(self):
        self.__observable = Observable(self)

    def quack(self):
        print "Quack"
        self.notify_observers()

    def register_observer(self, observer):
        self.__observable.register_observer(observer)

    def notify_observers(self):
        self.__observable.notify_observers()

    def __str__(self):
        return "Mallard Duck"


class RedheadDuck(Quackable):

    def __init__(self):
        self.__observable = Observable(self)

    def quack(self):
        print "Quack"
        self.notify_observers()

    def register_observer(self, observer):
        self.__observable.register_observer(observer)

    def notify_observers(self):
        self.__observable.notify_observers()

    def __str__(self):
        return "Redhead Duck"


class RubberDuck(Quackable):

    def __init__(self):
        self.__observable = Observable(self)

    def quack(self):
        print "Squeak"
        self.notify_observers()

    def register_observer(self, observer):
        self.__observable.register_observer(observer)

    def notify_observers(self):
        self.__observable.notify_observers()

    def __str__(self):
        return "Rubber Duck"


###############################################################################
# Goose classes
###############################################################################

class Goose:

    def honk(self):
        print "Honk"

    def __str__(self):
        return "Goose"


class GooseAdapter(Quackable):

    def __init__(self, goose):
        self.__goose = goose
        self.__observable = Observable(self)

    def quack(self):
        self.__goose.honk()
        self.notify_observers()

    def register_observer(self, observer):
        self.__observable.register_observer(observer)

    def notify_observers(self):
        self.__observable.notify_observers()

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

    def register_observer(self, observer):
        self.__duck.register_observer(observer)

    def notify_observers(self):
        self.__duck.notify_observers()
    
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
        self.__ducks = []

    def add(self, duck):
        self.__ducks.append(duck)

    def quack(self):
        for duck in self.__ducks:
            duck.quack()

    def register_observer(self, observer):
        for duck in self.__ducks:
            duck.register_observer(observer)

    def notify_observers():
        pass

    def __str__(self):
        return "Flock of Ducks"


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

        print "\nDuck Simulator: With Observer"

        quackologist = Quackologist()
        flock_of_ducks.register_observer(quackologist)

        self.simulate_duck(flock_of_ducks)

        print "The ducks quacked " + str(QuackCounter.get_quacks()) + " times"

    def simulate_duck(self, duck):
        duck.quack()


if __name__ == '__main__':
    simulator = DuckSimulator()
    duck_factory = CountingDuckFactory()
    simulator.simulate_factory(duck_factory)
