"""
Duck simulator

Author: m1ge7
Date: 2014/03/22
"""

from abc import ABCMeta, abstractmethod


###############################################################################
# Ducks
###############################################################################

class Duck:
    __metaclass__ = ABCMeta
    fly_behavior = None
    quack_behavior = None

    @abstractmethod
    def display(self):
        pass

    def fly(self):
        self.fly_behavior.fly()

    def quack(self):
        self.quack_behavior.quack()

    def set_quack_behavior(self, quack_behavior):
        self.quack_behavior = quack_behavior

    def set_fly_behavior(self, fly_behavior):
        self.fly_behavior = fly_behavior

    def swim(self):
        print("All ducks float, even decoys!!");


class MallardDuck(Duck):

    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Mallard duck")


class DecoyDuck(Duck):

    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    def display(self):
        print("I'm a duck Decoy")


class RubberDuck(Duck):

    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squeak()

    def display(self):
        print("I'm a rubber duckie")


class RedHeadDuck(Duck):

    def __init__(self):
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a real Red Headed duck")


class ModelDuck(Duck):

    def __init__(self):
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Quack()

    def display(self):
        print("I'm a model duck")


###############################################################################
# Quack behaviors
###############################################################################

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


###############################################################################
# Fly behaviors
###############################################################################

class FlyBehavior():
    __metaclass__ = ABCMeta

    @abstractmethod
    def fly(self):
        pass


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("I'm flying!!")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("I can't fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("I'm flying with a rocket!")


if __name__ == '__main__':
    mallard = MallardDuck()
    mallard.quack()
    mallard.fly()

    model = ModelDuck()
    model.fly()
    model.set_fly_behavior(FlyRocketPowered())
    model.fly()

