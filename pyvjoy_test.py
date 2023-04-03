import pyvjoy # for vitual joysticks
from pynput import keyboard # for keyboard capture

# set the virtual joystick we will emulating inputs on to be vjoy #3
j = pyvjoy.VJoyDevice(3)

# function to reset all previously on inputs to off
def resetOnStart():
    j.reset_buttons()

# when any key is pressed
def on_press(key):
    try:
        print(key)
        # keypad to vjoy emulation (including numlock failsafe)
        if str(key) == '<96>' or str(key) == 'Key.insert':
            #--num0--
            j.reset_buttons()
            j.set_button(1,1)
            print("vjoy button 1 pressed")

        if str(key) == '<97>' or str(key) == 'Key.end':
            #--num1--
            j.reset_buttons()
            j.set_button(2,1)
            print("vjoy button 2 pressed")
        
        if str(key) == '<98>' or str(key) == 'Key.down':
            #--num2--
            j.reset_buttons()
            j.set_button(3,1)
            print("vjoy button 3 pressed")

        if str(key) == '<99>' or str(key) == 'Key.page_down':
            #--num3--
            j.reset_buttons()
            j.set_button(4,1)
            print("vjoy button 4 pressed")
        
        if str(key) == '<100>' or str(key) == 'Key.left':
            #--num4--
            j.reset_buttons()
            j.set_button(5,1)
            print("vjoy button 5 pressed")

        if str(key) == '<101>' or str(key) == '<12>':
            #--num5--
            j.reset_buttons()
            j.set_button(6,1)
            print("vjoy button 6 pressed")

        if str(key) == '<102>' or str(key) == 'Key.right':
            #--num6--
            j.reset_buttons()
            j.set_button(7,1)
            print("vjoy button 7 pressed")

        if str(key) == '<103>' or str(key) == 'Key.home':
            #--num7--
            j.reset_buttons()
            j.set_button(8,1)
            print("vjoy button 8 pressed")

        if str(key) == '<104>' or str(key) == 'Key.up':
            #--num8--
            j.reset_buttons()
            j.set_button(9,1)
            print("vjoy button 9 pressed")

        if str(key) == '<105>' or str(key) == 'Key.page_up':
            #--num9--
            j.reset_buttons()
            j.set_button(10,1)
            print("vjoy button 10 pressed")
    
    # notify when a key not recognized by python is pressed
    except AttributeError:
        print('special key {0} pressed'.format(key))

# failsafe, stops listener when esc key is pressed
def on_release(key):
    if key == keyboard.Key.esc:
        return False

resetOnStart()
# initiate listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()