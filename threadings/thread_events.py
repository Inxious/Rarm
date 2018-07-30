
import wx



class ThreadEvents():
    def __init__(self):
        self.Executing_Event = "OFF"
        self.Trans_Record = True

        while True:
            if self.Executing_Event == "ON":

                if self.Event_Type == "Process":
                    self.CGenerateCommand(2, self.DataCommand_Raw)

                    #if dene
                    #print 'PROCESS DONE'
                    self.Cmd_Mnl_GoByClick.Enable()
                    self.Executing_Event = "OFF"


                elif self.Event_Type == "RunProcess1":
                    result = []
                    ints = 0
                    for item in self.Running_Data:
                        datapack = []

                        if item[0] == True:
                            name = item[1]
                            id = self.MGETSudut('HEADER',4,'',name=name)
                            #print id
                            try:
                                id = int(id)
                            except Exception:
                                id = id[0]
                            datapack = self.MGETSudut('DETAIL', 7, id,trial ='YES')


                            if len(datapack) == 0:
                                print "NO DATA IN " + str(name)

                            if len(datapack) != 1:
                                if  isinstance(datapack,list) == False:
                                    datafinal = []
                                    datafinal.append(item[1])#Motor
                                    datafinal.append(item[2])#Val
                                    datafinal.append(item[3])#Speed
                                    datafinal.append(item[4])#Dir
                                    result.append(datafinal)



                                for data in datapack:
                                    result.append(data)
                            else:
                                result.append(datapack[0])

                            ints += 1


                            if len(result) == 0:
                                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                                 message='[RunMovement]-NO DATA WAS SELECTED' )
                            else:
                                #print '============================='
                                #print 'RUN NUMBER > ' + str(ints)
                                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                                 message='[RunMovement]-'+ str(name) + '-' + str(result))
                                #print '============================='
                                self.CRunningProcess(result)

                                #print 'this is item'
                                #print item
                                #print 'this is item'

                                #SAVE LOG IN M_Transaction
                                #self.Trans_Record = False
                                if self.Trans_Record == True:
                                    for items in result:
                                        starttime = self.CCurTime()
                                        header_id = self.MRecordTransaction('HEADER', 1, name=name,
                                                                                start=starttime, config=items[1])

                                        if header_id != '' and len(str(header_id)) != 0 and header_id != 'FAIL':
                                            self.MRecordTransaction('DETAIL', 1, headerid=header_id, list=items[0], motorid=items[1],
                                                                    start=self.StartTime, end=self.EndTime, orientasi=items[4],
                                                                    value=items[2])

                            result = []

                    # if dene
                    #print 'PROCESS DONE'
                    self.Executing_Event = "OFF"
                    try:
                        self.Cmd_Prc_Process.Enable()
                    except Exception as e:
                        pass

                elif self.Event_Type == "RunZero":
                    result = []
                    ints = 0
                    for item in self.Running_Data:
                        datapack = []

                        if item[0] == True:
                            name = item[1]
                            id = self.MGETSudut('HEADER', 4, '', name=name)
                            # print id
                            try:
                                id = int(id)
                            except Exception:
                                id = id[0]
                            datapack = self.MGETSudut('DETAIL', 7, id, trial='YES')

                            if len(datapack) == 0:
                                print "NO DATA IN " + str(name)

                            if len(datapack) != 1:
                                if isinstance(datapack, list) == False:
                                    datafinal = []
                                    datafinal.append(item[1])  # Motor
                                    datafinal.append(item[2])  # Val
                                    datafinal.append(item[3])  # Speed
                                    datafinal.append(item[4])  # Dir
                                    result.append(datafinal)

                                for data in datapack:
                                    result.append(data)
                            else:
                                result.append(datapack[0])

                            ints += 1

                            if len(result) == 0:
                                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                                 message='[RunMovement]-NO DATA WAS SELECTED')
                            else:
                                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                                 message='[RunMovement]-' + str(name) + '-' + str(result))
                                self.CRunningZero(result)

                                # SAVE LOG IN M_Transaction
                                # self.Trans_Record = False
                                if self.Trans_Record == True:
                                    for items in result:
                                        starttime = self.CCurTime()
                                        header_id = self.MRecordTransaction('HEADER', 1, name=name,
                                                                            start=starttime, config=items[1])

                                        if header_id != '' and len(str(header_id)) != 0 and header_id != 'FAIL':
                                            self.MRecordTransaction('DETAIL', 1, headerid=header_id, list=items[0],
                                                                    motorid=items[1],
                                                                    start=self.StartTime, end=self.EndTime,
                                                                    orientasi=items[4],
                                                                    value=0)

                            result = []

                    # if dene
                    print 'ZERO DONE'
                    self.Executing_Event = "OFF"
                    try:
                        self.Cmd_Prc_Process.Enable()
                    except Exception as e:
                        pass

                    try:
                        self.Cmd_Mnl_ZeroByClick.Enable()
                    except Exception as e:
                        pass


                elif self.Event_Type == 'MnlHoming':
                    command = self.MGenerateCommand(1, 9, '', '', '')
                    feedback = [self.MGETMotor(6, 9)]
                    commandset = [{1: command}]
                    print command
                    print feedback

                    self.CExecutingCommand(commandset, feedback)
                    self.Executing_Event = "OFF"

                elif self.Event_Type == 'MnlMagnet':
                    self.Mnl_Tgl_Magnet.Disable()
                    if self.Magnet_Before == True:
                        self.Mnl_Tgl_Magnet.SetForegroundColour(wx.Colour(0, 255, 0))
                        self.Mnl_Tgl_Magnet.SetLabel('ON')
                        print 'MAG ON'
                        self.CFastExecutingCommand([{1: 'MAG;1'.decode()}])
                    else:
                        self.Mnl_Tgl_Magnet.SetForegroundColour(wx.Colour(255, 0, 0))
                        self.Mnl_Tgl_Magnet.SetLabel('OFF')
                        print 'MAG OFF'
                        self.CFastExecutingCommand([{1: 'MAG;0'.decode()}])
                        self.CPause(1)
                    self.Executing_Event = "OFF"
                    self.Mnl_Tgl_Magnet.Enable()

    # CUSTOMS ====================
    @classmethod
    def PrintS(self,word):
        print (word)


