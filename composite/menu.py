from abc import ABCMeta, abstractmethod


class MenuComponent:
    __metaclass__ = ABCMeta

    def add(self, menu_component):
        raise NotImplementedError()

    def remove(self, menu_component):
        raise NotImplementedError()

    def get_child(self, i):
        raise NotImplementedError()

    def get_description(self):
        raise NotImplementedError()

    def get_price(self):
        raise NotImplementedError()

    def is_vegetarian(self):
        raise NotImplementedError()

    def __str__(self):
        raise NotImplementedError()


class MenuItem(MenuComponent):

    def __init__(self, name, description, vegetarian, price):
        self.__name = name
        self.__description = description
        self.__vegetarian = vegetarian
        self.__price = price

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def is_vegetarian(self):
        return self.__vegetarian

    def __str__(self):
        result = "\n " + self.__name
        if self.__vegetarian is True:
            result += "(v)"
        result += ", " + str(self.__price) + "\n"
        result += "     -- " + self.__description + "\n"
        return result


class Waitress:

    def __init__(self, all_menus):
        self.__all_menus = all_menus

    def print_menu(self):
        print str(self.__all_menus)


class Menu(MenuComponent):

    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        self.__menu_components = []

    def add(self, menu_component):
        self.__menu_components.append(menu_component)

    def remove(self, menu_component):
        self.__menu_components.remove(menu_component)

    def get_child(self, i):
        return self.__menu_components[i]

    def get_name(self):
        return self.__name

    def get_description(self):
        return self.__description

    def __str__(self):
        result = "\n" + self.__name
        result += ", " + self.__description + "\n"
        result += "---------------------" + "\n"
        result += ''.join([str(menu) for menu in self.__menu_components])
        return result


if __name__ == '__main__':
    pancake_house_menu = Menu("PANCAKE HOUSE MENU", "Breakfast")
    diner_menu = Menu("DINER MENU", "Lunch")
    cafe_menu = Menu("CAFE MENU", "Dinner")
    dessert_menu = Menu("DESSERT MENU", "Dessert of course!")
    coffee_menu = Menu("COFFEE MENU", "Stuff to go with your afternoon coffee")
    all_menus = Menu("ALL MENUS", "All menus combined")

    all_menus.add(pancake_house_menu)
    all_menus.add(diner_menu)
    all_menus.add(cafe_menu)

    pancake_house_menu.add(MenuItem("K&B's Pancake Breakfast",
        "Pancakes with scrambled eggs, and toast", True, 2.99))
    pancake_house_menu.add(MenuItem("Regular Pancake Breakfast",
        "Pancakes with fried eggs, sausage", False, 2.99))
    pancake_house_menu.add(MenuItem("Blueberry Pancakes",
        "Pancakes made with fresh blueberries, and blueberry syrup", True, 3.49))
    pancake_house_menu.add(MenuItem("Waffles",
        "Waffles, with your choice of blueberries or strawberries", True, 3.59))

    diner_menu.add(MenuItem("Vegetarian BLT",
        "(Fakin') Bacon with lettuce & tomato on whole wheat", True, 2.99))
    diner_menu.add(MenuItem("BLT", "Bacon with lettuce & tomato on whole wheat",
        False, 2.99))
    diner_menu.add(MenuItem("Soup of the day",
        "A bowl of the soup of the day, with a side of potato salad", False, 3.29))
    diner_menu.add(MenuItem("Hotdog",
        "A hot dog, with saurkraut, relish, onions, topped with cheese", False, 3.05))
    diner_menu.add(MenuItem("Steamed Veggies and Brown Rice",
        "Steamed vegetables over brown rice", True, 3.99))
    diner_menu.add(MenuItem("Pasta",
        "Spaghetti with Marinara Sauce, and a slice of sourdough bread", True, 3.89))
    diner_menu.add(dessert_menu)

    dessert_menu.add(MenuItem("Apple Pie",
        "Apple pie with a flakey crust, topped with vanilla icecream", True, 1.59))
    dessert_menu.add(MenuItem("Cheesecake",
        "Creamy New York cheesecake, with a chocolate graham crust", True, 1.99))
    dessert_menu.add(MenuItem("Sorbet",
        "A scoop of raspberry and a scoop of lime", True, 1.89))
    
    cafe_menu.add(MenuItem("Veggie Burger and Air Fries",
        "Veggie burger on a whole wheat bun, lettuce, tomato, and fries", True, 3.99))
    cafe_menu.add(MenuItem("Soup of the day",
        "A cup of the soup of the day, with a side salad", False, 3.69))
    cafe_menu.add(MenuItem("Burrito",
        "A large burrito, with whole pinto beans, salsa, guacamole", True, 4.29))
    cafe_menu.add(coffee_menu)

    coffee_menu.add(MenuItem("Coffe Cake",
        "Crumbly cake topped with cinnamon and walnuts", True, 1.59))
    coffee_menu.add(MenuItem("Bagel",
        "Flavors include sesame, poppyseed, cinnamon raisin, pumpkin", False, 0.69))
    coffee_menu.add(MenuItem("Biscotti",
        "Three almond or hazelnut biscotti cookies", True, 0.89))

    waitress = Waitress(all_menus)
    waitress.print_menu()
