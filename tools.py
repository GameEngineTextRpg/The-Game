import os
import sys

# menu to display stuffs
class menu (object):

    # initializes the menu
    def __init__ (self, items):
        self.items = items

    # displays the menu until the user inputs something valid
    def disp (self):
        while True:
            clear()
            for item in self.items:
                print '- ' + item
            selectedInput = raw_input('> ')
            if selectedInput in self.items:
                return selectedInput 

# clears the screen
def clear ():
    os.system('clear')

# prints the raw text without a newline, like printf
def printRaw (text):
    sys.stdout.write(text)

# all y'alls custom text yeehawww
class custom_text (object):
    esc = '\033'
    off = esc + '[0m' 

class t (custom_text):
    esc = '\033'
    bold = esc + '[1m'
    blink = esc + '[5m'

class c (custom_text):
    esc = '\033'
    black = esc + '[30m'
    red = esc + '[31m'
    green = esc + '[32m'
    yellow = esc + '[33m' 
    blue = esc + '[34m'
    magenta = esc + '[35m'
    cyan = esc + '[36m'
    white = esc + '[37m'

class h (custom_text): 
    esc = '\033'
    black = esc + '[40m'
    red = esc + '[41m'
    green = esc + '[42m'
    yellow = esc + '[43m' 
    blue = esc + '[44m'
    magenta = esc + '[45m'
    cyan = esc + '[46m'
    white = esc + '[47m'
