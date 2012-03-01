import curses

class Window():
    def __init__(self):
        self.initscr()
        key = self.screen.getch()
        self.screen.addstr(5, 5, str(key), curses.color_pair(1))
        self.screen.refresh()
        self.screen.getch()
        self.endwin()

    def initscr(self):
        self.screen = curses.initscr()
        curses.noecho()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)

    def endwin(self):
        curses.echo()
        curses.endwin()
