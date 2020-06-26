# TODO: Safer Backups -> in case if the app cannot open json + file is not empty -> safe to another file and inform user about the occured error

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

# Start the loop
display_screen(state)