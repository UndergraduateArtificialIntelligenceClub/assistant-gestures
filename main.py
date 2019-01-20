import json
import os
# import pynput
from pynput.keyboard import Key, Controller

config = None

# opens config.json and saves it to a variable
with open('config.json') as f:
    config = json.load(f)["gestures"]

gesture = "2_fingers"

# type = config[gesture]["type"]
type = "media"

if (type == "script"):
    script = config[gesture]["action"]
    os.system(script)
elif (type == "python"):
    python_path = config[gesture]["action"]
    os.system("python " + "'" + python_path + "'")
elif (type == 'media'):
    keyboard = Controller()
    print(keyboard)
