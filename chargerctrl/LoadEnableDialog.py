__author__ = 'srodgers'
from .Dialog import *

class LoadEnableDialog(Dialog):
    def __init__(self, parent, cc, title = None, xoffset = 50, yoffset = 50):
        self.cc = cc
        self.state = "NO"
        Dialog.__init__(self, parent = parent, title=title, xoffset=xoffset, yoffset=yoffset)

    #
    # Dialog body
    def body(self, master):
        self.legend = Label(master, text= "Load Enabled")

        if self.cc.get_load_enable_state():
            self.state = 'YES'
        else:
            self.state = 'NO'

        self.field = Label(master, text = self.state, relief = SUNKEN, width = 3)
        self.legend.grid(row=0, column=0, sticky = W)
        self.field.grid(row=0, column=1, sticky = W)

    #
    # Buttons
    def buttonbox(self):

        box = Frame(self)

        self.enabutton = Button(box, text="ENABLE", width=10, command=self.enable)
        self.enabutton.pack(side=LEFT)
        self.disabutton = Button(box, text="DISABLE", width=10, command=self.disable, default=ACTIVE)
        self.disabutton.pack(side=LEFT)
        self.disabutton = Button(box, text="CLOSE", width=10, command=self.cancel)
        self.disabutton.pack(side=LEFT)

        self.bind("<Escape>", self.cancel)

        box.pack()


    #
    # Enable load
    def enable(self):
        self.cc.enable_load()
        self.state = 'YES'
        self.field.configure(text=self.state)

    #
    # Disable load
    def disable(self):
        self.cc.disable_load()
        self.state = 'NO'
        self.field.configure(text=self.state)




