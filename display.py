import curses
import pyodbc
import string
import time
from os import environ

LINE_Y = 3          # Default Y location to start server listing
RED = 1
GREEN = 2
BLUE = 3

class Window():
    def __init__(self):
        time_counter = 0
        self.freetds = "FreeTDS"
        ESCDELAY = 25
        self.initscr()
        self.default_refresh()
        self.screen.nodelay(1)
        self.update_servers()
        key = self.screen.getch()

        # this took a while to figure out
        # I run the getch() in the while loop
        # Immediately sleep 1 second
        # Do the logict
        # It picks up the ESC key instantly!
        while self.screen.getch() != 27:
            time.sleep(1)
            time_counter += 1
            if time_counter >= 50:
                self.update_servers()
                time_counter = 0
            self.screen.addstr(0, 0, str(time_counter), curses.color_pair(RED))
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
                curses.color_pair(BLUE))
        self.screen.refresh()

    def update_servers(self):
        self.screen.clear()
        self.check_servers()
        self.default_refresh()

    def check_servers(self):
        self.default_refresh()
        db_list = []
        file = open("db.config")
        for line in file:
            if "FreeTDS" in line:
                tds = line.strip().split('=')
                self.freetds = tds[-1]
            else:
                db_data = line.strip().split(',')
                db_list.append(db_data)
        file.close()
        self.loop_servers(db_list)
        return

    def loop_servers(self, db_list):
        line_y = LINE_Y
        for db in db_list:
            try:
                conn = pyodbc.connect('DRIVER=%s;SERVER=%s;DATABASE=%s;UID=%s;PWD=%s;TDS_VERSION=%s;PORT=%s;'
                        % (self.freetds, db[0], db[1], db[2], db[3], db[4],
                            db[5]))
                self.screen.addstr(line_y, 2, "%s:%s connected" % (db[0],
                    db[1]), curses.color_pair(GREEN))
            except:
                self.screen.addstr(line_y, 2, "Could not connect to %s:%s" %
                        (db[0], db[1]), curses.color_pair(RED))
            line_y += 1
        self.screen.refresh()

    def define_pairs(self):
        curses.start_color()
        curses.init_pair(RED, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(GREEN, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(BLUE, curses.COLOR_BLUE, curses.COLOR_BLACK)

        #wintitle = curses.newwin(10, 20, 5, 5)
        #wintitle.border(0)
        #wintitle.addstr(1, 1, "TESTING NEW WINDOW", curses.color_pair(1))
        #wintitle.refresh()

