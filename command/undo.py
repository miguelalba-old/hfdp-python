"""
Remote control with undo

Author: m1ge7
Date: 2014/03/28
"""


from abc import ABCMeta, abstractmethod

###############################################################################
# Appliances
###############################################################################

class CeilingFan:

    HIGH = 3
    MEDIUM = 2
    LOW = 1
    OFF = 0

    def __init__(self, location):
        self._location = location
        self._speed = CeilingFan.OFF

    def high(self):
        self._speed = CeilingFan.HIGH
        print self._location + " ceiling fan is on high"

    def medium(self):
        self._speed = CeilingFan.MEDIUM
        print self._location + " ceiling fan is on medium"

    def low(self):
        self._speed = CeilingFan.LOW
        print self._location + " ceiling fan is on low"

    def off(self):
        self._speed = CeilingFan.OFF
        print self._location + " ceiling fan is off"

    def get_speed(self):
        return self._speed

class Light:

    def __init__(self, location):
        self._location = location
        self._level = 0

    def on(self):
        self._level = 100
        print "Light is on"

    def off(self):
        self._level = 0
        print "Light is off"

    def dim(self, level):
        self._level = level
        if self._level == 0:
            self.off()
        else:
            print "Light is dimmed to " + str(self._level) + "%"

    def get_level(self):
        return self._level

###############################################################################
# Commands
###############################################################################

class Command:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass



class NoCommand(Command):
    
    def execute(self):
        pass

    def undo(self):
        pass


class CeilingFanHighCommand(Command):

    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan

    def execute(self):
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.high()

    def undo(self):
        if self._prev_speed == CeilingFan.HIGH:
            self._ceiling_fan.high()
        elif self._prev_speed == CeilingFan.MEDIUM:
            self._ceiling_fan.medium()
        elif self._prev_speed == CeilingFan.LOW:
            self._ceiling_fan.low()
        elif self._prev_speed == CeilingFan.OFF:
            self._ceiling_fan.off()


class CeilingFanMediumCommand(Command):

    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan

    def execute(self):
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.medium()

    def undo(self):
        if self._prev_speed == CeilingFan.HIGH:
            self._ceiling_fan.high()
        elif self._prev_speed == CeilingFan.MEDIUM:
            self._ceiling_fan.medium()
        elif self._prev_speed == CeilingFan.LOW:
            self._ceiling_fan.low()
        elif self._prev_speed == CeilingFan.OFF:
            self._ceiling_fan.off()


class CeilingFanLowCommand(Command):

    def __init__(self, ceiling_fan):
        self._ceiling_fan  = ceiling_fan

    def execute(self):
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.low()

    def undo(self):
        if self._prev_speed == CeilingFan.HIGH:
            self._ceiling_fan.high()
        elif self._prev_speed == CeilingFan.MEDIUM:
            self._ceiling_fan.medium()
        elif self._prev_speed == CeilingFan.LOW:
            self._ceiling_fan.low()
        elif self._prev_speed == CeilingFan.OFF:
            self._ceiling_fan.off()


class CeilingFanOffCommand(Command):

    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan

    def execute(self):
        self._prev_speed = self._ceiling_fan.get_speed()
        self._ceiling_fan.off()

    def undo(self):
        if self._prev_speed == CeilingFan.HIGH:
            self._ceiling_fan.high()
        elif self._prev_speed == CeilingFan.MEDIUM:
            self._ceiling_fan.medium()
        elif self._prev_speed == CeilingFan.LOW:
            self._ceiling_fan.low()
        elif self._prev_speed == CeilingFan.OFF:
            self._ceiling_fan.off()


class DimmerLightOnCommand(Command):

    def __init__(self, light):
        self._light = light
        self._prev_level = None

    def execute(self):
        self._prev_level = self._light.get_level()
        self._light.dim(75)
    
    def undo(self):
        self._light.dim(self._prev_level)


class DimmerLightOffCommand(Command):

    def __init__(self, light):
        self._light = light
        self._prev_level = 100

    def execute(self):
        self._prev_level = self._ligth.get_level()
        self._light.off()

    def undo(self):
        self._light.dim(self._prev_level)


class LightOnCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._level = self._light.get_level()
        self._light.on()

    def undo(self):
        self._light.dim(self._level)

class LightOffCommand(Command):

    def __init__(self, light):
        self._light = light
        self._level = 0

    def execute(self):
        self._level = self._light.get_level()
        self._light.off()
    
    def undo(self):
        self._light.dim(self._level)


###############################################################################
# Invoker
###############################################################################

class RemoteControlWithUndo:

    def __init__(self):
        self._on_commands = [NoCommand()] * 7
        self._off_commands = [NoCommand()] * 7
        self._undo_command = NoCommand()

    def set_command(self, slot, on_command, off_command):
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_was_pushed(self, slot):
        self._on_commands[slot].execute()
        self._undo_command = self._on_commands[slot]

    def off_button_was_pushed(self, slot):
        self._off_commands[slot].execute()
        self._undo_command = self._off_commands[slot]

    def undo_button_was_pushed(self):
        self._undo_command.undo()

    def __str__(self):
        string_buff = "\n------ Remote Control -------\n" 
        for i in range(len(self._on_commands)):
            string_buff += "[slot " + str(i) + "] "
            string_buff +=  self._on_commands[i].__class__.__name__ + "   "
            string_buff += self._off_commands[i].__class__.__name__ + "\n"
        string_buff += "[undo]" + self._undo_command.__class__.__name__ + "\n"
        return string_buff


if __name__ == '__main__':
    remote_control = RemoteControlWithUndo()

    living_room_light = Light("Living Room")

    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    print str(remote_control)
    remote_control.undo_button_was_pushed()
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(0)
    print str(remote_control)
    remote_control.undo_button_was_pushed()

    ceiling_fan = CeilingFan("Living Room")

    ceiling_fan_medium = CeilingFanMediumCommand(ceiling_fan)
    ceiling_fan_high = CeilingFanHighCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

    remote_control.set_command(0, ceiling_fan_medium, ceiling_fan_off)
    remote_control.set_command(1, ceiling_fan_high, ceiling_fan_off)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    print str(remote_control)
    remote_control.undo_button_was_pushed()

    remote_control.on_button_was_pushed(1)
    print str(remote_control)
    remote_control.undo_button_was_pushed()
