

#IMPORT LIB MODULE
import wx
import sys
import os

#APPEND CURR DIRECTORY TO SYSd
sys.path.append(os.getcwd())

#IMPORT OUR MODULE
from modules import controller


class StarterProgram(controller.Controller):
    def __init__(self):
        controller.Controller.__init__(self)

if __name__ == '__main__':
    MyApp = wx.App()
    StarterProgram()
    MyApp.MainLoop()




