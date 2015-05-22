__author__ = 'srodgers'

from tkinter import *
from .Wizard import *


class CalWizard(Wizard):
    def __init__(self, parent, title=None,xoffsetfromroot=50, yoffsetfromroot=50):
        Wizard.__init__(self, parent, title=title, xoffsetfromroot = xoffsetfromroot, yoffsetfromroot = yoffsetfromroot)
