# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
from wx.lib.pubsub import pub


###########################################################################
## Class Frm_SerialConn
###########################################################################

class Frm_SerialConn(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(313, 209), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        gSizer1 = wx.GridSizer(1, 1, 0, 0)

        fgSizer1 = wx.FlexGridSizer(4, 1, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer1.SetMinSize(wx.Size(300, -1))
        self.Lbl_SerialJdl = wx.StaticText(self, wx.ID_ANY, u"Serial Connection", wx.DefaultPosition, wx.Size(-1, -1),
                                           0)
        self.Lbl_SerialJdl.Wrap(-1)
        self.Lbl_SerialJdl.SetFont(wx.Font(16, 74, 90, 92, False, "Arial Black"))

        fgSizer1.Add(self.Lbl_SerialJdl, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        gbSizer1.SetMinSize(wx.Size(300, -1))
        self.Lbl_SerialCOM = wx.StaticText(self, wx.ID_ANY, u"COM", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_SerialCOM.Wrap(-1)
        gbSizer1.Add(self.Lbl_SerialCOM, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Txt_SerialCOM = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        gbSizer1.Add(self.Txt_SerialCOM, wx.GBPosition(0, 1), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Lbl_SerialBRATE = wx.StaticText(self, wx.ID_ANY, u"BaudRate", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_SerialBRATE.Wrap(-1)
        gbSizer1.Add(self.Lbl_SerialBRATE, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Txt_SerialBRATE = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(200, -1), 0)
        gbSizer1.Add(self.Txt_SerialBRATE, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        fgSizer1.Add(gbSizer1, 1, wx.EXPAND, 5)

        gSizer2 = wx.GridSizer(1, 2, 0, 0)

        self.Cmd_SerialConnect = wx.Button(self, wx.ID_ANY, u"Connect", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.Cmd_SerialConnect, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Cmd_SerialDisconnect = wx.Button(self, wx.ID_ANY, u"Disconnect", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.Cmd_SerialDisconnect, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer1.Add(gSizer2, 1, wx.EXPAND, 5)

        gSizer3 = wx.GridSizer(1, 1, 0, 0)

        self.Lbl_SerialStatus = wx.StaticText(self, wx.ID_ANY, u"MyLabel", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_SerialStatus.Wrap(-1)
        self.Lbl_SerialStatus.SetFont(wx.Font(12, 74, 90, 92, False, "Arial"))
        self.Lbl_SerialStatus.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        gSizer3.Add(self.Lbl_SerialStatus, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer1.Add(gSizer3, 1, wx.EXPAND, 5)

        gSizer1.Add(fgSizer1, 1, wx.EXPAND, 5)

        self.SetSizer(gSizer1)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Cmd_SerialConnect.Bind(wx.EVT_BUTTON, lambda x:self.SerialConnect())
        self.Cmd_SerialDisconnect.Bind(wx.EVT_BUTTON, lambda x:self.SerianDisconnect())

        self.Show()

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def SerialConnect(self):
        #mode, board, com, baudrate, timeout)
        try:
            wx.CallAfter(pub.sendMessage,'SerialConnect', mode=1, board=1,com=self.Txt_SerialCOM.GetValue(),
                            baudrate=self.Txt_SerialBRATE.GetValue(), timeout=0)
        except Exception as e:
            self.Lbl_SerialStatus.SetLabel('CANT CONNECT')
        else:
            self.Lbl_SerialStatus.SetLabel('CONNECTED')
            #if self.Magnet == True:
            #    print 'MAG ON'
            #    self.CFastExecutingCommand([{1: 'MAG;1'}])

    def SerianDisconnect(self):
        try:
            wx.CallAfter(pub.sendMessage, 'SerialDisconnect', board=1)
        except Exception as e:
            self.Lbl_SerialStatus.SetLabel('CANT DISCONNECT')
        else:
            self.Lbl_SerialStatus.SetLabel('DISCONNECTED')


