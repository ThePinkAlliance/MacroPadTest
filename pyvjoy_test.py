import pyvjoy
from pynput import keyboard

j = pyvjoy.VJoyDevice(1)

def resetOnStart():
    j.reset_buttons()

def on_press(key):
    try:
        #keys (including numlock failsafe)
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

        if str(key) == '<105>' or str(key) == 'key.page_up':
            #--num9--
            j.reset_buttons()
            j.set_button(10,1)
            print("vjoy button 10 pressed")
    
    except AttributeError:
        print('special key {0} pressed'.format(key))

def on_release(key):
    if key == keyboard.Key.esc:
        return False

resetOnStart()
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()