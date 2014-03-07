import stores

if __name__ == '__main__':
    nyStore = stores.NYPizzaStore()
    chicagoStore = stores.ChicagoPizzaStore()

    pizza = nyStore.order_pizza("cheese")
    print "Ethan ordered a " + str(pizza) + "\n"

    pizza = chicagoStore.order_pizza("cheese")
    print "Joel ordered a " + str(pizza) + "\n"

    pizza = nyStore.order_pizza("clam")
    print "Ethan ordered a " + str(pizza) + "\n"

    pizza = chicagoStore.order_pizza("clam")
    print "Joel ordered a " + str(pizza) + "\n"

    pizza = nyStore.order_pizza("pepperoni")
    print "Ethan ordered a " + str(pizza) + "\n"

    pizza = chicagoStore.order_pizza("pepperoni")
    print "Joel ordered a " + str(pizza) + "\n"

    pizza = nyStore.order_pizza("veggie")
    print "Ethan ordered a " + str(pizza) + "\n"

    pizza = chicagoStore.order_pizza("veggie")
    print "Joel ordered a " + str(pizza) + "\n"
