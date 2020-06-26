import time
from datetime import datetime
from command_processors import process_command
from clear_screen import clear as clear_console
import os

DAY_IN_MILLS = 24 * 60 * 60 * 1000 # 86400000

def unix_to_date(unix = int(time.time())):
    now = int(time.time())
    
    if(now - unix <= DAY_IN_MILLS): # Today at []
        return "Today at %s" % (
            time.strftime("%H:%M", time.gmtime(unix))
        )
    else:
        value = datetime.fromtimestamp(unix)
        t = value.strftime('%d %B %Y %H:%M:%S')
        return t

def clear_screen():
    clear_console()

def display_todo(state):
    todo = state.getState()["tasks"]
    
    for index in range(len(todo)):
        item = todo[index]
        
        print(
            '%s: "%s" - %s' % (
                index + 1, item["message"], unix_to_date(item["created_at"])
            )
        )            

def setConsoleCursor(y, x):
    print("\033[%d;%dH" % (int(y), int(x)))
    
def getConsoleDims():
    height, width = os.popen('stty size', 'r').read().split()
    
    return (
        int(width),
        int(height) - 1
    )

def display_inputbox(state, error = None):
    cdims = getConsoleDims()
    
    if(error != None):
        setConsoleCursor(cdims[1] - 1, 0)
        print("Error: %s" % error)
    #
    setConsoleCursor(
        cdims[1],
        0
    )
    #
    process_command(state, display_screen)

def display_screen(state, error = None):
    clear_screen()
    display_todo(state)
    # Print a break between the list and the input prompt # TODO: Display prompt on the last line of the terminal window
    # Display an error above the input prompt
    display_inputbox(state, error)