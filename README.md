# MacroPadTest
Testing for the external macro pad applications for FRC 2023 robot

**!IMPORTANT!** pyvjoy.py script requires vjoy to be installed. This is known to cause issues with windows controller management so do not install on any computer that needs flawless controller usage.


## How to Set Up VJOY

**1.** Download vjoy from [here](https://sourceforge.net/projects/vjoystick/) and install


**2.** open vjoy configurer

![image](https://user-images.githubusercontent.com/105398626/229634940-c4194835-f7cf-4d9e-abb6-da7c05b3a34c.png)


**3.** Navigate to tab 3 (the vjoy that the script uses by default) and click "add device". Then change setting to match the image below

![image](https://user-images.githubusercontent.com/105398626/229635728-6c18eb84-a23a-498d-9a57-049c3938dfda.png)


You should be ready to go, if you change the vjoy used in the script (`pyvjoy.VJoyDevice(x)`), make sure that it is added in the configurer and has all inputs that are used enabled.

---

## Adding Keystrokes to Joystick
If there are extra keys that you would like to utilize on the keypad or keyboard, it is very simple to set up another vjoy bind.

**1.** Find the key id by running the script and pressing the key you want to bind. If the key is recognized by python, the key id will be printed in the terminal. It might be a letter, a number, a set of words, or other. Whatever is printed on the terminal when the key is pressed is the id you must use for that key.

**2.** copy or remake an if statement using this format found in the on_press function:
```
if str(key) == '<key id>':
            j.reset_buttons()
            j.set_button(<your vjoy button>, <on(1) or off(0)>)
```

---

This project uses VGamePad for joystick emulation. View its documentation in their [repository](https://github.com/yannbouteiller/vgamepad)
