__author__ = 'srodgers'

from collections import OrderedDict
from .Dialog import *




class ChargerStatus(Dialog):
    def __init__(self, master, cc, title="Charger Status", xoffset=50, yoffset=50):
        self.cc = cc
        self.fields = OrderedDict([
            ('pv', {'text': 'PV Voltage', 'units': 'mV', 'sensor' : 'pvmv'}),
            ('battv', {'text': 'Battery Voltage', 'units': 'mV', 'sensor' : 'battmv'}),
            ('convi', {'text' : 'Converter Current', 'units': 'mA', 'sensor' : 'convma'}),
            ('loadi', {'text' : 'Load Current', 'units': 'mA', 'sensor' : 'loadma'}),
            ('batti', {'text' : 'Battery Current', 'units': 'mA', 'sensor': 'specialcase'}),
            ('convp', {'text' : 'Converter Power', 'units': 'mW', 'sensor': 'specialcase'}),
            ('convenergymwh', {'text' : 'Converter Energy', 'units': 'mWh', 'sensor': 'convenergymwh'}),
            ('battchargemah', {'text' : 'Battery Charge', 'units': 'mAh', 'sensor': 'battchargemah'}),
            ('battdischargemah', {'text' : 'Battery Discharge', 'units': 'mAh', 'sensor': 'battdischargemah'}),
            ('convs', {'text' : 'Converter State', 'units': '', 'info': 'state'}),
            ('convpwm', {'text' : 'Converter PWM', 'units': '', 'info': 'pwm'}),
            ('battemp', {'text' : 'Battery Temperature', 'units': u'\N{DEGREE SIGN}K', 'sensor': 'battemp'}),
            ('scanpower', {'text' : 'Scan Power', 'units': 'mW', 'info': 'maxpower'}),
            ('endbulkmv', {'text' : 'End Bulk Voltage', 'units': 'mV', 'info': 'endbulkmv'}),
            ('endabsorbmv', {'text' : 'End Absorb Voltage', 'units': 'mV', 'info': 'endabsorbmv'}),
            ('gassingmv', {'text' : 'Gassing Voltage', 'units': 'mV', 'info': 'gassingmv'}),
            ('floatholdmv', {'text' : 'Float Hold Voltage', 'units': 'mV', 'info': 'floatholdmv'}),
            ('tempoffset', {'text' : 'Temperature Offset', 'units': 'mV', 'info': 'tempoffset'}),
            ('scanpwm', {'text' : 'Scan PWM', 'units': '', 'info': 'pwmmaxpower'}),
            ('scanvoltage', {'text' : 'Scan Voltage', 'units': 'mV', 'info': 'maxpowermv'}),
            ('fgload', {'text' : 'Foreground Load', 'units': 'Ticks', 'info': 'fgload'})
        ])

        self.master = master
        Dialog.__init__(self, master, title = title, xoffset=xoffset, yoffset=yoffset)

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons

        box = Frame(self)

        self.closebutt = Button(box, text="Close", width=15, command=self.close, default=ACTIVE)
        self.closebutt.grid(row=0, column=0)
        self.resetconvebutt = Button(box, text="Reset Energy", width=15, command=self.resetconve)
        self.resetconvebutt.grid(row=0, column=1)
        self.resetbattc = Button(box, text="Reset Charge", width=15, command=self.resetbattc)
        self.resetbattc.grid(row=1, column=0)
        self.resetbattd = Button(box, text="Reset Discharge", width=15, command=self.resetbattd)
        self.resetbattd.grid(row=1, column=1)


        self.bind("<Return>", self.close)
        self.bind("<Escape>", self.close)

        box.pack()


    def resetconve(self):
        self.cc.reset_energy()


    def resetbattc(self):
        self.cc.reset_charge()

    def resetbattd(self):
        self.cc.reset_discharge()

    def close(self):

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()


    def cancel(self, event=None):
        self.after_cancel(self.job)
        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()



    def body(self, master) :
        master.columnconfigure(0, minsize = 20)
        master.columnconfigure(1, minsize = 50)
        master.columnconfigure(2, minsize = 20)
        master.columnconfigure(3, minsize = 30)
        master.columnconfigure(4, minsize = 20)
        master.columnconfigure(5, minsize = 50)
        master.columnconfigure(6, minsize = 20)
        master.columnconfigure(7, minsize = 30)
        master.columnconfigure(8, minsize = 20)


        # Create labels
        for item in self.fields:
            self.fields[item]['labelobj'] = Label(master, text= self.fields[item]['text'])
            self.fields[item]['valueobj'] = Label(master, text = '0', relief = SUNKEN, width = 5)
            if(len(self.fields[item]['units'])):
                self.fields[item]['unitsobj'] = Label(master, text = self.fields[item]['units'])

        # Place labels on grid
        for index, item in enumerate(self.fields):
            columnbase = ((index & 1) << 2) + 1
            row = index >> 1
            #print(columnbase)
            #print(row)
            #print()
            self.fields[item]['labelobj'].grid(row = row, column = columnbase, sticky = W)
            self.fields[item]['valueobj'].grid(row = row, column = columnbase + 1, sticky = W)
            if(len(self.fields[item]['units'])):
                self.fields[item]['unitsobj'].grid(row = row, column = columnbase + 2, sticky = W)

        # Do first update
        self.update_values()


    def update_values(self):
        sensors = self.cc.get_sensors()
        info = self.cc.get_conv_info()

        # Loop through all values in field dict
        for index, item in enumerate(self.fields):
            if('info' in self.fields[item]):
                self.fields[item]['valueobj'].configure(text = info[self.fields[item]['info']])
            else:
                if(self.fields[item]['sensor'] != 'specialcase'):
                    self.fields[item]['valueobj'].configure(text = sensors[self.fields[item]['sensor']])
                else:
                    if(item == 'convp'):
                        # Special case for converter power
                        self.fields[item]['valueobj'].configure(text = int((sensors['convma'] * sensors['battmv']) / 1000))
                    elif(item == 'batti'):
                        # Special case for battery current
                        self.fields[item]['valueobj'].configure(text = (sensors['convma'] - sensors['loadma']))

        self.job = self.master.after(250, self.update_values)



