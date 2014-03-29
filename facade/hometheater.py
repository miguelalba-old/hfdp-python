"""
Home Theater facade

Author: m1ge7
Date: 2014/03/29
"""

class Amplifier:

    def __init__(self, description):
        self._description = description
        self._tuner = None
        self._dvd_player = None
        self._cd_player = None

    def on(self):
        print self._description + " on"

    def off(self):
        print self._description + " off"

    def set_stereo_sound(self):
        print self._description + " stereo mode on"

    def set_surround_sound(self):
        print(self._description + " surround sound on "
              "(5 speakers, 1 subwoofer)")

    def set_volume(self, level):
        print self._description + " setting volume to " + str(level)

    def set_tuner(self, tuner):
        print self._description + " setting tuner to " + tuner
        self._tuner = tuner

    def set_dvd(self, dvd):
        print self._description + " setting DVD player to " + str(dvd)
        self._dvd_player = dvd

    def set_cd(self, cd):
        print self._description + " setting CD player to " + cd
        self._cd_player = cd

    def __str__(self):
        return self._description


class CdPlayer:

    def __init__(self, description, amplifier):
        self._description = description
        self._amplifier = amplifier
        self._current_track = None
        self._title = None

    def on(self):
        print self._description + " on"

    def off(self):
        print self._description + " off"

    def eject(self):
        self._title = None
        print self._description + " eject"

    def play_title(self, title):
        self._title = title
        self._current_track = 0
        print self._description + ' playing "' + self._title + '"'

    def play_track(self, track):
        if self._title is None:
            print(self._description + " can't play track " +
                  self._current_track + ", no cd inserted")
        else:
            self._current_track = track
            print self._description + " playing track " + self._current_track

    def stop(self):
        self._current_track = 0
        print self._description + " stopped"

    def pause(self):
        print self._description + ' paused "' + self._title + '"'

    def __str__(self):
        return self._description


class DvdPlayer:

    def __init__(self, description, amplifier):
        self._description = description
        self._amplifier = amplifier
        self._current_track = None
        self._movie = None

    def on(self):
        print self._description + " on"

    def off(self):
        print self._description + " off"

    def eject(self):
        print self._description + " eject"

    def play_movie(self, movie):
        self._movie = movie
        self._current_track = 0
        print self._description + ' playing "' + self._movie + '"'

    def play_track(self, track):
        if self._movie is None:
            print(self._description + " can't play track " + track +
                  " no dvd inserted")
        else:
            self._current_track = track
            print(self._description + " playing track " + self._current_track +
                  ' of "' + self._movie + '"')

    def stop(self):
        self._current_track = 0
        print self._description + ' stopped "' + self._movie + '"'

    def pause(self):
        print self._description + ' paused "' + self._movie + '"'

    def set_two_channel_audio(self):
        print self._description + " set two channel audio"

    def set_surround_audio(self):
        print self._description + " set surround audio"

    def __str__(self):
        return self._description


class HomeTheatherFacade:

    def __init__(self, amp, tuner, dvd, cd, projector, screen, lights, popper):
        self._amp = amp
        self._tuner = tuner
        self._dvd = dvd
        self._cd = cd
        self._projector = projector
        self._screen = screen
        self._lights = lights
        self._popper = popper

    def watch_movie(self, movie):
        print "Get ready to watch a movie..."

        self._popper.on()
        self._popper.pop()

        self._lights.dim(10)

        self._screen.down()

        self._projector.on()
        self._projector.wide_screen_mode()

        self._amp.on()
        self._amp.set_dvd(self._dvd)
        self._amp.set_surround_sound()
        self._amp.set_volume(5)

        self._dvd.on()
        self._dvd.play_movie(movie)

    def end_movie(self):
        print "Shutting movie theater down..."

        self._popper.off()
        self._lights.on()
        self._screen.up()
        self._projector.off()
        self._amp.off()
        self._dvd.stop()
        self._dvd.eject()
        self._dvd.off()

    def listen_to_cd(self, cd_title):
        print "Get ready for an audiopile experence..."

        self._lights.on()
        self._amp.on()
        self._amp.set_volume(5)
        self._amp.set_stereo_sound()
        self._cd.on()
        self._cd.play(cd_title)

    def end_cd(self):
        print "Shutting down CD..."
        self._amp.off()
        self._amp.set_cd(self._cd)
        self._cd.eject()
        self._cd.off()

    def listen_to_radio(self, frequency):
        print "Tuning in the airwaves..."

        self._tuner.on()
        self._tuner.set_frequency(frequency)
        self._amp.on()
        self._amp.set_volume(5)
        self._amp.set_tuner(self._tuner)

    def end_radio(self):
        print "Shutting down the tuner..."
        self._tuner.off()
        self._amp.off()


class PopcornPopper:

    def __init__(self, description):
        self._description = description

    def on(self):
        print self._description + " on"

    def off(self):
        print self._description + " off"

    def pop(self):
        print self._description + " popping popcorn!"

    def __str__(self):
        return self._description


class Projector:

    def __init__(self, description, dvd_player):
        self._description = description
        self._dvd_player = dvd_player

    def on(self):
        print self._description + " on"

    def off(self):
        print self._description + " off"

    def wide_screen_mode(self):
        print self._description + " in widescreen mode (16x9 aspect ratio)"

    def tv_move(self):
        print self._description + " in tv mode (4x3 aspect ratio)"

    def __str__(self):
        return self._description


class Screen:

    def __init__(self, description):
        self._description = description

    def up(self):
        print self._description + " going up"

    def down(self):
        print self._description + " going down"

    def __str__(self):
        return self._description


class TheaterLights:

    def __init__(self, description):
        self._description = description

    def on(self):
        print self._description + " on"

    def off(self):
        print self._description + " off"

    def dim(self, level):
        print self._description + " dimming to " + str(level) + " %"

    def __str__(self):
        return self._description


class Tuner:

    def __init__(self, description, amplifier):
        self._description = description
        self._frequency = None
        self._amplifier = amplifier

    def on(self):
        print self._description + " on"

    def off(self):
        print self._description + " off"

    def set_frequency(self, frequency):
        print self._description + " setting frequency to " + frequency
        self._frequency = frequency

    def set_am(self):
        print self._description + " setting AM mode"

    def set_fm(self):
        print self._description + " setting FM mode"

    def __str__(self):
        return self._description


if __name__ == '__main__':
    # Home Theater Test Drive
    AMP = Amplifier("Top-O-Line Amplifier")
    TUNER = Tuner("Top-O-Line AM/FM Tuner", AMP)
    DVD = DvdPlayer("Top-O-Line DVD Player", AMP)
    CD = CdPlayer("Top-O-Line CD Player", AMP)
    PROJECTOR = Projector("Top-O-Line Projector", DVD)
    LIGHTS = TheaterLights("Theater Ceiling Lights")
    SCREEN = Screen("Theater Screen")
    POPPER = PopcornPopper("Popcorn Popper")

    HOME_THEATER = HomeTheatherFacade(AMP, TUNER, DVD, CD, PROJECTOR, SCREEN,
                                      LIGHTS, POPPER)

    HOME_THEATER.watch_movie("Raiders of the Lost Ark")
    HOME_THEATER.end_movie()
