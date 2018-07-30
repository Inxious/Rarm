
import wx
import serial
from wx.lib.pubsub import pub
from modules import serialscan

class Th_Controller():
    def __init__(self):

        self.Controller_Mode = False
        self.Controller_Connection = 'OFF'
        faster = False
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
                            print ('NO CONTROLLER')
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
                        for string in hasil:
                            if string not in (' ',''):
                                container += string
                        pass

                    # WRITE SCROLL VALUE
                    if container != '':
                        try:
                            #Try Check Connection
                            self.Serial_List[2]
                        except Exception as e:
                            x = 0
                            self.Controller_Connection = 'OFF'
                            continue
                        else:
                            if 'DOL' in container:
                                axis = 0
                                val = 0
                                arraycommand = {1: str(container).encode()}
                                #print (arraycommand)
                                commandlist = []
                                commandlist.append(arraycommand)

                                if self.CurrForm == 'Manual':
                                    self.MnlResetScroll(controller = True)

                                #Reset TO ZERO
                                for i in range(4):
                                    self.CNows(5, type='value', motor=int(axis) + 1,
                                                value=int(val))
                                    axis += 1

                            else:
                                if faster == False:
                                    data = container.split(';')
                                    axis = data[1]
                                    val = data[2]
                                    self.Current_Focus = int(axis) + 1


                                    if int(axis) == 0:
                                        # Direksi
                                        posnow = self.CNows(2, need=self.Current_Focus)
                                        if posnow != None:

                                            if int(posnow) < int(val):
                                                dir = int(1)
                                            else:
                                                dir = int(0)
                                        else:

                                            if not int(val) < 0:
                                                dir = int(1)
                                            else:
                                                dir = int(0)

                                        valcalculated = self.CPulseCalculate(val, int(axis)+1)

                                        if self.Scroll_Axis0 == 'NORMAL':
                                            commanddata = self.CLoadConstantCommand('NORMAL', 1)
                                            container = self.CSearchAndCount(commanddata[0], commanddata[1],
                                                                           replace=True,
                                                                           array=[valcalculated, self.Speed[int(axis) + 1], dir])
                                            #Fix Command
                                            for i in range(4):
                                                check = self.CCommandCheck(1, container)
                                                if check == "pass":
                                                    break
                                                digit = [4, 4, 4]
                                                container = self.CCommandFix(1, check, container,
                                                                             value=int(valcalculated),
                                                                             speed=self.Speed[int(axis) + 1],
                                                                             dir=dir, digits=digit)

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

                                arraycommand = {1:str(container).encode()}
                                commandlist = []
                                if int(axis) == 0:
                                    if self.Scroll_Axis0 == 'NORMAL':
                                        commandlist.append({1: str('DEL')})
                                        commandlist.append(arraycommand)
                                        commandlist.append({1: str('RUN')})
                                    else:
                                        commandlist.append(arraycommand)
                                else:
                                    commandlist.append(arraycommand)

                                self.CNows(5, type='value', motor=int(axis)+1,
                                           value=int(val))


                            self.CFastExecutingCommand(commandlist, save=True)
                        #print commandlist
                        print 'NOW ' + '[' + str(int(axis)+1) + ']' + str(self.CNows(2, need=self.Current_Focus))


