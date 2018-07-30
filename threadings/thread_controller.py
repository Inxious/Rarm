
import wx
import serial
from wx.lib.pubsub import pub
from modules import serialscan

class Th_Controller():
    def __init__(self):

        self.Controller_Mode = False
        self.Controller_Connection = 'OFF'
        self.Controller_LastCmd = ''
        self.Controller_NowCmd = ''
        self.Controller_Run = ''
        self.CTRL_value_must = {}
        last_container = ''
        faster = False
        detected = True
        x = 0
        lastaxis = ''
        while True:

            if self.Controller_Mode == True:

                #Connect To Device
                if self.Controller_Connection  == 'OFF':
                    try:
                        ser = serial.Serial(str(self.Serial_Controller))
                        ser.close()
                    except Exception as e:
                        if x == 0:
                            x = 1
                            lastaxis = ''
                            print ('NO CONTROLLER')

                            if self.CurrForm == 'Manual':
                                #self.MnlResetScroll()
                                self.Lbl_Mnl_WidgetControllerStatsView.SetForegroundColour(wx.Colour(255, 0, 0))
                                self.Lbl_Mnl_WidgetControllerStatsView.SetLabel("DISCONNECTED")
                                self.Lbl_Mnl_WidgetControllerStatsView.SetForegroundColour(wx.Colour( 255, 0, 0))
                            elif self.CurrForm == 'Setup':
                                #self.StPrcResetScroll()
                                self.Lbl_StPrc_WidgetControllerStatsView.SetForegroundColour(wx.Colour(255, 0, 0))
                                self.Lbl_StPrc_WidgetControllerStatsView.SetLabel("DISCONNECTED")
                                self.Lbl_StPrc_WidgetControllerStatsView.SetForegroundColour(wx.Colour( 255, 0, 0))

                    else:
                        wx.CallAfter(pub.sendMessage, 'SerialConnect', mode=1, board=2, com=self.Serial_Controller,
                                     baudrate=self.Brate_Controller, timeout=0)

                        isconect = False
                        while isconect == False:
                            try:
                                self.Serial_List[2]
                                self.Serial_List[2].write(('TEST').encode())
                            except Exception as e:
                                pass
                            else:
                                isconect = True

                        if self.CurrForm == 'Manual':
                            self.MnlResetScroll()
                            self.Lbl_Mnl_WidgetControllerStatsView.SetForegroundColour(wx.Colour(0, 255, 0))
                            self.Lbl_Mnl_WidgetControllerStatsView.SetLabel("CONNECTED")
                            self.Lbl_Mnl_WidgetControllerStatsView.SetForegroundColour( wx.Colour( 0, 255, 0 ))
                        elif self.CurrForm == 'Setup':
                            self.StPrcResetScroll()
                            self.Lbl_StPrc_WidgetControllerStatsView.SetForegroundColour(wx.Colour(0, 255, 0))
                            self.Lbl_StPrc_WidgetControllerStatsView.SetLabel("CONNECTED")
                            self.Lbl_StPrc_WidgetControllerStatsView.SetForegroundColour( wx.Colour( 0, 255, 0))

                        detected = True
                        self.Controller_Connection = 'ON'

                        print('CONTROLLER CONNECTED')

                elif self.Controller_Connection == 'ON':
                    # READLINE FOCUS
                    try:
                        hasil = self.Serial_List[2].readline()
                    except Exception as e:
                        x = 0
                        self.Controller_Connection = 'OFF'
                        continue
                    else:
                        container = ''
                        for words in hasil:
                            re_word = ''
                            for strings in words:
                                if strings not in (' ',''):
                                    re_word += strings
                            if re_word != '':
                                container += re_word

                        if container == '':
                            if self.CurrForm == 'Manual':
                                if self.CurrentFocus == '' and lastaxis != '':
                                    if int(axis) == 1:
                                        oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                                        oevt.SetEventObject(self.Mnl_Spn_Value1)
                                        wx.PostEvent(self.Mnl_Spn_Value1, oevt)
                                    if int(axis) == 2:
                                        oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                                        oevt.SetEventObject(self.Mnl_Spn_Value2)
                                        wx.PostEvent(self.Mnl_Spn_Value2, oevt)
                                    if int(axis) == 3:
                                        oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                                        oevt.SetEventObject(self.Mnl_Spn_Value3)
                                        wx.PostEvent(self.Mnl_Spn_Value3, oevt)
                                    if int(axis) == 4:
                                        oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                                        oevt.SetEventObject(self.Mnl_Spn_Value4)
                                        wx.PostEvent(self.Mnl_Spn_Value4, oevt)
                                    if int(axis) == 5:
                                        oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                                        oevt.SetEventObject(self.Mnl_Spn_Value5)
                                        wx.PostEvent(self.Mnl_Spn_Value5, oevt)
                                    if int(axis) == 6:
                                        oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                                        oevt.SetEventObject(self.Mnl_Spn_Value6)
                                        wx.PostEvent(self.Mnl_Spn_Value6, oevt)

                                    self.CurrentFocus = int(lastaxis)



                    #DELAYING
                    #====================================================
                    if self.Scroll_TypeCommand == 'NORMAL':
                        if container == '' and last_container != '':
                            # ===============================================================
                            if detected == True:
                                detect_start = self.CCurTime(datetime=True)
                                detected = False

                            # Time save
                            detect_now = self.CCurTime(datetime=True)
                            detect_passed = detect_now - detect_start

                            # If Over The limit time
                            if float(detect_passed.total_seconds()) > float(self.Limit_Detect):
                                print 'Detect Done ' + str(float(detect_passed.total_seconds()))
                                print 'Running >>  ' + str(last_container)
                                detected = True
                                container = last_container
                                last_container = ''
                                self.Serial_List[2].flushOutput()
                            else:
                                continue
                        else:
                            detect_start = self.CCurTime(datetime=True)
                            last_container = container
                            continue
                    #====================================================
                    #print container

                    self.Arraynows = []

                    # IF DOL APPEAR
                    if 'DOL' in container:
                        axis = 0
                        val = 0
                        arraycommand = {1: str(container).encode()}
                        commandlist = []
                        commandlist.append(arraycommand)

                        if self.CurrForm == 'Manual':
                            self.MnlResetScroll(controller = True)

                        #Reset TO ZERO
                        for i in range(5):
                            self.CNows(5, type='value', motor=int(i) ,
                                        value=int(val))



                        print 'Running >>  ' + str(container)
                        arraymovement = []

                        self.CurrentFocus == ''
                    
                    elif 'RUN' in container:
                        # GENERATING COMMAND
                        #========================================================
                        try:
                            lenght = len(self.CTRL_value_must)
                        except Exception as e:
                            self.CTRL_value_must = {}
                            continue
                        else:
                            if lenght == 0 :
                                continue
                        ultimate_double_supper_celengan_ayam = self.CTRL_value_must.keys()

                        temp_arraycommmand = []
                        temp_arraymovement = []
                        temp_arrayvaluecommand = {}
                        for key in ultimate_double_supper_celengan_ayam:

                            #VALUE
                            val = self.CTRL_value_must[key]

                            #Validasi Bahwa Bukan 0
                            # ONLY GO WHEN REEEEEEEEEEEEE
                            #if int(val) == 0:
                                # PASS IF ITS A REEEEEEEEEEEE
                                #continue

                            # IF WITH CONSTANT COMMAND and not JUST SEND
                            if faster == False:
                                # IF AXIS = 1
                                if int(key) == 1:

                                    # Direksi
                                    #if int(val) < int(0):
                                    #    dir = int(1)
                                    #else:
                                    #    dir = int(0)
                                    valueinfo = self.CDefineStep(1,val)
                                    if valueinfo != None:
                                        val = valueinfo[0]
                                        dir = valueinfo[1]
                                    else:
                                        continue


                                    valcalculated = val

                                    if self.Scroll_Axis1 == 'NORMAL':
                                        commanddata = self.CLoadConstantCommand('NORMAL', 1)
                                        container = self.CSearchAndCount(commanddata[0], commanddata[1],
                                                                         replace=True,
                                                                         array=[valcalculated, self.Speed[int(key)],
                                                                                dir])
                                        digit = self.CGetDigitCmd(int(key))
                                        if digit == None:
                                            print ("DIGIT COMMMAND ERROR " + str(int(key)))
                                            continue

                                        # Fix Command
                                        for i in range(4):
                                            check = self.CCommandCheck(1, container , digits=digit)
                                            if check == "special_command":
                                                check = self.CCommandCheck(2, container, digits=digit)
                                                modes = 2
                                            else:
                                                modes = 1
                                            if check == "pass":
                                                break

                                            digit = self.CGetDigitCmd(int(key))
                                            if digit == None:
                                                print ("DIGIT COMMMAND ERROR " + str(int(key)))
                                                continue

                                            container = self.CCommandFix(modes, check, container,
                                                                         value=int(valcalculated),
                                                                         speed=self.Speed[int(key)],
                                                                         dir=dir, digits=digit)

                                # OTHER AXIS
                                else:
                                    # Direksi
                                    #if int(val) < int(0):
                                    #    dir = int(1)
                                    #else:
                                    #    dir = int(0)

                                    valueinfo = self.CDefineStep(1, val)
                                    if valueinfo != None:
                                        val = valueinfo[0]
                                        dir = valueinfo[1]
                                    else:
                                        continue

                                    valcalculated = val

                                    if self.Scroll_TypeCommand == 'NORMAL':
                                        commanddata = self.CLoadConstantCommand('NORMAL', int(key))
                                        container = self.CSearchAndCount(commanddata[0], commanddata[1],
                                                                         replace=True,
                                                                         array=[valcalculated,self.Speed[int(key)], dir])

                                        digit = self.CGetDigitCmd(int(key))
                                        if digit == None:
                                            print ("DIGIT COMMMAND ERROR " + str(int(key)))
                                            continue

                                        # Fix Command
                                        for i in range(4):
                                            check = self.CCommandCheck(1, container, digits=digit)
                                            if check == "special_command":
                                                check = self.CCommandCheck(2, container, digits=digit)
                                                modes = 2
                                            else:
                                                modes = 1

                                            if check == "pass":
                                                break

                                            digit = self.CGetDigitCmd(int(key))
                                            if digit == None:
                                                print ("DIGIT COMMMAND ERROR " + str(int(key)))
                                                continue

                                            container = self.CCommandFix(modes, check, container,
                                                                         value=int(valcalculated),
                                                                         speed=self.Speed[int(key)],
                                                                         dir=dir, digits=digit)

                                temp_arraymovement.append([int(key), valcalculated, self.Speed[int(key)], dir])
                                temp_arraycommmand.append(container)
                                temp_arrayvaluecommand.update({key:val})

                        commandlist = []
                        if self.Scroll_TypeCommand == 'NORMAL':
                            commandlist.append({1: str('DEL')})
                            self.Arraynows.append([])
                            for item in temp_arraycommmand:
                                commandlist.append({1:item})
                                self.Arraynows.append(temp_arraymovement[temp_arraycommmand.index(item)])
                            commandlist.append({1: str('RUN')})
                            self.Arraynows.append([])
                            self.CFastExecutingCommand(commandlist, save=True, timedelay=float(self.Limit_Controller))
                        else:
                            commandlist.append(arraycommand)
                            self.CFastExecutingCommand(commandlist, save=True)
                        temp_arrayconverted = []
                        for axislis in temp_arrayvaluecommand.keys():
                            # UPDATE UI
                            # ================================================================

                            try:
                                MicroStep = self.Motor_Data[axislis][14]
                            except Exception as e:
                                print (e)
                                continue
                            else:
                                val = self.CNows(2, need=int(axislis))
                                converted_value = self.CNowsConvert(1, Axis=axislis, PulseStepMotor=val,
                                                                    MicroStepDriver=MicroStep)
                                print converted_value
                                temp_arrayconverted.append([axislis,converted_value])

                            if self.CurrForm == 'Manual':
                                if int(axislis) == 1:
                                    oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                                    oevt.SetEventObject(self.Mnl_Spn_Value1)
                                    wx.PostEvent(self.Mnl_Spn_Value1, oevt)
                                if int(axislis) == 2:
                                    oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                                    oevt.SetEventObject(self.Mnl_Spn_Value2)
                                    wx.PostEvent(self.Mnl_Spn_Value2, oevt)
                                if int(axislis) == 3:
                                    oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                                    oevt.SetEventObject(self.Mnl_Spn_Value3)
                                    wx.PostEvent(self.Mnl_Spn_Value3, oevt)
                                if int(axislis) == 4:
                                    oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                                    oevt.SetEventObject(self.Mnl_Spn_Value4)
                                    wx.PostEvent(self.Mnl_Spn_Value4, oevt)
                                if int(axislis) == 5:
                                    oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                                    oevt.SetEventObject(self.Mnl_Spn_Value5)
                                    wx.PostEvent(self.Mnl_Spn_Value5, oevt)
                                if int(axislis) == 6:
                                    oevt = wx.CommandEvent(commandEventType=wx.EVT_SPINCTRLDOUBLE.typeId)
                                    oevt.SetEventObject(self.Mnl_Spn_Value6)
                                    wx.PostEvent(self.Mnl_Spn_Value6, oevt)

                                if int(axislis) == 1:
                                    self.Mnl_Spn_Value1.SetValue(float(converted_value))
                                    self.Mnl_Sld_Move1.SetValue(float(converted_value))
                                if int(axislis) == 2:
                                    self.Mnl_Spn_Value2.SetValue(float(converted_value))
                                    self.Mnl_Sld_Move2.SetValue(float(converted_value))
                                if int(axislis) == 3:
                                    self.Mnl_Spn_Value3.SetValue(float(converted_value))
                                    self.Mnl_Sld_Move3.SetValue(float(converted_value))
                                if int(axislis) == 4:
                                    self.Mnl_Spn_Value4.SetValue(float(converted_value))
                                    self.Mnl_Sld_Move4.SetValue(float(converted_value))
                                if int(axislis) == 5:
                                    self.Mnl_Spn_Value5.SetValue(int(val))
                                    self.Mnl_Sld_Move5.SetValue(int(val))
                                if int(axislis) == 6:
                                    self.Mnl_Spn_Value6.SetValue(int(val))
                                    self.Mnl_Sld_Move6.SetValue(int(val))
                                # ========================================================

                        print '============================================='
                        print 'value'
                        print temp_arrayvaluecommand
                        print 'converted'
                        print temp_arrayconverted
                        print 'command'
                        print commandlist
                        print '============================================='

                        print commandlist
                        print self.Arraynows
                        print 'NOW ' + '[' + str(int(axis)) + ']' + str(self.CNows(2, need=self.CurrentFocus))
                        
                        #========================================================

                        #RESETING
                        #========================================================

                        del temp_arraycommmand
                        del temp_arraymovement
                        del temp_arrayvaluecommand
                        del temp_arrayconverted
                        del commandlist
                        self.CTRL_value_must = {}
                        #========================================================
                        
                        print 'Running >>  ' + str(container)
                        arraymovement = []
                        
                    #OTHER COMMAND
                    else:
                        if container == '':
                                continue

                        #MINING DATA FROM STRING
                        data = container.split(';')
                        axis = int(data[1])
                        val = int(data[2])
                        self.CurrentFocus = int(axis)

                        #SAVING DATA BY AXIS
                        try:
                            self.CTRL_value_must[axis] = val
                        except Exception as e:
                            self.CTRL_value_must.update({axis:val})

                        print self.CTRL_value_must

                        lastaxis = axis




                        

