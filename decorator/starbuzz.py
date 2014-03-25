from abc import ABCMeta, abstractmethod


class Beverage:
    __metaclass__ = ABCMeta

    def __init__(self):
        self._description = "Unknown Beverage"

    def get_description(self):
        return self._description

    @abstractmethod
    def cost(self):
        pass


class CondimentDecorator(Beverage):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_description(self):
        pass


class Espresso(Beverage):

    def __init__(self):
        self._description = "Espresso"

    def cost(self):
        return 1.99


class HouseBlend(Beverage):

    def __init__(self):
        self._description = "House Blend Coffee"

    def cost(self):
        return .89


class DarkRoast(Beverage):

    def __init__(self):
        self._description = "Dark Roast Coffee"

    def cost(self):
        return .99


class Decaf(Beverage):

    def __init__(self):
        self._description = "Decaf Coffee"

    def cost(self):
        return 1.05


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Mocha"

    def cost(self):
        return .20 + self._beverage.cost()


class Milk(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Milk"

    def cost(self):
        return .10 + self._beverage.cost()


class Soy(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Soy"

    def cost(self):
        return .15 + self._beverage.cost()


class Whip(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Whip"

    def cost(self):
        return .10 + self._beverage.cost()


if __name__ == '__main__':
    beverage = Espresso()
    print(beverage.get_description() + " $" + str(beverage.cost()))

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description() + " $" + str(beverage2.cost()))

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.get_description() + " $" + str(beverage3.cost()))
