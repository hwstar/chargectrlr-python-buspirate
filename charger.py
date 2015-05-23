#!/usr/bin/env python3
__author__ = 'srodgers'

import tkinter.messagebox

from chargerctrl.I2C import *
from chargerctrl.ChargerCtrl import *
from chargerctrl.ChargerStatus import *
from chargerctrl.FullScreen import *
from chargerctrl.SerialSelect import *
from chargerctrl.CalWizard import *
from chargerctrl.LoadEnableDialog import *


port = None
i2c = None
cc = None
root = None
idInfo = None


def fatalError(errorText):
    tkinter.messagebox.showerror("Fatal Error", errorText)
    sys.exit(1)


#
# Select the serial port

def setSerial():
    global port
    global i2c
    global cc
    global idInfo

    while(True):
        ss = SerialSelect(root, title = 'Select Serial Port', udevportname='buspirate', xoffset=200, yoffset=200)
        port = ss.port()
        if(port is not None):
            break
    i2c = I2C(port, 115200)
    if i2c.BBmode():
        pass
    else:
        fatalError("Can't set binmode on Buspirate!")

    if i2c.enter_I2C():
        pass
    else:
        fatalError("Can't set raw mode on Buspirate!")

    if not i2c.cfg_pins(I2CPins.POWER | I2CPins.PULLUPS):
        fatalError("Failed to set I2C peripherals on BusPirate!")

    if not i2c.set_speed(I2CSpeed._50KHZ):
        fatalError("Can't set I2C speed on Buspirate!")

    i2c.timeout(0.2)

    cc = chargerctrl(i2c)
    idInfo = cc.get_id_info()
    if idInfo['designer'] != "HWSTAR" or idInfo['project'] != "66-000101":
        fatalError("Project or designer ID doesn't match! Are you using the correct utility program for this board?")



#
# Show charger status

def viewChargerStatus():
    global root
    cs = ChargerStatus(root, cc, xoffset=200, yoffset=200)


#
# Run calibration

def runCalibration():
    wiz = CalWizard(root, cc, title="Calibration", xoffset=200, yoffset=200)

#
# Enable/Disable load

def enableDisableLoad():
    led = LoadEnableDialog(root, cc, title="Load Enable", xoffset=200, yoffset=200)

if __name__ == '__main__':

    root = Tk()
    app=FullScreenApp(root)

    menubar = Menu(root, tearoff = 0)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Set Serial Port", command=setSerial)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    # display the menu
    root.config(menu=menubar)

    viewmenu = Menu(menubar, tearoff = 0)
    viewmenu.add_command(label="View Charger Status", command=viewChargerStatus)
    menubar.add_cascade(label="View", menu=viewmenu)

    actionmenu = Menu(menubar, tearoff = 0)
    actionmenu.add_command(label="Enable/Disable Load", command=enableDisableLoad)
    actionmenu.add_command(label="Perform Calibration", command=runCalibration)
    menubar.add_cascade(label="Action", menu=actionmenu)
    # display the menu
    root.config(menu=menubar)

    if(port is None):
        setSerial()



    root.mainloop()










