import sys
from .spinner import Spinner
from .color import Color


class Phaser:
    def __init__(self, phase=0, text=""):
        self.phase_text = text
        self.phase_number = phase
        self.spinner = Spinner()

    def start(self):
        sys.stdout.write(Color.BOLD + Color.YELLOW +
                         f"[{self.phase_number}]" + Color.END + " " +
                         self.phase_text + "...  ")
        self.spinner.start()

    def end(self, error=None):
        self.spinner.stop()
        if error:
            sys.stdout.write(Color.BOLD + Color.RED + f"ERROR: [{error}]" + Color.END + "\n")
        else:
            sys.stdout.write(Color.BOLD + Color.GREEN + "OK" + Color.END + '\n')
