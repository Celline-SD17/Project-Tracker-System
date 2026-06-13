import json
import os

def load_data(filename):
    if not os.path.exists(filename):
        return[]
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("No logs found. Log file does not exist.")
        return []
    
def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)