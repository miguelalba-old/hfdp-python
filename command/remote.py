"""
Remote

Author: m1ge7
Date: 2014/03/28
"""

from abc import ABCMeta, abstractmethod


###############################################################################
# Appliances
###############################################################################

class CeilingFan:

    HIGH = 2
    MEDIUM = 1
    LOW = 0

    def __init__(self, location):
        self._location = location
        self._level = 0

    def high(self):
        "turns the ceiling fan on to high"
        self._level = CeilingFan.HIGH
        print self._location + " ceiling fan is on high"

    def medium(self):
        "turns the ceiling fan on to medium"
        self._level = CeilingFan.MEDIUM
        print self._location + " ceiling fan is on medium"

    def low(self):
        "turns the ceiling fan on to low"
        self._level = CeilingFan.LOW
        print self._location + " ceiling fan is on low"

    def off(self):
        "turns the ceiling fan off"
        self._level = 0
        print self._location + " ceiling fan is off"

    def get_speed(self):
        return self._level
    

class GarageDoor:

    def __init__(self, location):
        self._location = location

    def up(self):
        print self._location + " garage Door is Up"

    def down(self):
        print self._location + " garage Door is Down"

    def stop(self):
        print self._location + " garage Door is Stopped"

    def light_on(self):
        print self._location + " garage light is on"

    def light_off(self):
        print self._location + " garage light is off"


class Hottub:

    def __init__(self):
        self._on = False
        self._temperature = 0

    def on(self):
        self._on = True

    def off(self):
        self._off = False

    def bubbles_on(self):
        if self._on is True:
            print "Hottub is bubbling!"
    
    def bubbles_off(self):
        if self._on is True:
            print "Hottub is not bubbling!"

    def jets_on(self):
        if self._on is True:
            print "Hottub jets are on"

    def jets_off(self):
        if self._on is True:
            print "Hottub jets are off"

    def set_temperature(self, temperature):
        self._temperature = temperature

    def heat(self):
        self._temperature = 105
        print "Hottub is heating to a steaming 105 degrees"

    def cool(self):
        self._temperature = 98
        print "Hottub is cooling to 98 degrees"


class Light:

    def __init__(self, location):
        self._location = location

    def on(self):
        print self._location + " light is on"

    def off(self):
        print self._location + " light is off"

class Stereo:

    def __init__(self, location):
        self._location = location

    def on(self):
        print self._location + " stereo is on"

    def off(self):
        print self._location + " stereo is off"

    def set_cd(self):
        print self._location + " stereo is set for CD input"

    def set_dvd(self):
        print self._location + " stereo is set for Radio"

    def set_volume(self, volume):
        """code to set the volume
        valid range: 1-11 (after all 11 is better than 10, right?)
        """
        print self._location + " Stereo volume set to " + str(volume)


class TV:

    def __init__(self, location):
        self._location = location
        self._channel = 0

    def on(self):
        print "TV is on"
    
    def off(self):
        print "TV is off"

    def set_input_channel(self):
        self._channel = 3
        print "Channell is set for VCR"


###############################################################################
# Commands
###############################################################################

class Command:
    __metaclass__ = ABCMeta

    @abstractmethod
    def execute(self):
        pass


class CeilingFanOnCommand(Command):

    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan

    def execute(self):
        self._ceiling_fan.high()


class CeilingFanOffCommand(Command):

    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan

    def execute(self):
        self._ceiling_fan.off()


class GarageDoorUpCommand(Command):

    def __init__(self, garage_door):
        self._garage_door = garage_door

    def execute(self):
        self._garage_door.up()


class GarageDoorDownCommand(Command):

    def __init__(self, garage_door):
        self._garage_door = garage_door

    def execute(self):
        self._garage_door.up()


class HottubOnCommand(Command):

    def __init__(self, hottub):
        self._hottub = hottub

    def execute(self):
        self._hottub.on()
        self._hottub.heat()
        self._hottub.bubbles_on()


class HottubOffCommand(Command):

    def __init__(self, hottub):
        self._hottub = hottub
    
    def execute(self):
        self._hottub.cool()
        self._hottub.off()


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


class LivingroomLightOnCommand(Command):

    def __init__(self, light):
        self._ligth = light

    def execute(self):
        self._light.on()


class LivingRoomLightOffCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()


class NoCommand(Command):
    def execute(self):
        pass


class StereoOnWithCDCommand(Command):

    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.on()
        self._stereo.set_cd()
        self._stereo.set_volume(11)


class StereoOffCommand(Command):

    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.off()


###############################################################################
# Invoker
###############################################################################

class RemoteControl:

    def __init__(self):
        self._on_commands = [NoCommand()] * 7
        self._off_commands = [NoCommand()] * 7

    def set_command(self, slot, on_command, off_command):
        self._on_commands[slot] = on_command
        self._off_commands[slot] = off_command

    def on_button_was_pushed(self, slot):
        self._on_commands[slot].execute()
    
    def off_button_was_pushed(self, slot):
        self._off_commands[slot].execute()

    def __str__(self):
        string_buff = "\n------ Remote Control -------\n" 
        for num, command in enumerate(self._on_commands):
            string_buff += ("[slot " + str(num) + "] " +
                            command.__class__.__name__ + "\n")
        return string_buff


if __name__ == '__main__':
    remote_control = RemoteControl()

    living_room_light = Light("Living Room")
    kitchen_light = Light("Kitchen")
    ceiling_fan = CeilingFan("Living Room")
    garage_door = GarageDoor("")
    stereo = Stereo("Living Room")
    
    living_room_light_on = LightOnCommand(living_room_light)
    living_room_light_off = LightOffCommand(living_room_light)
    kitchen_light_on = LightOnCommand(kitchen_light)
    kitchen_light_off = LightOffCommand(kitchen_light)

    ceiling_fan_on = CeilingFanOnCommand(ceiling_fan)
    ceiling_fan_off = CeilingFanOffCommand(ceiling_fan)

    garage_door_up = GarageDoorUpCommand(garage_door)
    garage_door_down = GarageDoorDownCommand(garage_door)

    stereo_on_with_cd = StereoOnWithCDCommand(stereo)
    stereo_off = StereoOffCommand(stereo)

    remote_control.set_command(0, living_room_light_on, living_room_light_off)
    remote_control.set_command(1, kitchen_light_on, kitchen_light_off)
    remote_control.set_command(2, ceiling_fan_on, ceiling_fan_off)
    remote_control.set_command(3, stereo_on_with_cd, stereo_off)

    print str(remote_control)

    remote_control.on_button_was_pushed(0)
    remote_control.off_button_was_pushed(0)
    remote_control.on_button_was_pushed(1)
    remote_control.off_button_was_pushed(1)
    remote_control.on_button_was_pushed(2)
    remote_control.off_button_was_pushed(2)
    remote_control.on_button_was_pushed(3)
    remote_control.off_button_was_pushed(3)
