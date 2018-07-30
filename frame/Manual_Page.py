# create a background image on a wxPython panel
# and show a button on top of the image

import wx
import os
import wx.dataview
import copy

class Manual_Movement(wx.Frame):
    """class Panel1 creates a panel with an image on it, inherits wx.Panel"""
    def __init__(self, parent, framename):


        #LOAD CONFIG FILE
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




        #UseBoard = self.config.get('ManualPage Setting', 'BoardUsed')


        # create the panel
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(1245, 615), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        if self.FrameObject.get(framename) == None:
            self.FrameObject.update({framename: self})

        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer1 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        #MENU BAR
        self.VMenuBars()
        self.SetMenuBar(self.MenuBar_Main)

        #PANEL CONTROL
        self.MnlPanelControl(self)
        fgSizer1.Add(self.Mnl_Pnl_Main, 1, wx.ALL | wx.EXPAND, 0)

        #PANEL VIEW
        self.MnlPanelView(self)
        fgSizer1.Add(self.Mnl_Pnl_View, 1, wx.ALL | wx.EXPAND, 0)

        self.SetSizer(fgSizer1)
        self.Layout()

        #PANEL EXTRA
            #PANEL MODE
        #self.MnlPnlModeTest(self.Bit_Background_Setup, 0, 480)
        self.MnlIndicator(self.Bit_Background_Setup,0 ,470)
            #PANEL BUTTON
        self.MnlTglMagnet(self.Bit_Background_Setup2,10, 370)
        self.MnlButtonByClick(self.Bit_Background_Setup2, 175, 370)
        self.MnlButtonHome(self.Bit_Background_Setup2, 340, 370)
        self.MnlZeroByClick(self.Bit_Background_Setup2, 175, 285)
        self.Pnl_Mnl_GoButton.Hide()
        self.Mnl_Pnl_MagnetTgl.Show()
            #PANEL MANUAL SPEED
        self.MnlPnlSpeed(self.Bit_Background_Setup2)
        #self.Pnl_ManualSpeed.Hide()
            #PANEL BY FORM
        self.MnlPnlByForm(self.Bit_Background_Setup2)
        self.Pnl_Mnl_ByForm.Hide()


        #LOAD CONSTANT
        self.MnlStarter()

        #EVENTS
        self.MnlEvents(framename)

        self.Centre(wx.BOTH)
        self.Show()

    def MnlStarter(self):

        #SLIDER LAST VALUE
        self.Last_Slider1 = ''
        self.Last_Slider2 = ''
        self.Last_Slider3 = ''
        self.Last_Slider4 = ''
        self.Last_Slider5 = ''
        self.Last_Slider6 = ''

        #focused box
        self.CurrentFocus = ''
        self.NowFocus = self.CurrentFocus


        # BOX 1
        self.Mnl_Spn_Value1.SetRange(self.min_axis1,self.max_axis1)
        self.Mnl_Spn_Value1.SetValue(0)
        self.Mnl_Spn_Value1.SetIncrement(1)

        datadict = self.CCalculate('SPIN-SLIDER', 1, max=self.Mnl_Spn_Value1.GetMax(), min=self.Mnl_Spn_Value1.GetMin(),
                        inc=self.Mnl_Spn_Value1.GetIncrement())

        self.Mnl_Sld_Move1.SetRange(datadict['min'],datadict['max'])
        self.Mnl_Sld_Move1.SetValue(0)

        # BOX 2
        self.Mnl_Spn_Value2.SetRange(self.min_axis2,self.max_axis2)
        self.Mnl_Spn_Value2.SetValue(0)
        self.Mnl_Spn_Value2.SetIncrement(1)

        datadict = self.CCalculate('SPIN-SLIDER', 1, max=self.Mnl_Spn_Value2.GetMax(), min=self.Mnl_Spn_Value2.GetMin(),
                                   inc=self.Mnl_Spn_Value2.GetIncrement())

        self.Mnl_Sld_Move2.SetRange(datadict['min'], datadict['max'])
        self.Mnl_Sld_Move2.SetValue(0)

        # BOX 3
        self.Mnl_Spn_Value3.SetRange(self.min_axis3,self.max_axis3)
        self.Mnl_Spn_Value3.SetValue(0)
        self.Mnl_Spn_Value3.SetIncrement(1)

        datadict = self.CCalculate('SPIN-SLIDER', 1, max=self.Mnl_Spn_Value3.GetMax(), min=self.Mnl_Spn_Value3.GetMin(),
                                   inc=self.Mnl_Spn_Value3.GetIncrement())

        self.Mnl_Sld_Move3.SetRange(datadict['min'], datadict['max'])
        self.Mnl_Sld_Move3.SetValue(0)

        # BOX 4
        self.Mnl_Spn_Value4.SetRange(self.min_axis4,self.max_axis4)
        self.Mnl_Spn_Value4.SetValue(0)
        self.Mnl_Spn_Value4.SetIncrement(1)

        datadict = self.CCalculate('SPIN-SLIDER', 1, max=self.Mnl_Spn_Value4.GetMax(), min=self.Mnl_Spn_Value4.GetMin(),
                                   inc=self.Mnl_Spn_Value4.GetIncrement())

        self.Mnl_Sld_Move4.SetRange(datadict['min'], datadict['max'])
        self.Mnl_Sld_Move4.SetValue(0)

        # BOX 5
        self.Mnl_Spn_Value5.SetRange(self.min_servo, self.max_servo)
        self.Mnl_Spn_Value5.SetValue(0)
        self.Mnl_Spn_Value5.SetIncrement(1)

        datadict = self.CCalculate('SPIN-SLIDER', 1, max=self.Mnl_Spn_Value5.GetMax(), min=self.Mnl_Spn_Value5.GetMin(),
                                   inc=self.Mnl_Spn_Value5.GetIncrement())

        self.Mnl_Sld_Move5.SetRange(datadict['min'], datadict['max'])
        self.Mnl_Sld_Move5.SetValue(0)

        # BOX 6
        self.Mnl_Spn_Value6.SetRange(0, 100)
        self.Mnl_Spn_Value6.SetValue(0)
        self.Mnl_Spn_Value6.SetIncrement(1)

        datadict = self.CCalculate('SPIN-SLIDER', 1, max=self.Mnl_Spn_Value6.GetMax(), min=self.Mnl_Spn_Value6.GetMin(),
                                   inc=self.Mnl_Spn_Value6.GetIncrement())

        self.Mnl_Sld_Move6.SetRange(datadict['min'], datadict['max'])
        self.Mnl_Sld_Move6.SetValue(0)

        #SET VALUE BASED ON NOWS VARIABLES


    def MnlEvents(self, framename):
        # ==== SLIDER & SPIN ====
        # 1
        self.Mnl_Spn_Value1.Bind(wx.EVT_SET_FOCUS, lambda x: self.MnlOnFocus(2, 1))
        self.Mnl_Spn_Value1.Bind( wx.EVT_TEXT, lambda x:self.MnlOnChange(2,1))
        self.Mnl_Spn_Value1.Bind(wx.EVT_SPINCTRLDOUBLE, lambda x:self.MnlOnChange(2,1))

        self.Mnl_Sld_Move1.Bind(wx.EVT_SET_FOCUS, lambda x:self.MnlOnFocus(1,1))
        self.Mnl_Sld_Move1.Bind(wx.EVT_SCROLL_CHANGED, lambda x:self.MnlOnChange(1,1))


        self.Mnl_Pnl_Move1.Bind(wx.EVT_SET_FOCUS, lambda x:self.MnlOnFocus(3,1, togglevalue=self.Tgl_Mnl_FocusButton1.GetValue()))
        self.Tgl_Mnl_FocusButton1.Bind(wx.EVT_TOGGLEBUTTON, lambda x:self.MnlOnFocus(3,1, togglevalue=self.Tgl_Mnl_FocusButton1.GetValue()))


        # 2
        self.Mnl_Spn_Value2.Bind(wx.EVT_SET_FOCUS, lambda x: self.MnlOnFocus(2, 2))
        self.Mnl_Spn_Value2.Bind(wx.EVT_TEXT, lambda x: self.MnlOnChange(2,2))
        self.Mnl_Spn_Value2.Bind(wx.EVT_SPINCTRLDOUBLE, lambda x: self.MnlOnChange(2,2))

        self.Axis1_Handler = self.Mnl_Spn_Value2.GetEventHandler()

        self.Mnl_Sld_Move2.Bind(wx.EVT_SET_FOCUS, lambda x:self.MnlOnFocus(1,2))
        self.Mnl_Sld_Move2.Bind(wx.EVT_SCROLL_CHANGED, lambda x: self.MnlOnChange(1,2))

        self.Mnl_Pnl_Move2.Bind(wx.EVT_SET_FOCUS, lambda x: self.MnlOnFocus(3, 2, togglevalue=self.Tgl_Mnl_FocusButton2.GetValue()))
        self.Tgl_Mnl_FocusButton2.Bind(wx.EVT_TOGGLEBUTTON, lambda x: self.MnlOnFocus(3, 2, togglevalue=self.Tgl_Mnl_FocusButton2.GetValue()))


        # 3
        self.Mnl_Spn_Value3.Bind(wx.EVT_SET_FOCUS, lambda x: self.MnlOnFocus(2, 3))
        self.Mnl_Spn_Value3.Bind(wx.EVT_TEXT, lambda x: self.MnlOnChange(2,3))
        self.Mnl_Spn_Value3.Bind(wx.EVT_SPINCTRLDOUBLE, lambda x: self.MnlOnChange(2,3))

        self.Axis2_Handler = self.Mnl_Spn_Value3.GetEventHandler()

        self.Mnl_Sld_Move3.Bind(wx.EVT_SET_FOCUS, lambda x:self.MnlOnFocus(1,3))
        self.Mnl_Sld_Move3.Bind(wx.EVT_SCROLL_CHANGED, lambda x: self.MnlOnChange(1,3))

        self.Mnl_Pnl_Move3.Bind(wx.EVT_SET_FOCUS, lambda x: self.MnlOnFocus(3, 3, togglevalue=self.Tgl_Mnl_FocusButton3.GetValue()))
        self.Tgl_Mnl_FocusButton3.Bind(wx.EVT_TOGGLEBUTTON, lambda x: self.MnlOnFocus(3, 3, togglevalue=self.Tgl_Mnl_FocusButton3.GetValue()))


        # 4
        self.Mnl_Spn_Value4.Bind(wx.EVT_SET_FOCUS, lambda x: self.MnlOnFocus(2,4 ))
        self.Mnl_Spn_Value4.Bind(wx.EVT_TEXT, lambda x: self.MnlOnChange(2,4))
        self.Mnl_Spn_Value4.Bind(wx.EVT_SPINCTRLDOUBLE, lambda x: self.MnlOnChange(2,4))

        self.Axis3_Handler = self.Mnl_Spn_Value4.GetEventHandler()

        self.Mnl_Sld_Move4.Bind(wx.EVT_SET_FOCUS, lambda x:self.MnlOnFocus(1,4))
        self.Mnl_Sld_Move4.Bind(wx.EVT_SCROLL_CHANGED, lambda x: self.MnlOnChange(1,4))

        self.Mnl_Pnl_Move4.Bind(wx.EVT_SET_FOCUS, lambda x: self.MnlOnFocus(3, 4, togglevalue=self.Tgl_Mnl_FocusButton4.GetValue()))
        self.Tgl_Mnl_FocusButton4.Bind(wx.EVT_TOGGLEBUTTON, lambda x: self.MnlOnFocus(3, 4, togglevalue=self.Tgl_Mnl_FocusButton4.GetValue()))


        # 5
        self.Mnl_Spn_Value5.Bind(wx.EVT_SET_FOCUS, lambda x: self.MnlOnFocus(2, 5))
        self.Mnl_Spn_Value5.Bind(wx.EVT_TEXT, lambda x: self.MnlOnChange(2,5))
        self.Mnl_Spn_Value5.Bind(wx.EVT_SPINCTRLDOUBLE, lambda x: self.MnlOnChange(2,5))

        self.Mnl_Sld_Move5.Bind(wx.EVT_SET_FOCUS, lambda x:self.MnlOnFocus(1,5))
        self.Mnl_Sld_Move5.Bind(wx.EVT_SCROLL_CHANGED, lambda x: self.MnlOnChange(1,5))

        self.Mnl_Pnl_Move5.Bind(wx.EVT_SET_FOCUS, lambda x: self.MnlOnFocus(3, 5, togglevalue=self.Tgl_Mnl_FocusButton5.GetValue()))
        self.Tgl_Mnl_FocusButton5.Bind(wx.EVT_TOGGLEBUTTON, lambda x: self.MnlOnFocus(3, 5, togglevalue=self.Tgl_Mnl_FocusButton5.GetValue()))


        # 6
        self.Mnl_Spn_Value6.Bind(wx.EVT_SET_FOCUS, lambda x: self.MnlOnFocus(2, 6))
        self.Mnl_Spn_Value6.Bind(wx.EVT_TEXT, lambda x: self.MnlOnChange(2,6))
        self.Mnl_Spn_Value6.Bind(wx.EVT_SPINCTRLDOUBLE, lambda x: self.MnlOnChange(2,6))

        self.Mnl_Sld_Move6.Bind(wx.EVT_SET_FOCUS, lambda x:self.MnlOnFocus(1,6))
        self.Mnl_Sld_Move6.Bind(wx.EVT_SCROLL_CHANGED, lambda x: self.MnlOnChange(1,6))

        self.Mnl_Pnl_Move6.Bind(wx.EVT_SET_FOCUS, lambda x: self.MnlOnFocus(3, 6, togglevalue=self.Tgl_Mnl_FocusButton6.GetValue()))
        self.Tgl_Mnl_FocusButton6.Bind(wx.EVT_TOGGLEBUTTON, lambda x: self.MnlOnFocus(3, 6, togglevalue=self.Tgl_Mnl_FocusButton6.GetValue()))



        # FORM EVENT
        self.Cmd_Mnl_WidgetUseMouse.Bind(wx.EVT_BUTTON, lambda x:self.MnlModeChange(1))
        self.Cmd_Mnl_WidgetUseController.Bind(wx.EVT_BUTTON, lambda x:self.MnlModeChange(2))
        self.Cmd_Mnl_WidgetUseForm.Bind(wx.EVT_BUTTON, lambda x: self.MnlModeChange(3))
        self.Cmd_Mnl_GoByClick.Bind(wx.EVT_BUTTON, lambda x:self.MnlFrameAct(2))
        self.Cmd_Mnl_ZeroByClick.Bind(wx.EVT_BUTTON, lambda x: self.MnlFrameAct(4))
        self.Cmd_Mnl_HomeByClick.Bind(wx.EVT_BUTTON, lambda x: self.MnlFrameAct(3))
        self.Cmd_Mnl_SetSpeed.Bind(wx.EVT_BUTTON, lambda x:self.MnlSetSpeedMotor(1))
        self.Cmd_Mnl_ResetSpeed.Bind(wx.EVT_BUTTON, lambda x: self.MnlFrameAct(1))
        self.Mnl_Tgl_Magnet.Bind(wx.EVT_TOGGLEBUTTON, lambda x:self.MnlSetMagnet(self.Mnl_Tgl_Magnet.GetValue()))

    def MnlSetMagnet(self, val):
        self.Magnet_Before = val
        self.Event_Type = 'MnlMagnet'
        self.CEventON()

    def MnlSetSld(self, mode , val):
        if mode == 1:
            self.Mnl_Sld_Move1.SetValue(int(val))
        if mode == 2:
            self.Mnl_Sld_Move2.SetValue(int(val))
        if mode == 3:
            self.Mnl_Sld_Move3.SetValue(int(val))
        if mode == 4:
            self.Mnl_Sld_Move4.SetValue(int(val))
        if mode == 5:
            self.Mnl_Sld_Move5.SetValue(int(val))
        if mode == 6:
            self.Mnl_Sld_Move6.SetValue(int(val))

    def MnlPanelControl(self,parent):
        self.Mnl_Pnl_Main = wx.Panel(parent, wx.ID_ANY, wx.DefaultPosition, wx.Size(720, -1), wx.TAB_TRAVERSAL)

        try:
            # pick an image file you have in the working folder

            # you can load .jpg  .png  .bmp  or .gif files
            image_file = os.path.normpath('.\\images\\background.png')
            bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()

            # image's upper left corner anchors at panel coordinates (0, 0)
            self.Bit_Background_Setup = wx.StaticBitmap(self.Mnl_Pnl_Main, -1, bmp1, pos=(0, 0))

            # show some image details
            str1 = "%s  %dx%d" % (image_file, bmp1.GetWidth(), bmp1.GetHeight())

        except IOError:
            print "Image file %s not found" % image_file
            raise SystemExit

        # button goes on the image --> self.bitmap1 is the parent
        # PANEL 1
        self.Mnl_Pnl_Move6 = wx.Panel(self.Bit_Background_Setup, wx.ID_ANY, wx.Point(10, 120), wx.Size(170, 60), wx.TAB_TRAVERSAL)
        # SET ID BASED BY MOTOR ID
        self.Mnl_Pnl_Move6.SetId(1)
        self.Mnl_Pnl_Move6.SetBackgroundColour(wx.Colour( 255, 255, 255 ))

        fgSizer17 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer17.SetFlexibleDirection(wx.BOTH)
        fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_MnlStats6 = wx.Panel(self.Mnl_Pnl_Move6, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                      wx.TAB_TRAVERSAL)
        self.Pnl_MnlStats6.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        fgSizer18 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer18.SetFlexibleDirection(wx.BOTH)
        fgSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Tgl_Mnl_FocusButton6 = wx.ToggleButton(self.Pnl_MnlStats6, wx.ID_ANY, u"6", wx.DefaultPosition,
                                                    wx.Size(50, 50), 0)
        self.Tgl_Mnl_FocusButton6.SetValue(False)
        self.Tgl_Mnl_FocusButton6.SetFont(wx.Font(36, 74, 90, 92, False, "Arial"))
        self.Tgl_Mnl_FocusButton6.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer18.Add(self.Tgl_Mnl_FocusButton6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.Txt_Mnl_StatsFocus6 = wx.StaticText(self.Pnl_MnlStats6, wx.ID_ANY, u"INACTIVE", wx.DefaultPosition,
                                                 wx.Size(70, 15), wx.ALIGN_CENTRE)
        self.Txt_Mnl_StatsFocus6.Wrap(-1)
        self.Txt_Mnl_StatsFocus6.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Txt_Mnl_StatsFocus6.SetForegroundColour(wx.Colour(255, 0, 0))
        self.Txt_Mnl_StatsFocus6.SetBackgroundColour(wx.Colour(0, 0, 0))

        fgSizer18.Add(self.Txt_Mnl_StatsFocus6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL , 5)

        self.Pnl_MnlStats6.SetSizer(fgSizer18)
        self.Pnl_MnlStats6.Layout()
        fgSizer18.Fit(self.Pnl_MnlStats6)
        fgSizer17.Add(self.Pnl_MnlStats6, 1, wx.EXPAND | wx.ALL, 0)

        self.Pnl_Mnl_Scroll6 = wx.Panel(self.Mnl_Pnl_Move6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        self.Pnl_Mnl_Scroll6.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer19 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer19.SetFlexibleDirection(wx.BOTH)
        fgSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer19.SetMinSize(wx.Size(-1, 80))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.Lbl_Mnl_Jdl_Sudut6 = wx.StaticText(self.Pnl_Mnl_Scroll6, wx.ID_ANY, u"Sudut Axis", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.Lbl_Mnl_Jdl_Sudut6.Wrap(-1)
        self.Lbl_Mnl_Jdl_Sudut6.SetFont(wx.Font(10, 74, 90, 92, False, "Arial"))

        bSizer9.Add(self.Lbl_Mnl_Jdl_Sudut6, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Mnl_Sld_Move6 = wx.Slider(self.Pnl_Mnl_Scroll6, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition, wx.Size(130, 20),
                                       wx.SL_HORIZONTAL)
        bSizer9.Add(self.Mnl_Sld_Move6, 0, wx.ALL, 5)

        self.Mnl_Spn_Value6 = wx.SpinCtrlDouble(self.Pnl_Mnl_Scroll6, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer9.Add(self.Mnl_Spn_Value6, 0, wx.ALL, 5)

        fgSizer19.Add(bSizer9, 1, wx.EXPAND, 5)

        self.Pnl_Mnl_Scroll6.SetSizer(fgSizer19)
        self.Pnl_Mnl_Scroll6.Layout()
        fgSizer19.Fit(self.Pnl_Mnl_Scroll6)
        fgSizer17.Add(self.Pnl_Mnl_Scroll6, 1, wx.EXPAND | wx.ALL, 0)

        self.Mnl_Pnl_Move6.SetSizer(fgSizer17)
        self.Mnl_Pnl_Move6.Layout()
        fgSizer17.Fit(self.Mnl_Pnl_Move6)



        # PANEL 2
        self.Mnl_Pnl_Move5 = wx.Panel(self.Bit_Background_Setup, wx.ID_ANY, wx.Point(375, 10), wx.Size(170, 60), wx.TAB_TRAVERSAL)
        # SET ID BASED BY MOTOR ID
        self.Mnl_Pnl_Move5.SetId(2)
        self.Mnl_Pnl_Move5.SetBackgroundColour(wx.Colour( 255, 255, 255 ))

        fgSizer17 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer17.SetFlexibleDirection(wx.BOTH)
        fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_MnlStats5 = wx.Panel(self.Mnl_Pnl_Move5, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                      wx.TAB_TRAVERSAL)
        self.Pnl_MnlStats5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        fgSizer18 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer18.SetFlexibleDirection(wx.BOTH)
        fgSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Tgl_Mnl_FocusButton5 = wx.ToggleButton(self.Pnl_MnlStats5, wx.ID_ANY, u"5", wx.DefaultPosition,
                                                    wx.Size(50, 50), 0)
        self.Tgl_Mnl_FocusButton5.SetValue(False)
        self.Tgl_Mnl_FocusButton5.SetFont(wx.Font(36, 74, 90, 92, False, "Arial"))
        self.Tgl_Mnl_FocusButton5.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer18.Add(self.Tgl_Mnl_FocusButton5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.Txt_Mnl_StatsFocus5 = wx.StaticText(self.Pnl_MnlStats5, wx.ID_ANY, u"INACTIVE", wx.DefaultPosition,
                                                 wx.Size(70, 15), wx.ALIGN_CENTRE)
        self.Txt_Mnl_StatsFocus5.Wrap(-1)
        self.Txt_Mnl_StatsFocus5.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Txt_Mnl_StatsFocus5.SetForegroundColour(wx.Colour(255, 0, 0))
        self.Txt_Mnl_StatsFocus5.SetBackgroundColour(wx.Colour(0, 0, 0))

        fgSizer18.Add(self.Txt_Mnl_StatsFocus5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL , 5)

        self.Pnl_MnlStats5.SetSizer(fgSizer18)
        self.Pnl_MnlStats5.Layout()
        fgSizer18.Fit(self.Pnl_MnlStats5)
        fgSizer17.Add(self.Pnl_MnlStats5, 1, wx.EXPAND | wx.ALL, 0)

        self.Pnl_Mnl_Scroll5 = wx.Panel(self.Mnl_Pnl_Move5, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        self.Pnl_Mnl_Scroll5.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer19 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer19.SetFlexibleDirection(wx.BOTH)
        fgSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer19.SetMinSize(wx.Size(-1, 80))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.Lbl_Mnl_Jdl_Sudut5 = wx.StaticText(self.Pnl_Mnl_Scroll5, wx.ID_ANY, u"Sudut Axis", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.Lbl_Mnl_Jdl_Sudut5.Wrap(-1)
        self.Lbl_Mnl_Jdl_Sudut5.SetFont(wx.Font(10, 74, 90, 92, False, "Arial"))

        bSizer9.Add(self.Lbl_Mnl_Jdl_Sudut5, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Mnl_Sld_Move5 = wx.Slider(self.Pnl_Mnl_Scroll5, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition,
                                       wx.Size(130, 20),
                                       wx.SL_HORIZONTAL)
        bSizer9.Add(self.Mnl_Sld_Move5, 0, wx.ALL, 5)

        self.Mnl_Spn_Value5 = wx.SpinCtrlDouble(self.Pnl_Mnl_Scroll5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer9.Add(self.Mnl_Spn_Value5, 0, wx.ALL, 5)

        fgSizer19.Add(bSizer9, 1, wx.EXPAND, 5)

        self.Pnl_Mnl_Scroll5.SetSizer(fgSizer19)
        self.Pnl_Mnl_Scroll5.Layout()
        fgSizer19.Fit(self.Pnl_Mnl_Scroll5)
        fgSizer17.Add(self.Pnl_Mnl_Scroll5, 1, wx.EXPAND | wx.ALL, 0)

        self.Mnl_Pnl_Move5.SetSizer(fgSizer17)
        self.Mnl_Pnl_Move5.Layout()
        fgSizer17.Fit(self.Mnl_Pnl_Move5)


        # PANEL 3
        self.Mnl_Pnl_Move4 = wx.Panel(self.Bit_Background_Setup, wx.ID_ANY, wx.Point(55, 235), wx.Size(170, 60),
                                  wx.TAB_TRAVERSAL)
        # SET ID BASED BY MOTOR ID
        self.Mnl_Pnl_Move4.SetId(3)
        self.Mnl_Pnl_Move4.SetBackgroundColour(wx.Colour( 255, 255, 255 ))

        fgSizer17 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer17.SetFlexibleDirection(wx.BOTH)
        fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_MnlStats4 = wx.Panel(self.Mnl_Pnl_Move4, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                      wx.TAB_TRAVERSAL)
        self.Pnl_MnlStats4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        fgSizer18 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer18.SetFlexibleDirection(wx.BOTH)
        fgSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Tgl_Mnl_FocusButton4 = wx.ToggleButton(self.Pnl_MnlStats4, wx.ID_ANY, u"4", wx.DefaultPosition,
                                                    wx.Size(50, 50), 0)
        self.Tgl_Mnl_FocusButton4.SetValue(False)
        self.Tgl_Mnl_FocusButton4.SetFont(wx.Font(36, 74, 90, 92, False, "Arial"))
        self.Tgl_Mnl_FocusButton4.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer18.Add(self.Tgl_Mnl_FocusButton4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.Txt_Mnl_StatsFocus4 = wx.StaticText(self.Pnl_MnlStats4, wx.ID_ANY, u"INACTIVE", wx.DefaultPosition,
                                                 wx.Size(70, 15), wx.ALIGN_CENTRE)
        self.Txt_Mnl_StatsFocus4.Wrap(-1)
        self.Txt_Mnl_StatsFocus4.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Txt_Mnl_StatsFocus4.SetForegroundColour(wx.Colour(255, 0, 0))
        self.Txt_Mnl_StatsFocus4.SetBackgroundColour(wx.Colour(0, 0, 0))

        fgSizer18.Add(self.Txt_Mnl_StatsFocus4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL , 5)

        self.Pnl_MnlStats4.SetSizer(fgSizer18)
        self.Pnl_MnlStats4.Layout()
        fgSizer18.Fit(self.Pnl_MnlStats4)
        fgSizer17.Add(self.Pnl_MnlStats4, 1, wx.EXPAND | wx.ALL, 0)

        self.Pnl_Mnl_Scroll4 = wx.Panel(self.Mnl_Pnl_Move4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        self.Pnl_Mnl_Scroll4.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer19 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer19.SetFlexibleDirection(wx.BOTH)
        fgSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer19.SetMinSize(wx.Size(-1, 80))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.Lbl_Mnl_Jdl_Sudut4 = wx.StaticText(self.Pnl_Mnl_Scroll4, wx.ID_ANY, u"Sudut Axis", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.Lbl_Mnl_Jdl_Sudut4.Wrap(-1)
        self.Lbl_Mnl_Jdl_Sudut4.SetFont(wx.Font(10, 74, 90, 92, False, "Arial"))

        bSizer9.Add(self.Lbl_Mnl_Jdl_Sudut4, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Mnl_Sld_Move4 = wx.Slider(self.Pnl_Mnl_Scroll4, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition,
                                       wx.Size(130, 20),
                                       wx.SL_HORIZONTAL)
        bSizer9.Add(self.Mnl_Sld_Move4, 0, wx.ALL, 5)

        self.Mnl_Spn_Value4 = wx.SpinCtrlDouble(self.Pnl_Mnl_Scroll4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer9.Add(self.Mnl_Spn_Value4, 0, wx.ALL, 5)

        fgSizer19.Add(bSizer9, 1, wx.EXPAND, 5)

        self.Pnl_Mnl_Scroll4.SetSizer(fgSizer19)
        self.Pnl_Mnl_Scroll4.Layout()
        fgSizer19.Fit(self.Pnl_Mnl_Scroll4)
        fgSizer17.Add(self.Pnl_Mnl_Scroll4, 1, wx.EXPAND | wx.ALL, 0)

        self.Mnl_Pnl_Move4.SetSizer(fgSizer17)
        self.Mnl_Pnl_Move4.Layout()
        fgSizer17.Fit(self.Mnl_Pnl_Move4)

        # PANEL 4
        self.Mnl_Pnl_Move3 = wx.Panel(self.Bit_Background_Setup, wx.ID_ANY, wx.Point(455, 125), wx.Size(170, 60),
                                  wx.TAB_TRAVERSAL)
        # SET ID BASED BY MOTOR ID
        self.Mnl_Pnl_Move3.SetId(4)
        self.Mnl_Pnl_Move3.SetBackgroundColour(wx.Colour( 255, 255, 255 ))

        fgSizer17 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer17.SetFlexibleDirection(wx.BOTH)
        fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_MnlStats3 = wx.Panel(self.Mnl_Pnl_Move3, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                      wx.TAB_TRAVERSAL)
        self.Pnl_MnlStats3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        fgSizer18 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer18.SetFlexibleDirection(wx.BOTH)
        fgSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Tgl_Mnl_FocusButton3 = wx.ToggleButton(self.Pnl_MnlStats3, wx.ID_ANY, u"3", wx.DefaultPosition,
                                                    wx.Size(50, 50), 0)
        self.Tgl_Mnl_FocusButton3.SetValue(False)
        self.Tgl_Mnl_FocusButton3.SetFont(wx.Font(36, 74, 90, 92, False, "Arial"))
        self.Tgl_Mnl_FocusButton3.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer18.Add(self.Tgl_Mnl_FocusButton3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.Txt_Mnl_StatsFocus3 = wx.StaticText(self.Pnl_MnlStats3, wx.ID_ANY, u"INACTIVE", wx.DefaultPosition,
                                                 wx.Size(70, 15), wx.ALIGN_CENTRE)
        self.Txt_Mnl_StatsFocus3.Wrap(-1)
        self.Txt_Mnl_StatsFocus3.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Txt_Mnl_StatsFocus3.SetForegroundColour(wx.Colour(255, 0, 0))
        self.Txt_Mnl_StatsFocus3.SetBackgroundColour(wx.Colour(0, 0, 0))

        fgSizer18.Add(self.Txt_Mnl_StatsFocus3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL , 5)

        self.Pnl_MnlStats3.SetSizer(fgSizer18)
        self.Pnl_MnlStats3.Layout()
        fgSizer18.Fit(self.Pnl_MnlStats3)
        fgSizer17.Add(self.Pnl_MnlStats3, 1, wx.EXPAND | wx.ALL, 0)

        self.Pnl_Mnl_Scroll3 = wx.Panel(self.Mnl_Pnl_Move3, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        self.Pnl_Mnl_Scroll3.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer19 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer19.SetFlexibleDirection(wx.BOTH)
        fgSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer19.SetMinSize(wx.Size(-1, 80))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.Lbl_Mnl_Jdl_Sudut3 = wx.StaticText(self.Pnl_Mnl_Scroll3, wx.ID_ANY, u"Sudut Axis", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.Lbl_Mnl_Jdl_Sudut3.Wrap(-1)
        self.Lbl_Mnl_Jdl_Sudut3.SetFont(wx.Font(10, 74, 90, 92, False, "Arial"))

        bSizer9.Add(self.Lbl_Mnl_Jdl_Sudut3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Mnl_Sld_Move3 = wx.Slider(self.Pnl_Mnl_Scroll3, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition,
                                       wx.Size(130, 20),
                                       wx.SL_HORIZONTAL)
        bSizer9.Add(self.Mnl_Sld_Move3, 0, wx.ALL, 5)

        self.Mnl_Spn_Value3 = wx.SpinCtrlDouble(self.Pnl_Mnl_Scroll3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer9.Add(self.Mnl_Spn_Value3, 0, wx.ALL, 5)

        fgSizer19.Add(bSizer9, 1, wx.EXPAND, 5)

        self.Pnl_Mnl_Scroll3.SetSizer(fgSizer19)
        self.Pnl_Mnl_Scroll3.Layout()
        fgSizer19.Fit(self.Pnl_Mnl_Scroll3)
        fgSizer17.Add(self.Pnl_Mnl_Scroll3, 1, wx.EXPAND | wx.ALL, 0)

        self.Mnl_Pnl_Move3.SetSizer(fgSizer17)
        self.Mnl_Pnl_Move3.Layout()
        fgSizer17.Fit(self.Mnl_Pnl_Move3)

        # PANEL 5
        self.Mnl_Pnl_Move2 = wx.Panel(self.Bit_Background_Setup, wx.ID_ANY, wx.Point(20, 360), wx.Size(170, 60),
                                  wx.TAB_TRAVERSAL)
        # SET ID BASED BY MOTOR ID
        self.Mnl_Pnl_Move2.SetId(5)
        self.Mnl_Pnl_Move2.SetBackgroundColour(wx.Colour( 255, 255, 255 ))

        fgSizer17 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer17.SetFlexibleDirection(wx.BOTH)
        fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_MnlStats2 = wx.Panel(self.Mnl_Pnl_Move2, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                      wx.TAB_TRAVERSAL)
        self.Pnl_MnlStats2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        fgSizer18 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer18.SetFlexibleDirection(wx.BOTH)
        fgSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Tgl_Mnl_FocusButton2 = wx.ToggleButton(self.Pnl_MnlStats2, wx.ID_ANY, u"2", wx.DefaultPosition,
                                                    wx.Size(50, 50), 0)
        self.Tgl_Mnl_FocusButton2.SetValue(False)
        self.Tgl_Mnl_FocusButton2.SetFont(wx.Font(36, 74, 90, 92, False, "Arial"))
        self.Tgl_Mnl_FocusButton2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer18.Add(self.Tgl_Mnl_FocusButton2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.Txt_Mnl_StatsFocus2 = wx.StaticText(self.Pnl_MnlStats2, wx.ID_ANY, u"INACTIVE", wx.DefaultPosition,
                                                 wx.Size(70, 15), wx.ALIGN_CENTRE)
        self.Txt_Mnl_StatsFocus2.Wrap(-1)
        self.Txt_Mnl_StatsFocus2.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Txt_Mnl_StatsFocus2.SetForegroundColour(wx.Colour(255, 0, 0))
        self.Txt_Mnl_StatsFocus2.SetBackgroundColour(wx.Colour(0, 0, 0))

        fgSizer18.Add(self.Txt_Mnl_StatsFocus2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL , 5)

        self.Pnl_MnlStats2.SetSizer(fgSizer18)
        self.Pnl_MnlStats2.Layout()
        fgSizer18.Fit(self.Pnl_MnlStats2)
        fgSizer17.Add(self.Pnl_MnlStats2, 1, wx.EXPAND | wx.ALL, 0)

        self.Pnl_Mnl_Scroll2 = wx.Panel(self.Mnl_Pnl_Move2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        self.Pnl_Mnl_Scroll2.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer19 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer19.SetFlexibleDirection(wx.BOTH)
        fgSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer19.SetMinSize(wx.Size(-1, 80))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.Lbl_Mnl_Jdl_Sudut2 = wx.StaticText(self.Pnl_Mnl_Scroll2, wx.ID_ANY, u"Sudut Axis", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.Lbl_Mnl_Jdl_Sudut2.Wrap(-1)
        self.Lbl_Mnl_Jdl_Sudut2.SetFont(wx.Font(10, 74, 90, 92, False, "Arial"))

        bSizer9.Add(self.Lbl_Mnl_Jdl_Sudut2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Mnl_Sld_Move2 = wx.Slider(self.Pnl_Mnl_Scroll2, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition,
                                       wx.Size(130, 20),
                                       wx.SL_HORIZONTAL)
        bSizer9.Add(self.Mnl_Sld_Move2, 0, wx.ALL, 5)

        self.Mnl_Spn_Value2 = wx.SpinCtrlDouble(self.Pnl_Mnl_Scroll2, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer9.Add(self.Mnl_Spn_Value2, 0, wx.ALL, 5)

        fgSizer19.Add(bSizer9, 1, wx.EXPAND, 5)

        self.Pnl_Mnl_Scroll2.SetSizer(fgSizer19)
        self.Pnl_Mnl_Scroll2.Layout()
        fgSizer19.Fit(self.Pnl_Mnl_Scroll2)
        fgSizer17.Add(self.Pnl_Mnl_Scroll2, 1, wx.EXPAND | wx.ALL, 0)

        self.Mnl_Pnl_Move2.SetSizer(fgSizer17)
        self.Mnl_Pnl_Move2.Layout()
        fgSizer17.Fit(self.Mnl_Pnl_Move2)

        # PANEL 6
        self.Mnl_Pnl_Move1 = wx.Panel(self.Bit_Background_Setup, wx.ID_ANY, wx.Point(450, 280), wx.Size(170, 60),
                                  wx.TAB_TRAVERSAL)
        # SET ID BASED BY MOTOR ID
        self.Mnl_Pnl_Move1.SetId(6)
        self.Mnl_Pnl_Move1.SetBackgroundColour(wx.Colour( 255, 255, 255 ))

        fgSizer17 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer17.SetFlexibleDirection(wx.BOTH)
        fgSizer17.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_MnlStats1 = wx.Panel(self.Mnl_Pnl_Move1, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                      wx.TAB_TRAVERSAL)
        self.Pnl_MnlStats1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_INACTIVECAPTION))

        fgSizer18 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer18.SetFlexibleDirection(wx.BOTH)
        fgSizer18.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Tgl_Mnl_FocusButton1 = wx.ToggleButton(self.Pnl_MnlStats1, wx.ID_ANY, u"1", wx.DefaultPosition,
                                                    wx.Size(50, 50), 0)
        self.Tgl_Mnl_FocusButton1.SetValue(False)
        self.Tgl_Mnl_FocusButton1.SetFont(wx.Font(36, 74, 90, 92, False, "Arial"))
        self.Tgl_Mnl_FocusButton1.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer18.Add(self.Tgl_Mnl_FocusButton1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.EXPAND, 5)

        self.Txt_Mnl_StatsFocus1 = wx.StaticText(self.Pnl_MnlStats1, wx.ID_ANY, u"INACTIVE", wx.DefaultPosition,
                                                 wx.Size(70, 15), wx.ALIGN_CENTRE)
        self.Txt_Mnl_StatsFocus1.Wrap(-1)
        self.Txt_Mnl_StatsFocus1.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Txt_Mnl_StatsFocus1.SetForegroundColour(wx.Colour(255, 0, 0))
        self.Txt_Mnl_StatsFocus1.SetBackgroundColour(wx.Colour(0, 0, 0))

        fgSizer18.Add(self.Txt_Mnl_StatsFocus1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL , 5)

        self.Pnl_MnlStats1.SetSizer(fgSizer18)
        self.Pnl_MnlStats1.Layout()
        fgSizer18.Fit(self.Pnl_MnlStats1)
        fgSizer17.Add(self.Pnl_MnlStats1, 1, wx.EXPAND | wx.ALL, 0)

        self.Pnl_Mnl_Scroll1 = wx.Panel(self.Mnl_Pnl_Move1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                        wx.TAB_TRAVERSAL)
        self.Pnl_Mnl_Scroll1.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer19 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer19.SetFlexibleDirection(wx.BOTH)
        fgSizer19.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer19.SetMinSize(wx.Size(-1, 80))

        bSizer9 = wx.BoxSizer(wx.VERTICAL)

        self.Lbl_Mnl_Jdl_Sudut1 = wx.StaticText(self.Pnl_Mnl_Scroll1, wx.ID_ANY, u"Sudut Axis", wx.DefaultPosition,
                                               wx.DefaultSize, 0)
        self.Lbl_Mnl_Jdl_Sudut1.Wrap(-1)
        self.Lbl_Mnl_Jdl_Sudut1.SetFont(wx.Font(10, 74, 90, 92, False, "Arial"))

        bSizer9.Add(self.Lbl_Mnl_Jdl_Sudut1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Mnl_Sld_Move1 = wx.Slider(self.Pnl_Mnl_Scroll1, wx.ID_ANY, 50, 0, 100, wx.DefaultPosition,
                                       wx.Size(130, 20),
                                       wx.SL_HORIZONTAL)
        bSizer9.Add(self.Mnl_Sld_Move1, 0, wx.ALL, 5)

        self.Mnl_Spn_Value1 = wx.SpinCtrlDouble(self.Pnl_Mnl_Scroll1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                                wx.DefaultSize,
                                                wx.SP_ARROW_KEYS, 0, 100, 0)
        bSizer9.Add(self.Mnl_Spn_Value1, 0, wx.ALL, 5)

        fgSizer19.Add(bSizer9, 1, wx.EXPAND, 5)

        self.Pnl_Mnl_Scroll1.SetSizer(fgSizer19)
        self.Pnl_Mnl_Scroll1.Layout()
        fgSizer19.Fit(self.Pnl_Mnl_Scroll1)
        fgSizer17.Add(self.Pnl_Mnl_Scroll1, 1, wx.EXPAND | wx.ALL, 0)

        self.Mnl_Pnl_Move1.SetSizer(fgSizer17)
        self.Mnl_Pnl_Move1.Layout()
        fgSizer17.Fit(self.Mnl_Pnl_Move1)


    def MnlPanelView(self,parent):
        self.Mnl_Pnl_View = wx.Panel(parent, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1,700),
                                   wx.TAB_TRAVERSAL | wx.TRANSPARENT_WINDOW)

        if self.Mnl_Pnl_View.CanSetTransparent:
            print 'can'
            self.Mnl_Pnl_View.SetTransparent(100)
        else:
            print 'cant'

        try:
            # pick an image file you have in the working folder
            # you can load .jpg  .png  .bmp  or .gif files
            image_file = os.path.normpath('.\\images\\background2.png')
            bmp1 = wx.Image(image_file, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
            # image's upper left corner anchors at panel coordinates (0, 0)
            self.Bit_Background_Setup2 = wx.StaticBitmap(self.Mnl_Pnl_View, -1, bmp1, pos=(0, 0))
            # show some image details
            str1 = "%s  %dx%d" % (image_file, bmp1.GetWidth(), bmp1.GetHeight())

        except IOError:
            print "Image file %s not found" % image_file
            raise SystemExit

        self.Mnl_Pnl_View.SetBackgroundColour(wx.Colour(152, 155, 175))

    def MnlTglMagnet(self, parent, x, y):
        self.Mnl_Pnl_MagnetTgl = wx.Panel(parent, wx.ID_ANY, wx.Point(x,y), wx.Size(160, 150), wx.TAB_TRAVERSAL)
        self.Mnl_Pnl_MagnetTgl.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer3 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Mnl_Lbl_MagnetStatus = wx.StaticText(self.Mnl_Pnl_MagnetTgl, wx.ID_ANY, u"Toggle Magnet",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.Mnl_Lbl_MagnetStatus.Wrap(-1)
        self.Mnl_Lbl_MagnetStatus.SetFont(wx.Font(12, 74, 90, 92, False, "Arial Black"))

        fgSizer3.Add(self.Mnl_Lbl_MagnetStatus, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Mnl_Tgl_Magnet = wx.ToggleButton(self.Mnl_Pnl_MagnetTgl, wx.ID_ANY, u"OFF", wx.DefaultPosition,
                                              wx.Size(150, 100), 0)
        self.Mnl_Tgl_Magnet.SetValue(False)
        self.Mnl_Tgl_Magnet.SetFont(wx.Font(24, 74, 90, 92, False, "Arial Black"))
        self.Mnl_Tgl_Magnet.SetForegroundColour(wx.Colour(255, 0, 0))

        fgSizer3.Add(self.Mnl_Tgl_Magnet, 0, wx.ALL, 5)

        self.Mnl_Pnl_MagnetTgl.SetSizer(fgSizer3)
        self.Mnl_Pnl_MagnetTgl.Layout()


    def MnlButtonByClick(self, parent, x, y):
        self.Pnl_Mnl_GoButton = wx.Panel(parent, wx.ID_ANY, wx.Point(x,y), wx.Size(160,150), wx.TAB_TRAVERSAL)
        self.Pnl_Mnl_GoButton.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        gSizer7 = wx.GridSizer(1, 1, 0, 0)

        fgSizer8 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Lbl_JdlGoByClick = wx.StaticText(self.Pnl_Mnl_GoButton, wx.ID_ANY, u"Go Button", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.Lbl_JdlGoByClick.Wrap(-1)
        self.Lbl_JdlGoByClick.SetFont(wx.Font(11, 74, 90, 92, False, "Arial Black"))

        fgSizer8.Add(self.Lbl_JdlGoByClick, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Cmd_Mnl_GoByClick = wx.Button(self.Pnl_Mnl_GoButton, wx.ID_ANY, u"GO", wx.DefaultPosition,
                                           wx.Size(150, 100), 0)
        self.Cmd_Mnl_GoByClick.SetFont(wx.Font(48, 70, 90, 92, False, "Arial"))
        self.Cmd_Mnl_GoByClick.SetForegroundColour(wx.Colour(0, 210, 0))

        fgSizer8.Add(self.Cmd_Mnl_GoByClick, 0, wx.ALL | wx.EXPAND, 5)

        gSizer7.Add(fgSizer8, 1, wx.EXPAND, 5)

        self.Pnl_Mnl_GoButton.SetSizer(gSizer7)
        self.Pnl_Mnl_GoButton.Layout()

    def MnlZeroByClick(self, parent, x, y):
        self.Pnl_Mnl_ZeroButton = wx.Panel(parent, wx.ID_ANY, wx.Point(x,y), wx.Size(160,80), wx.TAB_TRAVERSAL)
        self.Pnl_Mnl_ZeroButton.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        gSizer7 = wx.GridSizer(1, 1, 0, 0)

        fgSizer8 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Lbl_JdlZeroByClick = wx.StaticText(self.Pnl_Mnl_ZeroButton, wx.ID_ANY, u"Zero Button", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.Lbl_JdlZeroByClick.Wrap(-1)
        self.Lbl_JdlZeroByClick.SetFont(wx.Font(11, 74, 90, 92, False, "Arial Black"))

        fgSizer8.Add(self.Lbl_JdlZeroByClick, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Cmd_Mnl_ZeroByClick = wx.Button(self.Pnl_Mnl_ZeroButton, wx.ID_ANY, u"ZERO", wx.DefaultPosition,
                                           wx.Size(150, 40), 0)
        self.Cmd_Mnl_ZeroByClick.SetFont(wx.Font(18, 70, 90, 92, False, "Arial"))
        self.Cmd_Mnl_ZeroByClick.SetForegroundColour(wx.Colour(0, 210, 0))

        fgSizer8.Add(self.Cmd_Mnl_ZeroByClick, 0, wx.ALL | wx.EXPAND, 5)

        gSizer7.Add(fgSizer8, 1, wx.EXPAND, 5)

        self.Pnl_Mnl_ZeroButton.SetSizer(gSizer7)
        self.Pnl_Mnl_ZeroButton.Layout()

    def MnlButtonHome(self, parent, x, y):
        self.Pnl_Mnl_HomeButton = wx.Panel(parent, wx.ID_ANY, wx.Point(x,y), wx.Size(160,150), wx.TAB_TRAVERSAL)
        self.Pnl_Mnl_HomeButton.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        gSizer7 = wx.GridSizer(1, 1, 0, 0)

        fgSizer8 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer8.SetFlexibleDirection(wx.BOTH)
        fgSizer8.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Lbl_JdlHomeByClick = wx.StaticText(self.Pnl_Mnl_HomeButton, wx.ID_ANY, u"Home Button", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.Lbl_JdlHomeByClick.Wrap(-1)
        self.Lbl_JdlHomeByClick.SetFont(wx.Font(11, 74, 90, 92, False, "Arial Black"))

        fgSizer8.Add(self.Lbl_JdlHomeByClick, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Cmd_Mnl_HomeByClick = wx.Button(self.Pnl_Mnl_HomeButton, wx.ID_ANY, u"Home", wx.DefaultPosition,
                                           wx.Size(150, 100), 0)
        self.Cmd_Mnl_HomeByClick.SetFont(wx.Font(32, 70, 90, 92, False, "Arial"))
        self.Cmd_Mnl_HomeByClick.SetForegroundColour(wx.Colour(0, 210, 0))

        fgSizer8.Add(self.Cmd_Mnl_HomeByClick, 0, wx.ALL | wx.EXPAND, 5)

        gSizer7.Add(fgSizer8, 1, wx.EXPAND, 5)

        self.Pnl_Mnl_HomeButton.SetSizer(gSizer7)
        self.Pnl_Mnl_HomeButton.Layout()

    def MnlIndicator(self, parent, x, y):
        self.Pnl_Mnl_Indicator = wx.Panel(parent, id=wx.ID_ANY, pos=wx.Point(x,y), size=wx.Size(636, 95),
                          style=wx.TAB_TRAVERSAL)

        self.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ))

        fgSizer2 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Pnl_Mnl_WidgetChild1 = wx.Panel(self.Pnl_Mnl_Indicator, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Pnl_Mnl_WidgetChild1.SetBackgroundColour(wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVECAPTION ))

        fgSizer3 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Lbl_Jdl_Mnl_Widget = wx.StaticText(self.Pnl_Mnl_WidgetChild1, wx.ID_ANY, u"MANUAL TESTING",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_Jdl_Mnl_Widget.Wrap(-1)
        self.Lbl_Jdl_Mnl_Widget.SetFont(wx.Font(18, 74, 90, 92, False, "Arial Black"))
        self.Lbl_Jdl_Mnl_Widget.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))

        fgSizer3.Add(self.Lbl_Jdl_Mnl_Widget, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        bSizer2 = wx.BoxSizer(wx.HORIZONTAL)

        self.Cmd_Mnl_WidgetUseMouse = wx.Button(self.Pnl_Mnl_WidgetChild1, wx.ID_ANY, u"Use Mouse",
                                                  wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.Cmd_Mnl_WidgetUseMouse, 0, wx.ALL, 5)

        self.Cmd_Mnl_WidgetUseController = wx.Button(self.Pnl_Mnl_WidgetChild1, wx.ID_ANY, u"Use Controller",
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.Cmd_Mnl_WidgetUseController, 0, wx.ALL, 5)

        self.Cmd_Mnl_WidgetUseForm = wx.Button(self.Pnl_Mnl_WidgetChild1, wx.ID_ANY, u"Use Form",
                                                 wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer2.Add(self.Cmd_Mnl_WidgetUseForm, 0, wx.ALL, 5)

        fgSizer3.Add(bSizer2, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Pnl_Mnl_WidgetChild1.SetSizer(fgSizer3)
        self.Pnl_Mnl_WidgetChild1.Layout()
        fgSizer3.Fit(self.Pnl_Mnl_WidgetChild1)
        fgSizer2.Add(self.Pnl_Mnl_WidgetChild1, 1, wx.EXPAND | wx.ALL, 2)

        self.Pnl_Mnl_WidgetChild2 = wx.Panel(self.Pnl_Mnl_Indicator, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        self.Pnl_Mnl_WidgetChild2.SetBackgroundColour(wx.Colour(255, 255, 255))

        gbSizer3 = wx.GridBagSizer(0, 0)
        gbSizer3.SetFlexibleDirection(wx.BOTH)
        gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        gbSizer3.SetMinSize(wx.Size(390, -1))
        self.Lbl_Mnl_WidgetUsedMode = wx.StaticText(self.Pnl_Mnl_WidgetChild2, wx.ID_ANY, u" Used Mode =",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_Mnl_WidgetUsedMode.Wrap(-1)
        gbSizer3.Add(self.Lbl_Mnl_WidgetUsedMode, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_Mnl_WidgetUsedModeView = wx.StaticText(self.Pnl_Mnl_WidgetChild2, wx.ID_ANY, u"-",
                                                          wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_Mnl_WidgetUsedModeView.Wrap(-1)
        self.Lbl_Mnl_WidgetUsedModeView.SetFont(wx.Font(11, 70, 90, 92, False, "Arial"))

        gbSizer3.Add(self.Lbl_Mnl_WidgetUsedModeView, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_Mnl_WidgetControllerStats = wx.StaticText(self.Pnl_Mnl_WidgetChild2, wx.ID_ANY,
                                                             u"Controller Status =", wx.DefaultPosition, wx.DefaultSize,
                                                             0)
        self.Lbl_Mnl_WidgetControllerStats.Wrap(-1)
        gbSizer3.Add(self.Lbl_Mnl_WidgetControllerStats, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_Mnl_WidgetControllerStatsView = wx.StaticText(self.Pnl_Mnl_WidgetChild2, wx.ID_ANY,
                                                                 u"DISCONNECTED", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_Mnl_WidgetControllerStatsView.Wrap(-1)
        self.Lbl_Mnl_WidgetControllerStatsView.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))
        self.Lbl_Mnl_WidgetControllerStatsView.SetForegroundColour(wx.Colour(255, 4, 4))
        self.Lbl_Mnl_WidgetControllerStatsView.SetBackgroundColour(
            wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        gbSizer3.Add(self.Lbl_Mnl_WidgetControllerStatsView, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Pnl_Mnl_WidgetChild2.SetSizer(gbSizer3)
        self.Pnl_Mnl_WidgetChild2.Layout()
        gbSizer3.Fit(self.Pnl_Mnl_WidgetChild2)
        fgSizer2.Add(self.Pnl_Mnl_WidgetChild2, 1, wx.EXPAND | wx.ALL, 2)

        self.Pnl_Mnl_Indicator.SetSizer(fgSizer2)
        self.Pnl_Mnl_Indicator.Layout()


    def MnlPnlModeTest(self,parent,x, y):
        self.Pnl_Mnl_ModeTest = wx.Panel(parent, wx.ID_ANY, wx.Point(x,y), wx.Size(420,80), wx.TAB_TRAVERSAL)

        fgSizer5 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer6 = wx.FlexGridSizer(1, 1, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Lbl_Mnl_JdlModeText = wx.StaticText(self.Pnl_Mnl_ModeTest, wx.ID_ANY, u"Mode Testing", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.Lbl_Mnl_JdlModeText.Wrap(-1)
        self.Lbl_Mnl_JdlModeText.SetFont(wx.Font(11, 74, 90, 92, False, "Arial Black"))

        fgSizer6.Add(self.Lbl_Mnl_JdlModeText, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer5.Add(fgSizer6, 1, wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer7 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer7.SetFlexibleDirection(wx.BOTH)
        fgSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        gSizer6 = wx.GridSizer(1, 3, 0, 0)

        self.Cmd_Mnl_WidgetUseMouse = wx.Button(self.Pnl_Mnl_ModeTest, wx.ID_ANY, u"By Click", wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        gSizer6.Add(self.Cmd_Mnl_WidgetUseMouse, 0, wx.ALL, 5)

        self.Cmd_Mnl_WidgetUseController = wx.Button(self.Pnl_Mnl_ModeTest, wx.ID_ANY, u"By Scroll", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        gSizer6.Add(self.Cmd_Mnl_WidgetUseController, 0, wx.ALL, 5)

        self.Cmd_Mnl_WidgetUseForm = wx.Button(self.Pnl_Mnl_ModeTest, wx.ID_ANY, u"By Form", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gSizer6.Add(self.Cmd_Mnl_WidgetUseForm, 0, wx.ALL, 5)

        fgSizer7.Add(gSizer6, 1, wx.EXPAND, 5)

        self.Lbl_Mnl_WidgetUsedModeView = wx.StaticText(self.Pnl_Mnl_ModeTest, wx.ID_ANY, u"Mode", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.Lbl_Mnl_WidgetUsedModeView.Wrap(-1)
        self.Lbl_Mnl_WidgetUsedModeView.SetFont(wx.Font(14, 74, 90, 92, False, "Arial"))
        self.Lbl_Mnl_WidgetUsedModeView.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHT))

        fgSizer7.Add(self.Lbl_Mnl_WidgetUsedModeView, 0, wx.ALL, 5)

        fgSizer5.Add(fgSizer7, 1, wx.EXPAND, 5)

        self.Pnl_Mnl_ModeTest.SetSizer(fgSizer5)
        self.Pnl_Mnl_ModeTest.Layout()


    def MnlOnFocus(self, mode, type, **kwargs):
        if mode == 1:
            self.Mnl_CurrentSlider = type
        elif mode == 2:
            self.Mnl_CurrentSpin = type
        elif mode == 3:
            if type == 1:
                if kwargs['togglevalue'] == True:
                    self.MnlScrollSetINACT(mode)
                    self.Txt_Mnl_StatsFocus1.SetLabel('ACTIVE')
                    self.Txt_Mnl_StatsFocus1.SetForegroundColour(wx.Colour(0, 255, 0))
                    self.Mnl_CurrentSlider = type
                    self.Mnl_CurrentSpin = type

                    # Deactivate
                    self.MnlScrollSetINACT(1)
                    self.MnlScrollSetINACT(2)
                    self.MnlScrollSetINACT(3)
                    self.MnlScrollSetINACT(4)
                    self.MnlScrollSetINACT(5)
                    #self.MnlScrollSetINACT(6)

                else:
                    self.MnlScrollSetINACT(mode)
                    self.Txt_Mnl_StatsFocus1.SetLabel('ACTIVE')
                    self.Txt_Mnl_StatsFocus1.SetForegroundColour(wx.Colour(0, 255, 0))
                    self.Mnl_CurrentSlider = type
                    self.Mnl_CurrentSpin = type

                    # Deactivate
                    self.MnlScrollSetINACT(1)
                    self.MnlScrollSetINACT(2)
                    self.MnlScrollSetINACT(3)
                    self.MnlScrollSetINACT(4)
                    self.MnlScrollSetINACT(5)
                    # self.MnlScrollSetINACT(6)

            elif type == 2:
                if kwargs['togglevalue'] == True:
                    self.MnlScrollSetINACT(mode)
                    self.Txt_Mnl_StatsFocus2.SetLabel('ACTIVE')
                    self.Txt_Mnl_StatsFocus2.SetForegroundColour(wx.Colour(0, 255, 0))
                    self.Mnl_CurrentSlider = type
                    self.Mnl_CurrentSpin = type

                    # Deactivate
                    self.MnlScrollSetINACT(1)
                    self.MnlScrollSetINACT(2)
                    self.MnlScrollSetINACT(3)
                    self.MnlScrollSetINACT(4)
                    #self.MnlScrollSetINACT(5)
                    self.MnlScrollSetINACT(6)

                else:
                    self.MnlScrollSetINACT(mode)
                    self.Txt_Mnl_StatsFocus2.SetLabel('ACTIVE')
                    self.Txt_Mnl_StatsFocus2.SetForegroundColour(wx.Colour(0, 255, 0))
                    self.Mnl_CurrentSlider = type
                    self.Mnl_CurrentSpin = type

                    # Deactivate
                    self.MnlScrollSetINACT(1)
                    self.MnlScrollSetINACT(2)
                    self.MnlScrollSetINACT(3)
                    self.MnlScrollSetINACT(4)
                    # self.MnlScrollSetINACT(5)
                    self.MnlScrollSetINACT(6)

            elif type == 3:
                if kwargs['togglevalue'] == True:
                    self.MnlScrollSetINACT(mode)
                    self.Txt_Mnl_StatsFocus3.SetLabel('ACTIVE')
                    self.Txt_Mnl_StatsFocus3.SetForegroundColour(wx.Colour(0, 255, 0))
                    self.Mnl_CurrentSlider = type
                    self.Mnl_CurrentSpin = type

                    # Deactivate
                    self.MnlScrollSetINACT(1)
                    self.MnlScrollSetINACT(2)
                    self.MnlScrollSetINACT(3)
                    #self.MnlScrollSetINACT(4)
                    self.MnlScrollSetINACT(5)
                    self.MnlScrollSetINACT(6)

                else:
                    self.MnlScrollSetINACT(mode)
                    self.Txt_Mnl_StatsFocus3.SetLabel('ACTIVE')
                    self.Txt_Mnl_StatsFocus3.SetForegroundColour(wx.Colour(0, 255, 0))
                    self.Mnl_CurrentSlider = type
                    self.Mnl_CurrentSpin = type

                    # Deactivate
                    self.MnlScrollSetINACT(1)
                    self.MnlScrollSetINACT(2)
                    self.MnlScrollSetINACT(3)
                    # self.MnlScrollSetINACT(4)
                    self.MnlScrollSetINACT(5)
                    self.MnlScrollSetINACT(6)

            elif type == 4:
                if kwargs['togglevalue'] == True:
                    self.MnlScrollSetINACT(mode)
                    self.Txt_Mnl_StatsFocus4.SetLabel('ACTIVE')
                    self.Txt_Mnl_StatsFocus4.SetForegroundColour(wx.Colour(0, 255, 0))
                    self.Mnl_CurrentSlider = type
                    self.Mnl_CurrentSpin = type

                    # Deactivate
                    self.MnlScrollSetINACT(1)
                    self.MnlScrollSetINACT(2)
                    #self.MnlScrollSetINACT(3)
                    self.MnlScrollSetINACT(4)
                    self.MnlScrollSetINACT(5)
                    self.MnlScrollSetINACT(6)

                else:
                    self.MnlScrollSetINACT(mode)
                    self.Txt_Mnl_StatsFocus4.SetLabel('ACTIVE')
                    self.Txt_Mnl_StatsFocus4.SetForegroundColour(wx.Colour(0, 255, 0))
                    self.Mnl_CurrentSlider = type
                    self.Mnl_CurrentSpin = type

                    # Deactivate
                    self.MnlScrollSetINACT(1)
                    self.MnlScrollSetINACT(2)
                    # self.MnlScrollSetINACT(3)
                    self.MnlScrollSetINACT(4)
                    self.MnlScrollSetINACT(5)
                    self.MnlScrollSetINACT(6)


            elif type == 5:
                if kwargs['togglevalue'] == True:
                    self.MnlScrollSetINACT(mode)
                    self.Txt_Mnl_StatsFocus5.SetLabel('ACTIVE')
                    self.Txt_Mnl_StatsFocus5.SetForegroundColour(wx.Colour(0, 255, 0))
                    self.Mnl_CurrentSlider = type
                    self.Mnl_CurrentSpin = type

                    # Deactivate
                    self.MnlScrollSetINACT(1)
                    #self.MnlScrollSetINACT(2)
                    self.MnlScrollSetINACT(3)
                    self.MnlScrollSetINACT(4)
                    self.MnlScrollSetINACT(5)
                    self.MnlScrollSetINACT(6)

                else:
                    self.MnlScrollSetINACT(mode)
                    self.Txt_Mnl_StatsFocus5.SetLabel('ACTIVE')
                    self.Txt_Mnl_StatsFocus5.SetForegroundColour(wx.Colour(0, 255, 0))
                    self.Mnl_CurrentSlider = type
                    self.Mnl_CurrentSpin = type

                    # Deactivate
                    self.MnlScrollSetINACT(1)
                    # self.MnlScrollSetINACT(2)
                    self.MnlScrollSetINACT(3)
                    self.MnlScrollSetINACT(4)
                    self.MnlScrollSetINACT(5)
                    self.MnlScrollSetINACT(6)
            elif type == 6:
                if kwargs['togglevalue'] == True:
                    self.MnlScrollSetINACT(mode)
                    self.Txt_Mnl_StatsFocus6.SetLabel('ACTIVE')
                    self.Txt_Mnl_StatsFocus6.SetForegroundColour(wx.Colour(0, 255, 0))
                    self.Mnl_CurrentSlider = type
                    self.Mnl_CurrentSpin = type

                    #Deactivate
                    #self.MnlScrollSetINACT(1)
                    self.MnlScrollSetINACT(2)
                    self.MnlScrollSetINACT(3)
                    self.MnlScrollSetINACT(4)
                    self.MnlScrollSetINACT(5)
                    self.MnlScrollSetINACT(6)
                else:
                    self.MnlScrollSetINACT(mode)
                    self.Txt_Mnl_StatsFocus6.SetLabel('ACTIVE')
                    self.Txt_Mnl_StatsFocus6.SetForegroundColour(wx.Colour(0, 255, 0))
                    self.Mnl_CurrentSlider = type
                    self.Mnl_CurrentSpin = type

                    # Deactivate
                    # self.MnlScrollSetINACT(1)
                    self.MnlScrollSetINACT(2)
                    self.MnlScrollSetINACT(3)
                    self.MnlScrollSetINACT(4)
                    self.MnlScrollSetINACT(5)
                    self.MnlScrollSetINACT(6)
        self.CurrentFocus = type

    def MnlResetScroll(self, **kwargs):
        try:
            kwargs['controller']
        except Exception as e:
            # Deactivate
            self.MnlScrollSetINACT(1)
            self.MnlScrollSetINACT(2)
            self.MnlScrollSetINACT(3)
            self.MnlScrollSetINACT(4)
            self.MnlScrollSetINACT(5)
            self.MnlScrollSetINACT(6)
        else:
            self.Mnl_Sld_Move1.SetValue(0)
            self.Mnl_Spn_Value1.SetValue(0)
            self.Mnl_Sld_Move2.SetValue(0)
            self.Mnl_Spn_Value2.SetValue(0)
            self.Mnl_Sld_Move3.SetValue(0)
            self.Mnl_Spn_Value3.SetValue(0)
            self.Mnl_Sld_Move4.SetValue(0)
            self.Mnl_Spn_Value4.SetValue(0)
            self.Mnl_Sld_Move5.SetValue(0)
            self.Mnl_Spn_Value5.SetValue(0)
            self.Mnl_Sld_Move6.SetValue(0)
            self.Mnl_Spn_Value6.SetValue(0)
        self.PositionNow = ''
        self.CurrentFocus = ''


    def MnlScrollSetINACT(self, mode):
        if mode == 1:
            self.Txt_Mnl_StatsFocus6.SetLabel('INACTIVE')
            self.Tgl_Mnl_FocusButton6.SetValue(False)
            self.Txt_Mnl_StatsFocus6.SetForegroundColour(wx.Colour(255, 0, 0))
        elif mode == 2:
            self.Txt_Mnl_StatsFocus5.SetLabel('INACTIVE')
            self.Tgl_Mnl_FocusButton5.SetValue(False)
            self.Txt_Mnl_StatsFocus5.SetForegroundColour(wx.Colour(255, 0, 0))
        elif mode == 3:
            self.Txt_Mnl_StatsFocus4.SetLabel('INACTIVE')
            self.Tgl_Mnl_FocusButton4.SetValue(False)
            self.Txt_Mnl_StatsFocus4.SetForegroundColour(wx.Colour(255, 0, 0))
        elif mode == 4:
            self.Txt_Mnl_StatsFocus3.SetLabel('INACTIVE')
            self.Tgl_Mnl_FocusButton3.SetValue(False)
            self.Txt_Mnl_StatsFocus3.SetForegroundColour(wx.Colour(255, 0, 0))
        elif mode == 5:
            self.Txt_Mnl_StatsFocus2.SetLabel('INACTIVE')
            self.Tgl_Mnl_FocusButton2.SetValue(False)
            self.Txt_Mnl_StatsFocus2.SetForegroundColour(wx.Colour(255, 0, 0))
        elif mode == 6:
            self.Txt_Mnl_StatsFocus1.SetLabel('INACTIVE')
            self.Tgl_Mnl_FocusButton1.SetValue(False)
            self.Txt_Mnl_StatsFocus1.SetForegroundColour(wx.Colour(255, 0, 0))




    def MnlOnChange(self, mode , type):
        #SLIDER MOVEMENT
        self.Mnl_CurrentSlider = type
        self.Mnl_CurrentSpin = type
        self.CurrentFocus = self.Mnl_CurrentSlider

        if mode == 1:
            if self.Mnl_CurrentSlider == 1:
                self.MnlOnFocus(3, 1, togglevalue=self.Tgl_Mnl_FocusButton1.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 3, value=self.Mnl_Sld_Move1.GetValue(),
                                         inc=self.Mnl_Spn_Value1.GetIncrement())
                self.Mnl_Spn_Value1.SetValue(values)

            elif self.Mnl_CurrentSlider == 2:
                self.MnlOnFocus(3, 2, togglevalue=self.Tgl_Mnl_FocusButton2.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 3, value=self.Mnl_Sld_Move2.GetValue(),
                                         inc=self.Mnl_Spn_Value2.GetIncrement())
                self.Mnl_Spn_Value2.SetValue(values)

            elif self.Mnl_CurrentSlider == 3:
                self.MnlOnFocus(3, 3, togglevalue=self.Tgl_Mnl_FocusButton3.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 3, value=self.Mnl_Sld_Move3.GetValue(),
                                         inc=self.Mnl_Spn_Value3.GetIncrement())
                self.Mnl_Spn_Value3.SetValue(values)

            elif self.Mnl_CurrentSlider == 4:
                self.MnlOnFocus(3, 4, togglevalue=self.Tgl_Mnl_FocusButton4.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 3, value=self.Mnl_Sld_Move4.GetValue(),
                                         inc=self.Mnl_Spn_Value4.GetIncrement())
                self.Mnl_Spn_Value4.SetValue(values)

            elif self.Mnl_CurrentSlider == 5:
                self.MnlOnFocus(3, 5, togglevalue=self.Tgl_Mnl_FocusButton5.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 3, value=self.Mnl_Sld_Move5.GetValue(),
                                         inc=self.Mnl_Spn_Value5.GetIncrement())
                self.Mnl_Spn_Value5.SetValue(values)

            elif self.Mnl_CurrentSlider == 6:
                self.MnlOnFocus(3, 6, togglevalue=self.Tgl_Mnl_FocusButton6.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 3, value=self.Mnl_Sld_Move6.GetValue(),
                                         inc=self.Mnl_Spn_Value6.GetIncrement())
                self.Mnl_Spn_Value6.SetValue(values)
            else:
                return

            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message=('value sld>>spn [' + str(self.Mnl_CurrentSlider)+'] = ' + str(values)))

        elif mode == 2:
            if self.Mnl_CurrentSpin == 1:
                self.MnlOnFocus(3, 1, togglevalue=self.Tgl_Mnl_FocusButton1.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 2, value=self.Mnl_Spn_Value1.GetValue(),
                                         inc=self.Mnl_Spn_Value6.GetIncrement())
                self.Mnl_Sld_Move1.SetValue(values)

            elif self.Mnl_CurrentSpin == 2:
                self.MnlOnFocus(3, 2, togglevalue=self.Tgl_Mnl_FocusButton2.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 2, value=self.Mnl_Spn_Value2.GetValue(),
                                         inc=self.Mnl_Spn_Value2.GetIncrement())
                self.Mnl_Sld_Move2.SetValue(values)

            elif self.Mnl_CurrentSpin == 3:
                self.MnlOnFocus(3, 3, togglevalue=self.Tgl_Mnl_FocusButton3.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 2, value=self.Mnl_Spn_Value3.GetValue(),
                                         inc=self.Mnl_Spn_Value3.GetIncrement())
                self.Mnl_Sld_Move3.SetValue(values)

            elif self.Mnl_CurrentSpin == 4:
                self.MnlOnFocus(3, 4 , togglevalue=self.Tgl_Mnl_FocusButton4.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 2, value=self.Mnl_Spn_Value4.GetValue(),
                                         inc=self.Mnl_Spn_Value4.GetIncrement())
                self.Mnl_Sld_Move4.SetValue(values)

            elif self.Mnl_CurrentSpin== 5:
                self.MnlOnFocus(3, 5, togglevalue=self.Tgl_Mnl_FocusButton5.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 2, value=self.Mnl_Spn_Value5.GetValue(),
                                         inc=self.Mnl_Spn_Value5.GetIncrement())
                self.Mnl_Sld_Move5.SetValue(values)

            elif self.Mnl_CurrentSpin == 6:
                self.MnlOnFocus(3, 6, togglevalue=self.Tgl_Mnl_FocusButton6.GetValue())
                values = self.CCalculate('SPIN-SLIDER', 2, value=self.Mnl_Spn_Value6.GetValue(),
                                         inc=self.Mnl_Spn_Value6.GetIncrement())
                self.Mnl_Sld_Move6.SetValue(values)
            else:
                return

            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message=('value spn>>sld ['+str(self.Mnl_CurrentSpin)+'] = ' + str(values)))

    def MnlSetToFrame(self , dictkoor):
        if dictkoor.get(1) != None:
            self.Mnl_Spn_Value1.SetValue(dictkoor[1])
            self.Mnl_Sld_Move1.SetValue(dictkoor[1])
        if dictkoor.get(2) != None:
            self.Mnl_Spn_Value2.SetValue(dictkoor[1])
            self.Mnl_Sld_Move2.SetValue(dictkoor[1])
        if dictkoor.get(3) != None:
            self.Mnl_Spn_Value3.SetValue(dictkoor[1])
            self.Mnl_Sld_Move3.SetValue(dictkoor[1])
        if dictkoor.get(4) != None:
            self.Mnl_Spn_Value4.SetValue(dictkoor[1])
            self.Mnl_Sld_Move4.SetValue(dictkoor[1])
        if dictkoor.get(5) != None:
            self.Mnl_Spn_Value5.SetValue(dictkoor[1])
            self.Mnl_Sld_Move5.SetValue(dictkoor[1])




    def MnlPnlByForm(self, parent):
        self.Pnl_Mnl_ByForm = wx.Panel(parent, wx.ID_ANY, wx.Point(15,5), wx.Size(240,270), wx.TAB_TRAVERSAL)
        self.Pnl_Mnl_ByForm.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer71 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer71.SetFlexibleDirection(wx.BOTH)
        fgSizer71.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_staticText14 = wx.StaticText(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"Testing By Form", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText14.Wrap(-1)
        self.m_staticText14.SetFont(wx.Font(14, 74, 90, 92, False, "Arial"))

        fgSizer71.Add(self.m_staticText14, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gbSizer3 = wx.GridBagSizer(0, 0)
        gbSizer3.SetFlexibleDirection(wx.BOTH)
        gbSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Lbl_Mnl_byFM1 = wx.StaticText(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"M1", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_Mnl_byFM1.Wrap(-1)
        gbSizer3.Add(self.Lbl_Mnl_byFM1, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Txt_Mnl_ValM1 = wx.TextCtrl(self.Pnl_Mnl_ByForm, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.Txt_Mnl_ValM1.SetMaxLength(4)
        gbSizer3.Add(self.Txt_Mnl_ValM1, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        Cmb_Mnl_DirM1Choices = [u"CCW", u"CW",u"-"]
        self.Cmb_Mnl_DirM1 = wx.ComboBox(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize,
                                         Cmb_Mnl_DirM1Choices, 0)
        gbSizer3.Add(self.Cmb_Mnl_DirM1, wx.GBPosition(1, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_Mnl_byFM2 = wx.StaticText(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"M2", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_Mnl_byFM2.Wrap(-1)
        gbSizer3.Add(self.Lbl_Mnl_byFM2, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Txt_Mnl_ValM2 = wx.TextCtrl(self.Pnl_Mnl_ByForm, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.Txt_Mnl_ValM2.SetMaxLength(4)
        gbSizer3.Add(self.Txt_Mnl_ValM2, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        Cmb_Mnl_DirM2Choices = [u"CCW", u"CW",u"-"]
        self.Cmb_Mnl_DirM2 = wx.ComboBox(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize,
                                         Cmb_Mnl_DirM2Choices, 0)
        gbSizer3.Add(self.Cmb_Mnl_DirM2, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_Mnl_byFM3 = wx.StaticText(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"M3", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_Mnl_byFM3.Wrap(-1)
        gbSizer3.Add(self.Lbl_Mnl_byFM3, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Txt_Mnl_ValM3 = wx.TextCtrl(self.Pnl_Mnl_ByForm, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.Txt_Mnl_ValM3.SetMaxLength(4)
        gbSizer3.Add(self.Txt_Mnl_ValM3, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        Cmb_Mnl_DirM3Choices = [u"CCW", u"CW",u"-"]
        self.Cmb_Mnl_DirM3 = wx.ComboBox(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize,
                                         Cmb_Mnl_DirM3Choices, 0)
        gbSizer3.Add(self.Cmb_Mnl_DirM3, wx.GBPosition(3, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_Mnl_byFM4 = wx.StaticText(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"M4", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_Mnl_byFM4.Wrap(-1)
        gbSizer3.Add(self.Lbl_Mnl_byFM4, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Txt_Mnl_ValM4 = wx.TextCtrl(self.Pnl_Mnl_ByForm, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.Txt_Mnl_ValM4.SetMaxLength(4)
        gbSizer3.Add(self.Txt_Mnl_ValM4, wx.GBPosition(4, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        Cmb_Mnl_DirM4Choices = [u"CCW", u"CW",u"-"]
        self.Cmb_Mnl_DirM4 = wx.ComboBox(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize,
                                         Cmb_Mnl_DirM4Choices, 0)
        gbSizer3.Add(self.Cmb_Mnl_DirM4, wx.GBPosition(4, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_Mnl_byFM5 = wx.StaticText(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"M5", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_Mnl_byFM5.Wrap(-1)
        gbSizer3.Add(self.Lbl_Mnl_byFM5, wx.GBPosition(5, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Txt_Mnl_ValM5 = wx.TextCtrl(self.Pnl_Mnl_ByForm, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.DefaultSize, 0)
        self.Txt_Mnl_ValM5.SetMaxLength(4)
        gbSizer3.Add(self.Txt_Mnl_ValM5, wx.GBPosition(5, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_Mnl_byFM6 = wx.StaticText(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"M6", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_Mnl_byFM6.Wrap(-1)
        gbSizer3.Add(self.Lbl_Mnl_byFM6, wx.GBPosition(6, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        Cmb_Mnl_ValM6Choices = [u"ON", u"OFF",u"-"]
        self.Cmb_Mnl_ValM6 = wx.ComboBox(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize,
                                         Cmb_Mnl_ValM6Choices, 0)
        gbSizer3.Add(self.Cmb_Mnl_ValM6, wx.GBPosition(6, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_Mnl_HeaderMotor = wx.StaticText(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"Motor", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.Lbl_Mnl_HeaderMotor.Wrap(-1)
        self.Lbl_Mnl_HeaderMotor.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))

        gbSizer3.Add(self.Lbl_Mnl_HeaderMotor, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_Mnl_HeaderValue = wx.StaticText(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"Value", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.Lbl_Mnl_HeaderValue.Wrap(-1)
        self.Lbl_Mnl_HeaderValue.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))

        gbSizer3.Add(self.Lbl_Mnl_HeaderValue, wx.GBPosition(0, 1), wx.GBSpan(1, 1),
                     wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Lbl_Mnl_HeaderDirection = wx.StaticText(self.Pnl_Mnl_ByForm, wx.ID_ANY, u"Direction", wx.DefaultPosition,
                                                     wx.DefaultSize, 0)
        self.Lbl_Mnl_HeaderDirection.Wrap(-1)
        self.Lbl_Mnl_HeaderDirection.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))

        gbSizer3.Add(self.Lbl_Mnl_HeaderDirection, wx.GBPosition(0, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        fgSizer71.Add(gbSizer3, 1, wx.EXPAND, 5)

        self.Pnl_Mnl_ByForm.SetSizer(fgSizer71)
        self.Pnl_Mnl_ByForm.Layout()

    def MnlPnlSpeed(self,parent):
        self.Pnl_ManualSpeed = wx.Panel(parent, wx.ID_ANY, wx.Point(280,5), wx.Size(220,270), wx.TAB_TRAVERSAL)
        self.Pnl_ManualSpeed.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer4 = wx.FlexGridSizer(3, 1, 0, 0)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Lbl_Mnl_SpeedJdl = wx.StaticText(self.Pnl_ManualSpeed, wx.ID_ANY, u"Settingan Speed Motor",
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.Lbl_Mnl_SpeedJdl.Wrap(-1)
        self.Lbl_Mnl_SpeedJdl.SetFont(wx.Font(14, 74, 90, 92, False, "Arial"))
        fgSizer4.Add(self.Lbl_Mnl_SpeedJdl, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Lbl_Mnl_SpeedM1 = wx.StaticText(self.Pnl_ManualSpeed, wx.ID_ANY, u"M1", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.Lbl_Mnl_SpeedM1.Wrap(-1)
        gbSizer2.Add(self.Lbl_Mnl_SpeedM1, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Txt_Mnl_SpeedM1 = wx.TextCtrl(self.Pnl_ManualSpeed, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(150, -1), 0)
        gbSizer2.Add(self.Txt_Mnl_SpeedM1, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_Mnl_SpeedM2 = wx.StaticText(self.Pnl_ManualSpeed, wx.ID_ANY, u"M2", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.Lbl_Mnl_SpeedM2.Wrap(-1)
        gbSizer2.Add(self.Lbl_Mnl_SpeedM2, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Txt_Mnl_SpeedM2 = wx.TextCtrl(self.Pnl_ManualSpeed, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(150, -1), 0)
        gbSizer2.Add(self.Txt_Mnl_SpeedM2, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_Mnl_SpeedM3 = wx.StaticText(self.Pnl_ManualSpeed, wx.ID_ANY, u"M3", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.Lbl_Mnl_SpeedM3.Wrap(-1)
        gbSizer2.Add(self.Lbl_Mnl_SpeedM3, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Txt_Mnl_SpeedM3 = wx.TextCtrl(self.Pnl_ManualSpeed, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                     wx.Size(150, -1), 0)
        gbSizer2.Add(self.Txt_Mnl_SpeedM3, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Lbl_Mnl_SpeedM4 = wx.StaticText(self.Pnl_ManualSpeed, wx.ID_ANY, u"M4", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.Lbl_Mnl_SpeedM4.Wrap(-1)
        gbSizer2.Add(self.Lbl_Mnl_SpeedM4, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Txt_Mnl_SpeedM4 = wx.TextCtrl(self.Pnl_ManualSpeed, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gbSizer2.Add(self.Txt_Mnl_SpeedM4, wx.GBPosition(4, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        self.Lbl_Mnl_SpeedM5 = wx.StaticText(self.Pnl_ManualSpeed, wx.ID_ANY, u"M5", wx.DefaultPosition, wx.DefaultSize,
                                             0)
        self.Lbl_Mnl_SpeedM5.Wrap(-1)
        gbSizer2.Add(self.Lbl_Mnl_SpeedM5, wx.GBPosition(5, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Txt_Mnl_SpeedM5 = wx.TextCtrl(self.Pnl_ManualSpeed, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        gbSizer2.Add(self.Txt_Mnl_SpeedM5, wx.GBPosition(5, 1), wx.GBSpan(1, 1), wx.ALL | wx.EXPAND, 5)

        fgSizer4.Add(gbSizer2, 1, wx.EXPAND, 5)

        gSizer5 = wx.GridSizer(1, 2, 0, 0)

        self.Cmd_Mnl_SetSpeed = wx.Button(self.Pnl_ManualSpeed, wx.ID_ANY, u"Set", wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer5.Add(self.Cmd_Mnl_SetSpeed, 0, wx.ALL, 5)

        self.Cmd_Mnl_ResetSpeed = wx.Button(self.Pnl_ManualSpeed, wx.ID_ANY, u"Reset", wx.DefaultPosition, wx.DefaultSize,
                                         0)
        gSizer5.Add(self.Cmd_Mnl_ResetSpeed, 0, wx.ALL, 5)

        fgSizer4.Add(gSizer5, 1, wx.EXPAND, 5)

        self.Pnl_ManualSpeed.SetSizer(fgSizer4)
        self.Pnl_ManualSpeed.Layout()

    def MnlModeChange(self, mode):
        #By Click
        if mode == 1:
            # END CONTROLLER MODE
            self.Controller_Mode = False

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
            #self.CExecutingCommand(commandlists, feedbacklists, save=True)


            self.Cmd_Mnl_WidgetUseMouse.Disable()
            self.Cmd_Mnl_WidgetUseController.Enable()
            self.Cmd_Mnl_WidgetUseForm.Enable()
            #Realtime = False

            #PANEL BUTTON
            self.Lbl_Mnl_WidgetUsedModeView.SetLabel("BY MOUSE")
            self.Pnl_Mnl_GoButton.Show()
            self.Pnl_Mnl_ByForm.Hide()

            #START DETECTING POS
            self.DetectingPos = True


        #By Scroll
        elif mode == 2:

            self.Cmd_Mnl_WidgetUseMouse.Enable()
            self.Cmd_Mnl_WidgetUseController.Disable()
            self.Cmd_Mnl_WidgetUseForm.Enable()

            # PANEL BUTTON
            self.Lbl_Mnl_WidgetUsedModeView.SetLabel("BY CONTROLLER")
            self.Pnl_Mnl_GoButton.Hide()
            self.Pnl_Mnl_ByForm.Hide()


            #Reset Focus and Position Now
            self.MnlResetScroll()

            #START WITH CONTROLLER
            self.Controller_Mode = True

        # By Form
        elif mode == 3:
            #END CONTROLLER MODE
            self.Controller_Mode = False

            self.Cmd_Mnl_WidgetUseMouse.Enable()
            self.Cmd_Mnl_WidgetUseController.Enable()
            self.Cmd_Mnl_WidgetUseForm.Disable()

            # PANEL BUTTON
            self.Lbl_Mnl_WidgetUsedModeView.SetLabel("BY FORM")
            self.Pnl_Mnl_GoButton.Show()
            self.Pnl_Mnl_ByForm.Show()
            self.DetectingPos = False

    def MnlListingData(self, mode):
        ValueList = {}
        DirectionList = {}
        if mode == 1:
            valmotor1 = int(self.Mnl_Spn_Value1.GetValue())
            valmotor2 = int(self.Mnl_Spn_Value2.GetValue())
            valmotor3 = int(self.Mnl_Spn_Value3.GetValue())
            valmotor4 = int(self.Mnl_Spn_Value4.GetValue())
            valmotor5 = int(self.Mnl_Spn_Value5.GetValue())
            valmotor6 = int(self.Mnl_Spn_Value6.GetValue())

        #if self.Lbl_Mnl_WidgetUsedModeView.GetLabel == "BY SCROLL"
        elif mode == 2:
            if len(self.Txt_Mnl_ValM1.GetValue()) != 0:
                valmotor1 = int(self.Txt_Mnl_ValM1.GetValue())
                ValueList.update({1: valmotor1})
            if len(self.Txt_Mnl_ValM2.GetValue()) != 0:
                valmotor2 = int(self.Txt_Mnl_ValM2.GetValue())
                ValueList.update({2: valmotor2})
            if len(self.Txt_Mnl_ValM3.GetValue()) != 0:
                valmotor3 = int(self.Txt_Mnl_ValM3.GetValue())
                ValueList.update({3: valmotor3})
            if len(self.Txt_Mnl_ValM4.GetValue()) != 0:
                valmotor4 = int(self.Txt_Mnl_ValM4.GetValue())
                ValueList.update({4: valmotor4})
            if len(self.Txt_Mnl_ValM5.GetValue()) != 0:
                valmotor5 = int(self.Txt_Mnl_ValM5.GetValue())
                ValueList.update({5: valmotor5})
            if len(self.Cmb_Mnl_ValM6.GetValue()) != 0:
                valmotor6 = str(self.Cmb_Mnl_ValM6.GetValue())
                if valmotor6 == "ON":
                    valmotor6 = 1
                    ValueList.update({6: valmotor6})
                elif valmotor6 == "OFF":
                    valmotor6 = 0
                    ValueList.update({6: valmotor6})
                else:
                    print "M6 NONE"


            if len(self.Cmb_Mnl_DirM1.GetValue()) != 0 or len(self.Cmb_Mnl_DirM2.GetValue()) <= 1:
                Dir1 = self.Cmb_Mnl_DirM1.GetValue()
                DirectionList.update({1: Dir1})
            if len(self.Cmb_Mnl_DirM2.GetValue()) != 0 or len(self.Cmb_Mnl_DirM2.GetValue()) <= 1:
                Dir2 = self.Cmb_Mnl_DirM2.GetValue()
                DirectionList.update({2: Dir2})
            if len(self.Cmb_Mnl_DirM3.GetValue()) != 0 or len(self.Cmb_Mnl_DirM2.GetValue()) <= 1:
                Dir3 = self.Cmb_Mnl_DirM3.GetValue()
                DirectionList.update({3: Dir3})
            if len(self.Cmb_Mnl_DirM4.GetValue()) != 0 or len(self.Cmb_Mnl_DirM2.GetValue()) <= 1:
                Dir4 = self.Cmb_Mnl_DirM4.GetValue()
                DirectionList.update({4: Dir4})


            #Filtering Value
            ValueList = self.MnlDataFiltering(1, ValueList)


            #Filtering Direction And Changing its Value Cause its A 'CCW' and 'CC' format
            DirectionList = self.MnlDataFiltering(2, DirectionList)
            print DirectionList

            DataFinal = {}
            for id in ValueList:
                DataResult = {}

                if (ValueList[id] in ('',None)) == True:
                    print 'VALUE ADA YANG KOSONG'
                    continue
                if DirectionList.get(id) != None:
                    if str(DirectionList[id]) == '-':
                        print 'DIR BELUM DI INPUT'
                        continue
                DataResult.update({'value':ValueList[id]})
                if self.CNows(4, need=id) != None:
                    DataResult.update({'speed':self.CNows(4, need=id)})
                if DirectionList.get(id) != None:
                    DataResult.update({'direction':DirectionList[id]})
                DataFinal.update({id:DataResult})

            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[ListingData]-GoingTo-CGenerateCommand')
            #STORING RAW DATA TO GLOBAL VAR
            self.DataCommand_Raw = DataFinal
            print DataFinal
            self.MnlEventPasser(1)

        elif mode == 3:
            #1
            valmotor1 = int(self.Mnl_Spn_Value1.GetValue())
            vallast1 = self.CNows(2, need=1)
            if int(vallast1) < valmotor1:
                DirectionList.update({1: 1})
            ValueList.update({1: valmotor1})

            #2
            valmotor2 = int(self.Mnl_Spn_Value2.GetValue())
            vallast2 = self.CNows(2, need=2)
            if int(vallast2) < valmotor2:
                DirectionList.update({2: 1})
            ValueList.update({2: valmotor2})

            #3
            valmotor3 = int(self.Mnl_Spn_Value3.GetValue())
            vallast3 = self.CNows(2, need=3)
            if int(vallast3) < valmotor3:
                DirectionList.update({3: 1})
            ValueList.update({3: valmotor3})

            #4
            valmotor4 = int(self.Mnl_Spn_Value4.GetValue())
            vallast4 = self.CNows(2, need=4)
            if int(vallast4) < valmotor4:
                DirectionList.update({4: 1})
            ValueList.update({4: valmotor4})

            #5
            valmotor5 = int(self.Mnl_Spn_Value5.GetValue())
            ValueList.update({5: valmotor5})


            #6
            valmotor6 = int(self.Mnl_Spn_Value6.GetValue())
            ValueList.update({6: valmotor6})

            DirectionList = self.MnlDataFiltering(2, DirectionList)
            print DirectionList

            DataFinal = {}
            for id in ValueList:
                DataResult = {}

                if (ValueList[id] in ('', None)) == True:
                    print 'VALUE ADA YANG KOSONG'
                    continue

                if DirectionList.get(id) != None:
                    if str(DirectionList[id]) == '-':
                        print 'DIR BELUM DI INPUT'
                        continue

                DataResult.update({'value': ValueList[id]})
                if self.CNows(4, need=id) != None:
                    DataResult.update({'speed': self.CNows(4, need=id)})
                if DirectionList.get(id) != None:
                    DataResult.update({'direction': DirectionList[id]})
                DataFinal.update({id: DataResult})

            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[ListingData]-GoingTo-CGenerateCommand')

            # STORING RAW DATA TO GLOBAL VAR
            self.DataCommand_Raw = DataFinal
            print DataFinal
            #self.MnlEventPasser(1)



    def MnlEventPasser(self,mode):
        if mode == 1:
            self.Event_Type = 'Process'
            self.CEventON()
            self.Cmd_Mnl_GoByClick.Disable()

    def MnlDataFiltering(self, mode, dictarray):
        #Value
        if mode == 1:
            dellist = []
            for data in dictarray:
                if dictarray[data] in ("",None):
                    self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                     message='[Manual Frame]-Value Array-Deleting-' + str(dictarray[data]))
                    dellist.append(data)

                if len(dellist) != 0:
                    for item in dellist:
                        del dictarray[item]

        #Direction
        elif mode == 2:
            dellist = []
            for data in dictarray:
                if dictarray[data] in ("",None,"-") or dictarray[data] not in("CCW","CW"):
                    self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                     message='[Manual Frame]-Direction Array-Deleting-' + str(dictarray[data]))
                    dellist.append(data)

            if len(dellist) != 0:
                for item in dellist:
                    del dictarray[item]

            for data in dictarray:
                if data == 1:
                    if dictarray[data] == "CW":
                        dictarray[data] = 1
                    elif dictarray[data] == "CCW":
                        dictarray[data] = 0
                else:
                    if dictarray[data] == "CCW":
                        dictarray[data] = 1
                    elif dictarray[data] == "CW":
                        dictarray[data] = 0

        return dictarray

    def MnlSetSpeedMotor(self, mode):
        if mode == 1:



            spm1 = (self.Txt_Mnl_SpeedM1.GetValue())
            spm2 = (self.Txt_Mnl_SpeedM2.GetValue())
            spm3 = (self.Txt_Mnl_SpeedM3.GetValue())
            spm4 = (self.Txt_Mnl_SpeedM4.GetValue())
            spm5 = (self.Txt_Mnl_SpeedM5.GetValue())


            if spm1 in ('',None,):
                self.Speed.update({1: 0001})
            else:
                if self.Speed.get(1) is not None:
                    self.Speed[1] = int(spm1)
                else:
                    self.Speed.update({1: int(spm1)})

            if spm2 in ('', None,):
                self.Speed.update({2: 0001})
            else:
                if self.Speed.get(2) is not None:
                    self.Speed[2] = int(spm2)
                else:
                    self.Speed.update({2: int(spm2)})

            if spm3 in ('', None,):
                self.Speed.update({3: 0001})
            else:
                if self.Speed.get(3) is not None:
                    self.Speed[3] = int(spm3)
                else:
                    self.Speed.update({3: int(spm3)})

            if spm4 in ('', None,):
                self.Speed.update({4: 0001})
            else:
                if self.Speed.get(4) is not None:
                    self.Speed[4] = int(spm4)
                else:
                    self.Speed.update({4: int(spm4)})

            if spm5 in ('', None,):
                self.Speed.update({5: 0001})
            else:
                if self.Speed.get(5) is not None:
                    self.Speed[5] = int(spm5)
                else:
                    self.Speed.update({5: int(spm5)})

            print  self.Speed

            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[MnlFrame]-Setting Speed-' + spm1 + '/' + spm2 + '/' + spm3 + '/' + spm4 + '/' + spm5)

    def MnlFrameAct(self, mode):
        #RESET SPEED TO EMPTY
        if mode == 1:
            self.Txt_Mnl_SpeedM1.SetValue("")
            self.Txt_Mnl_SpeedM2.SetValue("")
            self.Txt_Mnl_SpeedM3.SetValue("")
            self.Txt_Mnl_SpeedM4.SetValue("")
            self.Txt_Mnl_SpeedM5.SetValue("")

            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[MnlFrame]-Reset Speed-ToEmpty')
        #
        elif mode == 2:
            #filter listing data by testing mode
            if self.Lbl_Mnl_WidgetUsedModeView.GetLabel() == "BY FORM":
                self.MnlListingData(2)
            elif self.Lbl_Mnl_WidgetUsedModeView.GetLabel() == "BY CLICK":
                self.MnlListingData(3)
                self.DetectingPos = True
            elif self.Lbl_Mnl_WidgetUsedModeView.GetLabel() == "BY SCROLL":
                pass
            else:
                pass

        #Homing Manual
        elif mode == 3:
            self.Event_Type = 'MnlHoming'
            self.CEventON()

        #Zero Button
        elif mode == 4:
            self.CZeroCoordinate(1)
            self.Cmd_Mnl_ZeroByClick.Disable()

    def MnlUpdateUI(self, axis):
        if self.CurrForm == 'Manual':
            if lastaxis != axis:
                if int(axis) == 0:
                    oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                    oevt.SetEventObject(self.Mnl_Spn_Value1)
                    wx.PostEvent(self.Mnl_Spn_Value1, oevt)
                if int(axis) == 1:
                    oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                    oevt.SetEventObject(self.Mnl_Spn_Value2)
                    wx.PostEvent(self.Mnl_Spn_Value2, oevt)
                if int(axis) == 2:
                    oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                    oevt.SetEventObject(self.Mnl_Spn_Value3)
                    wx.PostEvent(self.Mnl_Spn_Value3, oevt)
                if int(axis) == 3:
                    oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                    oevt.SetEventObject(self.Mnl_Spn_Value4)
                    wx.PostEvent(self.Mnl_Spn_Value4, oevt)

            if int(axis) == 0:
                self.Mnl_Spn_Value1.SetValue(int(val))
            if int(axis) == 1:
                self.Mnl_Spn_Value2.SetValue(int(val))
            if int(axis) == 2:
                self.Mnl_Spn_Value3.SetValue(int(val))
            if int(axis) == 3:
                self.Mnl_Spn_Value4.SetValue(int(val))

            lastaxis = axis










