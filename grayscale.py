#!/usr/bin/python

# Usage: https://github.com/8dcc/cruelty-squad-autofisher

import time
import keyboard
from pymouse import PyMouse
from PIL import Image, ImageGrab

# Seconds, accepts decimals
ROD_HOLD_DELAY = 1

def is_black(x, y):
    bbox = (x, y, x + 1, y + 1)
    grab = ImageGrab.grab(bbox=bbox)
    rgb  = grab.convert("RGB")
    r, g, b = rgb.getpixel((0, 0))
    return r == 0 and g == 0 and b == 0

def main():
    m = PyMouse()

    print("Getting position in 5 seconds, pause the game and move the mouse to a black area.")
    time.sleep(5)

    # Exit pause
    keyboard.press("ESC")

    x_pos, y_pos = m.position()
    print(f"Unpause the game. Starting in 3 seconds at position: ({x_pos}, {y_pos})")
    print(f"Quit by holding F4 for more than {ROD_HOLD_DELAY} seconds.")
    time.sleep(3)

    while not keyboard.is_pressed("F4"):
        # Scan for bubbles
        if not is_black(x_pos, y_pos):
            x, y = m.position()
            m.press(x, y)

            # Hold for N seconds
            time.sleep(ROD_HOLD_DELAY)

            x, y = m.position()
            m.release(x, y)

if __name__ == '__main__':
    main()
