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

def ColoredPrint(string, TextColor, BackgroundColor):
    print(TextColor, BackgroundColor)
    string = "\033[1;" + str(TextColor) + ';' + str(BackgroundColor) + 'm ' + string
    print(string)
