from abc import ABCMeta, abstractmethod
import flybehaviors
import quackbehaviors


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
        self.fly_behavior = flybehaviors.FlyWithWings()
        self.quack_behavior = quackbehaviors.Quack()

    def display(self):
        print("I'm a real Mallard duck")


class DecoyDuck(Duck):

    def __init__(self):
        self.fly_behavior = flybehaviors.FlyNoWay()
        self.quack_behavior = quackbehaviors.MuteQuack()

    def display(self):
        print("I'm a duck Decoy")


class RubberDuck(Duck):

    def __init__(self):
        self.fly_behavior = flybehaviors.FlyNoWay()
        self.quack_behavior = quackbehaviors.Squeak()

    def display(self):
        print("I'm a rubber duckie")


class RedHeadDuck(Duck):

    def __init__(self):
        self.fly_behavior = flybehaviors.FlyWithWings()
        self.quack_behavior = quackbehaviors.Quack()

    def display(self):
        print("I'm a real Red Headed duck")


class ModelDuck(Duck):

    def __init__(self):
        self.fly_behavior = flybehaviors.FlyNoWay()
        self.quack_behavior = quackbehaviors.Quack()

    def display(self):
        print("I'm a model duck")
