__author__ = 'srodgers'
from .Dialog import *

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

class LoadEnableDialog(Dialog):
    def __init__(self, parent, cc, title = None, xoffset=50, yoffset=50):
        self.cc = cc
        self.state = "NO"
        Dialog.__init__(self, parent=parent, title=title, xoffset=xoffset, yoffset=yoffset)

    #
    # Dialog body
    def body(self, master):
        self.legend = Label(master, text="Load Enabled", width=20)

        if self.cc.get_load_enable_state():
            self.state = 'YES'
        else:
            self.state = 'NO'

        self.field = Label(master, text = self.state, relief=SUNKEN, width=3, background= 'white', foreground='black')
        self.legend.grid(row=0, column=0, sticky=W)
        self.field.grid(row=0, column=1, sticky=W)

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




