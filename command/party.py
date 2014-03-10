from abc import ABCMeta, abstractmethod


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


class CeilingFanHighCommand(Command):

    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan
        self._prev_speed = None

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
        else:
            self._ceiling_fan.off()


class CeilingFanMediumCommand(Command):
    
    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan
        self._prev_speed = None

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
        else:
            self._ceiling_fan.off()


class CeilingFanOffCommand(Command):

    def __init__(self, ceiling_fan):
        self._ceiling_fan = ceiling_fan
        self._prev_speed = None

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
        else:
            self._ceiling_fan.off()


class HottubOffCommand(Command):

    def __init__(self, hottub):
        self._hottub = hottub

    def execute(self):
        self._hottub.set_temperature(98)
        self._hottub.off()

    def undo(self):
        self._hottub.on()


class HottubOnCommand(Command):

    def __init__(self, hottub):
        self._hottub = hottub

    def execute(self):
        self._hottub.on()
        self._hottub.set_temperature(104)
        self._hottub.circulate()

    def undo(self):
        self._hottub.off()


class LightOffCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()

    def undo(self):
        self._light.on()


class LightOnCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.on()

    def undo(self):
        self._light.off()


class LivingroomLightOffCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.off()
    
    def undo(self):
        self._light.on()


class LivingroomLightOnCommand(Command):

    def __init__(self, light):
        self._light = light

    def execute(self):
        self._light.on()

    def undo(self):
        self._light.off()


class StereoOffCommand(Command):

    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.off()

    def undo(self):
        self._stereo.on()


class StereoOnCommand(Command):

    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.on()

    def undo(self):
        self._stereo.off()


class StereoOnWithCDCommand(Command):

    def __init__(self, stereo):
        self._stereo = stereo

    def execute(self):
        self._stereo.on()
        self._stereo.set_cd()
        self._stereo.set_volume(11)

    def undo(self):
        self._stereo.off()


class TVOffCommand(Command):

    def __init__(self, tv):
        self._tv = tv

    def execute(self):
        self._tv.off()

    def undo(self):
        self._tv.on()


class TVOnCommand(Command):

    def __init__(self, tv):
        self._tv = tv

    def execute(self):
        self._tv.on()

    def undo(self):
        self._tv.off()


class MacroCommand(Command):

    def __init__(self, commands):
        self._commands = commands

    def execute(self):
        for command in self._commands:
            command.execute()

    def undo(self):
        for command in self._commands.reverse():
            command.undo()


class NoCommand(Command):
    __metaclass__ = ABCMeta

    def execute(self):
        pass

    def undo(self):
        pass


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
        self._speed = None

    def high(self):
        "turns the ceiling fan on to high"
        self._speed = self.HIGH

    def medium(self):
        "turns the ceiling fan on to medium"
        self._speed = self.MEDIUM
        print self._location + " ceiling fan is on medium"

    def low(self):
        "turns the ceiling fan on to low"
        self._speed = self.LOW
        print self._location + " ceiling fan is on low"

    def off(self):
        "turns the ceiling fan off"
        self._speed = self.OFF
        print self._location + " ceiling fan is off"

    def get_speed(self):
        return self._speed()


class Hottub:

    def __init__(self):
        self._on = None
        self._temperature = None

    def on(self):
        self._on = True

    def off(self):
        self._on = False

    def circulate(self):
        if self._on:
            print "Hottub is bubbling!"

    def jets_on(self):
        if self._on:
            print "Hottub jets are on" 

    def jets_off(self):
        if self._on:
            print "Hottub jets are off" 

    def set_temperature(self, temperature):
        if temperature > self._temperature:
            print "Hottub is heating to a steaming " + str(temperature) + " degrees"
        else:
            print "Hottub is cooling to " + str(temperature) + " degrees"
        self._temperature = temperature


class Light:

    def __init__(self, location):
        self._location = location
        self._level = None

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
            print "Light is dimmed to " + self._level + "%"

    def get_level(self):
        return self._level


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
        print self._location + " stereo is set for DVD input"

    def set_radio(self):
        print self._location + " stereo is set for Radio"

    def set_volume(self, volume):
        """ code to set the volume
        valid range: 1-11 (after all 11 is better than 10, right?)"""
        print self._location + " Stereo volume set to " + volume


class TV:

    def __init__(self, location):
        self._location = location
        self._channel = None

    def on(self):
        print self._location + " TV is on"

    def off(self):
        print self._location + " TV is off"

    def set_input_channel(self):
        self._channel = 3
        print self._location + " TV channel is set for DVD"


###############################################################################
# Remote control
###############################################################################

class RemoteControl:

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
        buff = "\n------ Remote Control -------\n"
        for i in range(len(self._on_commands)):
            buff += ("[slot " + str(i) + "] " + str(self._on_commands[i]) +
                    "    " + str(self._off_commands[i]) + "\n")
        buff += ("[undo] " + str(self._undo_command) + "\n")
        return buff


# Remote loader
if __name__ == '__main__':
    remote_control = RemoteControl()

    light = Light("Living Room")
    tv = TV("Living Room")
    stereo = Stereo("Living Room")
    hottub = Hottub()

    light_on = LightOnCommand(light)
    stereo_on = StereoOnCommand(stereo)
    tv_on = TVOnCommand(tv)
    hottub_on = HottubOnCommand(hottub)
    light_off = LightOffCommand(light)
    stereo_off = StereoOffCommand(stereo)
    tv_off = TVOffCommand(tv)
    hottub_off = HottubOffCommand(hottub)

    party_on = {light_on, stereo_on, tv_on, hottub_on}
    party_off = {light_off, stereo_off, tv_off, hottub_off}

    party_on_macro = MacroCommand(party_on)
    party_off_macro = MacroCommand(party_off)

    remote_control.set_command(0, party_on_macro, party_off_macro)

    print remote_control
    print "--- Pushing Macro On---"  
    remote_control.on_button_was_pushed(0)
    print "--- Pushing Macro Off---" 
    remote_control.off_button_was_pushed(0)
