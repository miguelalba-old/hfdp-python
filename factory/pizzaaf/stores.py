from abc import ABCMeta, abstractmethod
import factories
import pizzas


class PizzaStore:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_pizza(self, item):
        pass

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        print("--- Making a " + pizza.get_name() + " ---")

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):

    def create_pizza(self, item):
        pizza = None
        ingredient_factory = factories.NYPizzaIngredientFactory()

        if item == "cheese":
            pizza = pizzas.CheesePizza(ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")

        elif item == "veggie":
            pizza = pizzas.VeggiePizza(ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")

        elif item == "clam":
            pizza = pizzas.ClamPizza(ingredient_factory)
            pizza.set_name("New York Style Clam Pizza")

        elif item == "pepperoni":
            pizza = pizzas.PepperoniPizza(ingredient_factory)
            pizza.set_name("New York Style Pepperoni Pizza")

        return pizza


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, item):
        pizza = None
        ingredient_factory = factories.ChicagoPizzaIngredientFactory()

        if item == "cheese":
            pizza = pizzas.CheesePizza(ingredient_factory)
            pizza.set_name("Chicago Style Cheese Pizza")

        elif item == "veggie":
            pizza = pizzas.VeggiePizza(ingredient_factory)
            pizza.set_name("Chicago Style Veggie Pizza")

        elif item == "clam":
            pizza = pizzas.ClamPizza(ingredient_factory)
            pizza.set_name("Chicago Style Clam Pizza")

        elif item == "pepperoni":
            pizza = pizzas.PepperoniPizza(ingredient_factory)
            pizza.set_name("Chicago Style Pepperoni Pizza")

        return pizza
