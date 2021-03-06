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

from .Dialog import *


class Wizard(Dialog):
    def __init__(self, parent, title=None, xoffset=50, yoffset=50):
        self.pagenames = None
        Dialog.__init__(self, parent, title=title, xoffset=xoffset, yoffset=yoffset)

    #
    # Draw wizard body

    def body(self, master):
        # Example only. Meant to be overridden!
        self.page1 = Frame(master)
        Label(self.page1, text='This is page 1 of the wizard').pack()
        self.page1.pack(side=TOP)

        self.page2 = Frame(master)
        Label(self.page2, text='This is page 2 of the wizard.').pack()

        self.page3 = Frame(master)
        Label(self.page3, text='This is page 3.  It has an entry widget too!').pack()
        Entry(self.page3).pack()

        self.pages = [self.page1, self.page2, self.page3]
        self.current = self.page1


    #
    # Draw the button box frame

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons

        box = Frame(self)

        self.prevbutton = Button(box, text="Previous", width=10, command=self.prev, default=ACTIVE)
        self.prevbutton.pack(side=LEFT)
        self.nextbutton = Button(box, text="Next", width=10, command=self.next)
        self.nextbutton.pack(side=LEFT)

        self.bind("<Return>", self.next)
        self.bind("<Escape>", self.cancel)


        box.pack()

    #
    # Move to the a new wizard page

    def move(self, dirn):
        idx = self.pages.index(self.current) + dirn
        if not 0 <= idx < len(self.pages):
            return
        self.current.pack_forget()
        self.current = self.pages[idx]
        self.current.pack(side=TOP)


    #
    # Move to the next page in the wizard

    def next(self):
        self.move(+1)

    #
    # Move to the previous page in the wizard

    def prev(self):
        self.move(-1)

    #
    # Cancel the wizard

    def cancel(self, event=None):
        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()


