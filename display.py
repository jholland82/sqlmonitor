import curses

class Window():
    def __init__(self):
        self.initscr()
        key = self.screen.getch()
        self.screen.addstr(5, 5, str(key))
        self.screen.refresh()
        self.screen.getch()
        self.endwin()

    def initscr(self):
        self.screen = curses.initscr()

    def endwin(self):
        curses.endwin()
