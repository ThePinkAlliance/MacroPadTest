import vgamepad as vg
import time
from pynput import keyboard # for keyboard capture

# set the virtual joystick we will emulating inputs on to be vjoy #3
gamepad = vg.VX360Gamepad()

# function to reset all previously on inputs to off
def resetGP():
    # restart funtions
    None
    gamepad.reset()

def updateGP():
    gamepad.update()

# when any key is pressed
def on_press(key):
    try:
        key = str(key).replace("'", "")
        print(key)
        # keypad to vjoy emulation (including numlock failsafe)
        
        if str(key) == '<98>' or str(key) == 'Key.down':
            #--num2--
            resetGP()
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
            updateGP()
            print("|| vgp button A pressed")
        
        if str(key) == '<100>' or str(key) == 'Key.left':
            #--num4--
            resetGP()
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
            updateGP()
            print("|| vgp button X pressed")

        if str(key) == '<102>' or str(key) == 'Key.right':
            #--num6--
            resetGP()
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
            updateGP()
            print("|| vgp button B pressed")

        if str(key) == '<104>' or str(key) == 'Key.up':
            #--num8--
            resetGP()
            gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
            updateGP()
            print("|| vgp button Y pressed")

    
    # notify when a key not recognized by python is pressed
    except AttributeError:
        print('special key {0} pressed'.format(key))

# failsafe, stops listener when esc key is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        return False

resetGP()
# initiate listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

gamepad = vg.VX360Gamepad()

gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()
time.sleep(10)
gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
gamepad.update()