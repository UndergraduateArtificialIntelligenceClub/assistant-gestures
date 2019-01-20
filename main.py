import json
import os
import time
from pynput.keyboard import Key, Controller

config = None

# opens config.json and saves it to a variable
with open('config.json') as f:
    config = json.load(f)["gestures"]

gesture = "2_fingers"

type = config[gesture]["type"]


def convertKey(arg):
    if (arg == "alt"):
        return Key.alt
    elif (arg == "ctrl"):
        return Key.ctrl
    elif (arg == "cmd" or arg == "windows" or arg == "super"):
        return Key.cmd
    elif (arg == "shift"):
        return Key.shift
    elif (arg == "tab"):
        return Key.tab
    elif (arg == "enter"):
        return Key.enter
    elif (arg == "PLUS"):
        return "+"
    elif (arg == "backspace"):
        return Key.backspace
    elif (arg == "caps_lock"):
        return Key.caps_lock
    elif (arg == "delete"):
        return Key.delete
    elif (arg == "end"):
        return Key.end
    elif (arg == "down"):
        return Key.down
    elif (arg == "up"):
        return Key.up
    elif (arg == "esc"):
        return Key.esc
    elif (arg == "left"):
        return Key.left
    elif (arg == "right"):
        return Key.right
    elif (arg == "page_down"):
        return Key.page_down
    elif (arg == "page_up"):
        return Key.page_up
    elif (arg == "print_screen"):
        return Key.print_screen
    elif (arg == "menu"):
        return Key.menu
    elif (arg == "f1"):
        return Key.f1
    elif (arg == "f2"):
        return Key.f2
    elif (arg == "f3"):
        return Key.f3
    elif (arg == "f4"):
        return Key.f4
    elif (arg == "f5"):
        return Key.f5
    elif (arg == "f6"):
        return Key.f6
    elif (arg == "f7"):
        return Key.f7
    elif (arg == "f8"):
        return Key.f8
    elif (arg == "f9"):
        return Key.f1
    elif (arg == "f10"):
        return Key.f10
    elif (arg == "f11"):
        return Key.f11
    elif (arg == "f12"):
        return Key.f12
    return arg


if (type == "script"):
    script = config[gesture]["action"]
    os.system(script)
elif (type == "python"):
    python_path = config[gesture]["action"]
    os.system("python " + "'" + python_path + "'")
elif (type == 'media'):
    keyboard_stroke = config[gesture]["action"].split('+')
    print(keyboard_stroke)
    keyboard = Controller()
    keyboard_stroke = [convertKey(k) for k in keyboard_stroke]
    time.sleep(5)
    for k in keyboard_stroke:
        keyboard.press(k)
    for k in reversed(keyboard_stroke):
        keyboard.release(k)
