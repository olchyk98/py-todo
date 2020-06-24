# TODO: Display tasks -> display_screen -> display_todo
# TODO: Safer Backups -> in case if the app cannot open json + file is not empty -> safe to another file and inform user about the occured error
# TODO: Implement clear_screen()

#!/bin/python3
from state_manager import StateManager
from display_utils import display_screen
from constants import STATE_FILENAME

# Validate if the application launched correctly
if __name__ != "__main__":
	raise Exception("This application file cannot be a part of another app.");
#

# Get last saved state
state = StateManager("_state.json")

# Display created tasks 

# Wait for a new command
display_screen(state)