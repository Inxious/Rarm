# create a background image on a wxPython panel
# and show a button on top of the image

import wx
import os
import wx.dataview
from copy import deepcopy
from numpy import mean,array
import copy

class Setup_Process(wx.Frame):
    """class Panel1 creates a panel with an image on it, inherits wx.Panel"""
    def __init__(self, parent, framename):

        # LOAD CONFIG FILE
        self.max_axis1 = int(self.config.get('Scroll Limit', 'max_axis1'))
        self.min_axis1 = int(self.config.get('Scroll Limit', 'min_axis1'))
        self.max_axis2 = int(self.config.get('Scroll Limit', 'max_axis2'))
        self.min_axis2 = int(self.config.get('Scroll Limit', 'min_axis2'))
        self.max_axis3 = int(self.config.get('Scroll Limit', 'max_axis3'))
        self.min_axis3 = int(self.config.get('Scroll Limit', 'min_axis3'))
        self.max_axis4 = int(self.config.get('Scroll Limit', 'max_axis4'))
        self.min_axis4 = int(self.config.get('Scroll Limit', 'min_axis4'))
        self.max_servo = int(self.config.get('Scroll Limit', 'max_servo'))
        self.min_servo = int(self.config.get('Scroll Limit', 'min_servo'))


        # create the panel
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1145, 615), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.FrameObject.update({framename: self})

        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer1 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        #MENU BAR
        self.VMenuBars()
        self.SetMenuBar(self.MenuBar_Main)

        #PANEL CONTROL
        self.StPrcPanelControl(self)
        fgSizer1.Add(self.StPrc_Pnl_Main, 1, wx.ALL | wx.EXPAND, 0)

        #ADDS INS PANEL CONTROL
        self.StPrcIndicator(self.Bit_StPrc_Background_Setup, 0, 480)

        #PANEL VIEW
        self.StPrcPanelView()
        fgSizer1.Add(self.Pnl_StPrc_View, 1, wx.ALL | wx.EXPAND, 0)

        self.SetSizer(fgSizer1)
        self.Layout()

        #LOAD CONSTANT
        self.StPrcStarter()

        #DISABLES
        self.Cmd_StPrc_WidgetUseMouse.Disable()
        self.Cmd_StPrc_WidgetUseController.Disable()

        #EVENTS
        self.SetPrcEvents(framename)

        self.Centre(wx.BOTH)
        self.Show()

    #FRAME PART
    def StPrcIndicator(self, parent, x, y):
        self.Pnl_StPrcIndicator = wx.Panel(parent, id=wx.ID_ANY, pos=wx.Point(x,y), size=wx.Size(626, 95),
                          style=wx.TAB_TRAVERSAL)

        self.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ))

        fgSizer2 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_StPrc_WidgetChild1 = wx.Panel(self.Pnl_StPrcIndicator, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Pnl_StPrc_WidgetChild1.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ))

        fgSizer3 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Lbl_Jdl_StPrc_Widget = wx.StaticText(self.Pnl_StPrc_WidgetChild1, wx.ID_ANY, u"SETUP PROCESS",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_Jdl_StPrc_Widget.Wrap(-1)
        self.Lbl_Jdl_StPrc_Widget.SetFont(wx.Font(18, 74, 90, 92, False, "Arial Black"))
        self.Lbl_Jdl_StPrc_Widget.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        fgSizer3.Add(self.Lbl_Jdl_StPrc_Widget, 0, wx.ALL, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.Cmd_StPrc_WidgetUseMouse = wx.Button(self.Pnl_StPrc_WidgetChild1, wx.ID_ANY, u"Use Mouse",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.Cmd_StPrc_WidgetUseMouse, 0, wx.ALL, 5)

        self.Cmd_StPrc_WidgetUseController = wx.Button(self.Pnl_StPrc_WidgetChild1, wx.ID_ANY, u"Use Controller",
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.Cmd_StPrc_WidgetUseController, 0, wx.ALL, 5)

        fgSizer3.Add(bSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Pnl_StPrc_WidgetChild1.SetSizer(fgSizer3)
        self.Pnl_StPrc_WidgetChild1.Layout()
        fgSizer3.Fit(self.Pnl_StPrc_WidgetChild1)
        fgSizer2.Add(self.Pnl_StPrc_WidgetChild1, 1, wx.EXPAND | wx.ALL, 2)

        self.Pnl_StPrc_WidgetChild2 = wx.Panel(self.Pnl_StPrcIndicator, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        self.Pnl_StPrc_WidgetChild2.SetBackgroundColour(wx.Colour(255, 255, 255))

        gbSizer3 = wx.GridBagSizer(0, 0)
        gbSizer3.SetFlexibleDirection(wx.BOTH)
        gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        gbSizer3.SetMinSize(wx.Size(390, -1))
        self.Lbl_StPrc_WidgetUsedMode = wx.StaticText(self.Pnl_StPrc_WidgetChild2, wx.ID_ANY, u" Used Mode =",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_StPrc_WidgetUsedMode.Wrap(-1)
        gbSizer3.Add(self.Lbl_StPrc_WidgetUsedMode, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_StPrc_WidgetUsedModeView = wx.StaticText(self.Pnl_StPrc_WidgetChild2, wx.ID_ANY, u"-",
                                                          wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_StPrc_WidgetUsedModeView.Wrap(-1)
        self.Lbl_StPrc_WidgetUsedModeView.SetFont(wx.Font(11, 70, 90, 92, False, "Arial"))

        gbSizer3.Add(self.Lbl_StPrc_WidgetUsedModeView, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_StPrc_WidgetControllerStats = wx.StaticText(self.Pnl_StPrc_WidgetChild2, wx.ID_ANY,
                                                             u"Controller Status =", wx.DefaultPosition, wx.DefaultSize,
                                                             0)
        self.Lbl_StPrc_WidgetControllerStats.Wrap(-1)
        gbSizer3.Add(self.Lbl_StPrc_WidgetControllerStats, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_StPrc_WidgetControllerStatsView = wx.StaticText(self.Pnl_StPrc_WidgetChild2, wx.ID_ANY,
                                                                 u"DISCONNECTED", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_StPrc_WidgetControllerStatsView.Wrap(-1)
        self.Lbl_StPrc_WidgetControllerStatsView.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Lbl_StPrc_WidgetControllerStatsView.SetForegroundColour(wx.Colour(255, 4, 4))
        self.Lbl_StPrc_WidgetControllerStatsView.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        gbSizer3.Add(self.Lbl_StPrc_WidgetControllerStatsView, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Pnl_StPrc_WidgetChild2.SetSizer(gbSizer3)
        self.Pnl_StPrc_WidgetChild2.Layout()
        gbSizer3.Fit(self.Pnl_StPrc_WidgetChild2)
        fgSizer2.Add(self.Pnl_StPrc_WidgetChild2, 1, wx.EXPAND | wx.ALL, 2)

        self.Pnl_StPrcIndicator.SetSizer(fgSizer2)
        self.Pnl_StPrcIndicator.Layout()

    #STARTER
    def StPrcStarter(self):

        #START POSITION
        self.Start_Position = {1:None,2:None,3:None,4:None,5:None,6:None}

        #LAST SUDUT VALUE
        self.Checkpoint_Sudut = {1:None,2:None,3:None,4:None,5:None,6:None}

        #STATUS OF IS6
        self.Is6_Status = True

        # SLIDER LAST VALUE
        self.Last_Slider1 = ''
        self.Last_Slider2 = ''
        self.Last_Slider3 = ''
        self.Last_Slider4 = ''
        self.Last_Slider5 = ''
        self.Last_Slider6 = ''

        # focused box
        self.CurrentFocus = ''
        self.NowFocus = self.CurrentFocus

        # BOX 10
        val1 =  int(self.CNows(2, need=1))
        self.StPrc_Spn_Value1.SetRange(self.min_axis1, self.max_axis1)
        self.StPrc_Spn_Value1.SetValue(val1)
        self.StPrc_Spn_Value1.SetIncrement(1)

        datadict = self.CCalculate('SPIN-SLIDER', 1, max=self.StPrc_Spn_Value1.GetMax(),
                                   min=self.StPrc_Spn_Value1.GetMin(),
                                   inc=self.StPrc_Spn_Value1.GetIncrement())

        self.StPrc_Sld_Move1.SetRange(datadict['min'], datadict['max'])
        self.StPrc_Sld_Move1.SetValue(val1)

        # BOX 2
        val2 = int(self.CNows(2, need=2))
        self.StPrc_Spn_Value2.SetRange(self.min_axis2, self.max_axis2)
        self.StPrc_Spn_Value2.SetValue(val2)
        self.StPrc_Spn_Value2.SetIncrement(1)

        datadict = self.CCalculate('SPIN-SLIDER', 1, max=self.StPrc_Spn_Value2.GetMax(),
                                   min=self.StPrc_Spn_Value2.GetMin(),
                                   inc=self.StPrc_Spn_Value2.GetIncrement())

        self.StPrc_Sld_Move2.SetRange(datadict['min'], datadict['max'])
        self.StPrc_Sld_Move2.SetValue(val2)

        # BOX 3
        val3 = int(self.CNows(2, need=3))
        self.StPrc_Spn_Value3.SetRange(self.min_axis3, self.max_axis3)
        self.StPrc_Spn_Value3.SetValue(val3)
        self.StPrc_Spn_Value3.SetIncrement(1)

        datadict = self.CCalculate('SPIN-SLIDER', 1, max=self.StPrc_Spn_Value3.GetMax(),
                                   min=self.StPrc_Spn_Value3.GetMin(),
                                   inc=self.StPrc_Spn_Value3.GetIncrement())

        self.StPrc_Sld_Move3.SetRange(datadict['min'], datadict['max'])
        self.StPrc_Sld_Move3.SetValue(val3)

        # BOX 4
        val4 = int(self.CNows(2, need=4))
        self.StPrc_Spn_Value4.SetRange(self.min_axis4, self.max_axis4)
        self.StPrc_Spn_Value4.SetValue(val4)
        self.StPrc_Spn_Value4.SetIncrement(1)

        datadict = self.CCalculate('SPIN-SLIDER', 1, max=self.StPrc_Spn_Value4.GetMax(),
                                   min=self.StPrc_Spn_Value4.GetMin(),
                                   inc=self.StPrc_Spn_Value4.GetIncrement())

        self.StPrc_Sld_Move4.SetRange(datadict['min'], datadict['max'])
        self.StPrc_Sld_Move4.SetValue(val4)

        # BOX 5
        val5 = int(self.CNows(2, need=5))
        self.StPrc_Spn_Value5.SetRange(self.min_servo, self.max_servo)
        self.StPrc_Spn_Value5.SetValue(val5)
        self.StPrc_Spn_Value5.SetIncrement(1)

        datadict = self.CCalculate('SPIN-SLIDER', 1, max=self.StPrc_Spn_Value5.GetMax(),
                                   min=self.StPrc_Spn_Value5.GetMin(),
                                   inc=self.StPrc_Spn_Value5.GetIncrement())

        self.StPrc_Sld_Move5.SetRange(datadict['min'], datadict['max'])
        self.StPrc_Sld_Move5.SetValue(val5)

        # BOX 6
        val6 = int(self.CNows(2, need=6))
        self.StPrc_Spn_Value6.SetRange(0, 100)
        self.StPrc_Spn_Value6.SetValue(val6)
        self.StPrc_Spn_Value6.SetIncrement(1)

        datadict = self.CCalculate('SPIN-SLIDER', 1, max=self.StPrc_Spn_Value6.GetMax(),
                                   min=self.StPrc_Spn_Value6.GetMin(),
                                   inc=self.StPrc_Spn_Value6.GetIncrement())

        self.StPrc_Sld_Move6.SetRange(datadict['min'], datadict['max'])
        self.StPrc_Sld_Move6.SetValue(val6)

        # Disable Dv Down Button
        self.Cmd_Down_Save.Disable()
        self.Cmd_Down_Delete.Disable()
        self.Cmd_Down_DeleteAll.Disable()
        self.Cmd_Down_CheckDetail.Disable()

        #DATA
        self.StPrcViewConfigH(1)

    #START NEW
    def StPrcDisableStartNew(self):
        #Enable Mode
        self.Cmd_StPrc_WidgetUseMouse.Enable()
        self.Cmd_StPrc_WidgetUseController.Enable()

        #Enable Dv Down Button
        self.Cmd_Down_Save.Enable()
        self.Cmd_Down_Delete.Enable()
        self.Cmd_Down_DeleteAll.Enable()
        self.Cmd_Down_CheckDetail.Enable()

    #EVENT
    def SetPrcEvents(self , framename):
        # ==== SLIDER & SPIN ====
        # 1
        self.StPrc_Spn_Value1.Bind(wx.EVT_SET_FOCUS, lambda x: self.StPrcOnFocus(2, 1))
        self.StPrc_Spn_Value1.Bind(wx.EVT_TEXT, lambda x: self.StPrcOnChange(2, 1))
        self.StPrc_Spn_Value1.Bind(wx.EVT_SPINCTRLDOUBLE, lambda x: self.StPrcOnChange(2, 1))

        self.StPrc_Sld_Move1.Bind(wx.EVT_SET_FOCUS, lambda x: self.StPrcOnFocus(1, 1))
        self.StPrc_Sld_Move1.Bind(wx.EVT_SCROLL_CHANGED, lambda x: self.StPrcOnChange(1, 1))

        self.StPrc_Pnl_Move1.Bind(wx.EVT_SET_FOCUS,
                                lambda x: self.StPrcOnFocus(3, 1, togglevalue=self.Tgl_StPrc_FocusButton1.GetValue()))
        self.Tgl_StPrc_FocusButton1.Bind(wx.EVT_TOGGLEBUTTON, lambda x: self.StPrcOnFocus(3, 1,
                                                                                      togglevalue=self.Tgl_StPrc_FocusButton1.GetValue()))

        # 2
        self.StPrc_Spn_Value2.Bind(wx.EVT_SET_FOCUS, lambda x: self.StPrcOnFocus(2, 2))
        self.StPrc_Spn_Value2.Bind(wx.EVT_TEXT, lambda x: self.StPrcOnChange(2, 2))
        self.StPrc_Spn_Value2.Bind(wx.EVT_SPINCTRLDOUBLE, lambda x: self.StPrcOnChange(2, 2))

        self.Axis1_Handler = self.StPrc_Spn_Value2.GetEventHandler()

        self.StPrc_Sld_Move2.Bind(wx.EVT_SET_FOCUS, lambda x: self.StPrcOnFocus(1, 2))
        self.StPrc_Sld_Move2.Bind(wx.EVT_SCROLL_CHANGED, lambda x: self.StPrcOnChange(1, 2))

        self.StPrc_Pnl_Move2.Bind(wx.EVT_SET_FOCUS,
                                lambda x: self.StPrcOnFocus(3, 2, togglevalue=self.Tgl_StPrc_FocusButton2.GetValue()))
        self.Tgl_StPrc_FocusButton2.Bind(wx.EVT_TOGGLEBUTTON, lambda x: self.StPrcOnFocus(3, 2,
                                                                                      togglevalue=self.Tgl_StPrc_FocusButton2.GetValue()))

        # 3
        self.StPrc_Spn_Value3.Bind(wx.EVT_SET_FOCUS, lambda x: self.StPrcOnFocus(2, 3))
        self.StPrc_Spn_Value3.Bind(wx.EVT_TEXT, lambda x: self.StPrcOnChange(2, 3))
        self.StPrc_Spn_Value3.Bind(wx.EVT_SPINCTRLDOUBLE, lambda x: self.StPrcOnChange(2, 3))

        self.Axis2_Handler = self.StPrc_Spn_Value3.GetEventHandler()

        self.StPrc_Sld_Move3.Bind(wx.EVT_SET_FOCUS, lambda x: self.StPrcOnFocus(1, 3))
        self.StPrc_Sld_Move3.Bind(wx.EVT_SCROLL_CHANGED, lambda x: self.StPrcOnChange(1, 3))

        self.StPrc_Pnl_Move3.Bind(wx.EVT_SET_FOCUS,
                                lambda x: self.StPrcOnFocus(3, 3, togglevalue=self.Tgl_StPrc_FocusButton3.GetValue()))
        self.Tgl_StPrc_FocusButton3.Bind(wx.EVT_TOGGLEBUTTON, lambda x: self.StPrcOnFocus(3, 3,
                                                                                      togglevalue=self.Tgl_StPrc_FocusButton3.GetValue()))

        # 4
        self.StPrc_Spn_Value4.Bind(wx.EVT_SET_FOCUS, lambda x: self.StPrcOnFocus(2, 4))
        self.StPrc_Spn_Value4.Bind(wx.EVT_TEXT, lambda x: self.StPrcOnChange(2, 4))
        self.StPrc_Spn_Value4.Bind(wx.EVT_SPINCTRLDOUBLE, lambda x: self.StPrcOnChange(2, 4))

        self.Axis3_Handler = self.StPrc_Spn_Value4.GetEventHandler()

        self.StPrc_Sld_Move4.Bind(wx.EVT_SET_FOCUS, lambda x: self.StPrcOnFocus(1, 4))
        self.StPrc_Sld_Move4.Bind(wx.EVT_SCROLL_CHANGED, lambda x: self.StPrcOnChange(1, 4))

        self.StPrc_Pnl_Move4.Bind(wx.EVT_SET_FOCUS,
                                lambda x: self.StPrcOnFocus(3, 4, togglevalue=self.Tgl_StPrc_FocusButton4.GetValue()))
        self.Tgl_StPrc_FocusButton4.Bind(wx.EVT_TOGGLEBUTTON, lambda x: self.StPrcOnFocus(3, 4,
                                                                                      togglevalue=self.Tgl_StPrc_FocusButton4.GetValue()))

        # 5
        self.StPrc_Spn_Value5.Bind(wx.EVT_SET_FOCUS, lambda x: self.StPrcOnFocus(2, 5))
        self.StPrc_Spn_Value5.Bind(wx.EVT_TEXT, lambda x: self.StPrcOnChange(2, 5))
        self.StPrc_Spn_Value5.Bind(wx.EVT_SPINCTRLDOUBLE, lambda x: self.StPrcOnChange(2, 5))

        self.StPrc_Sld_Move5.Bind(wx.EVT_SET_FOCUS, lambda x: self.StPrcOnFocus(1, 5))
        self.StPrc_Sld_Move5.Bind(wx.EVT_SCROLL_CHANGED, lambda x: self.StPrcOnChange(1, 5))

        self.StPrc_Pnl_Move5.Bind(wx.EVT_SET_FOCUS,
                                lambda x: self.StPrcOnFocus(3, 5, togglevalue=self.Tgl_StPrc_FocusButton5.GetValue()))
        self.Tgl_StPrc_FocusButton5.Bind(wx.EVT_TOGGLEBUTTON, lambda x: self.StPrcOnFocus(3, 5,
                                                                                      togglevalue=self.Tgl_StPrc_FocusButton5.GetValue()))

        # 6
        self.StPrc_Spn_Value6.Bind(wx.EVT_SET_FOCUS, lambda x: self.StPrcOnFocus(2, 6))
        self.StPrc_Spn_Value6.Bind(wx.EVT_TEXT, lambda x: self.StPrcOnChange(2, 6))
        self.StPrc_Spn_Value6.Bind(wx.EVT_SPINCTRLDOUBLE, lambda x: self.StPrcOnChange(2, 6))

        self.StPrc_Sld_Move6.Bind(wx.EVT_SET_FOCUS, lambda x: self.StPrcOnFocus(1, 6))
        self.StPrc_Sld_Move6.Bind(wx.EVT_SCROLL_CHANGED, lambda x: self.StPrcOnChange(1, 6))

        self.StPrc_Pnl_Move6.Bind(wx.EVT_SET_FOCUS,
                                lambda x: self.StPrcOnFocus(3, 6, togglevalue=self.Tgl_StPrc_FocusButton6.GetValue()))
        self.Tgl_StPrc_FocusButton6.Bind(wx.EVT_TOGGLEBUTTON, lambda x: self.StPrcOnFocus(3, 6,
                                                                                      togglevalue=self.Tgl_StPrc_FocusButton6.GetValue()))

        #ToDo : FrameAction
        self.Cmd_Up_NewProcess.Bind(wx.EVT_BUTTON, lambda x:self.StPrcFrameAction(1))
        self.Cmd_Up_EditProcess.Bind(wx.EVT_BUTTON, lambda x:self.StPrcFrameAction())
        self.Cmd_Up_DeleteProcess.Bind(wx.EVT_BUTTON, lambda x: self.StPrcFrameAction())
        self.Cmd_Up_CancelNew.Bind(wx.EVT_BUTTON, lambda x: self.StPrcFrameAction(6))
        self.Cmd_Down_Save.Bind(wx.EVT_BUTTON, lambda x: self.StPrcFrameAction(2))

        # Connect Events
        self.Cmd_StPrc_WidgetUseMouse.Bind(wx.EVT_BUTTON, lambda x:self.StPrcUseMouse())
        self.Cmd_StPrc_WidgetUseController.Bind(wx.EVT_BUTTON, lambda x:self.StPrcUseController())

    #ACTION
    def StPrcFrameAction(self, mode):
        #NEW PROSES
        if mode == 1:
            #ToDo : Enable & Disable
            #Enable & Disable button
            self.StPrcDisableStartNew()
            self.Cmd_Up_CancelNew.Show()
            self.StPrc_MakingNewProcess = True
            pass

        #SAVE TO Dviewlist
        elif mode == 2:
            #Check if value on slider is same with spinner and self.Nows
            #ToDo : Func
            container_valid = {}
            container_value = {}
            for i in range(6):
                i += 1
                is_valid, val = self.StPrcValuesValidator(i)
                container_valid.update({i:is_valid})
                container_value.update({i:val})


            if len(container_valid) != 6:
                validation = None
                #ToDo : MsgBox
                return
            else:
                validation = deepcopy(container_valid)
                values = deepcopy(container_value)

            list_valid = [x for x in validation.keys()].sort()
            arraydata = {}
            for item in list_valid:
                arraydata.update({item:None})

                if validation[item] == True:
                    sudut = values[item]#0`

                #ToDo : Function To Check If Value Changes or Not
                is_change = True
                if is_change:
                    arraydata[item] = sudut


        #DELETE
        elif mode == 3:
            pass
        #DELETE ALL
        elif mode == 4:
            pass
        #Check Detail
        elif mode == 5:
            pass

        #CANCEL NEW PROCESS
        elif mode == 6:
            # Disable Mode
            self.Cmd_StPrc_WidgetUseMouse.Disable()
            self.Cmd_StPrc_WidgetUseController.Disable()

            # Disable Dv Down Button
            self.Cmd_Down_Save.Disable()
            self.Cmd_Down_Delete.Disable()
            self.Cmd_Down_DeleteAll.Disable()
            self.Cmd_Down_CheckDetail.Disable()

            self.Cmd_Up_CancelNew.Hide()


    #VALIDATOR
    def StPrcValuesValidator(self, mode):
        if mode == 1:
            val1 = self.StPrc_Sld_Move1.GetValue()
            val2 = self.StPrc_Spn_Value1.GetValue()
            val3 = self.CNows(2, need=int(mode))
            data = [int(val1),int(val2),int(val3)]
        elif mode == 2:
            val1 = self.StPrc_Sld_Move2.GetValue()
            val2 = self.StPrc_Spn_Value2.GetValue()
            val3 = self.CNows(2, need=int(mode))
            data = [int(val1),int(val2),int(val3)]
        elif mode == 3:
            val1 = self.StPrc_Sld_Move3.GetValue()
            val2 = self.StPrc_Spn_Value3.GetValue()
            val3 = self.CNows(2, need=int(mode))
            data = [int(val1),int(val2),int(val3)]
        elif mode == 4:
            val1 = self.StPrc_Sld_Move4.GetValue()
            val2 = self.StPrc_Spn_Value4.GetValue()
            val3 = self.CNows(2, need=int(mode))
            data = [int(val1),int(val2),int(val3)]
        elif mode == 5:
            val1 = self.StPrc_Sld_Move5.GetValue()
            val2 = self.StPrc_Spn_Value5.GetValue()
            val3 = self.CNows(2, need=int(mode))
            data = [int(val1),int(val2),int(val3)]
        elif mode == 6:
            val1 = self.StPrc_Sld_Move6.GetValue()
            val2 = self.StPrc_Spn_Value6.GetValue()
            val3 = self.CNows(2, need=int(mode))
            data = [int(val1),int(val2),int(val3)]
            #Made it to Numpy array
            data = array(data)

        if float(val1) != float(data.mean()):
            return ([False,float(val1)])
        else:
            return ([True,float(data.mean())])

    #SET INACTIVE
    def StPrcScrollSetINACT(self, mode):
        if mode == 1:
            self.Txt_StPrc_StatsFocus6.SetLabel('INACTIVE')
            self.Tgl_StPrc_FocusButton6.SetValue(False)
            self.Txt_StPrc_StatsFocus6.SetForegroundColour(wx.Colour(255, 0, 0))
        elif mode == 2:
            self.Txt_StPrc_StatsFocus5.SetLabel('INACTIVE')
            self.Tgl_StPrc_FocusButton5.SetValue(False)
            self.Txt_StPrc_StatsFocus5.SetForegroundColour(wx.Colour(255, 0, 0))
        elif mode == 3:
            self.Txt_StPrc_StatsFocus4.SetLabel('INACTIVE')
            self.Tgl_StPrc_FocusButton4.SetValue(False)
            self.Txt_StPrc_StatsFocus4.SetForegroundColour(wx.Colour(255, 0, 0))
        elif mode == 4:
            self.Txt_StPrc_StatsFocus3.SetLabel('INACTIVE')
            self.Tgl_StPrc_FocusButton3.SetValue(False)
            self.Txt_StPrc_StatsFocus3.SetForegroundColour(wx.Colour(255, 0, 0))
        elif mode == 5:
            self.Txt_StPrc_StatsFocus2.SetLabel('INACTIVE')
            self.Tgl_StPrc_FocusButton2.SetValue(False)
            self.Txt_StPrc_StatsFocus2.SetForegroundColour(wx.Colour(255, 0, 0))
        elif mode == 6:
            self.Txt_StPrc_StatsFocus1.SetLabel('INACTIVE')
            self.Tgl_StPrc_FocusButton1.SetValue(False)
            self.Txt_StPrc_StatsFocus1.SetForegroundColour(wx.Colour(255, 0, 0))

    #ON FOCUS
    def StPrcOnFocus(self, mode, type, **kwargs):
        if mode == 1:
            self.StPrc_CurrentSlider = type
        elif mode == 2:
            self.StPrc_CurrentSpin = type
        elif mode == 3:
            if type == 1:
                self.StPrcScrollSetINACT(mode)
                self.Txt_StPrc_StatsFocus1.SetLabel('ACTIVE')
                self.Txt_StPrc_StatsFocus1.SetForegroundColour(wx.Colour(0, 255, 0))
                self.StPrc_CurrentSlider = type
                self.StPrc_CurrentSpin = type

                # Deactivate
                self.StPrcScrollSetINACT(1)
                self.StPrcScrollSetINACT(2)
                self.StPrcScrollSetINACT(3)
                self.StPrcScrollSetINACT(4)
                self.StPrcScrollSetINACT(5)
                #self.StPrcScrollSetINACT(6)

            elif type == 2:
                self.StPrcScrollSetINACT(mode)
                self.Txt_StPrc_StatsFocus2.SetLabel('ACTIVE')
                self.Txt_StPrc_StatsFocus2.SetForegroundColour(wx.Colour(0, 255, 0))
                self.StPrc_CurrentSlider = type
                self.StPrc_CurrentSpin = type

                # Deactivate
                self.StPrcScrollSetINACT(1)
                self.StPrcScrollSetINACT(2)
                self.StPrcScrollSetINACT(3)
                self.StPrcScrollSetINACT(4)
                #self.StPrcScrollSetINACT(5)
                self.StPrcScrollSetINACT(6)

            elif type == 3:
                self.StPrcScrollSetINACT(mode)
                self.Txt_StPrc_StatsFocus3.SetLabel('ACTIVE')
                self.Txt_StPrc_StatsFocus3.SetForegroundColour(wx.Colour(0, 255, 0))
                self.StPrc_CurrentSlider = type
                self.StPrc_CurrentSpin = type

                # Deactivate
                self.StPrcScrollSetINACT(1)
                self.StPrcScrollSetINACT(2)
                self.StPrcScrollSetINACT(3)
                #self.StPrcScrollSetINACT(4)
                self.StPrcScrollSetINACT(5)
                self.StPrcScrollSetINACT(6)

            elif type == 4:
                self.StPrcScrollSetINACT(mode)
                self.Txt_StPrc_StatsFocus4.SetLabel('ACTIVE')
                self.Txt_StPrc_StatsFocus4.SetForegroundColour(wx.Colour(0, 255, 0))
                self.StPrc_CurrentSlider = type
                self.StPrc_CurrentSpin = type

                # Deactivate
                self.StPrcScrollSetINACT(1)
                self.StPrcScrollSetINACT(2)
                #self.StPrcScrollSetINACT(3)
                self.StPrcScrollSetINACT(4)
                self.StPrcScrollSetINACT(5)
                self.StPrcScrollSetINACT(6)

            elif type == 5:
                self.StPrcScrollSetINACT(mode)
                self.Txt_StPrc_StatsFocus5.SetLabel('ACTIVE')
                self.Txt_StPrc_StatsFocus5.SetForegroundColour(wx.Colour(0, 255, 0))
                self.StPrc_CurrentSlider = type
                self.StPrc_CurrentSpin = type

                # Deactivate
                self.StPrcScrollSetINACT(1)
                #self.StPrcScrollSetINACT(2)
                self.StPrcScrollSetINACT(3)
                self.StPrcScrollSetINACT(4)
                self.StPrcScrollSetINACT(5)
                self.StPrcScrollSetINACT(6)

            elif type == 6:
                self.StPrcScrollSetINACT(mode)
                self.Txt_StPrc_StatsFocus6.SetLabel('ACTIVE')
                self.Txt_StPrc_StatsFocus6.SetForegroundColour(wx.Colour(0, 255, 0))
                self.StPrc_CurrentSlider = type
                self.StPrc_CurrentSpin = type

                #Deactivate
                #self.StPrcScrollSetINACT(1)
                self.StPrcScrollSetINACT(2)
                self.StPrcScrollSetINACT(3)
                self.StPrcScrollSetINACT(4)
                self.StPrcScrollSetINACT(5)
                self.StPrcScrollSetINACT(6)

        self.CurrentFocus = type

    #ON CHANGE
    def StPrcOnChange(self, mode , type):
        #SLIDER MOVEMENT
        self.StPrc_CurrentSlider = type
        self.StPrc_CurrentSpin = type
        self.CurrentFocus = self.StPrc_CurrentSlider

        if mode == 1:
            if self.StPrc_CurrentSlider == 1:
                self.StPrcOnFocus(3, 1, togglevalue=self.Tgl_StPrc_FocusButton1.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 3, value=self.StPrc_Sld_Move1.GetValue(),
                                         inc=self.StPrc_Spn_Value1.GetIncrement())
                self.StPrc_Spn_Value1.SetValue(values)

            elif self.StPrc_CurrentSlider == 2:
                self.StPrcOnFocus(3, 2, togglevalue=self.Tgl_StPrc_FocusButton2.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 3, value=self.StPrc_Sld_Move2.GetValue(),
                                         inc=self.StPrc_Spn_Value2.GetIncrement())
                self.StPrc_Spn_Value2.SetValue(values)

            elif self.StPrc_CurrentSlider == 3:
                self.StPrcOnFocus(3, 3, togglevalue=self.Tgl_StPrc_FocusButton3.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 3, value=self.StPrc_Sld_Move3.GetValue(),
                                         inc=self.StPrc_Spn_Value3.GetIncrement())
                self.StPrc_Spn_Value3.SetValue(values)

            elif self.StPrc_CurrentSlider == 4:
                self.StPrcOnFocus(3, 4, togglevalue=self.Tgl_StPrc_FocusButton4.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 3, value=self.StPrc_Sld_Move4.GetValue(),
                                         inc=self.StPrc_Spn_Value4.GetIncrement())
                self.StPrc_Spn_Value4.SetValue(values)

            elif self.StPrc_CurrentSlider == 5:
                self.StPrcOnFocus(3, 5, togglevalue=self.Tgl_StPrc_FocusButton5.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 3, value=self.StPrc_Sld_Move5.GetValue(),
                                         inc=self.StPrc_Spn_Value5.GetIncrement())
                self.StPrc_Spn_Value5.SetValue(values)

            elif self.StPrc_CurrentSlider == 6:
                self.StPrcOnFocus(3, 6, togglevalue=self.Tgl_StPrc_FocusButton6.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 3, value=self.StPrc_Sld_Move6.GetValue(),
                                         inc=self.StPrc_Spn_Value6.GetIncrement())
                self.StPrc_Spn_Value6.SetValue(values)
            else:
                return

            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message=('value sld>>spn [' + str(self.StPrc_CurrentSlider)+'] = ' + str(values)))

        elif mode == 2:

            if self.StPrc_CurrentSpin == 1:
                self.StPrcOnFocus(3, 1, togglevalue=self.Tgl_StPrc_FocusButton1.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 2, value=self.StPrc_Spn_Value1.GetValue(),
                                         inc=self.StPrc_Spn_Value6.GetIncrement())
                self.StPrc_Sld_Move1.SetValue(values)

            elif self.StPrc_CurrentSpin == 2:
                self.StPrcOnFocus(3, 2, togglevalue=self.Tgl_StPrc_FocusButton2.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 2, value=self.StPrc_Spn_Value2.GetValue(),
                                         inc=self.StPrc_Spn_Value2.GetIncrement())
                self.StPrc_Sld_Move2.SetValue(values)

            elif self.StPrc_CurrentSpin == 3:
                self.StPrcOnFocus(3, 3, togglevalue=self.Tgl_StPrc_FocusButton3.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 2, value=self.StPrc_Spn_Value3.GetValue(),
                                         inc=self.StPrc_Spn_Value3.GetIncrement())
                self.StPrc_Sld_Move3.SetValue(values)

            elif self.StPrc_CurrentSpin == 4:
                self.StPrcOnFocus(3, 4 , togglevalue=self.Tgl_StPrc_FocusButton4.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 2, value=self.StPrc_Spn_Value4.GetValue(),
                                         inc=self.StPrc_Spn_Value4.GetIncrement())
                self.StPrc_Sld_Move4.SetValue(values)

            elif self.StPrc_CurrentSpin== 5:
                self.StPrcOnFocus(3, 5, togglevalue=self.Tgl_StPrc_FocusButton5.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 2, value=self.StPrc_Spn_Value5.GetValue(),
                                         inc=self.StPrc_Spn_Value5.GetIncrement())
                self.StPrc_Sld_Move5.SetValue(values)

            elif self.StPrc_CurrentSpin == 6:
                self.StPrcOnFocus(3, 6, togglevalue=self.Tgl_StPrc_FocusButton6.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 2, value=self.StPrc_Spn_Value6.GetValue(),
                                         inc=self.StPrc_Spn_Value6.GetIncrement())
                self.StPrc_Sld_Move6.SetValue(values)
            else:
                return

            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message=('value spn>>sld ['+str(self.StPrc_CurrentSpin)+'] = ' + str(values)))

    #PANEL CONTROL
    def StPrcPanelControl(self, parent):
        self.StPrc_Pnl_Main = wx.Panel(parent, wx.ID_ANY, wx.DefaultPosition, wx.Size(720, -1), wx.TAB_TRAVERSAL)

        try:
            # pick an image file you have in the working folder

            # you can load .jpg  .png  .bmp  or .gif files
            image_file = os.path.normpath('.\\images\\background.png')
            bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()

            # image's upper left corner anchors at panel coordinates (0, 0)
            self.Bit_StPrc_Background_Setup = wx.StaticBitmap(self.StPrc_Pnl_Main, -1, bmp1, pos=(0, 0))

            # show some image details
            str1 = "%s  %dx%d" % (image_file, bmp1.GetWidth(), bmp1.GetHeight())

        except IOError:
            print "Image file %s not found" % image_file
            raise SystemExit

        # button goes on the image --> self.bitmap1 is the parent
        # PANEL 1
        self.StPrc_Pnl_Move6 = wx.Panel(self.Bit_StPrc_Background_Setup, wx.ID_ANY, wx.Point(10, 120), wx.Size(170, 60),
                                      wx.TAB_TRAVERSAL)
        # SET ID BASED BY MOTOR ID
        self.StPrc_Pnl_Move6.SetId(1)
        self.StPrc_Pnl_Move6.SetBackgroundColour(wx.Colour(255, 255, 255))

        fgSizer17 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer17.SetFlexibleDirection(wx.BOTH)
        fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_StPrcStats6 = wx.Panel(self.StPrc_Pnl_Move6, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                      wx.TAB_TRAVERSAL)
        self.Pnl_StPrcStats6.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        fgSizer18 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer18.SetFlexibleDirection(wx.BOTH)
        fgSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Tgl_StPrc_FocusButton6 = wx.ToggleButton(self.Pnl_StPrcStats6, wx.ID_ANY, u"6", wx.DefaultPosition,
                                                    wx.Size(50, 50), 0)
        self.Tgl_StPrc_FocusButton6.SetValue(False)
        self.Tgl_StPrc_FocusButton6.SetFont(wx.Font(36, 74, 90, 92, False, "Arial"))
        self.Tgl_StPrc_FocusButton6.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer18.Add(self.Tgl_StPrc_FocusButton6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.Txt_StPrc_StatsFocus6 = wx.StaticText(self.Pnl_StPrcStats6, wx.ID_ANY, u"INACTIVE", wx.DefaultPosition,
                                                 wx.Size(70, 15), wx.ALIGN_CENTRE)
        self.Txt_StPrc_StatsFocus6.Wrap(-1)
        self.Txt_StPrc_StatsFocus6.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Txt_StPrc_StatsFocus6.SetForegroundColour(wx.Colour(255, 0, 0))
        self.Txt_StPrc_StatsFocus6.SetBackgroundColour(wx.Colour(0, 0, 0))

        fgSizer18.Add(self.Txt_StPrc_StatsFocus6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Pnl_StPrcStats6.SetSizer(fgSizer18)
        self.Pnl_StPrcStats6.Layout()
        fgSizer18.Fit(self.Pnl_StPrcStats6)
        fgSizer17.Add(self.Pnl_StPrcStats6, 1, wx.EXPAND | wx.ALL, 0)

        self.Pnl_StPrc_Scroll6 = wx.Panel(self.StPrc_Pnl_Move6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        self.Pnl_StPrc_Scroll6.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer19 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer19.SetFlexibleDirection(wx.BOTH)
        fgSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer19.SetMinSize(wx.Size(-1, 80))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.Lbl_StPrc_Jdl_Sudut6 = wx.StaticText(self.Pnl_StPrc_Scroll6, wx.ID_ANY, u"Sudut Axis", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.Lbl_StPrc_Jdl_Sudut6.Wrap(-1)
        self.Lbl_StPrc_Jdl_Sudut6.SetFont(wx.Font(10, 74, 90, 92, False, "Arial"))

        bSizer9.Add(self.Lbl_StPrc_Jdl_Sudut6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.StPrc_Sld_Move6 = wx.Slider(self.Pnl_StPrc_Scroll6, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition,
                                       wx.Size(130, 20),
                                       wx.SL_HORIZONTAL)
        bSizer9.Add(self.StPrc_Sld_Move6, 0, wx.ALL, 5)

        self.StPrc_Spn_Value6 = wx.SpinCtrlDouble(self.Pnl_StPrc_Scroll6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer9.Add(self.StPrc_Spn_Value6, 0, wx.ALL, 5)

        fgSizer19.Add(bSizer9, 1, wx.EXPAND, 5)

        self.Pnl_StPrc_Scroll6.SetSizer(fgSizer19)
        self.Pnl_StPrc_Scroll6.Layout()
        fgSizer19.Fit(self.Pnl_StPrc_Scroll6)
        fgSizer17.Add(self.Pnl_StPrc_Scroll6, 1, wx.EXPAND | wx.ALL, 0)

        self.StPrc_Pnl_Move6.SetSizer(fgSizer17)
        self.StPrc_Pnl_Move6.Layout()
        fgSizer17.Fit(self.StPrc_Pnl_Move6)

        # PANEL 2
        self.StPrc_Pnl_Move5 = wx.Panel(self.Bit_StPrc_Background_Setup, wx.ID_ANY, wx.Point(375, 10), wx.Size(170, 60),
                                      wx.TAB_TRAVERSAL)
        # SET ID BASED BY MOTOR ID
        self.StPrc_Pnl_Move5.SetId(2)
        self.StPrc_Pnl_Move5.SetBackgroundColour(wx.Colour(255, 255, 255))

        fgSizer17 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer17.SetFlexibleDirection(wx.BOTH)
        fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_StPrcStats5 = wx.Panel(self.StPrc_Pnl_Move5, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                      wx.TAB_TRAVERSAL)
        self.Pnl_StPrcStats5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        fgSizer18 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer18.SetFlexibleDirection(wx.BOTH)
        fgSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Tgl_StPrc_FocusButton5 = wx.ToggleButton(self.Pnl_StPrcStats5, wx.ID_ANY, u"5", wx.DefaultPosition,
                                                    wx.Size(50, 50), 0)
        self.Tgl_StPrc_FocusButton5.SetValue(False)
        self.Tgl_StPrc_FocusButton5.SetFont(wx.Font(36, 74, 90, 92, False, "Arial"))
        self.Tgl_StPrc_FocusButton5.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer18.Add(self.Tgl_StPrc_FocusButton5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.Txt_StPrc_StatsFocus5 = wx.StaticText(self.Pnl_StPrcStats5, wx.ID_ANY, u"INACTIVE", wx.DefaultPosition,
                                                 wx.Size(70, 15), wx.ALIGN_CENTRE)
        self.Txt_StPrc_StatsFocus5.Wrap(-1)
        self.Txt_StPrc_StatsFocus5.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Txt_StPrc_StatsFocus5.SetForegroundColour(wx.Colour(255, 0, 0))
        self.Txt_StPrc_StatsFocus5.SetBackgroundColour(wx.Colour(0, 0, 0))

        fgSizer18.Add(self.Txt_StPrc_StatsFocus5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Pnl_StPrcStats5.SetSizer(fgSizer18)
        self.Pnl_StPrcStats5.Layout()
        fgSizer18.Fit(self.Pnl_StPrcStats5)
        fgSizer17.Add(self.Pnl_StPrcStats5, 1, wx.EXPAND | wx.ALL, 0)

        self.Pnl_StPrc_Scroll5 = wx.Panel(self.StPrc_Pnl_Move5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        self.Pnl_StPrc_Scroll5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer19 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer19.SetFlexibleDirection(wx.BOTH)
        fgSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer19.SetMinSize(wx.Size(-1, 80))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.Lbl_StPrc_Jdl_Sudut5 = wx.StaticText(self.Pnl_StPrc_Scroll5, wx.ID_ANY, u"Sudut Axis", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.Lbl_StPrc_Jdl_Sudut5.Wrap(-1)
        self.Lbl_StPrc_Jdl_Sudut5.SetFont(wx.Font(10, 74, 90, 92, False, "Arial"))

        bSizer9.Add(self.Lbl_StPrc_Jdl_Sudut5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.StPrc_Sld_Move5 = wx.Slider(self.Pnl_StPrc_Scroll5, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition,
                                       wx.Size(130, 20),
                                       wx.SL_HORIZONTAL)
        bSizer9.Add(self.StPrc_Sld_Move5, 0, wx.ALL, 5)

        self.StPrc_Spn_Value5 = wx.SpinCtrlDouble(self.Pnl_StPrc_Scroll5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer9.Add(self.StPrc_Spn_Value5, 0, wx.ALL, 5)

        fgSizer19.Add(bSizer9, 1, wx.EXPAND, 5)

        self.Pnl_StPrc_Scroll5.SetSizer(fgSizer19)
        self.Pnl_StPrc_Scroll5.Layout()
        fgSizer19.Fit(self.Pnl_StPrc_Scroll5)
        fgSizer17.Add(self.Pnl_StPrc_Scroll5, 1, wx.EXPAND | wx.ALL, 0)

        self.StPrc_Pnl_Move5.SetSizer(fgSizer17)
        self.StPrc_Pnl_Move5.Layout()
        fgSizer17.Fit(self.StPrc_Pnl_Move5)

        # PANEL 3
        self.StPrc_Pnl_Move4 = wx.Panel(self.Bit_StPrc_Background_Setup, wx.ID_ANY, wx.Point(55, 235), wx.Size(170, 60),
                                      wx.TAB_TRAVERSAL)
        # SET ID BASED BY MOTOR ID
        self.StPrc_Pnl_Move4.SetId(3)
        self.StPrc_Pnl_Move4.SetBackgroundColour(wx.Colour(255, 255, 255))

        fgSizer17 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer17.SetFlexibleDirection(wx.BOTH)
        fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_StPrcStats4 = wx.Panel(self.StPrc_Pnl_Move4, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                      wx.TAB_TRAVERSAL)
        self.Pnl_StPrcStats4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        fgSizer18 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer18.SetFlexibleDirection(wx.BOTH)
        fgSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Tgl_StPrc_FocusButton4 = wx.ToggleButton(self.Pnl_StPrcStats4, wx.ID_ANY, u"4", wx.DefaultPosition,
                                                    wx.Size(50, 50), 0)
        self.Tgl_StPrc_FocusButton4.SetValue(False)
        self.Tgl_StPrc_FocusButton4.SetFont(wx.Font(36, 74, 90, 92, False, "Arial"))
        self.Tgl_StPrc_FocusButton4.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer18.Add(self.Tgl_StPrc_FocusButton4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.Txt_StPrc_StatsFocus4 = wx.StaticText(self.Pnl_StPrcStats4, wx.ID_ANY, u"INACTIVE", wx.DefaultPosition,
                                                 wx.Size(70, 15), wx.ALIGN_CENTRE)
        self.Txt_StPrc_StatsFocus4.Wrap(-1)
        self.Txt_StPrc_StatsFocus4.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Txt_StPrc_StatsFocus4.SetForegroundColour(wx.Colour(255, 0, 0))
        self.Txt_StPrc_StatsFocus4.SetBackgroundColour(wx.Colour(0, 0, 0))

        fgSizer18.Add(self.Txt_StPrc_StatsFocus4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Pnl_StPrcStats4.SetSizer(fgSizer18)
        self.Pnl_StPrcStats4.Layout()
        fgSizer18.Fit(self.Pnl_StPrcStats4)
        fgSizer17.Add(self.Pnl_StPrcStats4, 1, wx.EXPAND | wx.ALL, 0)

        self.Pnl_StPrc_Scroll4 = wx.Panel(self.StPrc_Pnl_Move4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        self.Pnl_StPrc_Scroll4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer19 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer19.SetFlexibleDirection(wx.BOTH)
        fgSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer19.SetMinSize(wx.Size(-1, 80))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.Lbl_StPrc_Jdl_Sudut4 = wx.StaticText(self.Pnl_StPrc_Scroll4, wx.ID_ANY, u"Sudut Axis", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.Lbl_StPrc_Jdl_Sudut4.Wrap(-1)
        self.Lbl_StPrc_Jdl_Sudut4.SetFont(wx.Font(10, 74, 90, 92, False, "Arial"))

        bSizer9.Add(self.Lbl_StPrc_Jdl_Sudut4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.StPrc_Sld_Move4 = wx.Slider(self.Pnl_StPrc_Scroll4, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition,
                                       wx.Size(130, 20),
                                       wx.SL_HORIZONTAL)
        bSizer9.Add(self.StPrc_Sld_Move4, 0, wx.ALL, 5)

        self.StPrc_Spn_Value4 = wx.SpinCtrlDouble(self.Pnl_StPrc_Scroll4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer9.Add(self.StPrc_Spn_Value4, 0, wx.ALL, 5)

        fgSizer19.Add(bSizer9, 1, wx.EXPAND, 5)

        self.Pnl_StPrc_Scroll4.SetSizer(fgSizer19)
        self.Pnl_StPrc_Scroll4.Layout()
        fgSizer19.Fit(self.Pnl_StPrc_Scroll4)
        fgSizer17.Add(self.Pnl_StPrc_Scroll4, 1, wx.EXPAND | wx.ALL, 0)

        self.StPrc_Pnl_Move4.SetSizer(fgSizer17)
        self.StPrc_Pnl_Move4.Layout()
        fgSizer17.Fit(self.StPrc_Pnl_Move4)

        # PANEL 4
        self.StPrc_Pnl_Move3 = wx.Panel(self.Bit_StPrc_Background_Setup, wx.ID_ANY, wx.Point(455, 125), wx.Size(170, 60),
                                      wx.TAB_TRAVERSAL)
        # SET ID BASED BY MOTOR ID
        self.StPrc_Pnl_Move3.SetId(4)
        self.StPrc_Pnl_Move3.SetBackgroundColour(wx.Colour(255, 255, 255))

        fgSizer17 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer17.SetFlexibleDirection(wx.BOTH)
        fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_StPrcStats3 = wx.Panel(self.StPrc_Pnl_Move3, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                      wx.TAB_TRAVERSAL)
        self.Pnl_StPrcStats3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        fgSizer18 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer18.SetFlexibleDirection(wx.BOTH)
        fgSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Tgl_StPrc_FocusButton3 = wx.ToggleButton(self.Pnl_StPrcStats3, wx.ID_ANY, u"3", wx.DefaultPosition,
                                                    wx.Size(50, 50), 0)
        self.Tgl_StPrc_FocusButton3.SetValue(False)
        self.Tgl_StPrc_FocusButton3.SetFont(wx.Font(36, 74, 90, 92, False, "Arial"))
        self.Tgl_StPrc_FocusButton3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer18.Add(self.Tgl_StPrc_FocusButton3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.Txt_StPrc_StatsFocus3 = wx.StaticText(self.Pnl_StPrcStats3, wx.ID_ANY, u"INACTIVE", wx.DefaultPosition,
                                                 wx.Size(70, 15), wx.ALIGN_CENTRE)
        self.Txt_StPrc_StatsFocus3.Wrap(-1)
        self.Txt_StPrc_StatsFocus3.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Txt_StPrc_StatsFocus3.SetForegroundColour(wx.Colour(255, 0, 0))
        self.Txt_StPrc_StatsFocus3.SetBackgroundColour(wx.Colour(0, 0, 0))

        fgSizer18.Add(self.Txt_StPrc_StatsFocus3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Pnl_StPrcStats3.SetSizer(fgSizer18)
        self.Pnl_StPrcStats3.Layout()
        fgSizer18.Fit(self.Pnl_StPrcStats3)
        fgSizer17.Add(self.Pnl_StPrcStats3, 1, wx.EXPAND | wx.ALL, 0)

        self.Pnl_StPrc_Scroll3 = wx.Panel(self.StPrc_Pnl_Move3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        self.Pnl_StPrc_Scroll3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer19 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer19.SetFlexibleDirection(wx.BOTH)
        fgSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer19.SetMinSize(wx.Size(-1, 80))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.Lbl_StPrc_Jdl_Sudut3 = wx.StaticText(self.Pnl_StPrc_Scroll3, wx.ID_ANY, u"Sudut Axis", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.Lbl_StPrc_Jdl_Sudut3.Wrap(-1)
        self.Lbl_StPrc_Jdl_Sudut3.SetFont(wx.Font(10, 74, 90, 92, False, "Arial"))

        bSizer9.Add(self.Lbl_StPrc_Jdl_Sudut3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.StPrc_Sld_Move3 = wx.Slider(self.Pnl_StPrc_Scroll3, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition,
                                       wx.Size(130, 20),
                                       wx.SL_HORIZONTAL)
        bSizer9.Add(self.StPrc_Sld_Move3, 0, wx.ALL, 5)

        self.StPrc_Spn_Value3 = wx.SpinCtrlDouble(self.Pnl_StPrc_Scroll3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer9.Add(self.StPrc_Spn_Value3, 0, wx.ALL, 5)

        fgSizer19.Add(bSizer9, 1, wx.EXPAND, 5)

        self.Pnl_StPrc_Scroll3.SetSizer(fgSizer19)
        self.Pnl_StPrc_Scroll3.Layout()
        fgSizer19.Fit(self.Pnl_StPrc_Scroll3)
        fgSizer17.Add(self.Pnl_StPrc_Scroll3, 1, wx.EXPAND | wx.ALL, 0)

        self.StPrc_Pnl_Move3.SetSizer(fgSizer17)
        self.StPrc_Pnl_Move3.Layout()
        fgSizer17.Fit(self.StPrc_Pnl_Move3)

        # PANEL 5
        self.StPrc_Pnl_Move2 = wx.Panel(self.Bit_StPrc_Background_Setup, wx.ID_ANY, wx.Point(20, 360), wx.Size(170, 60),
                                      wx.TAB_TRAVERSAL)
        # SET ID BASED BY MOTOR ID
        self.StPrc_Pnl_Move2.SetId(5)
        self.StPrc_Pnl_Move2.SetBackgroundColour(wx.Colour(255, 255, 255))

        fgSizer17 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer17.SetFlexibleDirection(wx.BOTH)
        fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_StPrcStats2 = wx.Panel(self.StPrc_Pnl_Move2, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                      wx.TAB_TRAVERSAL)
        self.Pnl_StPrcStats2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        fgSizer18 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer18.SetFlexibleDirection(wx.BOTH)
        fgSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Tgl_StPrc_FocusButton2 = wx.ToggleButton(self.Pnl_StPrcStats2, wx.ID_ANY, u"2", wx.DefaultPosition,
                                                    wx.Size(50, 50), 0)
        self.Tgl_StPrc_FocusButton2.SetValue(False)
        self.Tgl_StPrc_FocusButton2.SetFont(wx.Font(36, 74, 90, 92, False, "Arial"))
        self.Tgl_StPrc_FocusButton2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer18.Add(self.Tgl_StPrc_FocusButton2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.Txt_StPrc_StatsFocus2 = wx.StaticText(self.Pnl_StPrcStats2, wx.ID_ANY, u"INACTIVE", wx.DefaultPosition,
                                                 wx.Size(70, 15), wx.ALIGN_CENTRE)
        self.Txt_StPrc_StatsFocus2.Wrap(-1)
        self.Txt_StPrc_StatsFocus2.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Txt_StPrc_StatsFocus2.SetForegroundColour(wx.Colour(255, 0, 0))
        self.Txt_StPrc_StatsFocus2.SetBackgroundColour(wx.Colour(0, 0, 0))

        fgSizer18.Add(self.Txt_StPrc_StatsFocus2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Pnl_StPrcStats2.SetSizer(fgSizer18)
        self.Pnl_StPrcStats2.Layout()
        fgSizer18.Fit(self.Pnl_StPrcStats2)
        fgSizer17.Add(self.Pnl_StPrcStats2, 1, wx.EXPAND | wx.ALL, 0)

        self.Pnl_StPrc_Scroll2 = wx.Panel(self.StPrc_Pnl_Move2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        self.Pnl_StPrc_Scroll2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer19 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer19.SetFlexibleDirection(wx.BOTH)
        fgSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer19.SetMinSize(wx.Size(-1, 80))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.Lbl_StPrc_Jdl_Sudut2 = wx.StaticText(self.Pnl_StPrc_Scroll2, wx.ID_ANY, u"Sudut Axis", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.Lbl_StPrc_Jdl_Sudut2.Wrap(-1)
        self.Lbl_StPrc_Jdl_Sudut2.SetFont(wx.Font(10, 74, 90, 92, False, "Arial"))

        bSizer9.Add(self.Lbl_StPrc_Jdl_Sudut2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.StPrc_Sld_Move2 = wx.Slider(self.Pnl_StPrc_Scroll2, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition,
                                       wx.Size(130, 20),
                                       wx.SL_HORIZONTAL)
        bSizer9.Add(self.StPrc_Sld_Move2, 0, wx.ALL, 5)

        self.StPrc_Spn_Value2 = wx.SpinCtrlDouble(self.Pnl_StPrc_Scroll2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer9.Add(self.StPrc_Spn_Value2, 0, wx.ALL, 5)

        fgSizer19.Add(bSizer9, 1, wx.EXPAND, 5)

        self.Pnl_StPrc_Scroll2.SetSizer(fgSizer19)
        self.Pnl_StPrc_Scroll2.Layout()
        fgSizer19.Fit(self.Pnl_StPrc_Scroll2)
        fgSizer17.Add(self.Pnl_StPrc_Scroll2, 1, wx.EXPAND | wx.ALL, 0)

        self.StPrc_Pnl_Move2.SetSizer(fgSizer17)
        self.StPrc_Pnl_Move2.Layout()
        fgSizer17.Fit(self.StPrc_Pnl_Move2)

        # PANEL 6
        self.StPrc_Pnl_Move1 = wx.Panel(self.Bit_StPrc_Background_Setup, wx.ID_ANY, wx.Point(450, 280), wx.Size(170, 60),
                                      wx.TAB_TRAVERSAL)
        # SET ID BASED BY MOTOR ID
        self.StPrc_Pnl_Move1.SetId(6)
        self.StPrc_Pnl_Move1.SetBackgroundColour(wx.Colour(255, 255, 255))

        fgSizer17 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer17.SetFlexibleDirection(wx.BOTH)
        fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_StPrcStats1 = wx.Panel(self.StPrc_Pnl_Move1, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                      wx.TAB_TRAVERSAL)
        self.Pnl_StPrcStats1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        fgSizer18 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer18.SetFlexibleDirection(wx.BOTH)
        fgSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Tgl_StPrc_FocusButton1 = wx.ToggleButton(self.Pnl_StPrcStats1, wx.ID_ANY, u"1", wx.DefaultPosition,
                                                    wx.Size(50, 50), 0)
        self.Tgl_StPrc_FocusButton1.SetValue(False)
        self.Tgl_StPrc_FocusButton1.SetFont(wx.Font(36, 74, 90, 92, False, "Arial"))
        self.Tgl_StPrc_FocusButton1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer18.Add(self.Tgl_StPrc_FocusButton1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.Txt_StPrc_StatsFocus1 = wx.StaticText(self.Pnl_StPrcStats1, wx.ID_ANY, u"INACTIVE", wx.DefaultPosition,
                                                 wx.Size(70, 15), wx.ALIGN_CENTRE)
        self.Txt_StPrc_StatsFocus1.Wrap(-1)
        self.Txt_StPrc_StatsFocus1.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Txt_StPrc_StatsFocus1.SetForegroundColour(wx.Colour(255, 0, 0))
        self.Txt_StPrc_StatsFocus1.SetBackgroundColour(wx.Colour(0, 0, 0))

        fgSizer18.Add(self.Txt_StPrc_StatsFocus1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Pnl_StPrcStats1.SetSizer(fgSizer18)
        self.Pnl_StPrcStats1.Layout()
        fgSizer18.Fit(self.Pnl_StPrcStats1)
        fgSizer17.Add(self.Pnl_StPrcStats1, 1, wx.EXPAND | wx.ALL, 0)

        self.Pnl_StPrc_Scroll1 = wx.Panel(self.StPrc_Pnl_Move1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        self.Pnl_StPrc_Scroll1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer19 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer19.SetFlexibleDirection(wx.BOTH)
        fgSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer19.SetMinSize(wx.Size(-1, 80))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.Lbl_StPrc_Jdl_Sudut1 = wx.StaticText(self.Pnl_StPrc_Scroll1, wx.ID_ANY, u"Sudut Axis", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.Lbl_StPrc_Jdl_Sudut1.Wrap(-1)
        self.Lbl_StPrc_Jdl_Sudut1.SetFont(wx.Font(10, 74, 90, 92, False, "Arial"))

        bSizer9.Add(self.Lbl_StPrc_Jdl_Sudut1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.StPrc_Sld_Move1 = wx.Slider(self.Pnl_StPrc_Scroll1, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition,
                                       wx.Size(130, 20),
                                       wx.SL_HORIZONTAL)
        bSizer9.Add(self.StPrc_Sld_Move1, 0, wx.ALL, 5)

        self.StPrc_Spn_Value1 = wx.SpinCtrlDouble(self.Pnl_StPrc_Scroll1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer9.Add(self.StPrc_Spn_Value1, 0, wx.ALL, 5)

        fgSizer19.Add(bSizer9, 1, wx.EXPAND, 5)

        self.Pnl_StPrc_Scroll1.SetSizer(fgSizer19)
        self.Pnl_StPrc_Scroll1.Layout()
        fgSizer19.Fit(self.Pnl_StPrc_Scroll1)
        fgSizer17.Add(self.Pnl_StPrc_Scroll1, 1, wx.EXPAND | wx.ALL, 0)

        self.StPrc_Pnl_Move1.SetSizer(fgSizer17)
        self.StPrc_Pnl_Move1.Layout()
        fgSizer17.Fit(self.StPrc_Pnl_Move1)

    #PANEL VIEW
    def StPrcPanelView(self):
        self.Pnl_StPrc_View = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,600),
                                   wx.TAB_TRAVERSAL | wx.TRANSPARENT_WINDOW)


        if self.Pnl_StPrc_View.CanSetTransparent:
            print 'can'
            self.Pnl_StPrc_View.SetTransparent(100)
        else:
            print 'cant'

        try:
            # pick an image file you have in the working folder
            # you can load .jpg  .png  .bmp  or .gif files
            image_file = os.path.normpath('.\\images\\background2.png')
            bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            # image's upper left corner anchors at panel coordinates (0, 0)
            self.Bit_StPrc_Background_Setup2 = wx.StaticBitmap(self.Pnl_StPrc_View, -1, bmp1, pos=(0, 0))
            # show some image details
            str1 = "%s  %dx%d" % (image_file, bmp1.GetWidth(), bmp1.GetHeight())

        except IOError:
            print "Image file %s not found" % image_file
            raise SystemExit

        self.Pnl_StPrc_View.SetBackgroundColour(wx.Colour(152, 155, 175))

        fgSizer2 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer3 = wx.FlexGridSizer(3, 1, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer6 = wx.FlexGridSizer(0, 3, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Lbl_Up_ProcessName = wx.StaticText(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"Process Name", wx.DefaultPosition,
                                                wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
        self.Lbl_Up_ProcessName.Wrap(-1)
        fgSizer6.Add(self.Lbl_Up_ProcessName, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL         | wx.ALIGN_CENTER_VERTICAL, 5)

        Cmb_Up_ProcessNameChoices = []
        self.Cmb_Up_ProcessName = wx.ComboBox(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"From A To B", wx.DefaultPosition,
                                              wx.Size(200, -1), Cmb_Up_ProcessNameChoices, 0)
        fgSizer6.Add(self.Cmb_Up_ProcessName, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Cmd_Up_Refresh = wx.Button(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"Refresh Data", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        fgSizer6.Add(self.Cmd_Up_Refresh, 0, wx.ALL, 5)

        fgSizer3.Add(fgSizer6, 1, wx.EXPAND, 5)

        fgSizer7 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer7.SetFlexibleDirection(wx.BOTH)
        fgSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Dv_Up = wx.dataview.DataViewListCtrl(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 200), 0)
        fgSizer7.Add(self.Dv_Up, 0, wx.ALL, 5)

        self.Dv_Up.AppendTextColumn("ID")
        self.Dv_Up.AppendTextColumn("ConfigName")
        #self.Dv_Up.AppendTextColumn()

        fgSizer3.Add(fgSizer7, 1, wx.EXPAND, 5)

        fgSizer8 = wx.FlexGridSizer(1, 5, 0, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        #self.Cmd_Up_Home = wx.Button(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"Home", wx.DefaultPosition, wx.DefaultSize, 0)
        #fgSizer8.Add(self.Cmd_Up_Home, 0, wx.ALL, 5)

        #self.Cmd_Up_Zero = wx.Button(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"Zero", wx.DefaultPosition,
        #                                   wx.DefaultSize, 0)
        #fgSizer8.Add(self.Cmd_Up_Zero, 0, wx.ALL, 5)

        #ADD By Reza

        self.Cmd_Up_NewProcess = wx.Button(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"New Process",
                                           wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        fgSizer8.Add(self.Cmd_Up_NewProcess, 0, wx.ALL, 5)

        self.Cmd_Up_EditProcess = wx.Button(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"Edit Process",
                                           wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        fgSizer8.Add(self.Cmd_Up_EditProcess, 0, wx.ALL, 5)

        self.Cmd_Up_DeleteProcess = wx.Button(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"Delete Process",
                                           wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        fgSizer8.Add(self.Cmd_Up_DeleteProcess, 0, wx.ALL, 5)


        self.Cmd_Up_CancelNew = wx.Button(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"Cancel",
                                           wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        fgSizer8.Add(self.Cmd_Up_CancelNew, 0, wx.ALL, 5)

        #==================

        fgSizer3.Add(fgSizer8, 1, wx.EXPAND, 5)

        fgSizer2.Add(fgSizer3, 1, wx.EXPAND, 5)

        fgSizer5 = wx.FlexGridSizer(3, 1, 0, 0)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer9 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer9.SetFlexibleDirection(wx.BOTH)
        fgSizer9.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Lbl_Down_ProcessName = wx.StaticText(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"Process Name", wx.DefaultPosition,
                                                  wx.DefaultSize, 0|wx.TRANSPARENT_WINDOW )
        self.Lbl_Down_ProcessName.Wrap(-1)
        fgSizer9.Add(self.Lbl_Down_ProcessName, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Txt_Down_ProcessName = wx.TextCtrl(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.Size(200, -1), 0)
        fgSizer9.Add(self.Txt_Down_ProcessName, 0, wx.ALL, 5)

        self.Cmd_Down_SaveConfig = wx.Button(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"Save Config", wx.DefaultPosition,
                                     wx.DefaultSize, 0)
        fgSizer9.Add(self.Cmd_Down_SaveConfig, 0, wx.ALL, 5)

        fgSizer5.Add(fgSizer9, 1, wx.EXPAND, 5)

        fgSizer10 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer10.SetFlexibleDirection(wx.BOTH)
        fgSizer10.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Dv_Down = wx.dataview.DataViewListCtrl(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 200),
                                                    0)
        self.Dv_Down.AppendTextColumn("HeaderID")
        self.Dv_Down.AppendTextColumn("List")
        self.Dv_Down.AppendTextColumn("SudutID")
        self.Dv_Down.AppendTextColumn("Taggal Pembuatan")

        fgSizer10.Add(self.Dv_Down, 0, wx.ALL, 5)

        fgSizer5.Add(fgSizer10, 1, wx.EXPAND, 5)

        fgSizer11 = wx.FlexGridSizer(1, 4, 0, 0)
        fgSizer11.SetFlexibleDirection(wx.BOTH)
        fgSizer11.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Cmd_Down_Save = wx.Button(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"Save To Table", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer11.Add(self.Cmd_Down_Save, 0, wx.ALL, 5)

        self.Cmd_Down_Delete = wx.Button(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"Delete From Table", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer11.Add(self.Cmd_Down_Delete, 0, wx.ALL, 5)

        self.Cmd_Down_DeleteAll = wx.Button(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"Clear Table", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        fgSizer11.Add(self.Cmd_Down_DeleteAll, 0, wx.ALL, 5)

        self.Cmd_Down_CheckDetail = wx.Button(self.Bit_StPrc_Background_Setup2, wx.ID_ANY, u"Check Position",
                                            wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        fgSizer11.Add(self.Cmd_Down_CheckDetail, 0, wx.ALL, 5)

        fgSizer5.Add(fgSizer11, 1, wx.EXPAND, 5)

        fgSizer2.Add(fgSizer5, 1, wx.EXPAND, 5)

        self.Bit_StPrc_Background_Setup2.SetSizer(fgSizer2)
        self.Bit_StPrc_Background_Setup2.Layout()
        fgSizer2.Fit(self.Bit_StPrc_Background_Setup2)
        self.Cmd_Up_CancelNew.Hide()

    #USING CONTROLLER
    def StPrcUseController(self):
        self.Cmd_StPrc_WidgetUseMouse.Enable()
        self.Cmd_StPrc_WidgetUseController.Disable()

        # PANEL CHANGES
        self.Lbl_StPrc_WidgetUsedModeView.SetLabel("BY CONTROLLER")

        # Reset Focus and Position Now
        self.StPrcResetScroll()

        # START WITH CONTROLLER
        self.StPrcController_Mode = True

    #USING MOUSE
    def StPrcUseMouse(self):
        # END CONTROLLER MODE
        self.StPrcController_Mode = False

        # EXECUTE COMMAND
        commandlists = []
        feedbacklists = []

        # GET THE DOL COMMAND
        deleting = {}
        datacommand = self.MGETManualCommand(1, 8, group='MANUAL', type='RESET')
        command = datacommand[0]
        marker = datacommand[1]
        deleting = {1: str(command)}
        deletingfeedback = str('done')
        commandlists.append(copy.deepcopy(deleting))
        feedbacklists.append(copy.deepcopy(deletingfeedback))

        print commandlists
        print feedbacklists
        # DOL Command
        # self.CExecutingCommand(commandlists, feedbacklists, save=True)


        self.Cmd_StPrc_WidgetUseMouse.Disable()
        self.Cmd_StPrc_WidgetUseController.Enable()
        # Realtime = False

        # PANEL BUTTON
        self.Lbl_StPrc_WidgetUsedModeView.SetLabel("BY MOUSE")

        # START DETECTING POS
        self.DetectingPos = True

    #RESET SLIDER AND SPINER
    def StPrcResetScroll(self):
        self.StPrc_Sld_Move1.SetValue(0)
        self.StPrc_Spn_Value1.SetValue(0)
        self.StPrc_Sld_Move2.SetValue(0)
        self.StPrc_Spn_Value2.SetValue(0)
        self.StPrc_Sld_Move3.SetValue(0)
        self.StPrc_Spn_Value3.SetValue(0)
        self.StPrc_Sld_Move4.SetValue(0)
        self.StPrc_Spn_Value4.SetValue(0)
        self.StPrc_Sld_Move5.SetValue(0)
        self.StPrc_Spn_Value5.SetValue(0)
        self.StPrc_Sld_Move6.SetValue(0)
        self.StPrc_Spn_Value6.SetValue(0)
        self.PositionNow = ''
        self.CurrentFocus = ''

    #DATA Configurasi H From DBase
    def StPrcViewConfigH(self, mode):
        if mode == 1:
            self.Dv_Up.DeleteAllItems()
            #ToDo = Query Select / FuncSelect
            data = self.MGETConfig('HEADER', 4, None)

            for items in data:
                self.Dv_Up.AppendItem(items)


    #DATA Configurasi D FROM DataForm(Slider/etc)
    def StPrcViewConfigD(self, mode):
        if mode == 1:
            self.Dv_Down.DeleteAllItems()

            #ToDo = Get Data Form
            data = self.MGETConfig('DETAIL', 4, None)

            for items in data:
                self.Dv_Down.AppendItem(items)


    #SAVE TO DETAIL
    def StPrcSaveToDv(self, mode):
        #DETAIL
        if mode == 1:
            #ToDo Get Data
            data = kwargss_data

            #APPEND TO Dv
            maxitem = int(self.Dv_Down.GetItemCount())

            #ToDo Menage Data Format
            #ToDo GetData From Sld and Spin
            #SUDUT NOW
            listing = maxitem + 1
            sudutdata = self.StPrcGetSudut()
            for items in sudutdata:
                self.Dv_Down.AppendItem(items)
                listing += 1

        #HEADER
        elif mode == 2:
            pass
            #data = [name]

            #Save TO Header
            self.MSaveConfigHeader()

    def StPrcGetSudutData(self, mode):
        if mode == 1:
            lists = 0
            data1 = []
            val1 = self.StPrc_Spn_Value1.GetValue()
            #ToDo = Make StPrc_vLastPos[1]
            if val1 != '' and val1 != self.StPrc_vLastPos[1]:
                lists += 10
                data1.append(int(lists))
                data1.append(int(1))
                data1.append(float(val1))
                data1.append(float(self.Speed[1]))
                data1.append(str(self.StPrcGetDir(val1)))
            data1 = self.SsvDataInputFiltering(data1)

            data2 = []
            val2 = self.StPrc_Spn_Value2.GetValue()
            if val2 != '' and val2 != self.StPrc_vLastPos[2]:
                lists += 10
                data2.append(int(lists))
                data2.append(int(2))
                data2.append(float(val2))
                data2.append(float(self.Speed[2]))
                data2.append(str(self.StPrcGetDir(val2)))
            data2 = self.SsvDataInputFiltering(data2)

            data3 = []
            val3 = self.StPrc_Spn_Value3.GetValue()
            if val3 != '' and val3 != self.StPrc_vLastPos[3]:
                lists += 10
                data3.append(int(lists))
                data3.append(int(3))
                data3.append(float(val3))
                data3.append(float(self.Speed[3]))
                data3.append(str(self.StPrcGetDir(val3)))
            data3 = self.SsvDataInputFiltering(data3)

            data4 = []
            val4 = self.StPrc_Spn_Value4.GetValue()
            if val4 != '' and val4 != self.StPrc_vLasPos[4]:
                lists += 10
                data4.append(int(lists))
                data4.append(int(4))
                data4.append(float(val4))
                data4.append(float(self.Speed[4]))
                data4.append(str(self.StPrcGetDir(val4)))
            data4 = self.SsvDataInputFiltering(data4)

            data5 = []
            val5 = self.StPrc_Spn_Value5.GetValue()
            if val5 != '' and val5 != self.StPrc_vLastPos[5]:
                lists += 10
                data5.append(int(lists))
                data5.append(int(5))
                data5.append(int(val5))
                data5.append(int(self.Speed[5]))
            data5 = self.SsvDataInputFiltering(data5)

            data6 = []
            val6 = self.StPrc_Spn_Value6.GetValue()
            if val6 != '' and val6 != '' and val6 != '-' and val6 != self.StPrc_vLastPos[6]:
                lists += 10
                data6.append(int(lists))
                data6.append(int(6))
                data6.append(str(val6))
            data6 = self.SsvDataInputFiltering(data6)

            data7 = []
            if self.Ssv_Cmb_MagnetStat.GetValue() != '' and self.Ssv_Cmb_MagnetStat.GetValue() != '-':
                lists += 10
                data7.append(int(lists))
                data7.append(int(12))
                data7.append(str(self.Ssv_Cmb_MagnetStat.GetValue()))
            data7 = self.SsvDataInputFiltering(data7)

            hasil = [data1, data2, data3, data4, data5, data6, data7]

            return hasil

    def StPrcAppendDetail(self, mode, **kwargs):
        #Append For New
        if mode == 1:
            try:
                data = kwargs['data']
            except Exception as e:
                print (e)
                return
            else:
                if len(data) == 0:
                    print ('[SetupProcess]-NoData')
                    return
                else:
                    #ToDo : Data Filtering For input detail
                    #Validate Data Sudut
                    data = self.StPrcValuesValidator(2)

                    if data == None:
                        return
                    else:
                        for items in data:
                            pass

    def StPrcSaveSudut(self, mode, **kwargs):
        #Save Header
        if mode == 1:
            #Check Parameters
            try:
                name = kwargs['name']
            except Exception as e:
                print (e)
            else:
                self.MRecordSudut('HEADER', 1, name=name)

        #Save Detail
        elif mode == 2:
            #Check Parameters
            try:
                headid = kwargs['headerid']
                arraydata = kwargs['data']
            except Exception as e:
                print (e)
            else:
                if len(arraydata) == 0:
                    print ('No Data')
                    return

                for item in arraydata:
                    self.MRecordSudut('DETAIL', 1, headerid=headid, list=arraydata[0],
                                      motorid=arraydata[1], val=valuos, speed=speedos,
                                      dirc=directos)
            pass


















