from abc import ABCMeta, abstractmethod
from __builtin__ import super


class Pizza:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        self._name = None
        self._dough = None
        self._sauce = None
        self._toppings = []


    def prepare(self):
        print("Preparing " + self._name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        print("   ".join(self._toppings))

    def bake(self):
        print("Bake for 25 minutes at 350")
    
    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def get_name(self):
        return self._name


class PizzaStore:
    __metaclass__ = ABCMeta

    @abstractmethod
    def create_pizza(self, item):
        pass

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        print("--- Making a " + pizza.get_name() + " ---");

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):

    def create_pizza(self, item):
        if item == "cheese":
            return NYStyleCheesePizza()
        elif item == "veggie":
            return NYStyleVeggiePizza()
        elif item == "clam":
            return NYStyleClamPizza()
        elif item == "pepperoni":
            return NYStylePepperoniPizza()
        else:
            return None


class NYStyleCheesePizza(Pizza):
    
    def __init__(self):
        super(NYStyleCheesePizza, self).__init__()
        self._name = "NY Style Sauce and Cheese Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")


class NYStyleVeggiePizza(Pizza):

    def __init__(self):
        super(NYStyleVeggiePizza, self).__init__()
        self._name = "NY Style Veggie Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"

        self._toppings.append("Grated Reggiano Cheese")
        self._toppings.append("Garlic")
        self._toppings.append("Onion")
        self._toppings.append("Mushrooms")
        self._toppings.append("Red Pepper")


class NYStyleClamPizza(Pizza):

    def __init__(self):
        super(NYStyleClamPizza, self).__init__()
        self._name = "NY Style Clam Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")
        self._toppings.append("Fresh Clams from Long Island Sound")


class NYStylePepperoniPizza(Pizza):

    def __init__(self):
        super(NYStylePepperoniPizza, self).__init__()
        self._name = "NY Style Pepperoni Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")
        self._toppings.append("Sliced Pepperoni")
        self._toppings.append("Garlic")
        self._toppings.append("Onion")
        self._toppings.append("Mushrooms")
        self._toppings.append("Red Pepper")


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, item):
        if item == "cheese":
            return ChicagoStyleCheesePizza()
        elif item == "veggie":
            return ChicagoStyleVeggiePizza()
        elif item == "clam":
            return ChicagoStyleClamPizza()
        elif item == "pepperoni":
            return ChicagoStylePepperoniPizza()
        else:
            return None


class ChicagoStyleCheesePizza(Pizza):

    def __init__(self):
        super(ChicagoStyleCheesePizza, self).__init__()
        self._name = "Chicago Style Deep Dish Cheese Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"
        self._toppings.append("Shredded Mozzarella Cheese")


    def cut(self):
        print("Cutting the pizza into square slices")


class ChicagoStyleVeggiePizza(Pizza):
    
    def __init__(self):
        super(ChicagoStyleVeggiePizza, self).__init__()
        self._name = "Chicago Deep Dish Veggie Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"
        
        self._toppings.append("Shredded Mozzarella Cheese");
        self._toppings.append("Black Olives");
        self._toppings.append("Spinach");
        self._toppings.append("Eggplant");

    def cut(self):
        print("Cutting the pizza into square slices")


class ChicagoStyleClamPizza(Pizza):
    
    def __init__(self):
        super(ChicagoStyleClamPizza, self).__init__()
        self._name = "Chicago Style Clam Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"
        
        self._toppings.append("Shredded Mozzarella Cheese")
        self._toppings.append("Frozen Clams from Chesapeake Bay")
        

    def cut(self):
        print("Cutting the pizza into square slices")


class ChicagoStylePepperoniPizza(Pizza):
    
    def __init__(self):
        super(ChicagoStylePepperoniPizza, self).__init__()
        self._name = "Chicago Style Pepperoni Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"

        self._toppings.append("Shredded Mozzarella Cheese");
        self._toppings.append("Black Olives");
        self._toppings.append("Spinach");
        self._toppings.append("Eggplant");
        self._toppings.append("Sliced Pepperoni");
 
    def cut(self):
        print("Cutting the pizza into square slices")
    

if __name__ == '__main__':
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.order_pizza("cheese")
    print("Ethan ordered a " + pizza.get_name() + "\n")

    pizza = chicagoStore.order_pizza("cheese")
    print("Joel ordered a " + pizza.get_name() + "\n")

    pizza = nyStore.order_pizza("clam")
    print("Ethan ordered a " + pizza.get_name() + "\n")

    pizza = chicagoStore.order_pizza("clam")
    print("Joel ordered a " + pizza.get_name() + "\n")

    pizza = nyStore.order_pizza("pepperoni")
    print("Joel ordered a " + pizza.get_name() + "\n")

    pizza = chicagoStore.order_pizza("pepperoni")
    print("Ethan ordered a " + pizza.get_name() + "\n")

    pizza = nyStore.order_pizza("veggie")
    print("Joel ordered a " + pizza.get_name() + "\n")

