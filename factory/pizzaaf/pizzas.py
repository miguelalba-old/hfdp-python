from abc import ABCMeta, abstractmethod


class Pizza:
    __metaclass__ = ABCMeta

    def __init__(self):
        self._name = None
        self._dough = None
        self._sauce = None
        self._veggies = []
        self._cheese = None
        self._pepperoni = None
        self._clam = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print "Bake for 25 minutes at 350"

    def cut(self):
        print "Cutting the pizza into diagonal slices"

    def box(self):
        print "Place pizza in official PizzaStore box"

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def __str__(self):
        result = "---- " + self._name + " ----\n"

        if self._dough is not None:
            result += str(self._dough) + "\n"

        elif self._sauce is not None:
            result += str(self._sauce) + "\n"

        elif self._cheese is not None:
            result += str(self._cheese) + "\n"

        elif self._veggies is not None:
            result += ", ".join(self._veggies) + "\n"

        elif self._clam is not None:
            result += str(self._clam) + "\n"

        elif self._pepperoni is not None:
            result += str(self._pepperoni) + "\n"

        return result



class CheesePizza(Pizza):

    def __init__(self, ingredient_factory):
        super(CheesePizza, self).__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print "Preparing " + self._name
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()


class ClamPizza(Pizza):

    def __init__(self, ingredient_factory):
        super(ClamPizza, self).__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print "Preparing " + self._name

        self._cheese = self._ingredient_factory.create_cheese()
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._clam = self._ingredient_factory.create_clam()


class PepperoniPizza(Pizza):

    def __init__(self, ingredient_factory):
        super(PepperoniPizza, self).__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print "Preparing " + self._name

        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._veggies = self._ingredient_factory.create_veggies()
        self._pepperoni = self._ingredient_factory.create_pepperoni()


class VeggiePizza(Pizza):

    def __init__(self, ingredient_factory):
        super(VeggiePizza, self).__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print "Preparing " + self._name

        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._veggies = self._ingredient_factory.create_veggies()
