"""
Simple pizza factory

Author: m1ge7
Date: 2014/03/25
"""

from abc import ABCMeta, abstractmethod


class PizzaStore:

    def __init__(self, factory):
        self._factory = factory

    def order_pizza(self, pizza_type):
        pizza = self._factory.create_pizza(pizza_type)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class SimplePizzaFactory:

    def create_pizza(self, pizza_type):
        pizza = None

        if pizza_type == "cheese":
            pizza = CheesePizza()
        elif pizza_type == "pepperoni":
            pizza = PepperoniPizza()
        elif pizza_type == "clam":
            pizza = ClamPizza()
        elif pizza_type == "veggie":
            pizza = VeggiePizza()

        return pizza


###############################################################################
# Pizzas
###############################################################################

class Pizza:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    def get_name(self):
        return self._name

    def prepare(self):
        print("Preparing " + self._name)

    def bake(self):
        print("Baking " + self._name)

    def cut(self):
        print("Cutting " + self._name)

    def box(self):
        print("Boxing " + self._name)


class CheesePizza(Pizza):

    def __init__(self):
        self._name = "Cheese Pizza"
        self._dough = "Regular Crust"
        self._sauce = "Marinara Pizza Sauce"
        self._toppings = []
        self._toppings.append("Fresh Mozzarella")
        self._toppings.append("Parmesan")


class PepperoniPizza(Pizza):

    def __init__(self):
        self._name = "Pepperoni Pizza"
        self._dough = "Crust"
        self._sauce = "Marinara sauce"
        self._toppings = []
        self._toppings.append("Sliced Pepperoni")
        self._toppings.append("Sliced Onion")
        self._toppings.append("Grated parmesan cheese")


class ClamPizza(Pizza):

    def __init__(self):
        self._name = "Clam Pizza"
        self._dough = "Thin crust"
        self._sauce = "White garlic sauce"
        self._toppings = []
        self._toppings.append("Clams")
        self._toppings.append("Grated parmesan cheese")


class VeggiePizza(Pizza):

    def __init__(self):
        self._name = "Veggie Pizza"
        self._dough = "Crust"
        self._sauce = "Marinara sauce"
        self._toppings = []
        self._toppings.append("Shredded mozzarella")
        self._toppings.append("Grated parmesan")
        self._toppings.append("Diced onion")
        self._toppings.append("Sliced mushrooms")
        self._toppings.append("Sliced red pepper")
        self._toppings.append("Sliced black olives")


###############################################################################
# Simulation
###############################################################################

if __name__ == '__main__':
    factory = SimplePizzaFactory()
    store = PizzaStore(factory)

    pizza = store.order_pizza("cheese")
    print("We ordered a " + pizza.get_name() + "\n")

    pizza = store.order_pizza("veggie")
    print("We ordered a " + pizza.get_name() + "\n")
 
