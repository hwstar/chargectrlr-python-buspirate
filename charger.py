__author__ = 'srodgers'

from chargerctrl.I2C import *
from chargerctrl.chargerctrl import *
from chargerctrl.chargerstatus import *
from chargerctrl.fullscreen import *
from time import *
from Tkinter import *
import tkMessageBox



def yn(prompt, default = False):

    if(default is False):
        yesno = ' (y/N): '
    else:
        yesno = ' (Y/n): '

    res = raw_input(prompt + yesno)


    if(len(res) == 0):
        return default

    if(res[0] == 'Y' or res[0] == 'y'):
        return True
    else:
        return False

# Dump charge state variables until control C'd

def dump_charge_state(cc_obj):

    while(True):
        #print("Retrieve sensors")
        sensors = cc_obj.get_sensors()
        print(sensors)
        #print("Retrieve conv info")
        conv_info = cc_obj.get_conv_info()
        print(conv_info)
        print("Conv Power: {} mW".format((sensors['battmv'] * sensors['convma'])/1000))
        print("Battery {} mA".format((sensors['convma'] - sensors['loadma'])))
        print
        sleep(0.1)


# Calibrate the PV voltage

def cal_pv(cc_obj):
    cc_obj.cal_pv_start()
    while(True):
        sleep(0.1)
        if(cc_obj.cal_busy() == False):
            break
    cal = cc_obj.get_cal()



# Calibrate the battery voltage

def cal_batt(cc_obj):
    cc_obj.cal_batt_start()
    while(True):
        sleep(0.1)
        if(cc_obj.cal_busy() == False):
            break
    cal = cc_obj.get_cal()


def interactive_cal(cc_obj):
    cc_obj.cal_mode_enter()
    raw_input("Connect 6V reference to PV input, and press return")
    print "PV Cal started...",
    cal_pv(cc_obj)
    print "Done"
    raw_input("Connect 6V reference to BATT output, and press return")
    print "BATT Cal started...",
    cal_pv(cc_obj)
    print "Done"

    cal = cc_obj.get_cal()
    print('Cal PV:{} BATT:{}'.format(cal['pv'], cal['batt']))
    if(yn("Write calibration to EEPROM")):
        print "Writing calibraton to EEPROM...",
        cc_obj.cal_mode_write_exit()
        print "Done. Exiting cal"
    else:
        print "Exiting without write"
        cc_obj.cal_mode_exit()


if __name__ == '__main__':

    root = Tk()
    app=FullScreenApp(root)

    addr = 0x08
    i2c = I2C("/dev/ttyUSB1", 115200)
    print "Entering binmode: ",
    if i2c.BBmode():
        print "OK."
    else:
        raise IOError, "Binmode failed!"

    print "Entering raw I2C mode: ",
    if i2c.enter_I2C():
        print "OK."
    else:
        raise IOError, "Raw mode failed!"


    print "Configuring I2C."
    if not i2c.cfg_pins(I2CPins.POWER | I2CPins.PULLUPS):
        raise IOError, "Failed to set I2C peripherals."
    if not i2c.set_speed(I2CSpeed._50KHZ):
        raise IOError, "Failed to set I2C Speed."
    i2c.timeout(0.2)

    cc = chargerctrl(i2c)

    cs = ChargerStatus(root, cc)

    root.mainloop()










