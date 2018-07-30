
#IMPORT LIB MODULE
import sys
import os
import time
import copy
import threading
import serial
import logging
import datetime
import ConfigParser
from wx.lib.pubsub import pub
import Rumus
from time import gmtime, strftime
import wx
from ctypes import *

#IMPORT OUR MODULE
from modules import view,model,ConfigParsing
from threadings import thread_detectpos,thread_boards1,thread_events,thread_controller

class Controller(view.View, model.Model, thread_detectpos.Th_DetectPos,
                 thread_boards1.ThreadsB1,thread_events.ThreadEvents,
                 thread_controller.Th_Controller,ConfigParsing.ConfigPasser):
    def __init__(self):

        # DEFINE CONFIG FILE
        self.config = ConfigParser.ConfigParser()
        self.config.readfp(open(r'config.txt'))

        # CONFIG FILE DATA
        # =============================================================================
        self.Serial_Controller = self.config.get('Controller Configuration', 'Serial')
        self.Brate_Controller = self.config.get('Controller Configuration', 'BaudRate')
        self.Limit_Controller = self.config.get('Controller Configuration', 'DelayCommand')
        self.Scroll_Axis1 = self.config.get('Scroll Mode Configuration', 'Axis_0')
        self.Scroll_TypeCommand = self.config.get('Scroll Mode Configuration', 'TypeCommand')
        self.Limit_Detect = float(self.config.get('Scroll Mode Configuration', 'Limit_Detect'))
        self.Limit_Command = float(self.config.get('Scroll Mode Configuration', 'Limit_Command'))
        self.ISDebug = bool(int(self.config.get('Application Configuration', 'ISDebug')))
        #self.Zero_ID = int(self.config.get('Motor Configuration', 'ZeroID'))
        self.Non_IncrementalMotor = [5,6,7,8,9]


        #RUMUS DATA
        mydll = cdll.LoadLibrary("dll/dllProject.dll")
        self.CRumusAccel = getattr(mydll, "?calculateSpeed@CDllProject@@SAHHHH@Z")

        # CONSTANT VAR
        self.CStarter()
        self.Logger_List = {}
        # ToDo : Load Max and Min Motor Value


        #GET DATA FROM CONFIG FILE
        UseBoard = self.config.get('Machine Connection', 'BoardUsed')
        for i in range(int(UseBoard)):
            num = int(i) +  1
            self.Board_List.update({int(num):self.config.get('Machine Connection', str(num))})


        #LOG DEBUG
        #Basic
        logging.basicConfig()

        #Debug Main
        self.Main_Logging = logging.getLogger('Main-Log')
        #main_file = logging.FileHandler(#filename="filename")
        #main_format = logging.Formatter("")
        #main_file.setFormatter()
        #self.Main_Logging.addHandler(main_file)
        self.Main_Logging.setLevel(logging.DEBUG)
        self.Logger_List.update({'Main-Log':self.Main_Logging})

        # Debug Serial
        self.Ser_Logging = logging.getLogger('Serial-Log')
        # main_file = logging.FileHandler(#filename="filename")
        # main_format = logging.Formatter("")
        # main_file.setFormatter()
        # self.Main_Logging.addHandler(main_file)
        self.Ser_Logging.setLevel(logging.DEBUG)
        self.Logger_List.update({'Serial-Log': self.Ser_Logging})

        # Debug Serial
        self.Ser_Logging = logging.getLogger('Thread-Log')
        # main_file = logging.FileHandler(#filename="filename")
        # main_format = logging.Formatter("")
        # main_file.setFormatter()
        # self.Main_Logging.addHandler(main_file)
        self.Ser_Logging.setLevel(logging.DEBUG)
        self.Logger_List.update({'Thread-Log': self.Ser_Logging})


        # MAIN MODULE INIT
        model.Model.__init__(self)
        view.View.__init__(self, None)
        ConfigParsing.ConfigPasser.__init__(self)


        #ThreadContainer
        self.ThreadList = {}
        self.ThreadFailed = {}

        #THREADING INIT
        T_Event = self.CThreadManager(1, target=thread_events.ThreadEvents.__init__, args=(self,),
                                       name="Thread Events")
        T_DetectPos = self.CThreadManager(1,target=thread_detectpos.Th_DetectPos.__init__ , args=(self,),
                                          name="Thread DetectPos")
        T_Controller = self.CThreadManager(1, target=thread_controller.Th_Controller.__init__, args=(self,),
                                          name="Thread Controller")
        T_Board1 = self.CThreadManager(1, target=thread_boards1.ThreadsB1.__init__, args=(self,),
                                          name="Thread BOARD 1")

        #metode 1
        #thread_events.ThreadEvents.__init__(self)
        #thread_events.ThreadEvents.__init__
        #self.tambah()
        #T_Event = thread_events.ThreadEvents.__init__(self)
        #    T_Evebt.

        #SET DAEMON
        T_Event.daemon = True
        T_DetectPos.daemon = True
        T_Controller.daemon = True
        T_Board1.daemon = True


        #APPEND TO LIST
        self.ThreadList.update({T_DetectPos.getName():T_DetectPos})
        self.ThreadList.update({T_Controller.getName(): T_Controller})
        self.ThreadList.update({T_Board1.getName(): T_Board1})
        self.ThreadList.update({T_Event.getName(): T_Event})

        #THREADING START
        self.CThreadManager(2, list=self.ThreadList)


        #Bind
        #self.Bind(wx.EVT_CLOSE , lambda x: self.COnCloseApp() )

        #PUBSUB WX RECIEVER
        self.CPubSubReciever()

    def CPubSubReciever(self):
        pub.subscribe(self.CSerialConn, 'SerialConnect')
        pub.subscribe(self.CSerialDisconn, 'SerialDisconnect')
        pub.subscribe(self.TheEnd, 'CloseApp')

    def TheEnd(self):
        self.VDestroyAll()
        self.DetectingPos = False
        self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                         message='Ending Program')

    def CSerialConn(self, mode, board, com, baudrate, timeout):
        self.CPrintDebug(3, object=self.Logger_List['Serial-Log'], message='Trying To Connect ' + str(com) + ' ' + str(baudrate))
        if mode == 1:
            ser = serial.Serial()

            if ser.is_open == True:
                ser.close()

            try:
                ser.port = str(com)
                ser.baudrate = int(baudrate)
                ser.timeout = int(timeout)
                ser.open()
            except Exception as e:
                self.CPrintDebug(3,object=self.Logger_List['Main-Log'],message='SERIAL FAILED')
                self.CPrintDebug(3, object=self.Logger_List['Main-Log'], message=e)
            else:
                self.Serial_List.update({board:ser})
                self.CPrintDebug(3, object=self.Logger_List['Main-Log'], message='SERIAL CONNECTED')

                if self.Board_Connection.get(board) == None:
                    self.Board_Connection.update({board:"ON"})
                else:
                    self.Board_Connection[board] = "ON"

                if self.Board_Reading.get(board) == None:
                    self.Board_Reading.update({board:"OFF"})
                else:
                    self.Board_Reading[board] = 'OFF'

                if self.Board_Reading_Flag.get(board) == None:
                    self.Board_Reading_Flag.update({board:""})
                else:
                    self.Board_Reading_Flag[board] = ''

                if self.Serial_Active.get(board) == None:
                    self.Serial_Active.update({board:True})
                else:
                    self.Serial_Active[board] = True

    def CSerialDisconn(self, board):
        self.CPrintDebug(2, object=self.Logger_List['Serial-Log'],
                         message='Trying To Disconnect ' + str(self.Serial_List[board].port) + ' ' +
                                 str(self.Serial_List[board].baudrate))
        if self.Serial_List[board].is_open == True:
            if self.Board_Connection.get(board) != None:
                del self.Board_Connection[board]
                #self.Board_Connection[board] = "OFF"

            if self.Board_Reading.get(board) != None:
                del self.Board_Reading[board]
                #self.Board_Reading[board] = "OFF"

            if self.Serial_List.get(board) != None:
                del self.Serial_List[board]
                #self.Serial_List[board].close()

            if self.Serial_Active.get(board) != None:
                del self.Serial_Active[board]
                #self.Ser_Active[board] = False

        self.CPrintDebug(2, object=self.Logger_List['Main-Log'], message='SERIAL DISCONNECTED')

    def CGETCurrValue(self, mode, focus , **kwargs):
        #GET VALUE OF SPINNER FROM MANUAL FORM
        if mode == 1:
            if focus == 1:
                now = self.Mnl_Spn_Value1.GetValue()
            elif focus == 2:
                now = self.Mnl_Spn_Value2.GetValue()
            elif focus == 3:
                now = self.Mnl_Spn_Value3.GetValue()
            elif focus == 4:
                now = self.Mnl_Spn_Value4.GetValue()
            elif focus == 5:
                now = self.Mnl_Spn_Value5.GetValue()
            elif focus == 6:
                now = self.Mnl_Spn_Value6.GetValue()
            else:
                return


            if self.PositionMust.get(focus) == None:
                self.PositionMust.update({focus:int(now)})
            else:
                self.PositionMust[focus] = int(now)

        elif mode == 2:
            if focus == 1:
                now = self.Mnl_Sld_Move1.GetValue()
            elif focus == 2:
                now = self.Mnl_Sld_Move2.GetValue()
            elif focus == 3:
                now = self.Mnl_Sld_Move3.GetValue()
            elif focus == 4:
                now = self.Mnl_Sld_Move4.GetValue()
            elif focus == 5:
                now = self.Mnl_Sld_Move5.GetValue()
            elif focus == 6:
                now = self.Mnl_Sld_Move6.GetValue()
            else:
                return

            if self.PositionMust.get(focus) == None:
                self.PositionMust.update({focus:int(now)})
            else:
                self.PositionMust[focus] = int(now)

        elif mode == 3:

            if self.PositionMust.get(focus) == None:
                self.PositionMust.update({focus:int(kwargs['values'])})
            else:
                self.PositionMust[focus] = int(kwargs['values'])

    def COnCloseApp(self):
        board = self.Serial_List.keys()
        if len(board) != 0:
            for item in board:
                if self.Serial_List[board].is_open == True:
                    if self.Board_Connection.get(board) != None:
                        del self.Board_Connection[board]
                        #self.Board_Connection[board] = "OFF"

                    if self.Board_Reading.get(board) != None:
                        del self.Board_Reading[board]
                        #self.Board_Reading[board] = "OFF"

                    if self.Serial_List.get(board) != None:
                        del self.Serial_List[board]
                        #self.Serial_List[board].close()

                    if self.Serial_Active.get(board) != None:
                        del self.Serial_Active[board]
                        #self.Ser_Active[board] = False

            self.CPrintDebug(2, object=self.Logger_List['Main-Log'], message='SERIAL DISCONNECTED')
        self.Destroy()

    def CStarter(self):
        self.CurrentFocus = None
        self.PositionNow = ""
        self.PositionMust = {}
        self.DetectingPos = False

        self.Serial_List = {}
        self.Serial_Active = {}
        self.Board_List = {}
        self.Board_Reading_Flag = {}
        self.Board_Reading = {}
        self.Board_Connection = {}
        self.FrameObject = {}

        #NOW VALUE
        #self.Speed = {}
        self.Speed = {1:800,2:800,3:800,4:800,5:20}
        self.Now = {}
        self.Arraynows = []
        self.CNows(3)#AFTER ZERO
        self.CNows(6)#REAL

        #Zero Coordinate
        #self.CZeroCoordinate(3)

        #POSITION NOW
        self.Motor_PositionNow = {}
        self.M1_Now = None
        self.M2_Now = None
        self.M3_Now = None
        self.M4_Now = None
        self.M5_Now = None
        self.M6_Now = None

        #Command
        self.Scroll_Cmd = {}
        self.Scroll_Reset = {}

    def CCurTime(self, **kwargs):
        try:
            isdatetimes = kwargs['datetime']
        except Exception as e:
            #Return Ordinary time
            return (strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        else:
            if isdatetimes == True:
                time = datetime.datetime.now()
                return (time)

    def CEventON(self):
        if self.Executing_Event == "ON":
            while self.Executing_Event == "ON":
                pass
                self.Executing_Event = "ON"
        else:
            self.Executing_Event = "ON"

    def CThreadManager(self,mode, **kwargs):
        #Make Thread Object
        if mode == 1:
            container = []
            for item in kwargs['args']:
                container.append(item)
                container = tuple(container)
            return(threading.Thread(target=kwargs['target'], args=container,
                                    name=kwargs['name']))
        #INIT Thread
        elif mode == 2:
            for thread in kwargs['list']:
                try:
                    kwargs['list'][thread].daemon = True
                    kwargs['list'][thread].start()
                except Exception:
                    #IF FAILED
                    print "Thread Failed To Init"
                    self.ThreadFailed.update({thread:kwargs['list'][thread]})
                else:
                    #IF SUCCEDED
                    print "Thread " + str(kwargs['list'][thread].getName()) + " Succes To Init"

    def CConstantCommand(self, types):
        #Constant command mean command loaded on start of the programs
        #and never loaded again .. never

        if  types == 'SCROLL':
            self.Constant_ScrollCmd = True
            #Func to get
            self.MGETConstantCommand(types)
            #printself.Scroll_Cmd
        elif types == 'NORMAL':
            self.Constant_NormalCmd = True
            #Func to get
            self.MGETConstantCommand(types)
            #printself.Normal_Cmd
        elif types == 'ACTIVATION':
            self.Constant_ActivationCmd = True
            #Func to get
            self.MGETConstantCommand(types)
            #printself.Normal_Cmd self.Motor_MicroStep

    def CConstantData(self, types, **kwargs):
        #Constant command mean command loaded on start of the programs
        #and never loaded again .. never
        if  types == 'MOTOR':
            data = self.MGETConstantData(types,colwanted=kwargs['colwanted'])
            return (data)



    def CLoadConstantCommand(self, types, id):
        if types == 'SCROLL':
            try:
                result = self.Scroll_Cmd[id]
            except Exception as e:
                print e
            else:
                return (result)
        elif types == "RESET":
            try:
                result = self.Scroll_Reset[id]
            except Exception as e:
                print e
            else:
                return (result)
        elif types == "NORMAL":
            try:
                result = self.Normal_Cmd[id]
            except Exception as e:
                print e
            else:
                return (result)

    def CRoboMoveStep(self, mode, **kwargs):
        #TESTER VERSION
        if mode == 1:
            self.PositioningDone = False
            #OUTSIDE WHILE FOR MAKE SURE IT ACTUALY THE SAME OR NOT
            while self.PositioningDone != True:
                while self.PositionNow != self.PositionMust:
                    time.sleep(0.5)

                    #ToDo : self.RoboGO function

                    #print'a'#values

                time.sleep(1)
                if self.PositionNow == self.PositionMust:
                    self.PositioningDone = True

        #Just Move
        elif mode == 2:
            #RUN THE PROCESS
            arrays = [10,kwargs['motorid'],kwargs['sudut'],
                        self.Speed[kwargs['motorid']],kwargs['dir']]
            #printarrays
            #CRunning Process untuk Scroll Mode
            if kwargs['motorid'] == 1:
                self.CRunningProcess2([arrays],starter=True,ending=True)
            else:
                self.CRunningProcess2([arrays])


    def CCalculate(self, type, mode, **kwargs):
        #Calculate for Slider AND Spinner
        if type == 'SPIN-SLIDER':

            #GET FROM SPIN TO SLIDER
            if mode == 1:
                min = kwargs['min']
                max = (float(kwargs['max'])) / float(kwargs['inc']) #- float(kwargs['min'])
                incplus = kwargs['inc']
                #printmax
                return({'min':min,'max':max,'incplus':incplus})

            #SET VALUE SLIDER FROM SPIN
            elif mode == 3:
                value = kwargs['value'] * kwargs['inc']
                #printvalue
                return(value)

            #SET VALUE SPIN FROM SLIDER
            elif mode == 2 :
                value = kwargs['value'] / kwargs['inc']
                #printvalue
                return(value)

    def CPulseCalculate(self, mode, val, motorid, dir, **kwargs):
        # == ZERO BASED ==
        if mode == 1:
            # == ZERO BASED NOW
            now = self.CNows(2, need=motorid)

            if motorid in self.Non_IncrementalMotor:
                return ([int(val), int(dir)])

            #INT INTENSIFIES
            val = int(val)

            if now == None:
                now = 0
            if val != 0:
                hasil = int(val) - int(now)
            else:
                hasil = int(now) * (-1)

            truehasil = hasil

            #To Make Sure always positive
            if hasil < 0:
                hasil = hasil * int(-1)
                dirc = 0
            else:
                dirc = 1

            print 'SUDUT ['+str(motorid)+'] ' + str(now) + ' <+>' + str(dirc) + ' <+> ' +str(truehasil)
            return ([int(hasil),int(dirc)])

        # == REAL BASED ==
        # CALCULATE SUDUT NEEDED FOR REACHING ZERO POSITION
        elif mode == 2:
            try:
                #== REAL NOW ==
                now = self.CNows(8, need=motorid)
            except Exception as e:
                now = 0

            #CHECK DICTIONARY EXISTANCE
            try:
                self.vZero_Coordinate
            except Exception as e:
                self.vZero_Coordinate = self.CZeroCoordinate(2)

            #Only for filtering it was zero coordinate motor or not
            if self.vZero_Coordinate.get(motorid) != None:
                val = int(val)

                if now == None:
                    now = 0
                if val != 0:
                    hasil = int(val) - int(now)
                else:
                    hasil = int(now) * (-1)

                truehasil = hasil

                # To Make Sure always positive
                if hasil < 0:
                    hasil = hasil * int(-1)
                    dirc = 0
                else:
                    dirc = 1
            #IF MOTOR NOT EXIST IN ZERO MOVEMENT
            else:
                #DO NOTHING
                return ([int(0),int(1)])

            return ([int(hasil),int(dirc)])





    def CDefineStep(self, mode, pulsestep):
        if mode == 1:
            try:
                step = int(pulsestep)
            except Exception as e:
                print (e)
                return (None)
            else:
                if step < 0:
                    dir = 0
                    # Neutralizing step
                    step = step * -1
                elif step > 0:
                    dir = 1
                else:
                    dir = 1

                return ([step,dir])

    def CNows(self, mode, **kwargs):

        # == ZERO BASED ==
        #SET WITH PLUS MINUS METHOD
        if mode == 1:
            if kwargs['type'] == 'value':
                if kwargs['motor'] == 1:
                    if self.Now.get(1) == None:
                        self.Now.update({1:self.CNowsCalculate(1,1,kwargs['value'],kwargs['direction'])})
                    else:
                        self.Now[1] = self.CNowsCalculate(1,1,kwargs['value'],kwargs['direction'])

                elif kwargs['motor'] == 2:
                    if self.Now.get(2) == None:
                        self.Now.update({2:self.CNowsCalculate(1,2,kwargs['value'],kwargs['direction'])})
                    else:
                        self.Now[2] = self.CNowsCalculate(1,2,kwargs['value'],kwargs['direction'])

                elif kwargs['motor'] == 3:
                    if self.Now.get(3) == None:
                        self.Now.update({3:self.CNowsCalculate(1,3,kwargs['value'],kwargs['direction'])})
                    else:
                        self.Now[3] = self.CNowsCalculate(1,3,kwargs['value'],kwargs['direction'])

                elif kwargs['motor'] == 4:
                    if self.Now.get(4) == None:
                        self.Now.update({4:self.CNowsCalculate(1,4,kwargs['value'],kwargs['direction'])})
                    else:
                        self.Now[4] = self.CNowsCalculate(1,4,kwargs['value'],kwargs['direction'])

                elif kwargs['motor'] == 5:
                    if self.Now.get(5) == None:
                        self.Now.update({5:kwargs['value']})
                    else:
                        self.Now[5] = kwargs['value']

                elif kwargs['motor'] == 6:
                    if self.Now.get(6) == None:
                        self.Now.update({6:kwargs['value']})
                    else:
                        self.Now[6] = kwargs['value']

            elif kwargs['type'] == 'speed':
                if kwargs['motor'] == 1:
                    if self.Speed.get(1) == None:
                        self.Speed.update({1: kwargs['speed']})
                    else:
                        self.Speed[1] = kwargs['speed']

                elif kwargs['motor'] == 2:
                    if self.Speed.get(2) == None:
                        self.Speed.update({2: kwargs['speed']})
                    else:
                        self.Speed[2] = kwargs['speed']

                elif kwargs['motor'] == 3:
                    if self.Speed.get(3) == None:
                        self.Speed.update({3: kwargs['speed']})
                    else:
                        self.Speed[3] = kwargs['speed']

                elif kwargs['motor'] == 4:
                    if self.Speed.get(4) == None:
                        self.Speed.update({4: kwargs['speed']})
                    else:
                        self.Speed[4] = kwargs['speed']

                elif kwargs['motor'] == 5:
                    if kwargs['speed'] == 0:
                        kwargs['speed'] = 1
                    if self.Speed.get(5) == None:
                        self.Speed.update({5: kwargs['speed']})
                    else:
                        self.Speed[5] = kwargs['speed']

        # == ZERO BASED ==
        #GET Value
        elif mode == 2:
            if self.Now.get(kwargs['need']) != None :
                return(self.Now[kwargs['need']])
            else:
                print '>>>>>>' + str(kwargs['need'])
                return (0)

        # == ZERO BASED ==O
        #Starter
        elif mode == 3:
            self.Now = {1:0,2:0,3:0,4:0,5:0,6:0}

        # == ZERO BASED ==
        #Get Speed
        elif mode == 4:
            if self.Speed.get(kwargs['need']) != None :
                return(self.Speed[kwargs['need']])
            else:
                return (None)
        # == ZERO BASED ==
        #Set Value
        elif mode == 5:
            if self.Now.get(kwargs['motor']) == None:
                self.Now.update({kwargs['motor']:kwargs['value']})
            else:
                self.Now[kwargs['motor']] = kwargs['value']

        # == REAL ==
        #STARTER
        elif mode == 6:
            self.RealNow = {}

        # == REAL ==
        #SET REAL
        elif mode == 7:
            if kwargs['type'] == 'value':
                if kwargs['motor'] == 1:
                    if self.RealNow.get(1) == None:
                        self.RealNow.update({1: self.CNowsCalculate(2, 1, kwargs['value'], kwargs['direction'])})
                    else:
                        self.RealNow[1] = self.CNowsCalculate(2, 1, kwargs['value'], kwargs['direction'])

                elif kwargs['motor'] == 2:
                    if self.RealNow.get(2) == None:
                        self.RealNow.update({2: self.CNowsCalculate(2, 2, kwargs['value'], kwargs['direction'])})
                    else:
                        self.RealNow[2] = self.CNowsCalculate(2, 2, kwargs['value'], kwargs['direction'])

                elif kwargs['motor'] == 3:
                    if self.RealNow.get(3) == None:
                        self.RealNow.update({3: self.CNowsCalculate(2, 3, kwargs['value'], kwargs['direction'])})
                    else:
                        self.RealNow[3] = self.CNowsCalculate(2, 3, kwargs['value'], kwargs['direction'])

                elif kwargs['motor'] == 4:
                    if self.RealNow.get(4) == None:
                        self.RealNow.update({4: self.CNowsCalculate(2, 4, kwargs['value'], kwargs['direction'])})
                    else:
                        self.RealNow[4] = self.CNowsCalculate(2, 4, kwargs['value'], kwargs['direction'])

                elif kwargs['motor'] == 5:
                    if self.RealNow.get(5) == None:
                        self.RealNow.update({5: kwargs['value']})
                    else:
                        self.RealNow[5] = kwargs['value']

                elif kwargs['motor'] == 6:
                    if self.RealNow.get(6) == None:
                        self.RealNow.update({6: kwargs['value']})
                    else:
                        self.RealNow[6] = kwargs['value']

        # == REAL BASED ==
        # GET Value
        elif mode == 8:
            if self.RealNow.get(kwargs['need']) != None:
                return (self.RealNow[kwargs['need']])
            else:
                print '>>>>>>' + str(kwargs['need'])
                return (0)

    def CNowsZero(self, data):
        #SET MOTOR IN ZERO Movement TO 0 Nows
        for keys in data:
            try:
                #Check if exist in Now
                value = self.Now[keys]
            except Exception as e:
                pass
            else:
                self.Now[keys] = 0



    def CNowsCalculate(self,mode,motor,val,direction):
        #AFTER ZERO
        if mode == 1:
            now = self.CNows(2, need=int(motor))
            if int(direction) == 1:
                val = val * 1
            elif int(direction) == 0:
                val = val * (-1)
            result = now + val
            return result
        #REAL
        elif mode == 2:
            now = self.CNows(8, need=int(motor))
            if int(direction) == 1:
                val = val * 1
            elif int(direction) == 0:
                val = val * (-1)
            result = now + val
            return result

    def CZeroCalculate(self, mode, motorid, **kwargs):
        #CALCULATE FOR CNows
        if mode == 1:
            try:
                self.Zero_Coordinate = {}
            except Exception as e:
                pass
            else:
                val_now = self.CNows(2, need=int(motorid))
                val_zero = self.CGetZeroCoordinate(1,motorid)
                val_go = kwargs['valuego']
                val_must = float(val_now) + float(val_zero) + float(val_go)
                return (val_must)

    def CGetZeroCoordinate(self, mode, motorid):
        #DECLARE
        if mode == 1:
            try:
                val = self.vZero_Coordinate[motorid]
            except Exception as e:
                return (0)
            else:
                return (val)

    def CNowsConvert(self, mode, **kwargs):
        #PulseStep to Axis
        if mode == 1:
            #Validasi
            try:
                Axis = int(kwargs['Axis'])
            except Exception as e:
                print (e)
                return (None)
            else:
                SudutMotor = Rumus.Rumus.RumusSudutMotor('wSudutMotor',PulseStepMotor=kwargs['PulseStepMotor'],MicroStepDriver=kwargs['MicroStepDriver'])

                print SudutMotor

                if SudutMotor == None:
                    return (None)

                SudutAxis = Rumus.Rumus.RumusSudutAxis('wSudutAxis',SudutMotor=SudutMotor,PerbandinganGear=self.Perbandingan_Gear[Axis])

                print SudutAxis

                if SudutAxis == None:
                    return (None)

                return (SudutAxis)

        #Axis To Step
        elif mode == 2:
            # Validasi
            try:
                Axis = int(kwargs['Axis'])
            except Exception as e:
                print (e)
                return (None)
            else:
                SudutMotor = Rumus.Rumus.RumusSudutAxis('wSudutMotor', PerbandinganGear=self.Perbandingan_Gear[Axis],
                                                         SudutAxis=kwargs['SudutAxis'])

                print SudutMotor

                if SudutMotor == None:
                    return (None)

                PulseStep = Rumus.Rumus.RumusSudutMotor('wPulseStepMotor', SudutMotor=SudutMotor,
                                                       MicroStepDriver=kwargs['MicroStepDriver'])

                print PulseStep

                if PulseStep == None:
                    return (None)
                print PulseStep
                return (PulseStep)

    def CGetAccel(self, mode, pulse, microstep, time):
        #Get Accel
        if mode == 1:
            try:
                Accel = self.CRumusAccel(int(pulse),microstep,time)
                # print Accel
            except Exception as e:
                print (e)
                return
            else:
                return (Accel)

    def CGetWaktu(self, mode, pulsestep, speed, microstepdriver):
        #Get Accel
        if mode == 1:
            try:
                Waktu = Rumus.Rumus.RumusMenghitungWaktu(pulsestep, speed, microstepdriver)
            except Exception as e:
                print (e)
                return
            else:
                return (Waktu)

    def CGetSpeedAxis(self, mode, **kwargs):
        if mode == 1:
            pass


    def CCommandListing(self, mode):
        if mode == 1:
            Command_Dict = {}
            #ToDo : GetListData From SQL Based From Group dan Type Command Generated From CommandID

            #for row in data:
                #Command_Dict.update({type:command})

    def CReadAINO(self, mode, board, feedback):
        print("READAINO=======================")

        #MOVE
        if mode == 1:
            FLAG = feedback
            print FLAG
            self.timesoon = self.CCurTime()
            self.Board_Reading_Flag[board] = FLAG
            self.Board_Reading[board] = "ON"

        #HOME
        elif mode == 2:
            FLAG = feedback
            print FLAG
            self.timesoon = self.CCurTime()
            self.Board_Reading_Flag[board] = FLAG
            self.Board_Reading[board] = "ON"

        while self.Board_Reading[board] == "ON":
            pass

        print "FeedBack Read Done"
        self.Board_Reading_Flag[board] = ""

        if board == 1:
            return (self.Board1_Reading_Result)

    def CPrintDebug(self, mode, **kwargs):
        #Normal Debuging mode (print)
        if mode == 1:
            if self.ISDebug:
                print('DEBUG ' + str(kwargs['type']) + ' : ' + str(kwargs['message']))

        #Logging Debugging mode
        elif mode == 2:
            if self.ISDebug:
                kwargs['object'].debug(kwargs['message'])

        elif mode == 3:
            kwargs['object'].debug(kwargs['message'])

    def CSearchAndCount(self, text, searchword, **kwargs):
        if kwargs.get('start') == None or kwargs['start'] in ('', None):
            starts = 0
            ends = len(text)
        else:
            starts = kwargs['start']
            ends = kwargs['end']
        text = str(text)
        count = text.count(searchword, int(starts), int(ends))

        if kwargs['replace']:
            for i in range(count):
                text = text.replace(str(searchword), str(int(kwargs['array'][i])), 1)
            return (text)
        else:
            return (count)

    #FOR SCROLL Command
    def CRunningProcess2(self,arraydata, **kwargs):
        commandlists = []
        feedbacklists = []


        self.Arraynows = []
        for data in arraydata:
            motorid = data[1]
            sudut = data[2]
            speed = data[3]
            dir = data[4]

            #CHECK IF IT NEED ACTIVATION
            try:
                int(motorid) in self.Need_Activation
            except Exception:
                need_active = False
            else:
                need_active = True


            # GET THE DEL COMMAND For Axis_0
            try:
                kwargs['starter']
            except Exception as e:
                print e
            else:
                if kwargs['starter'] == True:
                    commandlists.append({1: 'DEL'})
                    feedbacklists.append(str('Deleted'))

            #NEED ACTIVE COMMAND
            if need_active == True:
                #if self.Constant_ActivationCmd == True
                command_active = self.CSearchAndCount(self.Activation_Cmd[int(motorid)], '[+]', replace=True,
                                               array=[1])
                commandlists.append({1: command_active})
                feedbacklists.append(str('Motor6_on'))


            #Axis 0
            if int(motorid) == 1:
                valuescal = self.CPulseCalculate(1,sudut, motorid, dir)
                sudut = valuescal[0]
                dirc = valuescal[1]
                # Generatecommand
                commanddata = self.CLoadConstantCommand('NORMAL', motorid)
            else:
                # Generatecommand
                commanddata = self.CLoadConstantCommand('SCROLL', motorid)


            command =  self.CSearchAndCount(commanddata[0], commanddata[1], replace=True, array=[sudut, speed, dir])

            #To Record Nows
            self.Arraynows.append([motorid, sudut, speed, dir])

            commandlists.append({1:str(command)})
            feedbacklists.append('done')

        try:
            kwargs['ending']
        except Exception as e:
            print e
        else:
            if kwargs['ending'] == True:
                # GET THE ENDING COMMAND
                commandlists.append({1: 'RUN'})
                feedbacklists.append(str('Ready'))

        # NEED DEACTIVE COMMAND
        if need_active == True:
            # if self.Constant_ActivationCmd == True
            command_active = self.CSearchAndCount(self.Activation_Cmd[int(motorid)], '[+]', replace=True,
                                                  array=[0])
            commandlists.append({1: command_active})
            feedbacklists.append(str('Motor6_off'))

        #print(commandlists)
        #print(feedbacklists)

        self.CFastExecutingCommand(commandlists, save=True)

    def CRunningProcess(self,arraydata, **kwargs):
        #DATA FORMAT OF ARRAY
        #[LIST,MOTORID,VAL,SPEED,DIR]

        commandlists = []
        feedbacklists = []
        self.Arraynows = []

        # GET THE DEL COMMAND
        deleting = {}
        deleting = {1: str(self.MGETCommand(3, self.MGETMotor(5, 8)))}
        deletingfeedback = str(self.MGETMotor(6, 8))
        self.Arraynows.append([])
        commandlists.append(copy.deepcopy(deleting))
        feedbacklists.append(copy.deepcopy(deletingfeedback))


        for data in arraydata:
            #print arraydata
            motorid = data[1]
            sudut = data[2]
            speed = data[3]
            dir = data[4]

            #ToDo : Home Check
            #self.CCheckTypesOfMovement(motorid)

            #KONVERSI SUDUT TO STEP
            if motorid in self.Need_ConvertValue:
                #SUDUT CONVERSION
                try:
                    MicroStep = self.Motor_Data[motorid][14]
                except Exception as e:
                    print (e)
                    continue
                else:
                    converted_value = self.CNowsConvert(2, Axis=motorid, SudutAxis=sudut,
                                                        MicroStepDriver=MicroStep)
                sudut = int(converted_value)

            #ACTIVATE IF WANT TO CONSTANT SUDUT METHOD
            valcal = self.CPulseCalculate(1,sudut, motorid, dir)
            sudut = valcal[0]
            dir = valcal[1]

            # CHECK IF IT NEED ACTIVATION
            try:
                data = bool(int(motorid) in self.Need_Activation)
                if data == False:
                    raise Exception
            except Exception:
                need_active = False
            else:
                need_active = True

            # NEED ACTIVE COMMAND
            if need_active == True:
                # if self.Constant_ActivationCmd == True
                print self.Activation_Cmd
                print motorid
                command_active = self.CSearchAndCount(self.Activation_Cmd[int(motorid)][0], self.Activation_Cmd[int(motorid)][1],
                                                      replace=True,
                                                      array=[1])
                commandlists.append({1: command_active})
                feedbacklists.append(str('Motor6_on'))

            data = self.CGenerateCommand(3,arraydata,motorid=motorid,value=sudut,speed=speed,dir=dir)
            self.Arraynows.append([motorid,sudut,speed,dir])

            #printdata

            command = data[0]
            feedback = data[1]
            commandlists.append(command)
            feedbacklists.append(copy.deepcopy(feedback))

        # GET THE ENDING COMMAND
        ending = {1: str(self.MGETCommand(3, self.MGETMotor(5, 7)))}
        endingfeedback = str(self.MGETMotor(6, 7))
        self.Arraynows.append([])
        commandlists.append(copy.deepcopy(ending))
        feedbacklists.append(copy.deepcopy(endingfeedback))

        # NEED ACTIVE COMMAND
        if need_active == True:
            # if self.Constant_ActivationCmd == True
            command_deactive = self.CSearchAndCount(self.Activation_Cmd[int(motorid)][0], self.Activation_Cmd[int(motorid)][1],
                                                    replace=True,
                                                  array=[0])
            commandlists.append({1: command_deactive})
            feedbacklists.append(str('Motor6_off'))

        print commandlists
        print feedbacklists

        self.CExecutingCommand(commandlists, feedbacklists, save=True)

    def CRunningZero(self,arraydata, **kwargs):
        #DATA FORMAT OF ARRAY
        #[LIST,MOTORID,VAL,SPEED,DIR]

        commandlists = []
        feedbacklists = []
        self.Arraynows = []

        # GET THE DEL COMMAND
        deleting = {}
        deleting = {1: str(self.MGETCommand(3, self.MGETMotor(5, 8)))}
        deletingfeedback = str(self.MGETMotor(6, 8))
        self.Arraynows.append([])
        commandlists.append(copy.deepcopy(deleting))
        feedbacklists.append(copy.deepcopy(deletingfeedback))


        for data in arraydata:
            #print arraydata
            motorid = data[1]
            sudut = data[2]
            speed = data[3]
            dir = data[4]

            if motorid in self.Need_ConvertValue:
                #SUDUT CONVERSION
                try:
                    MicroStep = self.Motor_Data[motorid][14]
                except Exception as e:
                    print (e)
                    continue
                else:
                    converted_value = self.CNowsConvert(2, Axis=motorid, SudutAxis=sudut,
                                                        MicroStepDriver=MicroStep)
                sudut = int(converted_value)

            #ACTIVATE IF WANT TO CONSTANT SUDUT METHOD
            # == REAL BASED == FOR ZERO MOVEMENT
            valcal = self.CPulseCalculate(2, sudut, motorid, dir)
            sudut = valcal[0]
            dir = valcal[1]

            # CHECK IF IT NEED ACTIVATION
            try:
                data = bool(int(motorid) in self.Need_Activation)
                if data == False:
                    raise Exception
            except Exception:
                need_active = False
            else:
                need_active = True

            # NEED ACTIVE COMMAND
            if need_active == True:
                # if self.Constant_ActivationCmd == True
                print self.Activation_Cmd
                print motorid
                command_active = self.CSearchAndCount(self.Activation_Cmd[int(motorid)][0], self.Activation_Cmd[int(motorid)][1],
                                                      replace=True,
                                                      array=[1])
                commandlists.append({1: command_active})
                feedbacklists.append(str('Motor6_on'))

            data = self.CGenerateCommand(3,arraydata,motorid=motorid,value=sudut,speed=speed,dir=dir)
            self.Arraynows.append([motorid,sudut,speed,dir])

            #printdata

            command = data[0]
            feedback = data[1]
            commandlists.append(command)
            feedbacklists.append(copy.deepcopy(feedback))

        # GET THE ENDING COMMAND
        ending = {1: str(self.MGETCommand(3, self.MGETMotor(5, 7)))}
        endingfeedback = str(self.MGETMotor(6, 7))
        self.Arraynows.append([])
        commandlists.append(copy.deepcopy(ending))
        feedbacklists.append(copy.deepcopy(endingfeedback))

        # NEED ACTIVE COMMAND
        if need_active == True:
            # if self.Constant_ActivationCmd == True
            command_deactive = self.CSearchAndCount(self.Activation_Cmd[int(motorid)][0], self.Activation_Cmd[int(motorid)][1],
                                                    replace=True,
                                                  array=[0])
            commandlists.append({1: command_deactive})
            feedbacklists.append(str('Motor6_off'))

        print commandlists
        print feedbacklists

        self.CExecutingCommand(commandlists, feedbacklists, save=True, isZero= True)



    def CExecutingCommand(self,arraycommand, arrayfeedback, **kwargs):
        print ' >>+>> ' + str([x for x in arraycommand])
        print ' <<-<< ' + str([x for x in arrayfeedback])

        try:
            float(kwargs['timedelay'])
        except Exception:
            time.sleep(1)
        else:
            time.sleep(float(kwargs['timedelay']))
        self.StartTime = self.CCurTime()
        for lists in arraycommand:
            for board in lists:
                serial = self.Serial_List[board]
                try:
                    data = str(lists[board])
                    if ('\r' not in data) == True and ('\n' not in data) == True:
                        data += '\r'
                    data = data.encode()
                    serial.write(data)
                except Exception as e:
                    self.CPrintDebug(2, object=self.Logger_List['Serial-Log'],
                                     message='[WriteCommand]-' + str(lists[board]) + '-error-' +str(e))
                else:
                    self.CPrintDebug(2, object=self.Logger_List['Serial-Log'],
                                     message='[WriteCommand]-' + str(lists[board]) + '-success')

                    if self.CurrForm == 'Process':
                        count = self.Dv_Table2.GetItemCount()
                        if count >= 100:
                            #ToDo : Get And Save To Text
                            self.Dv_Table2.DeleteAllItems()

                    if self.CReadAINO(1,board,arrayfeedback[arraycommand.index(lists)]) == 'SUCCESS':
                        try:
                            isZero = kwargs.get('isZero')
                        except Exception as e:
                            isZero = False

                        #SAVING CURRENT SUDUT
                        try:
                            item = self.Arraynows[arraycommand.index(lists)]
                            #IF LEN 0
                            if len(item) == 0:
                                raise Exception
                        except Exception as e:
                            pass
                        else:
                            #REAL CNOWS
                            # value
                            self.CNows(1, type='value', motor=item[0], value=item[1], direction=item[3])
                            # speed
                            self.CNows(1, type='speed', motor=item[0], speed=item[2])

                            if isZero:
                                #SET TO ZERROOO
                                self.CZeroCoordinate(3)

                            #AFTER ZERO CNOWS
                            # value
                            self.CNows(7, type='value', motor=item[0], value=item[1], direction=item[3])


        self.EndTime = self.CCurTime()



    def CFastExecutingCommand(self,arraycommand, **kwargs):
        print ' >>> ' + str([x for x in arraycommand])
        try:
            float(kwargs['timedelay'])
        except Exception:
            pass
        else:
            time.sleep(float(kwargs['timedelay']))
        for lists in arraycommand:
            for board in lists:
                serial = self.Serial_List[board]
                try:
                    data = str(lists[board])
                    if ('\r' not in data) == True and ('\n' not in data) == True:
                        data +=  '\r'
                    data = data.encode()
                    serial.write(data)
                    #time.sleep(1)
                except Exception as e:
                    print e
                    self.CPrintDebug(3, object=self.Logger_List['Serial-Log'],
                                     message='[WriteCommand]-' + str(lists[board]) + '-error-' +str(e))
                else:
                    print data
                    self.CPrintDebug(3, object=self.Logger_List['Serial-Log'],
                                     message='[WriteCommand]-' + str(lists[board]) + '-success')
                    try:
                        count = len(self.Arraynows)
                        if count == 0:
                            raise Exception
                    except Exception as e:
                        print e
                    else:
                        try:
                            item = self.Arraynows[arraycommand.index(lists)]
                            if len(item) == 0:
                                raise Exception
                        except Exception as e:
                            pass
                        else:
                            # value
                            self.CNows(1, type='value', motor=item[0], value=item[1], direction=item[3])
                            # speed
                            self.CNows(1, type='speed', motor=item[0], speed=item[2])



    def CGenerateCommand(self, mode, arraymotor, **kwargs):
        if mode == 1:
            CommandList = {0:'M1=[+];S1=[+];D1=[+]',
                           1: 'M2=[+];S2=[+];D2=[+]',
                           2: 'M3=[+];S3=[+];D3=[+]',
                           3: 'M4=[+];S4=[+];D4=[+]',
                           'End':'RUN'}

            marker = '[+]'
            ResultCommand = {}
            for motor in arraymotor:
                if str(motor).isdigit():
                    data = arraymotor[arraymotor.index(motor)]
                    result = self.CSearchAndCount(CommandList[command], marker, replace=True, array=[data['value'], data['speed'], data['direction']])
                ResultCommand.update({motor:result})

        elif mode == 2: #CRunningProcess(self,arraydata)
            hasil = []
            lists = 10
            for motorid in arraymotor:
                container = []
                data = arraymotor[motorid]

                #List
                container.append(lists)
                lists += 10

                #MOTOR ID
                container.append(motorid)
                if motorid == 5:
                    print data

                if data.get('value') != None:
                    valu = data['value']
                else:
                    value = 0
                container.append(valu)

                if data.get('speed') != None:
                    spee = data['speed']
                else:
                    spee = 1
                container.append(spee)

                if data.get('direction') != None:
                    dire = data['direction']
                else:
                    dire = 0
                container.append(dire)

                if len(container) <= 1:
                    pass
                else:
                    hasil.append(container)

                #ToDo : ADD RECORD



            self.CRunningProcess(hasil)

        elif mode == 4:
            commandlists = []
            feedbacklists = []

            # GET THE DEL COMMAND
            deleting = {}
            deleting = {1: str(self.MGETCommand(3, self.MGETMotor(5, 8)))}
            deletingfeedback = str(self.MGETMotor(6, 8))
            commandlists.append(copy.deepcopy(deleting))
            feedbacklists.append(copy.deepcopy(deletingfeedback))

            for motorid in arraymotor:
                commandboard = {}
                data = arraymotor[motorid]

                #printdata

                if data.get('value') != None:
                    valu = data['value']
                else:
                    valu = 0

                if data.get('speed') != None:
                    spee = data['speed']
                else:
                    spee = 0

                if data.get('direction') != None:
                    dire = data['direction']
                else:
                    dire = 0

                #GET COMMAND
                commandset = self.MGenerateCommand(1,motorid,valu,spee,dire)



                #GET FEEDBACK
                feedbackset = self.MGETMotor(6,motorid)
                if (feedbackset in ("",None)) == True:
                    feedbackset = "-"


                check = self.CCommandCheck(1, commandset ,digits=digit)

                if check == "special_command":
                    cmd_types = check
                else:
                    cmd_types = ""

                for i in range(4):
                    if check != "pass":
                        if cmd_types == "special_command":
                            check = self.CCommandCheck(2, commandset)
                            if check != "pass":
                                # ToDo : GetBoardID
                                motorname = self.MGETMotor(1, motorid)

                                digit = self.CGetDigitCmd(int(motorid))
                                if digit == None:
                                    print ("DIGIT COMMMAND ERROR " + str(int(motorid)))
                                    continue

                                commandset = self.CCommandFix(2, check, commandset, value=valu,
                                                              speed=spee, dir=dire,
                                                              motorname=motorname, digits=digit)
                            else:
                                cmd_types = ""
                                break
                        else:
                            check = self.CCommandCheck(1, commandset)
                            if check == "pass":
                                break
                            # ToDo : GetBoardID
                            motorname = self.MGETMotor(1, motorid)

                            digit = self.CGetDigitCmd(int(motorid))
                            if digit == None:
                                print ("DIGIT COMMMAND ERROR " + str(int(motorid)))
                                continue

                            commandset = self.CCommandFix(1, check, commandset, value=valu, speed=spee,
                                                          dir=dire, motorname=motorname, digits=digit)
                            #printcommandset

                    else:
                        commandset = copy.deepcopy(commandset)
                        break


                #commandlist.updata(boardid:commandset)
                commandboard.update({1:copy.deepcopy(commandset)})
                #printcommandboard
                commandlists.append(copy.deepcopy(commandboard))
                feedbacklists.append(copy.deepcopy(feedbackset))

            #GET THE ENDING COMMAND
            ending = {}
            ending = {1:str(self.MGETCommand(3,self.MGETMotor(5,7)))}
            endingfeedback = str(self.MGETMotor(6,7))
            commandlists.append(copy.deepcopy(ending))
            feedbacklists.append(copy.deepcopy(endingfeedback))

            #printcommandlists
            #printfeedbacklists

            self.CExecutingCommand(commandlists,feedbacklists)

        elif mode == 3:

            commandboard = {}
            motorid = kwargs['motorid']
            value = kwargs['value']
            speed = kwargs['speed']
            dirc = kwargs['dir']

            # GET COMMAND
            commandset = self.MGenerateCommand(1, motorid, value, speed, dirc)

            # GET FEEDBACK
            feedbackset = self.MGETMotor(6, motorid)
            if (feedbackset in ("", None)) == True:
                feedbackset = "-"

            digit = self.CGetDigitCmd(int(motorid))

            check = self.CCommandCheck(1, commandset ,digits=digit)
            if check == "special_command":
                cmd_types = check
            elif check == "home_command":
                cmd_types = check
            else:
                cmd_types = ""

            for i in range(4):
                if check != "pass":
                    if cmd_types == "special_command":
                        check = self.CCommandCheck(2, commandset ,digits=digit)
                        if check != "pass":
                            # ToDo : GetBoardID
                            motorname = self.MGETMotor(1, motorid)

                            digit = self.CGetDigitCmd(int(motorid))
                            if digit == None:
                                print ("DIGIT COMMMAND ERROR " + str(int(motorid)))
                                continue
                            commandset = self.CCommandFix(2, check, commandset, value=value,
                                                          speed=speed, dir=dirc,
                                                          motorname=motorname, digits=digit)
                        else:
                            cmd_types = ""
                            break
                    elif cmd_types == 'home_command':
                        commandset = commandset
                    else:
                        check = self.CCommandCheck(1, commandset ,digits=digit)
                        if check == "pass":
                            break
                        # ToDo : GetBoardID
                        motorname = self.MGETMotor(1, motorid)

                        digit = self.CGetDigitCmd(int(motorid))
                        if digit == None:
                            print ("DIGIT COMMMAND ERROR " + str(int(motorid)))
                            continue

                        commandset = self.CCommandFix(1, check, commandset, value=value, speed=speed,
                                                      dir=dirc, motorname=motorname, digits=digit)
                        #printcommandset

                else:
                    commandset = copy.deepcopy(commandset)
                    break


            #ToDo : GET BOARD
            commandboard.update({1: copy.deepcopy(commandset)})
            #printcommandboard
            return ([commandboard,feedbackset])

        elif mode == 5:
            commandboard = {}
            motorid = kwargs['motorid']
            value = kwargs['value']
            speed = kwargs['speed']
            dirc = kwargs['dir']

            # GET COMMAND
            commandset = self.MGenerateCommand(2, motorid, value, speed, dirc , focus=self.NowFocus)
            #printcommandset
            # GET FEEDBACK
            feedbackset = self.MGETMotor(6, motorid)
            if (feedbackset in ("", None)) == True:
                feedbackset = "-"

            check = self.CCommandCheck(3, commandset)

            for i in range(4):
                if check != "pass":
                    check = self.CCommandCheck(3, commandset)
                    if check != "pass":
                        # ToDo : GetBoardID
                        motorname = self.MGETMotor(1, motorid)
                        digit = [3]
                        commandset = self.CCommandFix(3, check, commandset, value=value,
                                                      speed=speed, dir=dirc,
                                                      motorname=motorname, digits=digit)
                    else:
                        break
                else:
                    commandset = copy.deepcopy(commandset)
                    break

            # ToDo : GET BOARD
            commandboard.update({1: copy.deepcopy(commandset)})
            #printcommandboard
            return ([commandboard, feedbackset])

    def CCommandFix(self, mode, error, command, **kwargs):
        self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                         message='[FIXCommand]-' + str(command) + '-' + str(error))
        if mode == 1:
            # PASS IF NOT USED
            try:
                kwargs['digits'][0]
            except Exception as e:
                print 'Val Passed'
                return

            data = command.split(";")

            if error == "error_val":
                data2 = data[0].split("=")
                if len(data2[0]) != 2:
                    self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                     message='[FIXCommand]-ValueIndicator-Wrong')
                elif len(data2[1]) != kwargs['digits'][0]:
                    data2[1] = kwargs['value']
                    lenstr = len(str(kwargs['value']))

                    if lenstr > kwargs['digits'][0]:
                        #ToDo : Error Salah Inputan
                        pass
                    else:
                        digit = kwargs['digits'][0]
                        needzero = digit - int(lenstr)
                        data2[1] = str(needzero * '0') + str(kwargs['value'])

                fix = str(data2[0]) + '=' + str(data2[1])
                result =  str(fix)+';'+str(data[1])+';'+str(data[2])
                return result

            elif error == "error_spd":
                # PASS IF NOT USED
                try:
                    kwargs['digits'][1]
                except Exception as e:
                    print 'Speed Passed'
                    return

                data2 = data[1].split("=")

                if len(data2[0]) != 2:
                    self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                     message='[FIXCommand]-SpeedIndicator-Wrong')
                elif len(data2[1]) != kwargs['digits'][1]:
                    data2[1] = kwargs['speed']
                    lenstr = len(str(kwargs['speed']))
                    #printlenstr

                    if lenstr > kwargs['digits'][1]:
                        # ToDo : Error Salah Inputan
                        pass
                    else:
                        digit = kwargs['digits'][1]
                        needzero = digit - int(lenstr)
                        data2[1] = str(needzero * '0') + str(kwargs['speed'])
                fix = str(data2[0]) + '=' + str(data2[1])
                #printfix

                result = data[0]+';'+str(fix)+';'+data[2]
                #printresult
                return result

            elif error == "error_dir":
                #PASS IF NOT USED
                try:
                    kwargs['digits'][2]
                except Exception as e:
                    print 'Dir Passed'
                    return


                data2 = data[2].split("=")
                if len(data2[0]) != 2:
                    self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                     message='[FIXCommand]-DirectionIndicator-Wrong')
                elif len(data2[1]) != kwargs['digits'][2]:
                    data2[1] = kwargs['dir']
                    lenstr = len(str(kwargs['dir']))

                    if lenstr > kwargs['digits'][2]:
                        # ToDo : Error Salah Inputan
                        pass
                    else:
                        digit = kwargs['digits'][2]
                        needzero = digit - int(lenstr)
                        data2[1] = str(needzero * '0') + str(kwargs['dir'])
                fix = str(data2[0]) + '=' + str(data2[1])

                result = data[0]+';'+data[1]+';'+str(fix)
                return result

            elif error == "error_all":
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[FIXCommand]-YourCommandIsShiiiieeeettt-VeryWrongDude')
                pass

        #FOR SPECIAL COMMAND
        elif mode == 2:
            #printcommand

            # PASS IF NOT USED
            try:
                kwargs['digits'][0]
            except Exception as e:
                print 'Val Passed'
                return

            data = command.split(";")
            longdata = len(data)

            if error == "error_val":
                data2 = data[0].split("=")
                if len(data2[0]) != 2:
                    self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                     message='[FIXCommand]-ValueIndicator-Wrong')
                elif len(data2[1]) != kwargs['digits'][0]:
                    data2[1] = kwargs['value']
                    lenstr = len(str(kwargs['value']))

                    if lenstr > kwargs['digits'][0]:
                        # ToDo : Error Salah Inputan
                        pass
                    else:
                        digit = kwargs['digits'][0]
                        needzero = digit - int(lenstr)
                        data2[1] = str(needzero * '0') + str(kwargs['value'])

                fix = str(data2[0]) + '=' + str(data2[1])

                if longdata == 3:
                    result = str(fix) + ';' + str(data[1]) + ';' + str(data[2])
                elif longdata == 2:
                    result = str(fix) + ';' + str(data[1])
                elif longdata == 1:
                    result = str(fix)


                #print'---'
                #printresult
                #print'---'
                return result

            elif error == "error_spd":
                # PASS IF NOT USED
                try:
                    kwargs['digits'][1]
                except Exception as e:
                    print 'Speed Passed'
                    return

                data2 = data[1].split("=")

                if len(data2[0]) != 2:
                    self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                     message='[FIXCommand]-SpeedIndicator-Wrong')
                elif len(data2[1]) != kwargs['digits'][1]:
                    data2[1] = kwargs['speed']
                    lenstr = len(str(kwargs['speed']))
                    #printlenstr

                    if lenstr > kwargs['digits'][1]:
                        # ToDo : Error Salah Inputan
                        pass
                    else:
                        digit = kwargs['digits'][1]
                        needzero = digit - int(lenstr)
                        data2[1] = str(needzero * '0') + str(kwargs['speed'])
                fix = str(data2[0]) + '=' + str(data2[1])
                #printfix

                if longdata == 3:
                    result = str(data[0])  + ';' + str(fix) + ';' + str(data[2])
                elif longdata == 2:
                    result = str(data[0]) + ';' + str(fix)
                elif longdata == 1:
                    print 'DA HELL'

                #printresult
                return result

            elif error == "error_dir":
                # PASS IF NOT USED
                try:
                    kwargs['digits'][2]
                except Exception as e:
                    print 'Dir Passed'
                    return

                data2 = data[2].split("=")
                if len(data2[0]) != 2:
                    self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                     message='[FIXCommand]-DirectionIndicator-Wrong')
                elif len(data2[1]) != kwargs['digits'][2]:
                    data2[1] = kwargs['dir']
                    lenstr = len(str(kwargs['dir']))

                    if lenstr > kwargs['digits'][2]:
                        # ToDo : Error Salah Inputan
                        pass
                    else:
                        digit = kwargs['digits'][2]
                        needzero = digit - int(lenstr)
                        data2[1] = str(needzero * '0') + str(kwargs['dir'])
                fix = str(data2[0]) + '=' + str(data2[1])

                if longdata == 3:
                    result = str(data[0])  + ';' + str(fix) + ';' + str(data[2])
                elif longdata == 2:
                    print 'NIBBA'
                elif longdata == 1:
                    print 'DA HELL'

                return result

            elif error == "error_all":
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[FIXCommand]-YourCommandIsShiiiieeeettt-VeryWrongDude')
                pass

        # FOR SCROLL COMMAND
        elif mode == 3:
            # PASS IF NOT USED
            try:
                kwargs['digits'][0]
            except Exception as e:
                print 'Val Passed'
                return

            data = command.split(";")

            if error == "error_val":
                data2 = data[2]
                if len(data2) != int(kwargs['digits'][0]):
                    data2 = kwargs['value']
                    lenstr = len(str(kwargs['value']))

                    if lenstr > int(kwargs['digits'][0]):
                        # ToDo : Error Salah Inputan
                        pass
                    else:
                        digit = kwargs['digits'][0]
                        needzero = digit - int(lenstr)
                        data2 = str(needzero * '0') + str(kwargs['value'])

                fix = str(data2)
                result = str(data[0]) + ';' + str(data[1]) + ';' + str(fix)
                #print'---'
                #printresult
                #print'---'
                return result



    def CCommandCheck(self, mode, command, **kwargs):
        #For First Check
        if mode == 1:
            try:
                data = str(command).split(";")
                print data
                print command
            except Exception as e:
                print e
                if ('[+]') not in str(command) and len(str(command)) == 3:
                    return ("home_command")
                print 'error_all'
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                     message='[CheckCommand]-'+str(command)+'-error_all')
                return ("error_all")

            if ('[+]') not in command and len(command) == 3:
                return ("home_command")

            if len(data) != 3:
                return ("special_command")

            #if len(data[0]) != 7:
            data1 = data[0].split('=')
            data2 = data[1].split('=')
            data3 = data[2].split('=')

            if len(data1[1]) != kwargs['digits'][0]:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[CheckCommand]-' + str(command) + '-error_val')
                return ("error_val")
            #elif len(data[1]) != 7:
            elif len(data2[1]) != kwargs['digits'][1]:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[CheckCommand]-' + str(command) + '-error_spd')
                return ("error_spd")
            #elif len(data[2]) != 4:
            elif len(data3[1]) != kwargs['digits'][2]:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[CheckCommand]-' + str(command) + '-error_dir')
                return ("error_dir")
            else:
                return("pass")

        #For Special Command
        elif mode == 2:
            #ToDo : Get Spliter
            data = command.split(";")
            #printdata
            if len(data) == 1:
                types = 1
            elif len(data) == 2:
                types = 2

            if types == 1:
                if len(data[0]) != 4:
                    self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                     message='[CheckCommand]-' + str(command) + '-error_val')
                    return ("error_val")
                else:
                    return ("pass")

            elif types == 2:
                if len(data[0]) != 6:
                    self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                     message='[CheckCommand]-' + str(command) + '-error_val')
                    return ("error_val")
                elif len(data[1]) != 6:
                    self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                     message='[CheckCommand]-' + str(command) + '-error_spd')
                    return ("error_spd")
                else:
                    return ("pass")

        #For Scroll Command
        elif mode == 3:
            try:
                data = command.split(';')
            except Exception as e:
                print e
            else:
                part1 = data[0]
                part2 = data[1]
                part3 = data[2]

                if len(part3) != 3:
                    return ("error_val")
                else:
                    return ("pass")

    def CScrollDelay(self, timeout):
        #===============================================================
        detected = True
        while self.Detect_Start == True:

            #UPDATEING Last Post
            self.CGETCurrValue(1, self.NowFocus)
            self.Detect_LastPos = int(self.PositionMust[self.NowFocus])

            if self.Detect_LastPos == self.Detect_Checkpoint:
                if detected == True:
                    detect_start = self.CCurTime(datetime=True)
                    detected = False

                #Time save
                detect_now = self.CCurTime(datetime=True)
                detect_passed = detect_now - detect_start

                #If Over The limit time
                if float(detect_passed.total_seconds()) > float(timeout):
                    self.Detect_Start = False
                    print 'Detect Done ' + str(float(detect_passed.total_seconds()))
                else:
                    pass
            else:
                detect_start = self.CCurTime(datetime=True)
                self.Detect_Checkpoint = self.Detect_LastPos
        # ===============================================================

    def CPause(self, timesleep):
        time.sleep(timesleep)

    def CGetDigitCmd(self,id):
        try:
            digit = self.Digit_Command[int(id)]
        except Exception as e:
            print (e)
            return (None)
        else:
            return (digit)

    def CFilterString(self, mode, string, **kwargs):
        #remove string
        if mode == 1:
            try:
                blacklist= kwargs['remove']
            except Exception as e:
                print (e)
                return
            else:
                container = ''
                for word in string:
                    if word in blacklist:
                        continue
                    container += word
                return (container)

    def CZeroCoordinate(self, mode):
        #Running Zero
        if mode == 1:
            try:
                self.Running_Data
            except Exception as e:
                # ToDo = Zero
                self.Running_Data = [[True, 'ZERO']]
                #self.Running_Data = [[True,'ZERO']]
            self.Event_Type = "RunZero"
            self.Executing_Event = "ON"

        #Return Dict Of Zero Coordinate
        elif mode == 2:
            #ToDo = Zero
            self.Zero_ID = 239
            data = self.MGETSudutDetailSet(1, headerid=self.Zero_ID)

            if len(data) == 0 or data == None:
                return
            else:
                container = {}
                for item in data:
                    id = int(item[1])
                    val = item[2]
                    dir = item[4]

                    #Calculate Val based on Direction
                    if int(dir) == 1:
                        val = float(val) * 1
                    elif int(dir) == 0:
                        val = float(val) * -1
                    container.update({id:val})

                return (container)
            pass

        #Set Zero Coordinate Motor TO 0
        #COMMONLY USED AFTER EXECUTE ZERO MOVEMENT
        elif mode == 3:
            try:
                self.vZero_Coordinate
            except Exception as e:
                self.vZero_Coordinate = self.CZeroCoordinate(2)
            self.CNowsZero(self.vZero_Coordinate)

    def CCheckTypesOfMovement(self, motor):
        pass






