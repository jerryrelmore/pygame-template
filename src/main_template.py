# main_template.py
# date: 7-jan-2023
# author: jelmore
# purpose: this is a pygame base template/dir structure that does nothing more than help w/ prelim repetitve setup
#    for the series of games I'm writing this year. update class GameOjb name and __main__ class 
#    calls to get started. also includes pyganim import for easy sprite animation. may update further
#    as I get through the year - or, may not. Look for # TODO: items that can be reviewed.

import os
import pygame as pg
from pygame.locals import *
import pyganim as anim

# Place window in center of user's screen
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Globals
GAME_TITLE = ""  # TODO: <- UPDATE THIS
# End Globals


class GameObj:  # TODO: <- UPDATE THIS
    def __init__(self) -> None:
        self._running = None  # Init game running bool
        self._screen = None  # Init screen surface
        self._first_run = True  # Bool if special behavior req'd on first game loop  # TODO: <- REMOVE if not needed
        self._main_clock = pg.time.Clock()  # Init game clock
        self.size, self.width, self.height = (), 0, 0

    def on_init(self) -> None:
        self._running = True  # If we're init'ing, we're running, make it so

        pg.init()  # Init all Pygame modules

        # Setup a roughly 4:3 aspect ratio
        display_info = pg.display.Info()
        self.width, self.height = int((display_info.current_h / 2) * 1.333), int(display_info.current_h / 2)
        self.size = (self.width, self.height)
        self._screen = pg.display.set_mode(self.size, pg.SHOWN | pg.RESIZABLE)

        pg.display.set_caption(GAME_TITLE)  # Set window title

        pg.key.set_repeat(50, 10)  # Setup keyboard key repeat freq (delay, interval)

        # Setup mixer
        pg.mixer.pre_init(44100, -16, 2, 512)
        pg.mixer.set_num_channels(32)

    def on_event(self, event: pg.event) -> None:
        if event.type == pg.QUIT or \
                (event.type == KEYDOWN and (
                        event.key == pg.K_ESCAPE or event.key == pg.K_q)):  # Quit if we press
            self._running = False
            # TODO: Add an "are you sure?" prompt before booting us out of the game

    def on_loop(self) -> None:
        if not self._first_run:  # TODO: <- UPDATE THIS if not needed
            # Do something if we're past first loop
            pass

    def on_render(self) -> None:
        # Erase previous screen
        self._screen.fill((0, 0, 0))

        # Update display
        pg.display.update()

    def on_cleanup(self) -> None:
        pg.quit()

    def on_game_over(self):  # -> None:  # TODO: <- UPDATE THIS if needed
        pass

    def on_execute(self) -> None:
        # Check if we're dead in the water out of the gate
        if self.on_init() is False:
            self._running = False

        while self._running:
            # Set framerate to 30 fps
            self._main_clock.tick(30)

            # Check for events
            for event in pg.event.get():
                self.on_event(event)

            # Do loop stuff
            self.on_loop()

            # Render new screen
            self.on_render()

        # Do cleanup stuff
        self.on_cleanup()


if __name__ == "__main__":
    GAMEObj = GameObj()  # TODO: <- UPDATE THIS
    GAMEObj.on_execute()  # TODO: <- UPDATE THIS
