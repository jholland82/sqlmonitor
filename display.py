import curses
import string
from os import environ


class Window():
    def __init__(self):
        ESCDELAY = 25
        self.initscr()
        self.default_refresh()
        key = self.screen.getch()
        wintitle = curses.newwin(10, 20, 5, 5)
        wintitle.border(0)
        wintitle.addstr(1, 1, "TESTING NEW WINDOW", curses.color_pair(1))
        wintitle.refresh()
        while key != 27:
            self.screen.addstr(5, 5, str(key), curses.color_pair(1))
            self.screen.refresh()
            key = self.screen.getch()
        self.endwin()

    def initscr(self):
        try:
            self.orig_ESCDELAY = environ['ESCDELAY']
        except KeyError:
            pass
        environ['ESCDELAY'] = str(25)
        self.screen = curses.initscr()
        self.y, self.x = self.screen.getmaxyx()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(1)
        curses.start_color()
        self.define_pairs()

    def endwin(self):
        curses.echo()
        curses.nocbreak()
        self.screen.keypad(0)
        curses.endwin()

    def default_refresh(self):
        self.screen.addstr(0, 0, string.center("SQL MONITOR", self.x),
                curses.color_pair(2))
        self.screen.refresh()

    def define_pairs(self):
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_BLUE, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
