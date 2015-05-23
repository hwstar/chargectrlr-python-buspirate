__author__ = 'srodgers'

from tkinter import *


class Wizard(Toplevel):
    def __init__(self, parent, title=None,xoffsetfromroot=50, yoffsetfromroot=50):
        Toplevel.__init__(self, parent)

        self.pagenames = None

        self.transient(parent)
        if title:
            self.title(title)

        self.parent = parent

        body = Frame(self)
        self.initial_focus = self.drawpageframes(body)


        body.pack(padx=5, pady=5)

        self.drawbuttonframe()

        self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        self.geometry("+%d+%d" % (parent.winfo_rootx() + xoffsetfromroot, parent.winfo_rooty() + yoffsetfromroot))

        self.initial_focus.focus_set()

        self.wait_window(self)



    def drawpageframes(self, master):
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

    def drawbuttonframe(self):
        # add standard button box. override if you don't want the
        # standard buttons

        box = Frame(self)

        self.prevbutton = Button(box, text="Previous", width=10, command=self.prev, default=ACTIVE)
        self.prevbutton.pack(side=LEFT, padx=5, pady=5)
        self.nextbutton = Button(box, text="Next", width=10, command=self.next)
        self.nextbutton.pack(side=LEFT, padx=5, pady=5)

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


