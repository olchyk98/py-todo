from constants import TASK_MAX_LENGTH
import string

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
    
        if(cinfo["is_command"]):
            #
            args = cinfo["content"].split(" ")
            head = args.pop(0)
            #
            if(head not in COMMAND_PROCESSORS):
                # Create a error message
                error_str = "Invalid command: '%s' | Type '!?' to get help..." % (
                    head[:1]
                )
                # Display all tasks and prompt again & break the function
                return display_screen(state, error_str)
            COMMAND_PROCESSORS[head](args, state)
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
        
        display_screen(state)
#------------------------------------------------------------------#


# def display_help():
#     pass

def display_screen(args, state):
    # DO NOT IMPLEMENT
    # process_command() function executes display_utils.display_screen() after command_processors.display_screen()
    pass

COMMAND_PROCESSORS = {
    # Display Help
    # "!": display_help,   
    # "!?": display_help,   
    # "!help": display_help,
    
    # Refresh the list of tasks
    "!see": display_screen,
    "!list": display_screen,
    "!todo": display_screen,
    "!tasks": display_screen,
    
    # Delete a task
    # "!del": delete_task,
    # "!delete": delete_task,
    
    # Edit a task
    # "!ed": edit_task,
    # "!edit": edit_task
}