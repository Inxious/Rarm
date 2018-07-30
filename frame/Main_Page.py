# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os


###########################################################################
## Class Main_Menu
###########################################################################

class Main_Menu(wx.Frame):
    def __init__(self, parent, framename):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='TESTER', pos=wx.DefaultPosition,
                          size=wx.Size(662, 444), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.FrameObject.update({framename: self})

        #self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        gSizer6 = wx.GridSizer(1, 1, 0, 0)

        # MENU BAR
        self.VMenuBars()
        self.SetMenuBar(self.MenuBar_Main)

        # MIDDLE BACKGROUND
        self.MainBackground()
        gSizer6.Add(self.Main_Background, 1, wx.EXPAND | wx.ALL, 20)

        self.SetSizer(gSizer6)
        self.Layout()

        #Event Load
        self.MainEvent(framename)


        self.Centre(wx.BOTH)
        self.Show()

    def MainEvent(self, framename):
        # FORM EVENT
        #self.Bind(wx.EVT_CLOSE, lambda x: self.VFrameClose(2, framename))
        pass

    def MainBackground(self):
        self.Main_Background = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)

        try:
            # pick an image file you have in the working folder
            # you can load .jpg  .png  .bmp  or .gif files
            image_file = os.path.normpath('.\\images\\company.png')
            bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            # image's upper left corner anchors at panel coordinates (0, 0)
            self.Bit_Background_Main = wx.StaticBitmap(self.Main_Background, -1, bmp1, pos=(0, 0))
            # show some image details
            str1 = "%s  %dx%d" % (image_file, bmp1.GetWidth(), bmp1.GetHeight())

        except IOError:
            print "Image file %s not found" % image_file
            raise SystemExit

        #self.Main_Background.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))


    def __del__(self):
        pass