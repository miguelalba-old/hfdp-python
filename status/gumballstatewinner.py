"""
Gumball machine with winner state

Author: m1ge7
Date: 2014/03/30
"""

import random
from abc import ABCMeta, abstractmethod


class State:
    __metaclass__ = ABCMeta

    @abstractmethod
    def insert_quarter(self):
        pass

    @abstractmethod
    def eject_quarter(self):
        pass

    @abstractmethod
    def turn_crank(self):
        pass

    @abstractmethod
    def dispense(self):
        pass


class HasQuarterState(State):

    def __init__(self, gumballmachine):
        self.__gumballmachine = gumballmachine
    
    def insert_quarter(self):
        print "You can't insert another quarter"

    def eject_quarter(self):
        print "Quarter returned"
        self.__gumballmachine.set_state(self.__gumballmachine.get_no_quarter_state())

    def turn_crank(self):
        print "You turned..."
        winner = random.randint(1,10)
        if winner == 1 and self.__gumballmachine.get_count() > 1:
            self.__gumballmachine.set_state(self.__gumballmachine.get_winner_state())
        else:
            self.__gumballmachine.set_state(self.__gumballmachine.get_sold_state())

    def dispense(self):
        print "No gumball dispensed"

    def __str__(self):
        return "waiting for turn of crank"


class NoQuarterState(State):

    def __init__(self, gumballmachine):
        self.__gumballmachine = gumballmachine

    def insert_quarter(self):
        print "You inserted a quarter"
        self.__gumballmachine.set_state(self.__gumballmachine.get_has_quarter_state())

    def eject_quarter(self):
        print "You haven't inserted a quarter"

    def turn_crank(self):
        print "You turned, but there's no quarter"

    def dispense(self):
        print "You need to pay first"

    def __str__(self):
        return "waiting for quarter"


class SoldOutState(State):

    def __init__(self, gumballmachine):
        self.__gumballmachine = gumballmachine

    def insert_quarter(self):
        print "You can't insert a quarter, the machine is sold out"

    def eject_quarter(self):
        print "You can't eject, you haven't inserted a quarter yet"

    def turn_crank(self):
        print "You turned, but there are no gumballs"

    def dispense(self):
        print "No gumball dispensed"

    def __str__(self):
        return "sold out"


class SoldState(State):

    def __init__(self, gumballmachine):
        self.__gumballmachine = gumballmachine

    def insert_quarter(self):
        print "Please wait, we're already giving you a gumball"

    def eject_quarter(self):
        print "Sorry, you already turned the crank"

    def turn_crank(self):
        print "Turning twice doesn't get you another gumball!"

    def dispense(self):
        self.__gumballmachine.release_ball()
        if self.__gumballmachine.get_count() > 0:
            self.__gumballmachine.set_state(self.__gumballmachine.get_no_quarter_state())
        else:
            print "Oops, out of gumballs!"
            self.__gumballmachine.set_state(self.__gumballmachine.get_sold_out_state())

    def __str__(self):
        return "dispensing a gumball"


class WinnerState(State):

    def __init__(self, gumballmachine):
        self.__gumballmachine = gumballmachine

    def insert_quarter(self):
        print "Please wait, we're already giving you a Gumball"

    def eject_quarter(self):
        print "Please wait, we're already giving you a Gumball"

    def turn_crank(self):
        print "Turning again doesn't get you another gumball!"

    def dispense(self):
        print "YOU'RE A WINNER! You get two gumballs for your quarter"
        self.__gumballmachine.release_ball()
        if self.__gumballmachine.get_count() == 0:
            self.__gumballmachine.set_state(self.__gumballmachine.get_sold_out_state())
        else:
            self.__gumballmachine.release_ball()
            if self.__gumballmachine.get_count() > 0:
                self.__gumballmachine.set_state(self.__gumballmachine.get_no_quarter_state())
            else:
                print "Oops, out of gumballs!"
                self.__gumballmachine.set_state(self.__gumballmachine.get_sold_out_state())

    def __str__(self):
        return "despensing two gumballs for your quarter, because YOU'RE A WINNER!" 


class GumballMachine:

    def __init__(self, number_gumballs):
        self.__sold_out_state = SoldOutState(self)
        self.__no_quarter_state = NoQuarterState(self)
        self.__has_quarter_state = HasQuarterState(self)
        self.__sold_state = SoldState(self)
        self.__winner_state = WinnerState(self)

        self.__state = self.__sold_state
        self.__count = number_gumballs
        if number_gumballs > 0:
            self.__state = self.__no_quarter_state

    def insert_quarter(self):
        self.__state.insert_quarter()

    def eject_quarter(self):
        self.__state.eject_quarter()

    def turn_crank(self):
        self.__state.turn_crank()

    def set_state(self, state):
        self.__state = state

    def release_ball(self):
        print "A gumball comes rolling out the slot..." 
        if self.__count != 0:
            self.__count -= 1

    def get_count(self):
        return self.__count

    def refill(self, count):
        self.__count = count
        self.__state = self.__no_quarter_state

    def get_state(self):
        return self.__state

    def get_sold_out_state(self):
        return self.__sold_out_state

    def get_no_quarter_state(self):
        return self.__no_quarter_state

    def get_has_quarter_state(self):
        return self.__has_quarter_state

    def get_sold_state(self):
        return self.__sold_state

    def get_winner_state(self):
        return self.__winner_state

    def __str__(self):
        result = ""
        result += "\nMighty Gumball, Inc."
        result += "\nJava-enabled Standing Gumball Model #2004"
        result += "\nInventory: " + str(self.__count) + " gumball"
        if self.__count != 1:
            result += "s"
        result += "\n"
        result += "Machine is " + str(self.__state) + "\n"
        return result

    

if __name__ == '__main__':
    gumballmachine = GumballMachine(10)

    print(gumballmachine)

    gumballmachine.insert_quarter()
    gumballmachine.turn_crank()
    gumballmachine.insert_quarter()
    gumballmachine.turn_crank()

    print(gumballmachine)

    gumballmachine.insert_quarter()
    gumballmachine.turn_crank()
    gumballmachine.insert_quarter()
    gumballmachine.turn_crank()

    print(gumballmachine)

    gumballmachine.insert_quarter()
    gumballmachine.turn_crank()
    gumballmachine.insert_quarter()
    gumballmachine.turn_crank()

    print(gumballmachine)

    gumballmachine.insert_quarter()
    gumballmachine.turn_crank()
    gumballmachine.insert_quarter()
    gumballmachine.turn_crank()

    print(gumballmachine)

    gumballmachine.insert_quarter()
    gumballmachine.turn_crank()
    gumballmachine.insert_quarter()
    gumballmachine.turn_crank()

    print(gumballmachine)
