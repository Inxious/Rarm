# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview


###########################################################################
## Class Process_Page
###########################################################################

class List_Process(wx.Frame):
    def __init__(self, parent, framename):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(789, 557), style=wx.DEFAULT_FRAME_STYLE)

        self.FrameObject.update({framename:self})

        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        gSizer4 = wx.GridSizer(1, 2, 0, 0)


        #MENU BAR
        self.VMenuBars()
        self.SetMenuBar(self.MenuBar_Main)

        #PANEL PROCESS
        self.PrcPanelProcess()
        gSizer4.Add(self.Pnl_Prc_Process, 1, wx.EXPAND | wx.ALL, 5)


        #PANEL LOG
        self.PrcPanelLog()
        gSizer4.Add(self.Pnl_Prc_Log, 1, wx.EXPAND | wx.ALL, 5)

        self.SetSizer(gSizer4)
        self.Layout()

        #LOAD CONSTANT
        self.PrcConstant()

        #EVENTS
        self.PrcEvents(framename)

        self.Centre(wx.BOTH)
        self.Show()

    def PrcEvents(self, framename):

        #ON Checked Item
        self.Bind(wx.dataview.EVT_DATAVIEW_ITEM_ACTIVATED,
                  lambda x:self.PrcFrameAction(2,'CheckItem', selected=self.Dv_Table1.GetSelectedRow()), id=wx.ID_ANY)

        #DV_1
        self.Cmd_Prc_DvClear.Bind(wx.EVT_BUTTON, lambda x:self.PrcClearDv(1))
        self.Cmd_Prc_DvRefresh.Bind(wx.EVT_BUTTON, lambda x:self.PrcRefreshDv(1))

        self.Cmb_Prc_Process.Bind( wx.EVT_TEXT, lambda x:self.PrcFrameAction(1,'LoadConfig'))
        #self.Bind(wx.EVT_CLOSE, lambda x: self.VFrameClose(2,framename))
        self.Cmd_Prc_Process.Bind(wx.EVT_BUTTON, lambda x: self.PrcFrameAction(2,'RunProcess'))
        self.Bind(wx.dataview.EVT_DATAVIEW_ITEM_VALUE_CHANGED,
                  lambda x: self.PrcFrameAction(2,'CheckedChange', selected=self.Dv_Table1.GetSelectedRow()), id=wx.ID_ANY)

    def PrcConstant(self):
        self.Vals = True
        self.Txt_Prc_ChkProcess.SetValue(str(0))
        #ADD TABLE ITEM
        #self.Dv_Table1.AppendColumn()
        #self.Dv_Table1.AppendItem()
        pass

    def PrcPanelProcess(self):
        self.Pnl_Prc_Process = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer11 = wx.FlexGridSizer(3, 1, 0, 0)
        fgSizer11.SetFlexibleDirection(wx.BOTH)
        fgSizer11.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer7 = wx.BoxSizer(wx.VERTICAL)

        self.Lbl_Prc_Process = wx.StaticText(self.Pnl_Prc_Process, wx.ID_ANY, u"Process", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.Lbl_Prc_Process.Wrap(-1)
        bSizer7.Add(self.Lbl_Prc_Process, 0, wx.ALL, 5)

        #Cmb_Prc_ProcessChoices = []
        #self.Cmb_Prc_Process = wx.ComboBox(self.Pnl_Prc_Process, wx.ID_ANY, u"Pick A Process", wx.DefaultPosition,
        #                                   wx.DefaultSize, Cmb_Prc_ProcessChoices, 0)
        #self.Cmb_Prc_Process.SetMaxSize(wx.Size(-1, 30))

        #bSizer7.Add(self.Cmb_Prc_Process, 0, wx.ALL, 5)

        gSizer6 = wx.GridSizer(0, 2, 0, 0)

        fgSizer15 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer15.SetFlexibleDirection(wx.BOTH)
        fgSizer15.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        Cmb_Prc_ProcessChoices = []
        self.Cmb_Prc_Process = wx.ComboBox(self.Pnl_Prc_Process, wx.ID_ANY, u"Pickup A To B", wx.DefaultPosition,
                                           wx.DefaultSize, Cmb_Prc_ProcessChoices, 0)
        self.Cmb_Prc_Process.SetMaxSize(wx.Size(-1, 30))

        fgSizer15.Add(self.Cmb_Prc_Process, 0, wx.ALL, 5)

        gSizer6.Add(fgSizer15, 1, wx.EXPAND, 5)

        fgSizer16 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer16.SetFlexibleDirection(wx.BOTH)
        fgSizer16.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Cmd_Prc_DvClear = wx.Button(self.Pnl_Prc_Process, wx.ID_ANY, u"Clear", wx.DefaultPosition, wx.Size(80, -1),
                                         0)
        fgSizer16.Add(self.Cmd_Prc_DvClear, 0, wx.ALL, 5)

        self.Cmd_Prc_DvRefresh = wx.Button(self.Pnl_Prc_Process, wx.ID_ANY, u"Refresh", wx.DefaultPosition,
                                           wx.Size(80, -1), 0)
        fgSizer16.Add(self.Cmd_Prc_DvRefresh, 0, wx.ALL, 5)

        gSizer6.Add(fgSizer16, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        bSizer7.Add(gSizer6, 1, wx.EXPAND, 0)

        fgSizer11.Add(bSizer7, 1, wx.EXPAND, 5)

        self.Dv_Table1 = wx.dataview.DataViewListCtrl(self.Pnl_Prc_Process, wx.ID_ANY, wx.DefaultPosition,
                                                      wx.Size(350, 300), 0)
        fgSizer11.Add(self.Dv_Table1, 0, wx.ALL, 5)

        # ======== TABLE SETTING ===============
        self.Dv_Table1.AppendToggleColumn("Is Run", 1, width=50)
        self.Dv_Table1.AppendTextColumn("Sudut Name", 2, width=197)
        self.Dv_Table1.AppendTextColumn("Status", 3, width=120)
        # ======================================

        #self.Cmd_Prc_Process = wx.Button(self.Pnl_Prc_Process, wx.ID_ANY, u"Run Process", wx.DefaultPosition,
        #                                 wx.DefaultSize, 0)
        #fgSizer11.Add(self.Cmd_Prc_Process, 0, wx.ALL, 5)

        gSizer5 = wx.GridSizer(1, 2, 0, 0)

        fgSizer13 = wx.FlexGridSizer(0, 2, 0, 0)
        fgSizer13.SetFlexibleDirection(wx.BOTH)
        fgSizer13.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Cmd_Prc_Process = wx.Button(self.Pnl_Prc_Process, wx.ID_ANY, u"Run Process", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        fgSizer13.Add(self.Cmd_Prc_Process, 0, wx.ALL, 5)

        gSizer5.Add(fgSizer13, 1, wx.EXPAND, 5)

        fgSizer141 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer141.SetFlexibleDirection(wx.BOTH)
        fgSizer141.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Lbl_Prc_ChkProcess = wx.StaticText(self.Pnl_Prc_Process, wx.ID_ANY, u"Checked Process", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.Lbl_Prc_ChkProcess.Wrap(-1)
        fgSizer141.Add(self.Lbl_Prc_ChkProcess, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Txt_Prc_ChkProcess = wx.TextCtrl(self.Pnl_Prc_Process, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.Size(40, -1), wx.TE_READONLY)
        fgSizer141.Add(self.Txt_Prc_ChkProcess, 0, wx.ALL, 5)

        gSizer5.Add(fgSizer141, 0, wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer11.Add(gSizer5, 1, wx.EXPAND, 5)

        self.Pnl_Prc_Process.SetSizer(fgSizer11)
        self.Pnl_Prc_Process.Layout()
        fgSizer11.Fit(self.Pnl_Prc_Process)

    def PrcPanelLog(self):
        self.Pnl_Prc_Log = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer14 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer14.SetFlexibleDirection(wx.BOTH)
        fgSizer14.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer10 = wx.BoxSizer(wx.VERTICAL)

        bSizer10.AddSpacer(30)

        self.Lbl_Prc_Log = wx.StaticText(self.Pnl_Prc_Log, wx.ID_ANY, u"Log", wx.DefaultPosition, wx.DefaultSize,
                                         0 | wx.TRANSPARENT_WINDOW)
        self.Lbl_Prc_Log.Wrap(-1)
        bSizer10.Add(self.Lbl_Prc_Log, 0, wx.ALL, 8)

        fgSizer14.Add(bSizer10, 1, wx.EXPAND, 5)

        self.Dv_Table2 = wx.dataview.DataViewListCtrl(self.Pnl_Prc_Log, wx.ID_ANY, wx.DefaultPosition,
                                                      wx.Size(350, 300), 0)
        fgSizer14.Add(self.Dv_Table2, 0, wx.ALL, 5)



        # ======== TABLE SETTING ===============
        self.Dv_Table2.AppendTextColumn("Board", 1, width=50)
        self.Dv_Table2.AppendTextColumn("Data", 2, width=200)
        # ======================================

        self.Pnl_Prc_Log.SetSizer(fgSizer14)
        self.Pnl_Prc_Log.Layout()
        fgSizer14.Fit(self.Pnl_Prc_Log)

    def PrcClearDv(self, mode):
        if mode == 1:
            self.Dv_Table1.DeleteAllItems()
            self.Txt_Prc_ChkProcess.SetValue(str(0))

    def PrcRefreshDv(self, mode):
        if mode == 1:
            self.Dv_Table1.DeleteAllItems()
            self.PrcFrameAction(2,'LoadToDataview')
            self.Txt_Prc_ChkProcess.SetValue(str(0))

    def PrcFrameAction(self, mode, types, **kwargs):
        #DBASE
        if mode == 1:
            if types == 'LoadConfigToTable':
                nama = self.Cmb_Prc_Process.GetValue()
                #headerid = #ToDo : Get ProcessHeaderID
                #datalist = #ToDo : Get ProcessDetailSet


        #FRAME
        elif mode == 2:
            if types == 'LoadToDataview':
                self.Dv_Table1.DeleteAllItems()
                data = self.MGETSudut('HEADER', 3, '')
                for i in data:
                    #print i
                    hasil = []
                    hasil.extend([False, i, "PENDING"])
                    self.Dv_Table1.AppendItem(hasil)   #hasil = [False,2,'3',4]

            elif types == 'RunProcess':
                hasil = []
                rowcount = self.Dv_Table1.GetItemCount()
                colcount = self.Dv_Table1.GetColumnCount()
                for rows in range(rowcount):
                    allitem = []
                    for cols in range(colcount):
                        if cols == 0:
                            data = self.Dv_Table1.GetToggleValue(rows, cols)
                        else:
                            data = self.Dv_Table1.GetValue(rows, cols)
                            data = data.encode()
                        allitem.append(data)

                    hasil.append(allitem)

                Empty = True
                for value in hasil:
                    if (True in value) == True or ("True" in value) == True:
                        #print value
                        Empty = False
                if Empty == True:
                    print 'NONE HAS CHOOSEN'
                    pass
                elif Empty == False:
                    pass
                    #print hasil

                self.PrcActionPasser("RunProcess", data=hasil)

            elif types == 'CheckedChange':
                if self.Vals == False:
                    self.Vals = True
                    return

                value = self.Dv_Table1.GetToggleValue(kwargs["selected"], 0)
                #print value

                if value == True:
                    hasil = "SELECTED"
                elif value == False:
                    hasil = "PENDING"

                self.Vals = False
                self.Dv_Table1.SetValue(hasil, kwargs["selected"], 2)
                self.PrcOnActivate()

            elif types == 'CheckItem':

                value = self.Dv_Table1.GetToggleValue(kwargs["selected"], 0)
                #print value

                if value == True:
                    self.Dv_Table1.SetToggleValue(False,kwargs["selected"],0)
                elif value == False:
                    self.Dv_Table1.SetToggleValue(True, kwargs["selected"], 0)

                self.PrcOnActivate()


    def PrcOnActivate(self):
        rowcount = [rows for rows in range(self.Dv_Table1.GetItemCount())]
        Checked = list(filter(lambda x: self.Dv_Table1.GetToggleValue(x, 0), rowcount))

        self.Txt_Prc_ChkProcess.SetValue(str(len(Checked)))

    def PrcActionPasser(self, types, **kwargs):
        if types == "LoadConfig":
            pass
        elif types == "RunProcess":
            self.Running_Data = kwargs['data']
            self.Event_Type = "RunProcess1"
            self.Executing_Event = "ON"
            self.Cmd_Prc_Process.Disable()


    def __del__(self):
        pass


