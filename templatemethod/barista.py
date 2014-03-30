"""
Barista

Author: m1ge7
Date: 2014/03/30
"""

from abc import ABCMeta, abstractmethod


class CaffeineBeverage:
    __metaclass__ = ABCMeta

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print "Boiling water"

    def pour_in_cup(self):
        print "Pouring into cup"


class Tea(CaffeineBeverage):

    def brew(self):
        print "Steeping the tea"

    def add_condiments(self):
        print "Adding Lemon"


class Coffee(CaffeineBeverage):

    def brew(self):
        print "Dripping Coffee through filter"

    def add_condiments(self):
        print "Adding Sugar and Milk"


class CaffeineBeverageWithHook:
    __metaclass__ = ABCMeta

    def prepare_recipe(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        if self.customer_wants_condiments() is True:
            self.add_condiments()

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def add_condiments(self):
        pass

    def boil_water(self):
        print "Boiling water"

    def pour_in_cup(self):
        print "Pouring into cup"

    def customer_wants_condiments(self):
        return True


class CoffeeWithHook(CaffeineBeverageWithHook):

    def brew(self):
        print "Dripping Coffee through filter"

    def add_condiments(self):
        print "Adding Sugar and Milk"

    def customer_wants_condiments(self):
        prompt = "Would you like milk and sugar with your coffee (y/n)?"
        answer = raw_input(prompt)
        return answer.lower().startswith('y')


class TeaWithHook(CaffeineBeverageWithHook):
    def brew(self):
        print "Stepping the tea"

    def add_condiments(self):
        print "Adding Lemon"

    def customer_wants_condiments(self):
        prompt = "Would you like lemmon with your tea (y/n)?"
        answer = raw_input(prompt)
        return answer.lower().startswith('y')


if __name__ == '__main__':
    tea = Tea()
    coffee = Coffee()

    print "\nMaking tea..."
    tea.prepare_recipe()

    print "\nMaking coffee..."
    coffee.prepare_recipe()

    tea_with_hook = TeaWithHook()
    coffee_with_hook = CoffeeWithHook()

    print "\nMaking tea..."
    tea_with_hook.prepare_recipe()

    print "\nMaking coffee..."
    coffee_with_hook.prepare_recipe()
