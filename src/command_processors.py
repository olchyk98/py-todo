from constants import TASK_MAX_LENGTH
import string
from readchar import readkey

ERR_INVALID_TODO_ID = "Invalid todo id"

def process_stdin():
    command = input("> ");
    
    if("!" not in command):
        return ({
            "is_command": False,
            "content": command
        })
    else:
        return ({
            "is_command": True,
            "content": command
        })

def process_command(state, display_screen):
        cinfo = process_stdin()
        
        validContent = False
        for letter in cinfo["content"]:
            if(letter in string.printable):
                validContent = True
                break
        
        if(not validContent):
            return display_screen(state, "Cannot create an empty task.")
    
        fnerror = None
    
        if(cinfo["is_command"]):
            #
            args = cinfo["content"].split(" ")
            head = args.pop(0)
            #
            if(head not in commandsManager.getHeads()):
                # Create a error message
                error_str = "Invalid command: '%s' | Type '!?' to get help..." % (
                    head
                )
                # Display all tasks and prompt again & break the function
                return display_screen(state, error_str)
            fnerror = commandsManager.getCommandBody(head)['executor'](args, state)
            pass
        else: # Add a new task
            contentlen = len(cinfo["content"])
            
            if(contentlen > TASK_MAX_LENGTH):
                # Create a error message
                error_str = "Task is too log. The content should be at least %s characters shorter" % (
                    TASK_MAX_LENGTH - contentlen
                )
                # Display all tasks and prompt again & break the function
                return display_screen(state, error_str)
            
            state.add_task(cinfo["content"])
        
        display_screen(state, fnerror)
#------------------------------------------------------------------#

def display_help(args, state):
    commands = commandsManager.getCommands()
    
    for item in commands:
        print("%s : %s" % (item['callers'][0], item['description']))
        for caller in item['callers']:
            print(' - %s' % caller)
            
    print("Press any key to continue...")
    readkey()

def display_screen(args, state):
    # DO NOT IMPLEMENT
    # process_command() function executes display_utils.display_screen() after command_processors.display_screen()
    pass

def delete_task(args, state):
    if(len(args) == 0): return "You should pass the [id] argument"
    
    try:
        index = int(args[0]) - 1
    except:
        return ERR_INVALID_TODO_ID
    
    err = state.remove_task(index)
    
    if(err): return err
    
def edit_task(args, state):
    if(len(args) == 0): return "You should pass the [id] argument"
    
    try:
        index = int(args[0]) - 1
    except:
        return ERR_INVALID_TODO_ID
    
    if(len(state.getState()['tasks']) - 1 < index):
        return ERR_INVALID_TODO_ID

    content = input("New name: ")
    contentlen = len(content)
            
    if(contentlen > TASK_MAX_LENGTH):
        return "Task is too log. The content should be at least %s characters shorter" % (
            TASK_MAX_LENGTH - contentlen
        )
    
    err = state.edit_task(index, content)
    
    if(err): return err
    

#------------------------------------------------------------------#

class CommandsManager():
    def __init__(self):
        self.commands = [
            {
                "executor": display_screen,
                "callers": [
                    "!see",
                    "!list",
                    "!todo",
                    "!tasks"
                ],
                "description": "Displays the todo list"
            },
            {
                "executor": delete_task,
                "callers": [
                    "!del",
                    "!delete"
                ],
                "description": "Deletes a task. Takes one argument: [id]"
            },
            {
                "executor": display_help,
                "callers": [
                    "!",
                    "!?",
                    "!help"
                ],
                "description": "Display this list of commands"
            },
            {
                "executor": edit_task,
                "callers": [
                    "!ed",
                    "!edit"
                ],
                "description": "Opens an input field, so you will be able to change a task name. Takes one argument: [id]"
            }
        ]
        
    def getCommands(self):
        return self.commands
        
    def getHeads(self):
        commands = [];
    
        for item in self.commands:
            commands = [
                *commands,
                *item["callers"]
            ]
        
        return commands
    
    def getCommandBody(self, head):
        body = None
        
        for item in self.commands:
            if(head in item['callers']):
                body = item
                break
        
        if(not body):
            raise Exception("Internal Program Error. Please, repport the incident")
        return body
        
commandsManager = CommandsManager()