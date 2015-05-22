__author__ = 'srodgers'

import tkinter.ttk as ttk
from tkinter import *
import tkinter.messagebox

from chargerctrl.I2C import *
from chargerctrl.chargerctrl import *
from chargerctrl.chargerstatus import *
from chargerctrl.fullscreen import *
from chargerctrl.serialselect import *


port = None
i2c = None
cc = None
root = None

#
# Select the serial port

def setSerial():
    global port
    global i2c
    global cc

    while(True):
        ss = SerialSelect(root, 'Select Serial Port', udevportname='buspirate')
        port = ss.port()
        if(port is not None):
            break
    i2c = I2C(port, 115200)
    if i2c.BBmode():
        pass
    else:
        tkinter.messagebox.showerror("Can't set binmode on Buspirate!")
        sys.exit(1)
    if i2c.enter_I2C():
        pass
    else:
        tkinter.messagebox.showerror("Can't set raw mode on Buspirate!")
        sys.exit(1)
    print("Configuring I2C.")
    if not i2c.cfg_pins(I2CPins.POWER | I2CPins.PULLUPS):
        tkinter.messagebox.showerror("Failed to set I2C peripherals on BusPirate!")
        sys.exit(1)
    if not i2c.set_speed(I2CSpeed._50KHZ):
        tkinter.messagebox.showerror("Can't set I2C speed on Buspirate!")
        sys.exit(1)
    i2c.timeout(0.2)

    cc = chargerctrl(i2c)

#
# Show charger status

def viewChargerStatus():
    global root
    cs = ChargerStatus(root, cc)


#
# Run calibration

def runCalibration():
    pass;

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

    runmenu = Menu(menubar, tearoff = 0)
    runmenu.add_command(label="Perform Calibration", command=runCalibration)
    menubar.add_cascade(label="Run", menu=runmenu)
    # display the menu
    root.config(menu=menubar)

    if(port is None):
        setSerial()



    root.mainloop()










