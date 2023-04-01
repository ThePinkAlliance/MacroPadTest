import ntcore
from pynput import keyboard
import pygetwindow
import threading
import customtkinter

class ApplicationGUI:
    def __init__(self):
        super().__init__()

        self.title("minimal example app")
        self.minsize(400, 300)

        self.button = customtkinter.CTkButton(master=self, command=self.button_callback)
        self.button.pack(padx=20, pady=20)

class Example:

    dblTopic = None

    def __init__(self, dblTopic: ntcore.DoubleTopic):

        self.dblTopic = dblTopic

    def periodic(self):

        dblPub = self.dblTopic.publish()

        currentWin = pygetwindow.getActiveWindow().title
        print(currentWin)
        if currentWin == 'Shuffleboard':
            print("shuffleboard is active")

        def on_press(key):

            currentWin = pygetwindow.getActiveWindow().title
            print(currentWin)
            if currentWin == 'Shuffleboard':
                print("shuffleboard is active")
            

            try:
                # keys (including numlock failsafe)
                if str(key) == '<96>' or str(key) == 'Key.insert':
                    print("0")
                    dblPub.set(0)
                if str(key) == '<97>' or str(key) == 'Key.end':
                    print("1")
                    dblPub.set(1)
                if str(key) == '<98>' or str(key) == 'Key.down':
                    print("2")
                    dblPub.set(2)
                if str(key) == '<99>' or str(key) == 'Key.page_down':
                    print("3")
                    dblPub.set(3)
                if str(key) == '<100>' or str(key) == 'Key.left':
                    print("4")
                    dblPub.set(4)
                if str(key) == '<101>' or str(key) == '<12>':
                    print("5")
                    dblPub.set(5)
                if str(key) == '<102>' or str(key) == 'Key.right':
                    print("6")
                    dblPub.set(6)
                if str(key) == '<103>' or str(key) == 'Key.home':
                    print("7")
                    dblPub.set(7)
                if str(key) == '<104>' or str(key) == 'Key.up':
                    print("8")
                    dblPub.set(8)
                if str(key) == '<105>' or str(key) == 'Key.page_up':
                    print("9")
                    dblPub.set(9)

            except AttributeError:
                print('special key {0} pressed'.format(key))

        def on_release(key):
            if key == keyboard.Key.esc:
                return False

        # Collect events until released
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()

if __name__ == "__main__":
    inst = ntcore.NetworkTableInstance.getDefault()
    table = inst.getTable("datatable")
       
    inst.startClient4("example client")
    inst.setServerTeam(233)
    inst.startDSClient()


    # get a topic from a NetworkTableInstance
    # the topic name in this case is the full name
    dblTopic = inst.getDoubleTopic("/datatable/CUI")

    # start publishing; the return value must be retained (in this case, via
    # an instance variable)
    ###dblPub = dblTopic.publish()
    myExample = Example(dblTopic=dblTopic)
    myExample.periodic()
    
    app = ApplicationGUI()
    app.mainloop()
