import json
import time
import os

def get_unixt():
    return int(time.time())

class StateManager():
    def __init__(self, fname):
        self.filename = fname
        self.state = self.load_state()
        
    def load_state(self):
        # Check if there is a saved _state file
        if(not os.path.exists(self.filename)):
            fileCIO = open(self.filename, 'w+')
            fileCIO.close()
        
        # Open the state file.
        fileIO = open(self.filename, 'r')
        file = fileIO.read()
        
        # Try to extract the json.
        try:
            state = json.loads(file)
        except:
            state = self.write_state(None)
        #
        # assert state != None
        #
        fileIO.close()
        self.state = state
        return state

    def write_state(self, state = None):
        if(state == None):
            state = {
                "tasks": [],
                "edited_at": None
            }
        
        # Update edited_at value
        state["edited_at"] = get_unixt()
        
        # Open the state file.
        file = open(self.filename, 'w')
        
        # Convert the state dictionary to a json string.
        state_str = json.dumps(state)
        
        # Write that string to the state file using newly opened IO stream.
        file.write(state_str)
        
        # Close the IO stream.
        file.close()
        
        # Return the new state
        return state
    
    def add_task(self, text):
        self.state["tasks"].append({
            "message": text,
            "created_at": get_unixt()
        })
        
        self.write_state(self.state)
    
    # Getters
    def getState(self):
        return self.state
    