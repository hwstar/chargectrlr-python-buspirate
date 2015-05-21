__author__ = 'srodgers'

from chargerctrl.I2C import *
from chargerctrl.chargerctrl import *
from chargerctrl.chargerstatus import *
from chargerctrl.fullscreen import *
from chargerctrl.serialselect import *
from chargerctrl.Dialog import *
from tkinter import *


import os


if __name__ == '__main__':

    root = Tk()
    app=FullScreenApp(root)

    ss = SerialSelect(root,'Select Serial Port', udevportname='buspirate')
    port = ss.port()


    i2c = I2C(port, 115200)
    print ("Entering binmode: ", end='')
    if i2c.BBmode():
        print ("OK.")
    else:
        raise IOError("Binmode failed!")

    print("Entering raw I2C mode: ",end='')
    if i2c.enter_I2C():
        print ("OK.")
    else:
        raise IOError("Raw mode failed!")


    print("Configuring I2C.")
    if not i2c.cfg_pins(I2CPins.POWER | I2CPins.PULLUPS):
        raise IOError("Failed to set I2C peripherals.")
    if not i2c.set_speed(I2CSpeed._50KHZ):
        raise IOError("Failed to set I2C Speed.")
    i2c.timeout(0.2)


    cc = chargerctrl(i2c)

    cs = ChargerStatus(root, cc)


    root.mainloop()










