"""
Simple barista

Author: m1ge7
Date: 2014/03/30
"""


class Coffee:

    def prepare_recipe(self):
        self.boil_water()
        self.brew_coffee_grinds()
        self.pour_in_cup()
        self.add_sugar_and_milk()

    def boil_water(self):
        print "Boiling water"

    def brew_coffee_grinds(self):
        print "Dripping Coffee through filter"

    def pour_in_cup(self):
        print "Pouring into cup"

    def add_sugar_and_milk(self):
        print "Adding Sugar and Milk"


class Tea:

    def prepare_recipe(self):
        self.boil_water()
        self.steep_tea_bag()
        self.pour_in_cup()
        self.add_lemon()

    def boil_water(self):
        print "Boiling water"

    def steep_tea_bag(self):
        print "Stepping the tea"

    def add_lemon(self):
        print "Adding Lemon"

    def pour_in_cup(self):
        print "Pouring into cup"


if __name__ == '__main__':
    tea = Tea()
    coffee = Coffee()
    print 'Making tea...'
    tea.prepare_recipe()
    print 'Making coffee...'
    coffee.prepare_recipe()
