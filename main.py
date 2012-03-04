import curses
import os
import time

import display

FREETDS = 'FreeTDS'

class App():
    def __init__(self):
        pass

    def main(self):
        window = display.Window()

# run the check to see if we are running standalone or as an import
if __name__ == "__main__":
    app = App()
    app.main()
