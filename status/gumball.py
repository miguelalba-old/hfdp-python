"""
Original gumball machine (without patterns)

Author: m1ge7
Date: 2014/03/30
"""


class GumballMachine:

    SOLD_OUT = 0
    NO_QUARTER = 1
    HAS_QUARTER = 2
    SOLD = 3

    def __init__(self, count):
        self._count = count
        if count > 0:
            self._state = GumballMachine.NO_QUARTER
        else:
            self._state = GumballMachine.SOLD_OUT

    def insert_quarter(self):
        if self._state == GumballMachine.HAS_QUARTER:
            print "You can't insert another quarter"
        elif self._state == GumballMachine.NO_QUARTER:
            print "You inserted a quarter"
        elif self._state == GumballMachine.SOLD_OUT:
            print "You can't insert a quarter, the machine is sold out"
        elif self._state == GumballMachine.SOLD:
            print "Please wait, we're already giving you a gumball"
    
    def eject_quarter(self):
        if self._state == GumballMachine.HAS_QUARTER:
            print "Quarter returned"
            self._state = GumballMachine.NO_QUARTER
        elif self._state == GumballMachine.NO_QUARTER:
            print "You haven't inserted a quarter"
        elif self._state == GumballMachine.SOLD:
            print "Sorry, you already turned the crank"
        elif self._state == GumballMachine.SOLD_OUT:
            print "You can't eject, you haven't inserted a quarter yet"

    def turn_crank(self):
        if self._state == GumballMachine.SOLD:
            print "Turning twice doesn't get you another gumball"
        elif self._state == GumballMachine.NO_QUARTER:
            print "You turned but there's no quarter"
        elif self._state == GumballMachine.SOLD_OUT:
            print "You turned, but there are no gumballs"
        elif self._state == GumballMachine.HAS_QUARTER:
            print "You turned..."
            self._state = GumballMachine.SOLD
            self.dispense()

    def dispense(self):
        if self._state == GumballMachine.SOLD:
            print "A gumball comes rolling out the slot"
            self._count -= 1
            if self._count == 0:
                print "Oops, out of gumballs!"
                self._state = GumballMachine.SOLD_OUT
            else:
                self._state = GumballMachine.NO_QUARTER
        elif self._state == GumballMachine.NO_QUARTER:
            print "You need to pay first"
        elif self._state == GumballMachine.SOLD_OUT:
            print "No gumball dispensed"
        elif self._state == GumballMachine.HAS_QUARTER:
            print "No gumball dispensed"

    def refill(self, num_gum_balls):
        self._count = num_gum_balls
        self._state = GumballMachine.NO_QUARTER

    def __str__(self):
        buff = "\nMighty Gumball, Inc."
        buff +="\nJava-enabled Standing Gumball Model #2004\n" 
        buff += "Inventory: " + str(self._count) + " gumball"
        if self._count != 1:
            buff += "s"
        buff += "\nMachine is "
        if self._state == GumballMachine.SOLD_OUT:
            buff += "sold out"
        elif self._state == GumballMachine.NO_QUARTER:
            buff += "waiting for quarter"
        elif self._state == GumballMachine.HAS_QUARTER:
            buff += "waiting for turn of crank"
        elif self._state == GumballMachine.SOLD:
            buff += "delivering a gumball"
        buff += "\n"
        return buff


if __name__ == '__main__':
    gumball_machine = GumballMachine(5)

    print str(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print str(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.eject_quarter()
    gumball_machine.turn_crank()

    print str(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.eject_quarter()

    print str(gumball_machine)

    gumball_machine.insert_quarter()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()
    gumball_machine.insert_quarter()
    gumball_machine.turn_crank()

    print str(gumball_machine)
