from abc import ABCMeta, abstractmethod


###############################################################################
# Cheese
###############################################################################
class Cheese:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self):
        pass


class MozzarellaCheese(Cheese):
    def __str__(self):
        return "Shredded Mozzarella"


class ParmesanCheese(Cheese):
    def __str__(self):
        return "Shredded Parmesan"


class ReggianoCheese(Cheese):
    def __str__(self):
        return "Reggiano Cheese"


###############################################################################
# Clams
###############################################################################
class Clams:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self):
        pass


class FreshClams(Clams):
    def __str__(self):
        return "Fresh Clams from Long Island Sound"


class FrozenClams(Clams):
    def __str__(self):
        return "Frozen Clams from Chesapeake Bay"


###############################################################################
# Dough
###############################################################################
class Dough:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self):
        pass


class ThickCrustDough(Dough):
    def __str__(self):
        return "Thin Crust Dough"


class ThinCrustDough(Dough):
    def __str__(self):
        return "ThickCrust style extra thick crust dough"


###############################################################################
# Pepperoni
###############################################################################
class Pepperoni:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self):
        pass


class SlicedPepperoni(Pepperoni):
    def __str__(self):
        return "Sliced Pepperoni"


###############################################################################
# Sauce
###############################################################################

class Sauce:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self):
        pass


class MarinaraSauce(Sauce):
    def __str__(self):
        return "Marinara Sauce"


class PlumTomatoSauce(Sauce):
    def __str__(self):
        return "Tomato sauce with plum tomatoes"


###############################################################################
# Veggie
###############################################################################
class Veggie:
    __metaclass__ = ABCMeta

    @abstractmethod
    def __str__(self):
        pass


class BlackOlives(Veggie):
    def __str__(self):
        return "Black Olives"


class Eggplant(Veggie):
    def __str__(self):
        return "Eggplant"


class Garlic(Veggie):
    def __str__(self):
        return "Garlic"


class Mushroom(Veggie):
    def __str__(self):
        return "Mushrooms"


class Onion(Veggie):
    def __str__(self):
        return "Onion"


class RedPepper(Veggie):
    def __str__(self):
        return "Red Pepper"


class Spinach(Veggie):
    def __str__(self):
        return "Spinach"
