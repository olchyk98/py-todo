import time
from datetime import datetime
from command_processors import process_command

DAY_IN_MILLS = 24 * 60 * 60 * 1000 # 86400000

def unix_to_date(unix = time.time()):
    now = time.time()
    
    if(now - unix <= DAY_IN_MILLS): # Today at []
        return "Today at %s" % (
            time.strftime("%H:%M", time.gmtime(unix))
        )
    else:
        value = datetime.fromtimestamp(unix)
        t = value.strftime('%d %B %Y %H:%M:%S')
        return t

def clear_screen():
    # TODO
    # Implement by placing \n in each line of the terminal window
    pass

def display_todo(state):
    todo = state.getState()["tasks"]
    
    for index in range(len(todo)):
        item = todo[index]
        
        print(
            '%s: "%s" - %s' % (
                index + 1, item["message"], unix_to_date(item["created_at"])
            )
        )            

def display_screen(state, error = None):
    clear_screen()
    display_todo(state)
    # Print a break between the list and the input prompt # TODO: Display prompt on the last line of the terminal window
    print("\n\n")
    # Display an error above the input prompt
    if(error != None):
        print(error)
    #
    process_command(state, display_screen)