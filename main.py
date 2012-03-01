import colorama
import curses
import os
import time
from colorama import Fore, Back, Style

import display

FREETDS = 'FreeTDS'

class App():
    def __init__(self):
        pass

    def main(self):
        window = display.Window()
        colorama.init(autoreset=True)
        print Fore.BLUE + "Testing"


if __name__ == "__main__":
    app = App()
    app.main()
