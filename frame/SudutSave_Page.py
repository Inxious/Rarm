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
import time
import copy


###########################################################################
## Class MyFrame1
###########################################################################

class SudutSave(wx.Frame):
    def __init__(self, parent):

        #INIT
        self.SsvFrameData(1)


        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                          size=wx.Size(829, 710), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        fgSizer1 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer1.SetFlexibleDirection(wx.BOTH)
        fgSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer4 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer4.SetFlexibleDirection(wx.BOTH)
        fgSizer4.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Ssv_Pnl_ConfigManager = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        fgSizer2 = wx.FlexGridSizer(3, 1, 0, 0)
        fgSizer2.SetFlexibleDirection(wx.BOTH)
        fgSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Ssv_Pnl_CM_Header = wx.Panel(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                          wx.TAB_TRAVERSAL)
        gSizer1 = wx.GridSizer(1, 2, 0, 0)

        self.Ssv_Jdl_1 = wx.StaticText(self.Ssv_Pnl_CM_Header, wx.ID_ANY, u"Config Manager", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.Ssv_Jdl_1.Wrap(-1)
        self.Ssv_Jdl_1.SetFont(wx.Font(11, 70, 90, 92, False, "Arial"))

        gSizer1.Add(self.Ssv_Jdl_1, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Ssv_Pnl_HeaderID = wx.Panel(self.Ssv_Pnl_CM_Header, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                         wx.TAB_TRAVERSAL)
        gSizer5 = wx.GridSizer(0, 2, 0, 0)

        self.m_staticText26 = wx.StaticText(self.Ssv_Pnl_HeaderID, wx.ID_ANY, u"HeaderID =", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.m_staticText26.Wrap(-1)
        gSizer5.Add(self.m_staticText26, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Ssv_Txt_HeadID = wx.TextCtrl(self.Ssv_Pnl_HeaderID, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size(50, -1), 0)
        gSizer5.Add(self.Ssv_Txt_HeadID, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

        self.Ssv_Pnl_HeaderID.SetSizer(gSizer5)
        self.Ssv_Pnl_HeaderID.Layout()
        gSizer5.Fit(self.Ssv_Pnl_HeaderID)
        gSizer1.Add(self.Ssv_Pnl_HeaderID, 1, wx.EXPAND | wx.ALL, 5)

        self.Ssv_Pnl_CM_Header.SetSizer(gSizer1)
        self.Ssv_Pnl_CM_Header.Layout()
        gSizer1.Fit(self.Ssv_Pnl_CM_Header)
        fgSizer2.Add(self.Ssv_Pnl_CM_Header, 1, wx.EXPAND | wx.ALL, 5)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Ssv_Lbl_M1 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"M1", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Ssv_Lbl_M1.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_M1, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Txt_ValM1 = wx.TextCtrl(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(80, -1), 0)
        gbSizer1.Add(self.Ssv_Txt_ValM1, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_Spd1 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Speed", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.Ssv_Lbl_Spd1.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_Spd1, wx.GBPosition(2, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Txt_SpdM1 = wx.TextCtrl(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(70, -1), 0)
        gbSizer1.Add(self.Ssv_Txt_SpdM1, wx.GBPosition(2, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_DirM1 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Dir", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.Ssv_Lbl_DirM1.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_DirM1, wx.GBPosition(2, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        Ssv_Cmb_DirM1Choices = []
        self.Ssv_Cmb_DirM1 = wx.ComboBox(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"-", wx.DefaultPosition,
                                         wx.Size(70, -1), Ssv_Cmb_DirM1Choices, 0)
        gbSizer1.Add(self.Ssv_Cmb_DirM1, wx.GBPosition(2, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_M2 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"M2", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Ssv_Lbl_M2.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_M2, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Txt_ValM2 = wx.TextCtrl(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(80, -1), 0)
        gbSizer1.Add(self.Ssv_Txt_ValM2, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_Spd2 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Speed", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.Ssv_Lbl_Spd2.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_Spd2, wx.GBPosition(3, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Txt_SpdM2 = wx.TextCtrl(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(70, -1), 0)
        gbSizer1.Add(self.Ssv_Txt_SpdM2, wx.GBPosition(3, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_DirM2 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Dir", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.Ssv_Lbl_DirM2.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_DirM2, wx.GBPosition(3, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        Ssv_Cmb_DirM2Choices = []
        self.Ssv_Cmb_DirM2 = wx.ComboBox(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"-", wx.DefaultPosition,
                                         wx.Size(70, -1), Ssv_Cmb_DirM2Choices, 0)
        gbSizer1.Add(self.Ssv_Cmb_DirM2, wx.GBPosition(3, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_M3 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"M3", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Ssv_Lbl_M3.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_M3, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Txt_ValM3 = wx.TextCtrl(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(80, -1), 0)
        gbSizer1.Add(self.Ssv_Txt_ValM3, wx.GBPosition(4, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_Spd3 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Speed", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.Ssv_Lbl_Spd3.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_Spd3, wx.GBPosition(4, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Txt_SpdM3 = wx.TextCtrl(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(70, -1), 0)
        gbSizer1.Add(self.Ssv_Txt_SpdM3, wx.GBPosition(4, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_DirM3 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Dir", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.Ssv_Lbl_DirM3.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_DirM3, wx.GBPosition(4, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        Ssv_Cmb_DirM3Choices = []
        self.Ssv_Cmb_DirM3 = wx.ComboBox(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"-", wx.DefaultPosition,
                                         wx.Size(70, -1), Ssv_Cmb_DirM3Choices, 0)
        gbSizer1.Add(self.Ssv_Cmb_DirM3, wx.GBPosition(4, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_M4 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"M4", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Ssv_Lbl_M4.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_M4, wx.GBPosition(5, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Txt_ValM4 = wx.TextCtrl(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(80, -1), 0)
        gbSizer1.Add(self.Ssv_Txt_ValM4, wx.GBPosition(5, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_Spd4 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Speed", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.Ssv_Lbl_Spd4.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_Spd4, wx.GBPosition(5, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Txt_SpdM4 = wx.TextCtrl(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(70, -1), 0)
        gbSizer1.Add(self.Ssv_Txt_SpdM4, wx.GBPosition(5, 3), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_DirM4 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Dir", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.Ssv_Lbl_DirM4.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_DirM4, wx.GBPosition(5, 4), wx.GBSpan(1, 1), wx.ALL, 5)

        Ssv_Cmb_DirM4Choices = []
        self.Ssv_Cmb_DirM4 = wx.ComboBox(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"-", wx.DefaultPosition,
                                         wx.Size(70, -1), Ssv_Cmb_DirM4Choices, 0)
        gbSizer1.Add(self.Ssv_Cmb_DirM4, wx.GBPosition(5, 5), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_M5 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"M5", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Ssv_Lbl_M5.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_M5, wx.GBPosition(6, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Txt_ValM5 = wx.TextCtrl(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                         wx.Size(80, -1), 0)
        gbSizer1.Add(self.Ssv_Txt_ValM5, wx.GBPosition(6, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_IncreM5 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Increment", wx.DefaultPosition,
                                             wx.DefaultSize, 0)
        self.Ssv_Lbl_IncreM5.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_IncreM5, wx.GBPosition(6, 2), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Txt_IncreM5 = wx.TextCtrl(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                           wx.Size(80, -1), 0)
        gbSizer1.Add(self.Ssv_Txt_IncreM5, wx.GBPosition(6, 3), wx.GBSpan(1, 3), wx.ALL, 5)

        self.Ssv_Lbl_M6 = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"M6", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Ssv_Lbl_M6.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_M6, wx.GBPosition(7, 0), wx.GBSpan(1, 1), wx.ALL, 5)

        Ssv_Cmb_ValM6Choices = [u"ON", u"OFF"]
        self.Ssv_Cmb_ValM6 = wx.ComboBox(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"-", wx.DefaultPosition,
                                         wx.DefaultSize, Ssv_Cmb_ValM6Choices, 0)
        gbSizer1.Add(self.Ssv_Cmb_ValM6, wx.GBPosition(7, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_MagnetStat = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Magnet", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.Ssv_Lbl_MagnetStat.Wrap(-1)
        self.Ssv_Lbl_MagnetStat.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))

        gbSizer1.Add(self.Ssv_Lbl_MagnetStat, wx.GBPosition(8, 0), wx.GBSpan(1, 1), wx.ALL | wx.ALIGN_CENTER_VERTICAL,
                     5)

        Cmb_MagnetStatChoices = [u"ON", u"OFF"]
        self.Ssv_Cmb_MagnetStat = wx.ComboBox(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"-", wx.DefaultPosition,
                                          wx.DefaultSize, Cmb_MagnetStatChoices, 0)
        gbSizer1.Add(self.Ssv_Cmb_MagnetStat, wx.GBPosition(8, 1), wx.GBSpan(1, 1), wx.ALL, 5)

        self.Ssv_Lbl_MovingTime = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Moving Time(second)",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        self.Ssv_Lbl_MovingTime.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_MovingTime, wx.GBPosition(0, 0), wx.GBSpan(1, 2),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Ssv_Lbl_Discription = wx.StaticText(self.Ssv_Pnl_ConfigManager, wx.ID_ANY,
                                                 u"**Input Coordinate Based from Zero Coordinate", wx.DefaultPosition,
                                                 wx.DefaultSize, 0)
        self.Ssv_Lbl_Discription.Wrap(-1)
        gbSizer1.Add(self.Ssv_Lbl_Discription, wx.GBPosition(1, 0), wx.GBSpan(1, 4),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Ssv_Cmd_ZeroSeeDetails = wx.Button(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"See Details",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.Ssv_Cmd_ZeroSeeDetails, wx.GBPosition(1, 4), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.Ssv_Txt_MovingTime = wx.TextCtrl(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                              wx.Size(100, -1), 0)
        gbSizer1.Add(self.Ssv_Txt_MovingTime, wx.GBPosition(0, 2), wx.GBSpan(1, 2),
                     wx.ALIGN_CENTER_VERTICAL | wx.ALL | wx.EXPAND, 5)

        self.Ssv_Cmd_CalculateSpeed = wx.Button(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Calculate Speed",
                                                wx.DefaultPosition, wx.DefaultSize, 0)
        gbSizer1.Add(self.Ssv_Cmd_CalculateSpeed, wx.GBPosition(0, 4), wx.GBSpan(1, 2),
                     wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer2.Add(gbSizer1, 1, wx.EXPAND, 5)

        gSizer2 = wx.GridSizer(1, 3, 0, 0)

        self.Ssv_Cmd_AppendInput = wx.Button(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Append Config",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        gSizer2.Add(self.Ssv_Cmd_AppendInput, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Ssv_Cmd_AppendHome = wx.Button(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Append Home", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        gSizer2.Add(self.Ssv_Cmd_AppendHome, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Ssv_Cmd_ClearInput = wx.Button(self.Ssv_Pnl_ConfigManager, wx.ID_ANY, u"Clear Config", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        gSizer2.Add(self.Ssv_Cmd_ClearInput, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer2.Add(gSizer2, 1, wx.EXPAND, 5)

        self.Ssv_Pnl_ConfigManager.SetSizer(fgSizer2)
        self.Ssv_Pnl_ConfigManager.Layout()
        fgSizer2.Fit(self.Ssv_Pnl_ConfigManager)
        fgSizer4.Add(self.Ssv_Pnl_ConfigManager, 1, wx.EXPAND | wx.ALL, 0)

        self.Ssv_Pnl_Config = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1), wx.TAB_TRAVERSAL)
        self.Ssv_Pnl_Config.SetBackgroundColour(wx.Colour(208, 208, 208))

        fgSizer11 = wx.FlexGridSizer(1, 2, 0, 0)
        fgSizer11.SetFlexibleDirection(wx.BOTH)
        fgSizer11.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer3 = wx.FlexGridSizer(5, 1, 0, 0)
        fgSizer3.SetFlexibleDirection(wx.BOTH)
        fgSizer3.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        fgSizer3.SetMinSize(wx.Size(420, -1))
        self.Ssv_Pnl_Jdl_2 = wx.Panel(self.Ssv_Pnl_Config, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                      wx.TAB_TRAVERSAL)
        self.Ssv_Pnl_Jdl_2.SetBackgroundColour(wx.Colour(51, 153, 255))

        gSizer51 = wx.GridSizer(1, 1, 0, 0)

        gSizer51.SetMinSize(wx.Size(400, -1))
        self.Ssv_Jdl_2 = wx.StaticText(self.Ssv_Pnl_Jdl_2, wx.ID_ANY, u"Config Header Set", wx.DefaultPosition,
                                       wx.Size(-1, -1), 0)
        self.Ssv_Jdl_2.Wrap(-1)
        self.Ssv_Jdl_2.SetFont(wx.Font(11, 70, 90, 92, False, "Arial"))

        gSizer51.Add(self.Ssv_Jdl_2, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Ssv_Pnl_Jdl_2.SetSizer(gSizer51)
        self.Ssv_Pnl_Jdl_2.Layout()
        gSizer51.Fit(self.Ssv_Pnl_Jdl_2)
        fgSizer3.Add(self.Ssv_Pnl_Jdl_2, 1, wx.EXPAND | wx.ALL, 5)

        self.Ssv_Pnl_OptionHeaderButton = wx.Panel(self.Ssv_Pnl_Config, wx.ID_ANY, wx.DefaultPosition, wx.Size(-1, -1),
                                                   wx.TAB_TRAVERSAL)
        self.Ssv_Pnl_OptionHeaderButton.SetBackgroundColour(wx.Colour(144, 144, 144))

        gSizer3 = wx.GridSizer(1, 3, 0, 0)

        gSizer3.SetMinSize(wx.Size(400, -1))
        self.Ssv_Cmd_NewConfig = wx.Button(self.Ssv_Pnl_OptionHeaderButton, wx.ID_ANY, u"New", wx.DefaultPosition,
                                           wx.Size(-1, -1), 0)
        self.Ssv_Cmd_NewConfig.SetFont(wx.Font(12, 74, 90, 92, False, "Arial"))
        self.Ssv_Cmd_NewConfig.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))
        self.Ssv_Cmd_NewConfig.SetBackgroundColour(wx.Colour(51, 153, 255))

        gSizer3.Add(self.Ssv_Cmd_NewConfig, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Ssv_Cmd_LoadConfig = wx.Button(self.Ssv_Pnl_OptionHeaderButton, wx.ID_ANY, u"Edit", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.Ssv_Cmd_LoadConfig.SetFont(wx.Font(12, 74, 90, 92, False, "Arial"))
        self.Ssv_Cmd_LoadConfig.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))
        self.Ssv_Cmd_LoadConfig.SetBackgroundColour(wx.Colour(51, 153, 255))

        gSizer3.Add(self.Ssv_Cmd_LoadConfig, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Ssv_Cmd_DeleteConfig = wx.Button(self.Ssv_Pnl_OptionHeaderButton, wx.ID_ANY, u"Delete", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        self.Ssv_Cmd_DeleteConfig.SetFont(wx.Font(12, 74, 90, 92, False, "Arial"))
        self.Ssv_Cmd_DeleteConfig.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_HIGHLIGHTTEXT))
        self.Ssv_Cmd_DeleteConfig.SetBackgroundColour(wx.Colour(51, 153, 255))

        gSizer3.Add(self.Ssv_Cmd_DeleteConfig, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Ssv_Pnl_OptionHeaderButton.SetSizer(gSizer3)
        self.Ssv_Pnl_OptionHeaderButton.Layout()
        gSizer3.Fit(self.Ssv_Pnl_OptionHeaderButton)
        fgSizer3.Add(self.Ssv_Pnl_OptionHeaderButton, 1, wx.EXPAND | wx.ALL, 5)

        self.Ssv_Pnl_HeaderSetPanel = wx.Panel(self.Ssv_Pnl_Config, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize,
                                               wx.TAB_TRAVERSAL)
        self.Ssv_Pnl_HeaderSetPanel.SetBackgroundColour(wx.Colour(255, 255, 255))

        fgSizer12 = wx.FlexGridSizer(5, 1, 0, 0)
        fgSizer12.SetFlexibleDirection(wx.BOTH)
        fgSizer12.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Ssv_Lbl_Jdl_SettingConfig = wx.StaticText(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"",
                                                       wx.DefaultPosition, wx.DefaultSize, 0)
        self.Ssv_Lbl_Jdl_SettingConfig.Wrap(-1)
        self.Ssv_Lbl_Jdl_SettingConfig.SetFont(wx.Font(9, 74, 90, 92, False, "Arial"))

        fgSizer12.Add(self.Ssv_Lbl_Jdl_SettingConfig, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        fgSizer7 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer7.SetFlexibleDirection(wx.BOTH)
        fgSizer7.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Ssv_Jdl_Save = wx.StaticText(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"Save / Save As To DB",
                                          wx.DefaultPosition, wx.Size(270, -1), 0)
        self.Ssv_Jdl_Save.Wrap(-1)
        fgSizer7.Add(self.Ssv_Jdl_Save, 0, wx.ALL, 5)

        bSizer1 = wx.BoxSizer(wx.HORIZONTAL)

        self.Ssv_Lbl_SaveName = wx.StaticText(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"Name", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.Ssv_Lbl_SaveName.Wrap(-1)
        bSizer1.Add(self.Ssv_Lbl_SaveName, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Ssv_Txt_SaveName = wx.TextCtrl(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.Ssv_Txt_SaveName.SetMinSize(wx.Size(250, -1))
        self.Ssv_Txt_SaveName.SetMaxSize(wx.Size(250, -1))

        bSizer1.Add(self.Ssv_Txt_SaveName, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Ssv_Cmd_Save = wx.Button(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"Save", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        bSizer1.Add(self.Ssv_Cmd_Save, 0, wx.ALL, 5)

        fgSizer7.Add(bSizer1, 1, wx.EXPAND, 5)

        fgSizer12.Add(fgSizer7, 1, wx.EXPAND, 5)

        fgSizer71 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer71.SetFlexibleDirection(wx.BOTH)
        fgSizer71.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer7 = wx.BoxSizer(wx.HORIZONTAL)

        self.Ssv_Jdl_Load = wx.StaticText(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"Load From DB", wx.DefaultPosition,
                                          wx.DefaultSize, 0)
        self.Ssv_Jdl_Load.Wrap(-1)
        bSizer7.Add(self.Ssv_Jdl_Load, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Ssv_Cmd_RefreshLoad = wx.Button(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"Refresh List",
                                             wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer7.Add(self.Ssv_Cmd_RefreshLoad, 0, wx.ALL, 5)

        fgSizer71.Add(bSizer7, 1, wx.EXPAND, 5)

        bSizer11 = wx.BoxSizer(wx.HORIZONTAL)

        self.Ssv_Lbl_LoadName = wx.StaticText(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"Name", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.Ssv_Lbl_LoadName.Wrap(-1)
        bSizer11.Add(self.Ssv_Lbl_LoadName, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        Ssv_Cmb_LoadNameChoices = []
        self.Ssv_Cmb_LoadName = wx.ComboBox(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"- choose config to load -", wx.DefaultPosition,
                                            wx.DefaultSize, Ssv_Cmb_LoadNameChoices, 0)
        self.Ssv_Cmb_LoadName.SetMinSize(wx.Size(250, -1))
        self.Ssv_Cmb_LoadName.SetMaxSize(wx.Size(250, -1))

        bSizer11.Add(self.Ssv_Cmb_LoadName, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Ssv_Cmd_Load = wx.Button(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"Load", wx.DefaultPosition,
                                      wx.DefaultSize, 0)
        bSizer11.Add(self.Ssv_Cmd_Load, 0, wx.ALL, 5)

        fgSizer71.Add(bSizer11, 1, wx.EXPAND, 5)

        fgSizer12.Add(fgSizer71, 1, wx.EXPAND, 5)

        fgSizer711 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer711.SetFlexibleDirection(wx.BOTH)
        fgSizer711.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer71 = wx.BoxSizer(wx.HORIZONTAL)

        self.Ssv_Jdl_Update = wx.StaticText(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"Update To DB", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.Ssv_Jdl_Update.Wrap(-1)
        bSizer71.Add(self.Ssv_Jdl_Update, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Ssv_Txt_IDUpdate = wx.TextCtrl(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, wx.TE_READONLY)
        self.Ssv_Txt_IDUpdate.SetMinSize(wx.Size(250, -1))

        bSizer71.Add(self.Ssv_Txt_IDUpdate, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer711.Add(bSizer71, 1, wx.EXPAND, 5)

        bSizer111 = wx.BoxSizer(wx.HORIZONTAL)

        self.Ssv_Lbl_UpdateName = wx.StaticText(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"Name", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.Ssv_Lbl_UpdateName.Wrap(-1)
        bSizer111.Add(self.Ssv_Lbl_UpdateName, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Ssv_Txt_UpdateName = wx.TextCtrl(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, wx.EmptyString,
                                              wx.DefaultPosition, wx.DefaultSize, 0)
        self.Ssv_Txt_UpdateName.SetMinSize(wx.Size(250, -1))
        self.Ssv_Txt_UpdateName.SetMaxSize(wx.Size(250, -1))

        bSizer111.Add(self.Ssv_Txt_UpdateName, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Ssv_Cmd_Update = wx.Button(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"Update", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer111.Add(self.Ssv_Cmd_Update, 0, wx.ALL, 5)

        fgSizer711.Add(bSizer111, 1, wx.EXPAND, 5)

        fgSizer12.Add(fgSizer711, 1, wx.EXPAND, 5)

        fgSizer121 = wx.FlexGridSizer(2, 1, 0, 0)
        fgSizer121.SetFlexibleDirection(wx.BOTH)
        fgSizer121.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

        self.Ssv_Lbl_DeleteSelectItem = wx.StaticText(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"Delete Config",
                                                      wx.DefaultPosition, wx.DefaultSize, 0)
        self.Ssv_Lbl_DeleteSelectItem.Wrap(-1)
        bSizer6.Add(self.Ssv_Lbl_DeleteSelectItem, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer121.Add(bSizer6, 1, wx.EXPAND, 5)

        bSizer72 = wx.BoxSizer(wx.HORIZONTAL)

        self.Ssv_Lbl_NameDelete = wx.StaticText(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"Name", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.Ssv_Lbl_NameDelete.Wrap(-1)
        bSizer72.Add(self.Ssv_Lbl_NameDelete, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        Ssv_Cmb_DeleteListChoices = []
        self.Ssv_Cmb_DeleteList = wx.ComboBox(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"- choose config to delete -",
                                              wx.DefaultPosition, wx.DefaultSize, Ssv_Cmb_DeleteListChoices, 0)
        self.Ssv_Cmb_DeleteList.SetMinSize(wx.Size(250, -1))

        bSizer72.Add(self.Ssv_Cmb_DeleteList, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Ssv_Cmd_Delete = wx.Button(self.Ssv_Pnl_HeaderSetPanel, wx.ID_ANY, u"Delete", wx.DefaultPosition,
                                        wx.DefaultSize, 0)
        bSizer72.Add(self.Ssv_Cmd_Delete, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer121.Add(bSizer72, 1, wx.EXPAND, 5)

        fgSizer12.Add(fgSizer121, 1, wx.EXPAND, 5)

        self.Ssv_Pnl_HeaderSetPanel.SetSizer(fgSizer12)
        self.Ssv_Pnl_HeaderSetPanel.Layout()
        fgSizer12.Fit(self.Ssv_Pnl_HeaderSetPanel)
        fgSizer3.Add(self.Ssv_Pnl_HeaderSetPanel, 1,
                     wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer11.Add(fgSizer3, 1, wx.EXPAND, 5)

        self.Ssv_Pnl_Config.SetSizer(fgSizer11)
        self.Ssv_Pnl_Config.Layout()
        fgSizer11.Fit(self.Ssv_Pnl_Config)
        fgSizer4.Add(self.Ssv_Pnl_Config, 1, wx.EXPAND | wx.ALL, 5)

        fgSizer1.Add(fgSizer4, 1, wx.EXPAND, 5)

        fgSizer5 = wx.FlexGridSizer(3, 1, 0, 0)
        fgSizer5.SetFlexibleDirection(wx.BOTH)
        fgSizer5.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Ssv_Jdl_3 = wx.StaticText(self, wx.ID_ANY, u"Config Detail Content Data", wx.DefaultPosition,
                                       wx.DefaultSize, 0)
        self.Ssv_Jdl_3.Wrap(-1)
        self.Ssv_Jdl_3.SetFont(wx.Font(11, 74, 90, 92, False, "Arial"))

        fgSizer5.Add(self.Ssv_Jdl_3, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Ssv_Dv_ConfigDetail = wx.dataview.DataViewListCtrl(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(650, 150),
                                                                0)
        self.Ssv_Dv_ConfigDetail.SetMinSize(wx.Size(800, 200))

        fgSizer5.Add(self.Ssv_Dv_ConfigDetail, 0,
                     wx.ALL | wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 5)

        fgSizer6 = wx.FlexGridSizer(1, 3, 0, 0)
        fgSizer6.SetFlexibleDirection(wx.BOTH)
        fgSizer6.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Ssv_Cmd_ClearDetail = wx.Button(self, wx.ID_ANY, u"Clear Content", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.Ssv_Cmd_ClearDetail, 0, wx.ALL, 5)

        self.Ssv_Cmd_EditDetail = wx.Button(self, wx.ID_ANY, u"Edit Content", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.Ssv_Cmd_EditDetail, 0, wx.ALL, 5)

        self.Ssv_Cmd_DeleteDetail = wx.Button(self, wx.ID_ANY, u"Delete Content", wx.DefaultPosition, wx.DefaultSize, 0)
        fgSizer6.Add(self.Ssv_Cmd_DeleteDetail, 0, wx.ALL, 5)

        fgSizer5.Add(fgSizer6, 1, wx.EXPAND, 5)

        fgSizer1.Add(fgSizer5, 1, wx.EXPAND, 5)

        self.SetSizer(fgSizer1)
        self.Layout()

        self.Centre(wx.BOTH)
        self.Show()

        #FUNC
        self.SsvStarter()

        # Connect Events
        self.Ssv_Cmd_AppendInput.Bind(wx.EVT_BUTTON, lambda x:self.SsvAppendInput())
        self.Ssv_Cmd_AppendHome.Bind(wx.EVT_BUTTON, lambda x:self.SsvAppendHome())
        self.Ssv_Cmd_ClearInput.Bind(wx.EVT_BUTTON, lambda x:self.SsvClearInput())
        self.Ssv_Cmd_Save.Bind(wx.EVT_BUTTON, lambda x:self.SsvSaveCHeader())
        self.Ssv_Cmd_RefreshLoad.Bind(wx.EVT_BUTTON, lambda x:self.SsvRefreshLoad())
        self.Ssv_Cmd_Load.Bind(wx.EVT_BUTTON, lambda x:self.SsvLoadCHeader())
        self.Ssv_Cmd_Update.Bind(wx.EVT_BUTTON, lambda x:self.SsvUpdateCHeader())
        self.Ssv_Cmd_NewConfig.Bind(wx.EVT_BUTTON, lambda x:self.SsvMAIN_NewCHeader())
        self.Ssv_Cmd_LoadConfig.Bind(wx.EVT_BUTTON, lambda x:self.SsvMAIN_LoadCHeader())
        self.Ssv_Cmd_DeleteConfig.Bind(wx.EVT_BUTTON, lambda x: self.SsvMAIN_DeleteCHeader())
        self.Ssv_Cmd_ClearDetail.Bind(wx.EVT_BUTTON, lambda x:self.SsvClearCDetail())
        self.Ssv_Cmd_EditDetail.Bind(wx.EVT_BUTTON, lambda x:self.SsvEditCDetail())
        self.Ssv_Cmd_DeleteDetail.Bind(wx.EVT_BUTTON, lambda x:self.SsvDelCDetail())
        self.Ssv_Cmd_Delete.Bind(wx.EVT_BUTTON, lambda x: self.SsvDeleteCHeader())
        self.Ssv_Cmd_CalculateSpeed.Bind(wx.EVT_BUTTON, lambda x: self.SsvGetAutoSpeed(1,microstep=16,
                                                                                       waktu=self.Ssv_Txt_MovingTime.GetValue()))
        self.Ssv_Cmb_DeleteList.Bind(wx.EVT_TEXT, lambda x:self.SsvSuggestWord(2,self.Ssv_Cmb_DeleteList.GetValue()))


    def SsvPnlDelete(self, parent):
        self.Ssv_Pnl_Delete = wx.Panel(parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL)
        self.Ssv_Pnl_Delete.SetBackgroundColour(wx.Colour(255, 255, 255))

        fgSizer1232 = wx.FlexGridSizer(3, 1, 0, 0)
        fgSizer1232.SetFlexibleDirection(wx.BOTH)
        fgSizer1232.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.Ssv_Jdl_Delete = wx.StaticText(self.Ssv_Pnl_Delete, wx.ID_ANY, u"List Sudut Header", wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        self.Ssv_Jdl_Delete.Wrap(-1)
        fgSizer1232.Add(self.Ssv_Jdl_Delete, 0, wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Ssv_Dv_DeleteList = wx.dataview.DataViewListCtrl(self.Ssv_Pnl_Delete, wx.ID_ANY, wx.DefaultPosition,
                                                              wx.Size(200, 150), 0)
        fgSizer1232.Add(self.Ssv_Dv_DeleteList, 0, wx.ALL, 5)

        bSizer1232 = wx.BoxSizer(wx.HORIZONTAL)

        self.Ssv_Lbl_HeaderID = wx.StaticText(self.Ssv_Pnl_Delete, wx.ID_ANY, u"Header ID", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.Ssv_Lbl_HeaderID.Wrap(-1)
        bSizer1232.Add(self.Ssv_Lbl_HeaderID, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        self.Ssv_Txt_HeaderID = wx.TextCtrl(self.Ssv_Pnl_Delete, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                            wx.DefaultSize, 0)
        bSizer1232.Add(self.Ssv_Txt_HeaderID, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 5)

        fgSizer1232.Add(bSizer1232, 1, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL, 5)

        self.Ssv_Pnl_Delete.SetSizer(fgSizer1232)
        self.Ssv_Pnl_Delete.Layout()
        fgSizer1232.Fit(self.Ssv_Pnl_Delete)

    def SsvSuggestWord(self, mode, word):
        if mode == 1:
            pass

        #DELETE COMBO
        elif mode == 2:

            try:
                lastword = self.Ssv_LastWord
            except Exception as e:
                lastword = ''
            else:
                if word == lastword:
                    return

            sequence = {}
            sequence1 = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
            sequence2 = {10:'a',11:'b',12:'c',13:'d',14:'e',15:'f',16:'g',
                        17: 'h',18:'i',19:'j',20:'k',21:'l',22:'m',23:'n',
                        24: 'o',25:'p',26:'q',27:'r',28:'s',29:'t',30:'u',
                        31: 'v',32:'w',33:'x',34:'y',35:'z','ex':'ex'}
            sequence.update(sequence1)
            sequence.update(sequence2)
            sequence = {v: k for k, v in sequence.iteritems()}


            data = self.Ssv_ConfigData
            if len(data) == 0:
                return
            else:
                container = []
                for string in data:
                    listswat = list(str(string))
                    correct = len(list(str(word)))
                    corrcount = 0
                    for wut in list(str(word)):
                        if wut.lower() in listswat:
                            corrcount += 1
                        elif wut.upper() in listswat:
                            corrcount += 1

                    if corrcount == correct:

                        #WORD
                        wordnum = list(str(word))
                        for stritem in word:
                            try:
                                num = sequence[stritem.lower()]
                            except Exception as e:
                                wordnum[wordnum.index(stritem)] = 'ex'
                            else:
                                wordnum[wordnum.index(stritem)] = num

                        #STRING
                        strarr = list(str(string))
                        for stritem in strarr:
                            try:
                                num = sequence[stritem.lower()]
                            except Exception as e:
                                strarr[strarr.index(stritem)] = 'ex'
                            else:
                                strarr[strarr.index(stritem)] = num

                        #VALIDATOR
                        if len(wordnum) == 0:
                            return ([])
                        else:
                            passed = True
                            for i in range(len(wordnum)):
                                if wordnum[i] not in strarr:
                                    passed = False

                            if passed == True:
                                container.append([strarr[0],string])

                #ORDERER
                orderarray = []
                for item in container:
                    orderarray.append([item[0],item[1]])

                sortedarray = sorted(orderarray)
                print sortedarray
                print orderarray
                print orderarray.sort()
                hasil = [x[1] for x in sortedarray]

                longs = len(self.Ssv_Cmb_DeleteList.GetItems())
                while longs != 0:
                    try:
                        self.Ssv_Cmb_DeleteList.GetItems()[longs-1]
                    except Exception as e:
                        print e
                    else:
                        self.Ssv_Cmb_DeleteList.Delete(longs-1)
                    longs = len(self.Ssv_Cmb_DeleteList.GetItems())
                self.Ssv_LastWord = word
                self.Ssv_Cmb_DeleteList.AppendItems(hasil)

                #===============================================================================
                #lastitem = []
                #for item in sortedarray:
                #    if item == 'None':
                #        lastitem.append(sortedarray.index(item))
                #        sortedarray[sortedarray.index(item)] = 'GONE'
                #    elif item == 'GONE':
                #        pass

                #    keyitem = item
                #    keyindex = sortedarray.index(item)
                #    sortedarray[keyindex] = 'GONE'

                #ToDo = !!!
                #LOOP AGAIN UNTIL DONE
                #THEN FILTER IT 1 BY ONE [IF SAME ... LOOK ARRAY AFTER THEN COMPARE AGAIN)
                #================================================================================



    def SsvStarter(self):
        #Save
        self.Ssv_Jdl_Save.Hide()
        self.Ssv_Lbl_SaveName.Hide()
        self.Ssv_Txt_SaveName.Hide()
        self.Ssv_Cmd_Save.Hide()

        #Load
        self.Ssv_Jdl_Load.Hide()
        self.Ssv_Lbl_LoadName.Hide()
        self.Ssv_Cmb_LoadName.Hide()
        self.Ssv_Cmd_RefreshLoad.Hide()
        self.Ssv_Cmd_Load.Hide()

        #Update
        self.Ssv_Jdl_Update.Hide()
        self.Ssv_Txt_UpdateName.Hide()
        self.Ssv_Cmd_Update.Hide()
        self.Ssv_Txt_IDUpdate.Hide()
        self.Ssv_Lbl_UpdateName.Hide()

        #Delete
        self.Ssv_Lbl_DeleteSelectItem.Hide()
        self.Ssv_Lbl_NameDelete.Hide()
        self.Ssv_Cmb_DeleteList.Hide()
        self.Ssv_Cmd_Delete.Hide()

        #APPEND DATAVIEW
        self.Ssv_Dv_ConfigDetail.DeleteAllItems()
        self.Ssv_Dv_ConfigDetail.AppendTextColumn('List')
        self.Ssv_Dv_ConfigDetail.AppendTextColumn('MotorID')
        self.Ssv_Dv_ConfigDetail.AppendTextColumn('Value')
        self.Ssv_Dv_ConfigDetail.AppendTextColumn('Speed')
        self.Ssv_Dv_ConfigDetail.AppendTextColumn('Direction')

    def SsvStartDelete(self):
        #self.Ssv_Pnl_Delete.Show()
        self.Ssv_Mode = 'DELETE'

        # Save
        self.Ssv_Jdl_Save.Hide()
        self.Ssv_Lbl_SaveName.Hide()
        self.Ssv_Txt_SaveName.Hide()
        self.Ssv_Cmd_Save.Hide()

        # Load
        self.Ssv_Jdl_Load.Hide()
        self.Ssv_Lbl_LoadName.Hide()
        self.Ssv_Cmb_LoadName.Hide()
        self.Ssv_Cmd_RefreshLoad.Hide()
        self.Ssv_Cmd_Load.Hide()

        # Update
        self.Ssv_Jdl_Update.Hide()
        self.Ssv_Txt_UpdateName.Hide()
        self.Ssv_Cmd_Update.Hide()
        self.Ssv_Txt_IDUpdate.Hide()
        self.Ssv_Lbl_UpdateName.Hide()

        # Delete
        self.Ssv_Lbl_DeleteSelectItem.Show()
        self.Ssv_Lbl_NameDelete.Show()
        self.Ssv_Cmb_DeleteList.Show()
        self.Ssv_Cmd_Delete.Show()

        # self.Ssv_Cmd_Back.Show()
        self.SsvClearInput()
        self.Ssv_Dv_ConfigDetail.DeleteAllItems()
        self.Ssv_Txt_SaveName.SetValue('')
        self.Ssv_Txt_HeadID.SetValue('')
        data = self.Ssv_ConfigData
        for items in data:
            self.Ssv_Cmb_DeleteList.AppendItems(items)

    def SsvStartNew(self):
        #self.Ssv_Pnl_Delete.Hide()
        self.Ssv_Mode = 'NEW'

        # Save
        self.Ssv_Jdl_Save.Show()
        self.Ssv_Lbl_SaveName.Show()
        self.Ssv_Txt_SaveName.Show()
        self.Ssv_Cmd_Save.Show()
        self.Ssv_Cmd_Save.SetLabel('Save')

        # Load
        self.Ssv_Jdl_Load.Show()
        self.Ssv_Lbl_LoadName.Show()
        self.Ssv_Cmb_LoadName.Show()
        self.Ssv_Cmd_RefreshLoad.Show()
        self.Ssv_Cmd_Load.Show()

        # Update
        self.Ssv_Jdl_Update.Hide()
        self.Ssv_Txt_UpdateName.Hide()
        self.Ssv_Cmd_Update.Hide()
        self.Ssv_Txt_IDUpdate.Hide()
        self.Ssv_Lbl_UpdateName.Hide()

        # Delete
        self.Ssv_Lbl_DeleteSelectItem.Hide()
        self.Ssv_Lbl_NameDelete.Hide()
        self.Ssv_Cmb_DeleteList.Hide()
        self.Ssv_Cmd_Delete.Hide()

        #self.Ssv_Cmd_Back.Show()
        self.SsvClearInput()
        self.Ssv_Dv_ConfigDetail.DeleteAllItems()
        self.Ssv_Txt_SaveName.SetValue('')

    def SsvStartLoad(self):
        #self.Ssv_Pnl_Delete.Hide()
        self.Ssv_Txt_SaveName.SetValue('')
        self.Ssv_Mode = 'EDIT'


        # Save
        self.Ssv_Jdl_Save.Hide()
        self.Ssv_Lbl_SaveName.Hide()
        self.Ssv_Txt_SaveName.Hide()
        self.Ssv_Cmd_Save.Hide()

        # Load
        self.Ssv_Jdl_Load.Show()
        self.Ssv_Lbl_LoadName.Show()
        self.Ssv_Cmb_LoadName.Show()
        self.Ssv_Cmd_RefreshLoad.Show()
        self.Ssv_Cmd_Load.Show()

        # Update
        self.Ssv_Jdl_Update.Show()
        self.Ssv_Txt_UpdateName.Show()
        self.Ssv_Cmd_Update.Show()
        self.Ssv_Txt_IDUpdate.Show()
        self.Ssv_Lbl_UpdateName.Show()

        # Delete
        self.Ssv_Lbl_DeleteSelectItem.Hide()
        self.Ssv_Lbl_NameDelete.Hide()
        self.Ssv_Cmb_DeleteList.Hide()
        self.Ssv_Cmd_Delete.Hide()

        #Clear
        self.Ssv_Txt_HeadID.SetValue('')
        self.SsvClearInput()
        self.Ssv_Dv_ConfigDetail.DeleteAllItems()

        #self.Ssv_Cmd_Back.Show()

    def SsvHide(self):
        self.Ssv_Jdl_Save.Hide()
        self.Ssv_Lbl_SaveName.Hide()
        self.Ssv_Txt_SaveName.Hide()
        self.Ssv_Cmd_Save.Hide()

        # Load
        self.Ssv_Jdl_Load.Hide()
        self.Ssv_Lbl_LoadName.Hide()
        self.Ssv_Cmb_LoadName.Hide()
        self.Ssv_Cmd_RefreshLoad.Hide()
        self.Ssv_Cmd_Load.Hide()

        # Update
        self.Ssv_Jdl_Update.Hide()
        self.Ssv_Txt_UpdateName.Hide()
        self.Ssv_Cmd_Update.Hide()
        self.Ssv_Txt_IDUpdate.Hide()
        self.Ssv_Lbl_UpdateName.Hide()

        # Delete
        self.Ssv_Lbl_DeleteSelectItem.Hide()
        self.Ssv_Lbl_NameDelete.Hide()
        self.Ssv_Cmb_DeleteList.Hide()
        self.Ssv_Cmd_Delete.Hide()

        self.Ssv_Cmd_NewConfig.Show()
        self.Ssv_Cmd_LoadConfig.Show()
        #self.Ssv_Cmd_Back.Hide()

    def SsvFrameData(self,mode,**kwargs):
        if mode == 1:
            data = self.MGETSudut('HEADER', 3, '')
            self.Ssv_ConfigData = data

        elif mode == 2:
            for item in kwargs['arraydata']:
                if len(item) != 0:
                    if len(item) == 3:
                        valuos = item[2]
                        if len(item) == 4:
                            speedos = item[3]
                            directos = None
                        else:
                            if len(item) == 5:
                                speedos = item[3]
                                directos = item[4]
                            else:
                                speedos = None
                                directos = None
                    else:
                        print 'WHAT!'
                        return

                    self.MRecordSudut('DETAIL', 1,headerid=kwargs['headerid'],list=item[0],
                                      motorid = item[1], val = valuos, speed=speedos,
                                      dirc= directos)

        elif mode == 3:
            self.MRecordSudut('HEADER', 1, name = kwargs['name'])

    def SsvArrayLongCheck(self, array, must):
        for item in array:
            if len(item) != int(must):
                gap = int(must) - len(item)
                for i in range(gap):
                    item.append(None)

        return array

    def SsvArrayItemCheck(self, data):
        array = copy.deepcopy(data)

        if type(array) != list:
            return
        angery = False
        DELETE_DIS = []
        for index_item in range(len(array)):
            item = array[index_item]
            none = True
            for subitem in item:
                if subitem not in ('-',None,''):
                    none = False
            if none == True:
                angery = True
                DELETE_DIS.append(index_item)

        if angery == True:
            for i in range(len(DELETE_DIS)):
                index = max(DELETE_DIS)
                del data[index]
                del DELETE_DIS[DELETE_DIS.index(index)]
            angery = False



        return(data)


    def SsvAppendInput(self):
        datas = self.SsvGetDataInput()
        datas = self.SsvArrayLongCheck(datas,5)
        self.Ssv_Dv_ConfigDetail.DeleteAllItems()
        self.SsvDvLoadArray(datas)

    def SsvAppendHome(self):
        maxrow = self.Ssv_Dv_ConfigDetail.GetItemCount()
        if maxrow == 0:
            sequence = 10
        else:
            seqlast = self.Ssv_Dv_ConfigDetail.GetValue(row=(maxrow-1),col=0)
            try:
                seqlast = int(seqlast)
            except Exception as e:
                print seqlast
                return
            else:
                sequence = seqlast + 10
        self.Ssv_Dv_ConfigDetail.AppendItem([sequence,9,'-','-','-'])

    def SsvGetDataInput(self):
        lists = 0
        data1 = []
        if self.Ssv_Txt_ValM1.GetValue() != '':
            lists += 10
            data1.append(int(lists))
            data1.append(int(1))
            data1.append(float(self.Ssv_Txt_ValM1.GetValue()))
            data1.append(float(self.Ssv_Txt_SpdM1.GetValue()))
            data1.append(str(self.Ssv_Cmb_DirM1.GetValue()))
        data1 = self.SsvDataInputFiltering(data1)

        data2 = []
        if self.Ssv_Txt_ValM2.GetValue() != '':
            lists += 10
            data2.append(int(lists))
            data2.append(int(2))
            data2.append(float(self.Ssv_Txt_ValM2.GetValue()))
            data2.append(float(self.Ssv_Txt_SpdM2.GetValue()))
            data2.append(str(self.Ssv_Cmb_DirM2.GetValue()))
        data2 = self.SsvDataInputFiltering(data2)

        data3 = []
        if self.Ssv_Txt_ValM3.GetValue() != '':
            lists += 10
            data3.append(int(lists))
            data3.append(int(3))
            data3.append(float(self.Ssv_Txt_ValM3.GetValue()))
            data3.append(float(self.Ssv_Txt_SpdM3.GetValue()))
            data3.append(str(self.Ssv_Cmb_DirM3.GetValue()))
        data3 = self.SsvDataInputFiltering(data3)

        data4 = []
        if self.Ssv_Txt_ValM4.GetValue() != '':
            lists += 10
            data4.append(int(lists))
            data4.append(int(4))
            data4.append(float(self.Ssv_Txt_ValM4.GetValue()))
            data4.append(float(self.Ssv_Txt_SpdM4.GetValue()))
            data4.append(str(self.Ssv_Cmb_DirM4.GetValue()))
        data4 = self.SsvDataInputFiltering(data4)

        data5 = []
        if self.Ssv_Txt_ValM5.GetValue() != '':
            lists += 10
            data5.append(int(lists))
            data5.append(int(5))
            data5.append(int(self.Ssv_Txt_ValM5.GetValue()))
            data5.append(int(self.Ssv_Txt_IncreM5.GetValue()))
        data5 = self.SsvDataInputFiltering(data5)

        data6 = []
        if self.Ssv_Cmb_ValM6.GetValue() != '' and self.Ssv_Cmb_ValM6.GetValue() != '-':
            lists += 10
            data6.append(int(lists))
            data6.append(int(6))
            data6.append(str(self.Ssv_Cmb_ValM6.GetValue()))
        data6 = self.SsvDataInputFiltering(data6)

        data7 = []
        if self.Ssv_Cmb_MagnetStat.GetValue() != '' and self.Ssv_Cmb_MagnetStat.GetValue() != '-':
            lists += 10
            data7.append(int(lists))
            data7.append(int(12))
            data7.append(str(self.Ssv_Cmb_MagnetStat.GetValue()))
        data7 = self.SsvDataInputFiltering(data7)

        hasil = [data1,data2,data3,data4,data5,data6,data7]

        return hasil


    def SsvDataInputFiltering(self,array):
        #Filter Value
        if len(array) != 0:
            #ON OFF
            if len(array) == 3:
                if array[2] == 'ON':
                    array[2] = 1
                elif array[2] == 'OFF':
                    array[2] = 0
            #SERVO
            if len(array) == 4:
                #Not necessary Yet
                pass
            #MOTOR
            if len(array) == 5:
                #PERBEDAAN DIREKSI
                if array[1] == 1:
                    if array[4] == 'CW':
                        array[4] = 1
                    elif array[4] == 'CCW':
                        array[4] = 0
                else:
                    if array[4] == 'CW':
                        array[4] = 0
                    elif array[4] == 'CCW':
                        array[4] = 1
        return (array)


    def SsvClearInput(self):
        self.Ssv_Txt_ValM1.SetValue('')
        self.Ssv_Txt_SpdM1.SetValue('')
        self.Ssv_Cmb_DirM1.SetValue('')

        self.Ssv_Txt_ValM2.SetValue('')
        self.Ssv_Txt_SpdM2.SetValue('')
        self.Ssv_Cmb_DirM2.SetValue('')

        self.Ssv_Txt_ValM3.SetValue('')
        self.Ssv_Txt_SpdM3.SetValue('')
        self.Ssv_Cmb_DirM3.SetValue('')

        self.Ssv_Txt_ValM4.SetValue('')
        self.Ssv_Txt_SpdM4.SetValue('')
        self.Ssv_Cmb_DirM4.SetValue('')

        self.Ssv_Txt_ValM5.SetValue('')
        self.Ssv_Txt_IncreM5.SetValue('')

        self.Ssv_Cmb_ValM6.SetValue('')

    def SsvSaveCHeader(self):
        if self.Ssv_Mode == 'NEW':

            #Save HEADER
            name = self.Ssv_Txt_SaveName.GetValue()
            if name == '':
                print 'No Name'
                return
            try:
                self.MRecordSudut('HEADER', 1, name = name)
            except Exception as e:
                print e
                return
            else:
                #Get Header ID
                headid = self.MGETSudut('HEADER', 4, '', name=name)


            #Save DETAIL
            data = self.SsvGetTableData()
            if data == None:
                return
            data = self.SsvRemoveDataMarker(data)
            print data

            for item in data:
                if len(item) != 0:
                    lists = item[0]
                    motorid = item[1]
                    val = item[2]
                    if len(item) == 4:
                        spd = item[3]
                        dirc = None
                    else:
                        if len(item) == 5:
                            spd = item[3]
                            dirc = item[4]
                        else:
                            spd = None
                            dirc = None

                    # Save Data
                    try:
                        print 'SAVING'
                        self.MRecordSudut('DETAIL', 1, headerid=headid, list=lists, motorid=motorid,
                                          val=val, speed=spd, dirc=dirc)
                    except Exception as e:
                        print  e
                    else:
                        print 'SAVE SUCCESS'

                    self.SsvRefreshLoad()

    def SsvRefreshLoad(self):
        self.Ssv_Cmb_LoadName.Clear()
        # RefreshArray
        self.SsvFrameData(1)
        self.Ssv_Cmb_LoadName.AppendItems(self.Ssv_ConfigData)
        self.Ssv_Cmb_LoadName.SetValue('- choose config to load -')

    def SsvLoadCHeader(self):

        self.Ssv_Cmd_Save.SetLabel('Save As')
        self.Ssv_Dv_ConfigDetail.DeleteAllItems()
        self.SsvClearInput()

        self.Ssv_Txt_UpdateName.SetValue(self.Ssv_Cmb_LoadName.GetValue())
        id = self.MGETSudut('HEADER', 4, '', name=self.Ssv_Cmb_LoadName.GetValue())
        print id

        if self.Ssv_Mode == 'EDIT':
            self.Ssv_HeadID = id
            self.Ssv_Txt_HeadID.SetValue(str(id))
            self.Ssv_Txt_IDUpdate.SetValue('ID = ' + str(id))
        elif self.Ssv_Mode == 'NEW':
            self.Ssv_Txt_HeadID.SetValue('')
            pass

        data = self.MGETSudutDetailSet(1,id)
        print data

        if len(data) == 0:
            print 'NO DATA'
            self.SsvClearInput()
            self.Ssv_Dv_ConfigDetail.DeleteAllItems()
            return

        self.Ssv_Dv_ConfigDetail.DeleteAllItems()
        self.SsvDvLoadArray(data)

    def SsvDvLoadArray(self,data):

        if len(data) == 0:
            print 'NO LOADED DATA'
            return

        #print len(data)
        #print data

        data = self.SsvArrayItemCheck(data)

        for item in data:
            #None Checker
            for subitem in item:
                if subitem == None:
                    id1 = data.index(item)
                    id2 = item.index(subitem)
                    data[id1][id2] = '-'
            self.Ssv_Dv_ConfigDetail.AppendItem(item)

    def SsvDeleteCHeader(self, headername):
        #DEL DETAIL
        self.MDeleteSudut('DETAIL',1,headerid=headid)

        #DEL HEADER
        self.MDeleteSudut('HEADER',1,headerid=headid,name=headername)

        #RefreshArray
        self.SsvFrameData(1)


    def SsvRemoveDataMarker(self,array):
        for item in array:
            for subitem in item:
                if subitem[0] != '-':
                    if subitem == '-':
                        id1 = array.index(item)
                        id2 = item.index(subitem)
                        array[id1][id2] = None
                else:
                    try:
                        del array[array.index(item)]
                    except Exception:
                        pass
                print array
        print array
        return array

    def SsvUpdateCHeader(self):
        print ('UPDATING')

        #UPDATE HEADER
        headid = int(self.Ssv_Txt_HeadID.GetValue())
        name = self.Ssv_Txt_UpdateName.GetValue()
        self.MUpdateSudut('HEADER', 1,headerid=headid , name = name)

        #UPDATE DETAIL
        data = self.SsvGetTableData()
        if data == None:
            data = []
        self.MUpdateSudut('DETAIL', 1, arraydata=data, headerid=headid)

    def SsvMAIN_DeleteCHeader(self):
        self.SsvStartDelete()
        self.Ssv_Jdl_2.SetLabel('DELETE CONFIG')

    def SsvMAIN_NewCHeader(self):
        #self.Ssv_Pnl_Delete.Hide()
        self.SsvStartNew()
        self.Ssv_Txt_HeadID.SetValue('')
        self.Ssv_Txt_UpdateName.SetValue('')
        self.Ssv_Cmb_LoadName.AppendItems(self.Ssv_ConfigData)
        self.Ssv_Cmb_LoadName.SetValue('- choose config to load -')
        self.Ssv_Jdl_2.SetLabel('MAKING NEW CONFIG')


    def SsvMAIN_LoadCHeader(self):
        #self.Ssv_Pnl_Delete.Hide()
        self.SsvStartLoad()
        self.Ssv_Txt_SaveName.SetValue('')
        self.Ssv_Jdl_2.SetLabel('UPDATE OLD CONFIG')
        self.Ssv_Cmb_LoadName.AppendItems(self.Ssv_ConfigData)
        self.Ssv_Cmb_LoadName.SetValue('- choose config to load -')
        self.Ssv_Txt_UpdateName.SetValue('')
        self.Ssv_Cmb_LoadName.AppendItems(self.Ssv_ConfigData)


    def SsvClearCDetail(self):
        self.Ssv_Dv_ConfigDetail.DeleteAllItems()

    def SsvEditCDetail(self):
        hasil = self.SsvGetTableData()
        self.SsvDataToInput(hasil)

    def SsvGetTableData(self):
        if self.Ssv_Dv_ConfigDetail.GetItemCount() == 0:
            print 'NO ITEM'
            return

        hasil = []
        for row in range(self.Ssv_Dv_ConfigDetail.GetItemCount()):
            rowsline = []
            for col in range(self.Ssv_Dv_ConfigDetail.GetColumnCount()):
                rowsline.append(str(self.Ssv_Dv_ConfigDetail.GetValue(row,col)))
            hasil.append(rowsline)

        return hasil


    def SsvDataToInput(self,arraydata):
        self.SsvClearInput()
        if arraydata == None or len(arraydata) == 0:
            return
        for item in arraydata:
            list = item[0]
            id = int(item[1])
            val = item[2]
            speed = item[3]
            dirc = item[4]

            #PERBEDAAN VAL
            if id == 1:
                if str(dirc) == '1':
                    dirc = 'CW'
                elif str(dirc) == '0':
                    dirc = 'CCW'
            else:
                if str(dirc) == '0':
                    dirc = 'CW'
                elif str(dirc) == '1':
                    dirc = 'CCW'



            if id == 1:
                self.Ssv_Txt_ValM1.SetValue(val)
                self.Ssv_Txt_SpdM1.SetValue(speed)
                self.Ssv_Cmb_DirM1.SetValue(dirc)
            elif id == 2:
                self.Ssv_Txt_ValM2.SetValue(val)
                self.Ssv_Txt_SpdM2.SetValue(speed)
                self.Ssv_Cmb_DirM2.SetValue(dirc)
            elif id == 3:
                self.Ssv_Txt_ValM3.SetValue(val)
                self.Ssv_Txt_SpdM3.SetValue(speed)
                self.Ssv_Cmb_DirM3.SetValue(dirc)
            elif id == 4:
                self.Ssv_Txt_ValM4.SetValue(val)
                self.Ssv_Txt_SpdM4.SetValue(speed)
                self.Ssv_Cmb_DirM4.SetValue(dirc)
            elif id == 5:
                self.Ssv_Txt_ValM5.SetValue(val)
                self.Ssv_Txt_IncreM5.SetValue(speed)
            elif id == 6:
                stepper = ''
                print val
                if int(val) == 1:
                    stepper = 'ON'
                elif int(val) == 0:
                    stepper = 'OFF'
                self.Ssv_Cmb_ValM6.SetValue(stepper)
            elif id == 12:
                magnet = ''
                print val
                if int(val) == 1:
                    magnet = 'ON'
                elif int(val) == 0:
                    magnet = 'OFF'
                self.Ssv_Cmb_MagnetStat.SetValue(magnet)


    def SsvGoBack(self):
        pass

    def SsvDelCDetail(self):
        if self.Ssv_Dv_ConfigDetail.GetItemCount() in (None,0):
            print ('NO ITEM')
            return
        rows = self.Ssv_Dv_ConfigDetail.GetSelectedRow()
        if rows == None:
            print ('NO SELECTED ROW')
            return
        self.Ssv_Dv_ConfigDetail.DeleteItem(rows)

    def SsvAutoSpeed(self, mode, **kwargs):
        #Version 1
        if mode == 1:
            #Collecting data
            try:
                # Get The Data Array
                data = kwargs['data']
                waktu = kwargs['waktu']
                microstepdriver = kwargs['microstep']
            except Exception as e:
                print e
                return
            else:
                #copy to set speed
                container = copy.deepcopy(data)

                #copy for value
                container_val = copy.deepcopy(container)

                #CONVERT TO STEP
                for keys in container_val:
                    if int(keys) in self.Need_ConvertValue:
                        # SUDUT CONVERSION
                        sudut = container_val[keys]
                        try:
                            MicroStep = self.Motor_Data[keys][14]
                        except Exception as e:
                            print (e)
                            continue
                        else:
                            converted_value = self.CNowsConvert(2, Axis=keys, SudutAxis=sudut,
                                                                MicroStepDriver=MicroStep)
                        sudut = int(converted_value)

                        #update
                        container_val[keys] = sudut

                print ('=============')
                print container
                print container_val
                print ('=============')

                # Get Max value from data
                maxs = max(container_val.items(), key = lambda x: x[1])
                maxvalue = maxs[1]
                maxvalue_key = maxs[0]

                #CALCULATE SPEED FOR MAX VAL
                #ToDo : Get The Rumus Here
                speed = self.CGetAccel(1,maxvalue,microstepdriver,waktu)
                container[maxvalue_key] = speed

                #CALCULATE SPEED FOR OTHER
                #Del the maxval
                del container_val[maxvalue_key]
                for item in container_val:
                    # Calculate Speed
                    # ToDo : Get The Rumus Here
                    othervalue = container_val[item]
                    print ('-----')
                    print othervalue
                    speed = self.CGetAccel(1,othervalue,microstepdriver,waktu)
                    print speed
                    print ('-----')
                    container[item] = speed
                    pass

                return (container)

    def SsvGetDataInput2(self):
        hasil = {}
        if self.Ssv_Txt_ValM1.GetValue() != '':
            data = (float(self.Ssv_Txt_ValM1.GetValue()))
            data1 = {1:data}
            hasil.update(data1)

        if self.Ssv_Txt_ValM2.GetValue() != '':
            data = (float(self.Ssv_Txt_ValM2.GetValue()))
            data2 = {2:data}
            hasil.update(data2)

        if self.Ssv_Txt_ValM3.GetValue() != '':
            data = (float(self.Ssv_Txt_ValM3.GetValue()))
            data3 = {3:data}
            hasil.update(data3)

        if self.Ssv_Txt_ValM4.GetValue() != '':
            data = (float(self.Ssv_Txt_ValM4.GetValue()))
            data4 = {4:data}
            hasil.update(data4)

        print hasil
        return hasil


    def SsvGetAutoSpeed(self, mode ,**kwargs):
        if mode == 1:
            try:
                waktujalan = int(kwargs['waktu'])
                microstepdriver = int(kwargs['microstep'])
            except Exception as e:
                print 'INVALID INPUTED TIME VALUE'
                print e
                return
            else:
                if int(kwargs['waktu']) < 1:
                    print ('CANNOT < ZERO')
                    return
                data_config = self.SsvGetDataInput2()
                if len(data_config) == 0:
                    print ('NO DATA TO CALCULATE [1-4?]')
                    return
                speed_data = self.SsvAutoSpeed(1,microstep = microstepdriver,
                                                  waktu = waktujalan, data = data_config)
                print speed_data

                for id in speed_data:
                    if id == 1:
                        self.Ssv_Txt_SpdM1.SetValue(str(speed_data[id]))
                    elif id == 2:
                        self.Ssv_Txt_SpdM2.SetValue(str(speed_data[id]))
                    elif id == 3:
                        self.Ssv_Txt_SpdM3.SetValue(str(speed_data[id]))
                    elif id == 4:
                        self.Ssv_Txt_SpdM4.SetValue(str(speed_data[id]))















