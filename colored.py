import sys
import os
import subprocess

class TextColor():
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    PURPLE = 35
    CYAN = 36
    WHITE = 37

class BackgroundColor():
    BLACK = 40
    RED = 41
    GREEN = 42
    YELLOW = 43
    BLUE = 44
    PURPLE = 45
    CYAN = 46
    WHITE = 47

def ColoredPrint(string, TextColor, BackgroundColor = BackgroundColor.BLACK, end='\n', file=sys.stdout, flush=False):
    string = "\033[1;" + str(TextColor) + ';' + str(BackgroundColor) + 'm' + string
    print(string, end=end, file=file, flush=flush)

def ClearScreen():
    # there must be some clever code, but subprocess.run("cls") and subprocess.run("clear") didn't work for me
    print("\n" * 100)
