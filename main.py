import json
import os

config = None

# opens config.json and saves it to a variable
with open('config.json') as f:
    config = json.load(f)

gesture = "3_fingers"
script = config["gestures"][gesture]["action"]
# print(script)
os.system(script)
