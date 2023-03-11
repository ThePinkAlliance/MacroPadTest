import ntcore
from pynput import keyboard


class Example:

    dblTopic = None

    def __init__(self, dblTopic: ntcore.DoubleTopic):

        self.dblTopic = dblTopic

    def periodic(self):

        dblPub = self.dblTopic.publish()

        def on_press(key):
            try:
                #keys (including numlock failsafe)
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

            ###self.dblPub.set(2.0, 0)  # 0 = use current time

            # publish a value with a specific timestamp with microsecond resolution.
            # On the roboRIO, this is the same as the FPGA timestamp (e.g.
            # RobotController.getFPGATime())
            ###self.dblPub.set(3.0, ntcore._now())

    # often not required in robot code, unless this class doesn't exist for
    # the lifetime of the entire robot program, in which case close() needs to be
    # called to stop publishing
    ###def close(self):
        # stop publishing
        ###dblPub.close()

if __name__ == "__main__":
    inst = ntcore.NetworkTableInstance.getDefault()
    table = inst.getTable("datatable")
    ###xSub = table.getDoubleTopic("GridTarget").subscribe(0)
    ###ySub = table.getDoubleTopic("y").subscribe(0)# start publishing; the return value must be retained (in this case, via
       
    inst.startClient4("example client")
    inst.setServerTeam(233) # where TEAM=190, 294, etc, or use inst.setServer("hostname") or similar
    inst.startDSClient() # recommended if running on DS computer; this gets the robot IP from the DS
     # an instance variable)


    # get a topic from a NetworkTableInstance
    # the topic name in this case is the full name
    dblTopic = inst.getDoubleTopic("/datatable/CUI")

    # start publishing; the return value must be retained (in this case, via
    # an instance variable)
    ###dblPub = dblTopic.publish()
    myExample = Example(dblTopic=dblTopic)
    myExample.periodic()
