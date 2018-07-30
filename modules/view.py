
#IMPORT LIB MODULE
import wx
import sys
import os
from wx.lib.pubsub import pub


#IMPORT OUR MODULE
from frame import Main_Page,Manual_Page,Process_Page,\
    SetupProcess_Page, SerialConnection_Page,SudutSave_Page


class View(Main_Page.Main_Menu,Manual_Page.Manual_Movement,
           Process_Page.List_Process,SetupProcess_Page.Setup_Process,
           SudutSave_Page.SudutSave):
    def __init__(self, parent):
        self.CurrForm = 'Main'
        Main_Page.Main_Menu.__init__(self,None,'Main')


    def VFrameLoad(self, mode):
        if mode == 1:
            self.VFrameClose(1,self.CurrForm)
            self.CurrForm = 'Process'
            Process_Page.List_Process.__init__(self,None,'Process')
            self.PrcFrameAction(2, 'LoadToDataview')

        elif mode == 2:
            self.VFrameClose(1,self.CurrForm)
            Manual_Page.Manual_Movement.__init__(self,None,'Manual')
            self.CurrForm = 'Manual'

        elif mode == 3:
            self.VFrameClose(1,self.CurrForm)
            self.CurrForm = 'Setup'
            SetupProcess_Page.Setup_Process.__init__(self,None,'Setup')

        elif mode == 4:
            SerialConnection_Page.Frm_SerialConn(None)

        elif mode == 5:
            self.CurrForm = ''
            SudutSave_Page.SudutSave.__init__(self,None)

    def VFrameClose(self, mode, form):
        pass
        #if mode == 1:
        #    self.FrameObject[form].Hide()
        #elif mode == 2:
        #    if self.CurrForm != 'Main' and self.CurrForm != '':
        #        self.FrameObject[form].Hide()
        #        self.CurrForm = 'Main'
        #        Main_Page.Main_Menu.__init__(self, None, 'Main')
        #    elif self.CurrForm == 'Main':
        #        self.FrameObject[form].Destroy()
        #        wx.CallAfter(pub.sendMessage,'CloseApp')

    def VDestroyAll(self):
        for item in wx.GetTopLevelWindows():
            item.Destroy()


    #UNIVERSAL MENUBAR
    def VMenuBars(self):
        self.MenuBar_Main = wx.MenuBar(0)
        self.Mbar_Menu = wx.Menu()
        self.MenuBar_Main.Append(self.Mbar_Menu, u"Menu")

        self.MenuBar_Main = wx.MenuBar(0)
        self.Mbar_Menu = wx.Menu()

        #================================ ITEM ==============================
        self.Mbar_SerConnection = wx.MenuItem(self.Mbar_Menu, wx.ID_ANY, u"Connection", wx.EmptyString, wx.ITEM_NORMAL)
        self.Mbar_Menu.Append(self.Mbar_SerConnection)

        self.Mbar_Menu_SudutSave = wx.MenuItem(self.Mbar_Menu, wx.ID_ANY, u"SudutSave", wx.EmptyString, wx.ITEM_NORMAL)
        self.Mbar_Menu.Append(self.Mbar_Menu_SudutSave)

        self.Mbar_Menu_Process = wx.MenuItem(self.Mbar_Menu, wx.ID_ANY, u"Process", wx.EmptyString, wx.ITEM_NORMAL)
        self.Mbar_Menu.Append(self.Mbar_Menu_Process)

        self.Mbar_Menu_Manual = wx.MenuItem(self.Mbar_Menu, wx.ID_ANY, u"Manual Movement", wx.EmptyString, wx.ITEM_NORMAL)
        self.Mbar_Menu.Append(self.Mbar_Menu_Manual)

        self.Mbar_Menu_Setup = wx.MenuItem(self.Mbar_Menu, wx.ID_ANY, u"Setup Process", wx.EmptyString, wx.ITEM_NORMAL)
        self.Mbar_Menu.Append(self.Mbar_Menu_Setup)
        # ================================ == ==============================

        self.MenuBar_Main.Append(self.Mbar_Menu, u"Menu")

        self.Mbar_Help = wx.Menu()
        self.MenuBar_Main.Append(self.Mbar_Help, u"Help")

        # Connect Events
        self.Bind(wx.EVT_MENU, lambda x: self.VFrameLoad(4), id=self.Mbar_SerConnection.GetId())
        self.Bind(wx.EVT_MENU, lambda x:self.VFrameLoad(5), id=self.Mbar_Menu_SudutSave.GetId())
        self.Bind(wx.EVT_MENU, lambda x:self.VFrameLoad(1), id=self.Mbar_Menu_Process.GetId())
        self.Bind(wx.EVT_MENU, lambda x:self.VFrameLoad(2), id=self.Mbar_Menu_Manual.GetId())
        self.Bind(wx.EVT_MENU, lambda x:self.VFrameLoad(3), id=self.Mbar_Menu_Setup.GetId())


    def VFrameAct(self, frame, mode):
        if frame == "Setup_Process":
            if mode == "Tambah":
                self.Spn_Value1.SetValue(self.S)
