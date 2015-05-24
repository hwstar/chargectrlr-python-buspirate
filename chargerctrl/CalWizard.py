__author__ = 'srodgers'

from .Wizard import *


class CalWizard(Wizard):
    #
    # Constructor
    def __init__(self, parent, cc, title=None,xoffset=50, yoffset=50):
        self.cc = cc
        self.didpvcal = False
        self.didbattcal = False
        self.calerror = False
        Wizard.__init__(self, parent, title=title, xoffset = xoffset, yoffset = yoffset)

    #
    # Cancel and return control to parent
    def cancel(self, event=None):
        self.cc.cal_mode_exit()
        Wizard.cancel(self,event)

    #
    # Draw pages
    def body(self, master):
        self.pagenames = ['Setup','PV Cal','BV Cal', 'EEPROM Write']
        self.page1 = Frame(master)
        Label(self.page1, text='1.Connect the Bus Pirate I2C leads to the Arduino.').pack(anchor = W)
        Label(self.page1, text='2.Connect the charge controller to a 6 volt calibration source.').pack(anchor = W)
        self.page1.pack(side=TOP)

        self.page2 = Frame(master)
        self.page2text = Frame(self.page2)
        Label(self.page2text, text='Press the calibrate button below to calibrate the PV voltage').pack(anchor = W)
        self.page2text.pack()
        self.page2button = Frame(self.page2)
        Button(self.page2text, text="Calibrate PV Voltage", command=self.calpv).pack()
        self.page2button.pack()


        self.page3 = Frame(master)
        self.page3text = Frame(self.page3)
        Label(self.page3, text='Press the calibrate button below to calibrate the Battery voltage').pack(anchor = W)
        self.page3text.pack()
        self.page3button = Frame(self.page3)
        Button(self.page3, text="Calibrate Battery Voltage", command = self.calbatt).pack()
        self.page3button.pack()

        self.page4 = Frame(master)
        self.page4text = Frame(self.page4)
        Label(self.page4text, text='PV calibration value').grid(row=0, column=0, sticky=W)
        self.pvlabelvalue = Label(self.page4text, text='0', padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.pvlabelvalue.grid(row=0, column=1, sticky=W)
        Label(self.page4text, text='Battery calibration value').grid(row=1, column=0, sticky=W)
        self.battlabelvalue = Label(self.page4text, text='0', padx = 2, pady = 2, relief = SUNKEN, width = 5)
        self.battlabelvalue.grid(row=1, column=1, sticky=W)
        Label(self.page4text, text='').grid(row=2, column=0, sticky=W)
        self.page4text.pack()

        self.page4button = Frame(self.page4)
        self.writeeeprombutton = Button(self.page4button, text="Write to EEPROM", command=self.eeprom_write_exit)
        self.writeeeprombutton.pack()
        self.page4button.pack()

        self.pages = [self.page1, self.page2, self.page3, self.page4]
        self.current = self.page1

        self.drawmapframe()

    #
    # Draw the button box frame

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons

        box = Frame(self)

        self.prevbutton = Button(box, text="Previous", width=10, command=self.prev, default=ACTIVE)
        self.prevbutton.pack(side=LEFT, padx=5, pady=5)
        self.nextbutton = Button(box, text="Next", width=10, command=self.next)
        self.nextbutton.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.next)
        self.bind("<Escape>", self.cancel)

        self.prevbutton.config(state='disabled')

        box.pack()


    #
    # Draw the wizard map frame which shows progress through the wizard

    def drawmapframe(self):
        m = Frame(self)
        self.maplabels = []
        for i in range(len(self.pages)):
            if(self.pagenames is not None):
                pn = self.pagenames[i]
            else:
                pn = str(i+1)
            self.maplabels.append(Label(m, text=pn))
            self.maplabels[i].grid(row = 0, column=i, padx=10)
        self.mapbg = self.maplabels[0].cget('bg')
        i = self.pages.index(self.current)
        self.updatemap(i, 'yellow')
        m.pack()

    #
    # Update the wizard map

    def updatemap(self, entry, color):
        self.maplabels[entry].configure(background=color)



    def move(self, dirn):
        nextpage = self.pages.index(self.current) + dirn
        if not 0 <= nextpage < len(self.pages):
            return

        # Enable prev button if not on first page
        if(nextpage == 0):
            self.prevbutton.config(state='disabled')
        else:
            self.prevbutton.config(state='normal')

        # Disable next button if cal not performed on a page
        if self.pages[nextpage] is self.page2 and self.didpvcal == False :
            self.nextbutton.config(state='disabled')
        elif self.pages[nextpage] is self.page3 and self.didbattcal == False :
            self.nextbutton.config(state='disabled')
        elif self.pages[nextpage] is self.page4:
            self.nextbutton.config(state='disabled')
            if(self.calerror == False):
                self.pvlabelvalue.configure(text = self.cal['pv'])
                self.battlabelvalue.configure(text = self.cal['batt'])
                self.writeeeprombutton.config(state='normal')

            else:
                self.pvlabelvalue.configure(text = 'error')
                self.battlabelvalue.configure(text = 'error')
                self.writeeeprombutton.config(state='disabled')

        else:
            self.nextbutton.config(state = 'normal')

        # Get current page index
        curpage = self.pages.index(self.current)
        # change background back to default
        self.updatemap(curpage, self.mapbg)
        # stop displaying current frame
        self.current.pack_forget()
        # set current page to the next page
        self.current = self.pages[nextpage]
        # display the new page
        self.current.pack(side=TOP)
        # highlight current page
        self.updatemap(nextpage, 'yellow')


    #
    #  Calibrate PV voltage
    def calpv(self):
        self.cc.cal_mode_enter()
        self.cc.cal_pv_start()
        self.calbusy()
        self.didpvcal = True
        self.nextbutton.config(state='normal')


    #
    # Calibrate battery voltage
    def calbatt(self):
        self.cc.cal_batt_start()
        self.calbusy()
        self.cal = self.cc.get_cal()
        if self.cal['pv'] < 4800  or self.cal['pv'] > 5200 or self.cal['batt'] < 4800 or self.cal['batt'] > 5200:
            self.calerror = True
        self.didbattcal = True
        self.nextbutton.config(state = 'normal')

    #
    # Set mouse cursor busy during cal process
    def calbusy(self):
        self.current.config(cursor = 'watch')
        self.current.update()
        while(self.cc.cal_busy()):
            pass
        self.current.config(cursor = '')

    #
    # Write to EEPROM and exit
    def eeprom_write_exit(self):
        self.cc.cal_mode_write_exit()
        self.cancel()
