__author__ = 'srodgers'

"""
    This file is part of chargectrl-python-buspirate.

    chargectrl-python-buspirate is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    chargectrl-python-buspirate is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with chargectrl-python-buspirate.  If not, see <http://www.gnu.org/licenses/>.

"""

import glob
import serial
from .Dialog import *


class SerialSelect(Dialog):

    def __init__(self, parent, title="Select Serial Port", udevportname='', xoffset=50, yoffset=50):
        self.sindex=0
        self.rbuttons = []
        self.udevportname = udevportname
        self.ports= self._serial_ports(udevportname)
        Dialog.__init__(self, parent, title=title, xoffset=xoffset, yoffset=yoffset)

    def body(self, master):
        self.rbvar = IntVar()
        selected = 0

        for index, port in enumerate(self.ports):
            self.rbuttons.append(Radiobutton(master, text=port, variable=self.rbvar, value=index, command=self._action, width=15).grid(row = index, column = 0))
            if(port == '/dev/'+self.udevportname):
                selected = index
            self.rbvar.set(selected)

    def port(self):
        if(self.sindex != None):
            return self.ports[self.sindex]
        return None

    def _action(self):
        self.sindex = self.rbvar.get()

    def _serial_ports(self, udevportname=''):
        """Lists serial ports

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of available serial ports
        """
        isLinux = False
        if sys.platform.startswith('win'):
            ports = ['COM' + str(i + 1) for i in range(256)]

        elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
            isLinux = True
            # this is to exclude your current terminal "/dev/tty"
            ports = glob.glob('/dev/ttyUSB*')
            if(len(udevportname)):
                ports += glob.glob('/dev/'+udevportname+'*')

        elif sys.platform.startswith('darwin'):
            ports = glob.glob('/dev/tty.*')

        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                if(isLinux == False):
                    # Doing this in Linux disturbs the serial port
                    s = serial.Serial(port)
                    s.close()
                result.append(port)
            except (OSError, serial.SerialException):
                pass
        return result
