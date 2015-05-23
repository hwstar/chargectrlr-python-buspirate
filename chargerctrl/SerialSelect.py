__author__ = 'srodgers'

import glob
import sys
import serial
from tkinter import *
from .Dialog import *


class SerialSelect(Dialog):

    def __init__(self, parent, title=None, udevportname=''):
        self.sindex=None
        self.udevportname = udevportname
        self.ports= self._serial_ports(udevportname)
        Dialog.__init__(self, parent, title)

    def body(self, master):
        self.rbvar = IntVar()
        for index, port in enumerate(self.ports):
            Radiobutton(master, text='', variable=self.rbvar, value=index, command=self._action).grid(row = index, column = 0)
            Label(master, text=port).grid(row = index, column = 1)

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
