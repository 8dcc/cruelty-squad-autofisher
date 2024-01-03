#!/usr/bin/python

# Usage: https://github.com/8dcc/cruelty-squad-autofisher

import time
import keyboard
from pymouse import PyMouse
from PIL import Image, ImageGrab

# Seconds, accepts decimals
ROD_HOLD_DELAY = 1

def has_fishing_bubble(x, y):
    bbox = (x, y, x + 1, y + 1)
    grab = ImageGrab.grab(bbox=bbox)
    rgb  = grab.convert("RGB")
    r, g, b = rgb.getpixel((0, 0))

    # If you are fishing in darkworkd with the Night Vision Goggles, use this:
    # return r != 0 or g != 0 or b != 0

    # The texture for the fishing bubbles goes from #406000 to #101000
    return r != 0 and g != 0 and b == 0


def main():
    m = PyMouse()

    print("Pause the game and move the mouse where the green bubbles will appear.")
    print("Getting position in 5 seconds...")
    time.sleep(5)

    # Exit pause
    keyboard.press("ESC")

    x_pos, y_pos = m.position()
    print("Unpause the game.")
    print(f"Starting in 5 seconds at position: ({x_pos}, {y_pos})")
    time.sleep(5)

    print(f"Toggle the autofisher by holding F4 for more than {ROD_HOLD_DELAY} seconds.")

    try:
        paused = False
        while True:
            if keyboard.is_pressed("F4"):
                paused = not paused
                print("Pausing..." if paused else "Resuming...")
                time.sleep(0.5)

            # Scan for bubbles
            if not paused and has_fishing_bubble(x_pos, y_pos):
                x, y = m.position()
                m.press(x, y)

                # Hold for N seconds
                time.sleep(ROD_HOLD_DELAY)

                x, y = m.position()
                m.release(x, y)
    except KeyboardInterrupt:
        print("\rCtrl-C detected. Exiting...")

if __name__ == '__main__':
    main()
