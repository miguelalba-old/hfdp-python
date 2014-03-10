"Simple Remote Control"
from abc import ABCMeta, abstractmethod


class Light:

    def on(self):
        print "Light is on"

    def off(self):
        print "Light is off"


class GarageDoor:

    def up(self):
        print "Garage Door is Open" 

    def down(self):
        print "Garage Door is Closed" 

    def stop(self):
        print "Garage Door is Stopped" 

    def light_on(self):
        print "Garage light is on" 

    def light_off(self):
        print "Garage light is off" 


class Command:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


class GarageDoorOpenCommand(Command):

    def __init__(self, garage_door):
        self._garage_door = garage_door

    def execute(self):
        self._garage_door.up()


class LightOnCommand(Command):
    
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.on()


class LightOffCommand(Command):
    
    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()


class SimpleRemoteControl(object):

    def __init__(self):
        self._slot = None

    def set_command(self, command):
        self._slot = command

    def button_was_pressed(self):
        self._slot.execute()


if __name__ == '__main__':
    # Remote control test
    remote = SimpleRemoteControl()
    light = Light()
    garage_door = GarageDoor()
    light_on = LightOnCommand(light)
    garage_open = GarageDoorOpenCommand(garage_door)

    remote.set_command(light_on)
    remote.button_was_pressed()
    remote.set_command(garage_open)
    remote.button_was_pressed()
