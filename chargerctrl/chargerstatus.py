__author__ = 'srodgers'

from tkinter import *




class ChargerStatus():
    def __init__(self, master, cc):
        self.cc = cc
        self.master = master
        self.subwin = Toplevel(master)
        self.subwin.title("Charger Status")
        self.subwin.lift(aboveThis=master)


        self.mframe = Frame(self.subwin)
        self.mframe.pack()

        self.bframe = Frame(self.mframe)
        self.sframe = Frame(self.mframe)

        self.bframe.pack()


        self.sframe.columnconfigure(1, minsize = 50)
        self.sframe.columnconfigure(2, minsize = 20)
        self.sframe.columnconfigure(3, minsize = 30)
        self.sframe.columnconfigure(5, minsize = 50)
        self.sframe.columnconfigure(6, minsize = 20)
        self.sframe.columnconfigure(7, minsize = 30)
        self.sframe.pack()

        self.energyresetbutton = Button(self.bframe,text = "Reset Energy", command=cc.reset_energy, )
        self.chargeresetbutton = Button(self.bframe, text = "Reset Charge", command = cc.reset_charge,)
        self.dischargeresetbutton = Button(self.bframe, text = "Reset Discharge", command = cc.reset_discharge,)
        self.quitbutton = Button(self.bframe, text = "Quit", command = self.quit)



        self.pvlabel = Label(self.sframe, text= 'PV Voltage')
        self.pvvalue = Label(self.sframe, text = '0', padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.pvvunits = Label(self.sframe, text = 'mV')

        self.battvlabel = Label(self.sframe, text = 'Battery Voltage')
        self.battvvalue = Label(self.sframe, text = '0', padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.battvunits = Label(self.sframe, text = 'mV')

        self.convilabel = Label(self.sframe, text = 'Converter Current')
        self.convivalue = Label(self.sframe, text = '0',padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.conviunits = Label(self.sframe, text = 'mA')

        self.loadilabel = Label(self.sframe, text = 'Load Current')
        self.loadivalue = Label(self.sframe, text = '0',padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.loadiunits = Label(self.sframe, text = 'mA')


        self.battilabel = Label(self.sframe, text = 'Battery Current')
        self.battivalue = Label(self.sframe, text = '0',padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.battiunits = Label(self.sframe, text = 'mA')

        self.convplabel = Label(self.sframe, text = 'Converter Power')
        self.convpvalue = Label(self.sframe, text = '0', padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.convpunits = Label(self.sframe, text = 'mW')

        self.convenergymwhlabel = Label(self.sframe, text = 'Converter Energy')
        self.convenergymwhvalue = Label(self.sframe, text = '0', padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.convenergymwhunits = Label(self.sframe, text = 'mWh')

        self.battchargemahlabel = Label(self.sframe, text = 'Battery Charge')
        self.battchargemahvalue = Label(self.sframe, text = '0', padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.battchargemahunits = Label(self.sframe, text = 'mAh')

        self.battdischargemahlabel = Label(self.sframe, text = 'Battery Discharge')
        self.battdischargemahvalue = Label(self.sframe, text = '0', padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.battdischargemahunits = Label(self.sframe, text = 'mAh')

        self.convslabel = Label(self.sframe, text = 'Converter State')
        self.convsvalue = Label(self.sframe, text = '0', padx = 2, pady = 2, relief = SUNKEN, width = 5)

        self.convpwmlabel = Label(self.sframe, text = 'Converter PWM')
        self.convpwmvalue = Label(self.sframe, text = '0', padx = 2, pady = 2, relief = SUNKEN, width = 5)

        self.batttemplabel = Label(self.sframe, text = 'Battery Temp')
        self.batttempvalue = Label(self.sframe, text = '0', padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.batttempunits = Label(self.sframe, text = 'K')

        self.maxpowerlabel = Label(self.sframe, text = 'Max mppt power')
        self.maxpowervalue = Label(self.sframe, text = '0',padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.maxpowerunits = Label(self.sframe, text = 'mW')

        self.endbulkvlabel = Label(self.sframe, text= 'End Bulk Voltage')
        self.endbulkvvalue = Label(self.sframe, text = '0', padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.endbulkvunits = Label(self.sframe, text = 'mV')

        self.endabsvlabel = Label(self.sframe, text = 'End Absorb Voltage')
        self.endabsvvalue = Label(self.sframe, text = '0', padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.endabsvunits = Label(self.sframe, text = 'mV')

        self.gassingvlabel = Label(self.sframe, text = 'Gassing Voltage')
        self.gassingvvalue = Label(self.sframe, text = '0',padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.gassingvunits = Label(self.sframe, text = 'mV')

        self.floatvlabel = Label(self.sframe, text = 'Float Hold Voltage')
        self.floatvvalue = Label(self.sframe, text = '0',padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.floatvunits = Label(self.sframe, text = 'mV')

        self.tempoffsetvlabel = Label(self.sframe, text = 'Temperature offset')
        self.tempoffsetvvalue = Label(self.sframe, text = '0',padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.tempoffsetvunits = Label(self.sframe, text = 'mV')

        self.scanpwmlabel = Label(self.sframe, text = 'Scan PWM')
        self.scanpwmvalue = Label(self.sframe, text = '0',padx = 2, pady = 2, relief = SUNKEN, width = 5)

        self.maxpowermvlabel = Label(self.sframe, text = 'Voltage at Pmax')
        self.maxpowermvvalue = Label(self.sframe, text = '0',padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.maxpowermvunits = Label(self.sframe, text = 'mV')

        self.fgloadlabel = Label(self.sframe, text = 'Foreground load')
        self.fgloadvalue = Label(self.sframe, text = '0',padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.fgloadunits = Label(self.sframe, text = 'Ticks')





        self.energyresetbutton.pack(side = LEFT,expand = True)
        self.chargeresetbutton.pack(side = LEFT, expand = True)
        self.dischargeresetbutton.pack(side = LEFT, expand = True)
        self.quitbutton.pack(side = LEFT, expand = True)


        self.pvlabel.grid(row = 0, column = 0, sticky = W)
        self.pvvalue.grid(row = 0, column = 1, sticky = W)
        self.pvvunits.grid(row = 0, column = 2, sticky = W)

        self.battvlabel.grid(row = 0, column = 4, sticky = W)
        self.battvvalue.grid(row = 0, column = 5, sticky = W)
        self.battvunits.grid(row = 0, column = 6, sticky = W)

        self.convilabel.grid(row = 1,column = 0, sticky = W)
        self.convivalue.grid(row = 1, column = 1, sticky = W)
        self.conviunits.grid(row = 1, column = 2, sticky = W)

        self.loadilabel.grid(row = 1, column = 4, sticky = W)
        self.loadivalue.grid(row = 1, column = 5, sticky = W)
        self.loadiunits.grid(row = 1, column = 6, sticky = W)

        self.battilabel.grid(row = 2, column = 0, sticky = W)
        self.battivalue.grid(row = 2, column = 1, sticky = W)
        self.battiunits.grid(row = 2, column = 2, sticky = W)

        self.convplabel.grid(row = 2, column = 4, sticky = W)
        self.convpvalue.grid(row = 2, column = 5, sticky = W)
        self.convpunits.grid(row = 2, column = 6, sticky = W)

        self.convenergymwhlabel.grid(row = 3, column = 0, sticky = W)
        self.convenergymwhvalue.grid(row = 3, column = 1, sticky = W)
        self.convenergymwhunits.grid(row = 3, column = 2, sticky = W)

        self.battchargemahlabel.grid(row = 3, column = 4, sticky = W)
        self.battchargemahvalue.grid(row = 3, column = 5, sticky = W)
        self.battchargemahunits.grid(row = 3, column = 6, sticky = W)

        self.battdischargemahlabel.grid(row = 4, column = 0, sticky = W)
        self.battdischargemahvalue.grid(row = 4, column = 1, sticky = W)
        self.battdischargemahunits.grid(row = 4, column = 2, sticky = W)

        self.convslabel.grid(row = 4, column = 4, sticky = W)
        self.convsvalue.grid(row = 4, column = 5, sticky = W)

        self.convpwmlabel.grid(row = 5, column = 0, sticky = W)
        self.convpwmvalue.grid(row = 5, column = 1, sticky = W)

        self.batttemplabel.grid(row = 5, column = 4, sticky = W)
        self.batttempvalue.grid(row = 5, column = 5, sticky = W)
        self.batttempunits.grid(row = 5, column = 6, sticky = W)

        self.endbulkvlabel.grid(row = 6, column = 0, sticky = W)
        self.endbulkvvalue.grid(row = 6, column = 1, sticky = W)
        self.endbulkvunits.grid(row = 6, column = 2, sticky = W)

        self.endabsvlabel.grid(row = 6, column = 4, sticky = W)
        self.endabsvvalue.grid(row = 6, column = 5, sticky = W)
        self.endabsvunits.grid(row = 6, column = 6, sticky = W)

        self.gassingvlabel.grid(row = 7, column = 0, sticky = W)
        self.gassingvvalue.grid(row = 7, column = 1, sticky = W)
        self.gassingvunits.grid(row = 7, column = 2, sticky = W)

        self.floatvlabel.grid(row = 7, column = 4, sticky = W)
        self.floatvvalue.grid(row = 7, column = 5, sticky = W)
        self.floatvunits.grid(row = 7, column = 6, sticky = W)

        self.tempoffsetvlabel.grid(row = 8, column = 0, sticky = W)
        self.tempoffsetvvalue.grid(row = 8, column = 1, sticky = W)
        self.tempoffsetvunits.grid(row = 8, column = 2, sticky = W)

        self.scanpwmlabel.grid(row = 8, column = 4, sticky = W)
        self.scanpwmvalue.grid(row = 8, column = 5, sticky = W)

        self.maxpowermvlabel.grid(row = 9, column = 0, sticky = W)
        self.maxpowermvvalue.grid(row = 9, column = 1, sticky = W)
        self.maxpowermvunits.grid(row = 9, column = 2, sticky = W)

        self.fgloadlabel.grid(row = 9, column = 4, sticky = W)
        self.fgloadvalue.grid(row = 9, column = 5, sticky = W)
        self.fgloadunits.grid(row = 9, column = 6, sticky = W)

        self.update_values()


    def update_values(self):
        sensors = self.cc.get_sensors()
        info = self.cc.get_conv_info()
        self.pvvalue.configure(text = sensors['pvmv'])
        self.battvvalue.configure(text = sensors['battmv'])
        self.convivalue.configure(text = sensors['convma'])
        self.loadivalue.configure(text = sensors['loadma'])
        self.battivalue.configure(text = sensors['convma'] - sensors['loadma'])
        self.convpvalue.configure(text = int((sensors['convma'] * sensors['battmv']) / 1000))
        self.convenergymwhvalue.configure(text = sensors['convenergymwh'])
        self.battchargemahvalue.configure(text = sensors['battchargemah'])
        self.battdischargemahvalue.configure(text = sensors['battdischargemah'])
        self.convsvalue.configure(text = info['state'])
        self.convpwmvalue.configure(text = info['pwm'])
        self.batttempvalue.configure(text = sensors['battemp'])
        self.maxpowervalue.configure(text = info['maxpower'])
        self.endbulkvvalue.configure(text = info['endbulkmv'])
        self.endabsvvalue.configure(text = info['endabsorbmv'])
        self.gassingvvalue.configure(text = info['gassingmv'])
        self.floatvvalue.configure(text = info['floatholdmv'])
        self.tempoffsetvvalue.configure(text = info['tempoffset'])
        self.scanpwmvalue.configure(text = info['pwmmaxpower'])
        self.maxpowermvvalue.configure(text = info['maxpowermv'])
        self.fgloadvalue.configure(text = info['fgload'])
        self.sframe.after(250, self.update_values)

    def quit(self):
        self.mframe.destroy()

