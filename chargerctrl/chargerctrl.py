__author__ = 'srodgers'

"""
Created by Steve Rodgers on 2015-05-15.
Copyright 2015 Steve Rodgers <steveatrodgers619dotcom>

This is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this code.  If not, see <http://www.gnu.org/licenses/>.
"""

import struct
import time

class chargerctrl :


    def __init__(self, i2c_object, charger_addr = 0x08):
        self.i2c = i2c_object
        self.addr = charger_addr

    # Wait for data to become ready
    def _wait_ready(self):
        time.sleep(0.001)

    # Send a command to a slave

    def send_command(self, command):
        self.i2c.send_start_bit()
        stat = self.i2c.bulk_trans(2, [self.addr << 1, command])
        self.i2c.send_stop_bit()
        if stat[0] == chr(0x01):
            raise IOError, "I2C write command on address 0x%02x not acknowledged!"%(self.addr)


    # Return a string containing the i2c response bytes

    def read_response(self):
        result = ''
        self.i2c.send_start_bit()
        stat = self.i2c.bulk_trans(1, [self.addr << 1 | 1])
        if stat[0] == chr(0x01):
            raise IOError, "I2C read command on address 0x%02x not acknowledged!"%(self.addr)
        command = ord(self.i2c.read_byte())
        self.i2c.send_ack()
        length = ord(self.i2c.read_byte())
        self.i2c.send_ack()
        count = 0
        while(length):
            result = result + self.i2c.read_byte()
            count += 1
            if(count == length):
                self.i2c.send_nack()
                break
            else:
                self.i2c.send_ack()
        self.i2c.send_stop_bit()
        return result

    # Enter calibration mode

    def cal_mode_enter(self):
        self.send_command(1)

    # Write calibration data to eeprom and exit

    def cal_mode_write_exit(self):
        self.send_command(2)


    # Exit calibration mode

    def cal_mode_exit(self):
        self.send_command(3)


    # Start pv cal

    def cal_pv_start(self):
        self.send_command(4)


    # Start batt cal

    def cal_batt_start(self):
        self.send_command(5)


    # Return true if busy

    def cal_busy(self):
        self.send_command(6)
        self._wait_ready();
        result = self.read_response()
        if(ord(result[0])):
            return True
        else:
            return False


    # Return calibration data

    def get_cal(self):
        fields = 'pv', 'batt'
        self.send_command(7)
        self._wait_ready()
        response = self.read_response()
        values = struct.unpack('<HH', response)
        result = dict(zip(fields, values))
        return result

    # Return sensor data

    def get_sensors(self):

        fields = 'pvmv','battmv','convma','loadma','battemp','convenergymwh','battchargemah','battdischargemah'
        self.send_command(10)
        self._wait_ready()
        response = self.read_response()
        values = struct.unpack('<HHHHHHHH', response)
        result = dict(zip(fields, values))
        return result


    def get_conv_info(self):
        info = {}
        fields = 'state','servocurrentstate','pwm','pwmmaxpower','calibrate',\
                 'maxpower','tempoffset','endbulkmv','endabsorbmv','gassingmv','floatholdmv','maxpowermv','fgload'

        self.send_command(12)
        self._wait_ready()
        response = self.read_response()
        values = struct.unpack('<BBBBBIhHHHHHH', response)
        result = dict(zip(fields, values))
        return result

    def reset_energy(self):
        self.send_command(13)

    def reset_charge(self):
        self.send_command(14)

    def reset_discharge(self):
        self.send_command(15)
