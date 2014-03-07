############################
# Pizza Ingredient Factories
############################

from abc import ABCMeta, abstractmethod
import ingredients


class PizzaIngredientFactory:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_veggies(self):
        pass

    @abstractmethod
    def create_pepperoni(self):
        pass

    @abstractmethod
    def create_clam(self):
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ingredients.ThinCrustDough()

    def create_sauce(self):
        return ingredients.MarinaraSauce()

    def create_cheese(self):
        return ingredients.ReggianoCheese()

    def create_veggies(self):
        return [ingredients.Garlic(), ingredients.Onion(),
                ingredients.Mushroom(), ingredients.RedPepper()]

    def create_pepperoni(self):
        return ingredients.SlicedPepperoni()

    def create_clam(self):
        return ingredients.FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ingredients.ThickCrustDough()

    def create_sauce(self):
        return ingredients.PlumTomatoSauce()

    def create_cheese(self):
        return ingredients.MozzarellaCheese()

    def create_veggies(self):
        return [ingredients.BlackOlives(), ingredients.Spinach(),
                ingredients.Eggplant()]

    def create_pepperoni(self):
        return ingredients.SlicedPepperoni()

    def create_clam(self):
        return ingredients.FrozenClams()
