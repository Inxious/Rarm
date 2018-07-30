

import ConfigParser
import pyodbc
import os,sys


class Model():
    def __init__(self):

        #GET DATA FROM CONFIG FILE
        self.Trusted = self.config.get('Database Configuration', 'Trusted')
        self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                         message='[DBConnection]-TRUSTED CONNECTION-' + str(self.Trusted))
        self.Driver = self.config.get('Database Configuration', 'Driver')
        self.Server = self.config.get('Database Configuration', 'Server')
        self.Database = self.config.get('Database Configuration', 'Database')
        self.Uid = self.config.get('Database Configuration', 'Uid')
        self.Pwd = self.config.get('Database Configuration', 'Pwd')


        if self.Trusted == "yes":
            self.MDBConnect(2, self.Driver, self.Server, self.Database)
        elif self.Trusted == "no":
            self.MDBConnect(1, self.Driver, self.Server, self.Database, uid=self.Uid, pwd=self.Pwd)

    def MDBConnect(self, mode, driver, server, database, **kwargs):
        #NON TRUSTED CONNECTION
        status = ""
        if mode == 1:
            try:
                self.Conn = pyodbc.connect(r"Driver={" + str(driver) + "};" +
                                           r"Server=" + str(server) + ";" +
                                           r"Database=" + str(database) + ";" +
                                           r"uid=" + str(kwargs["uid"]) + ";" +
                                           r"pwd=" + str(kwargs["pwd"]))
            except Exception:
                try:
                    self.Conn = pyodbc.connect(r"Driver={" + str(driver) + "};" +
                                               r"Server=" + str(server) + ";" +
                                               r"Database=" + str(database) + ";" +
                                               r"uid=" + str(kwargs["uid"]) + ";" +
                                               r"pwd=" + str(kwargs["pwd"]))
                except Exception:
                     status = ("KONEKSI GAGAL")

        #TRUSTED CONNECTION
        elif mode == 2:
            try:
                self.Conn = pyodbc.connect(r"Driver={" + str(driver) + "};" +
                                           r"Server=" + str(server) + ";" +
                                           r"Database=" + str(database) + ";" +
                                           r"Trusted_Connection=yes")
            except Exception:
                try:
                    self.Conn = pyodbc.connect(r"Driver={" + str(driver) + "};" +
                                               r"Server=" + str(server) + ";" +
                                               r"Database=" + str(database) + ";" +
                                               r"Trusted_Connection=yes")
                except Exception:
                    status = ("KONEKSI GAGAL")

        if status != "":
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'], message=status)
            raise SystemExit
        else:
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'], message="KONEKSI BERHASIL")
        self.oConn = self.Conn.cursor()

    def MGenerateCommand(self, mode, motorid, value, speed, direction ,**kwargs):
        #Move Command
        if mode == 1:
            #print motorid
            commandid = self.MGETMotor(5,motorid)
            command = self.MGETCommand(3,commandid)
            marker = self.MGETCommand(4,commandid)
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[Model]-GenerateCommand-' + str(commandid) + '/' + str(command) + '/' + str(marker))
            result = self.CSearchAndCount(command, marker, replace=True, array=[value, speed, direction])
            ##print result

            return(result)

        #Scroll Command
        elif mode == 2:
            datacommand = self.MGETManualCommand(1, motorid , group='MANUAL', type='SCROLL' )
            command = datacommand[0]
            marker = datacommand[1]
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[Model]-GenerateCommand-' + str(motorid) + '/' + str(command) + '/' + str(
                                 marker))
            result = self.CSearchAndCount(command, marker, replace=True, array=[kwargs['item']])
            # #print result

            return (result)

    #Versi Fleksible
    def MGenerateCommands(self, mode, motorid, **kwargs):
        if mode == 1:
            datacommand = self.MGETManualCommand(1, motorid, group=kwargs['groupcommand'], type=kwargs['typecommand'])
            command = datacommand[0]
            marker = datacommand[1]
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[Model]-GenerateCommand-' + str(motorid) + '/' + str(command) + '/' + str(
                                 marker))
            #result = self.CSearchAndCount(command, marker, replace=True, array=[value])
            # #print result

            return ([command,marker])


    #GET MOTOR DATA
    def MGETMotor(self, mode, motorid):
        #MODE TO GET MotorID
        if mode == 0:
            pass
        else:
            sSQL = "EXEC SP_Arm_GetMotorData ? , ?"
            Values = [mode, str(motorid)]

            ##print sSQL, Values

            data = self.oConn.execute(sSQL, Values)
            data = [x[0] for x in data.fetchall()]

            if len(data) == 0:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'], message='[SP-Failure]-SP_Arm_GetMotorData-NoDataLoaded')
                self.Conn.commit()
                return (data)

            data = data[0]

            self.Conn.commit()
            return (data)

    #GET ALL MOTOR DATA
    def MGETAllMotorData(self, mode, motorid):
        sSQL = "EXEC SP_Arm_GetAllMotorData ? , ?"
        if mode == 1:
            Values = [mode, int(motorid)]
        elif mode == 2:
            Values = [mode, motorid]

        ##print sSQL, Values

        data = self.oConn.execute(sSQL, Values)
        data = data.fetchall()

        if len(data) == 0:
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[SP-Failure]-SP_Arm_GetAllMotorData-NoDataLoaded')
            self.Conn.commit()
            return (data)
        elif len(data) == 1:
            data = data[0]

        # Wrapping data
        print data
        data_item = [list(x) for x in data]
        data_id = [x[0] for x in data_item]
        print data_id
        container = {data_id[x]: data_item[x] for x in range(len(data_item))}

        self.Conn.commit()
        return (container)


    def MGETCommand(self, mode, commandid):
        if mode == 0:
            pass
        else:
            sSQL = "EXEC SP_Arm_GetCommandData ? , ?"
            Values = [mode, int(commandid)]

            #print sSQL, Values

            data = self.oConn.execute(sSQL, Values)
            data = [x[0] for x in data.fetchall()]

            if len(data) == 0:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[SP-Failure]-SP_Arm_GetCommandData-NoDataLoaded')
                self.Conn.commit()
                return (data)

            data = data[0]

            self.Conn.commit()
            return (data)

    #COMMAND BASED BY GROUP AND TYPE
    def MGETManualCommand(self, mode, motorid,**kwargs):
        #USING NEW METHOD

        if mode == 0:
            pass
        else:
            noCount = " SET NOCOUNT ON; "
            sSQL = "EXEC SP_Arm_GetManualCommand ? , ? , ? , ?"
            Values = [mode, int(motorid), kwargs['group'], kwargs['type']]

            #print sSQL, Values

            data = self.oConn.execute(noCount + sSQL, Values)
            data = data.fetchall()

            if len(data) == 0:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[SP-Failure]-SP_Arm_GetManualCommand-NoDataLoaded')
                self.Conn.commit()
                return (data)

            self.Conn.commit()

            data = data[0]

            return (data)



    def MGETBoard(self , mode, boardid):
        sSQL = "EXEC SP_Arm_GetBoardData ? , ?"
        Values = [mode, str(boardid)]

        ##print sSQL, Values

        data = self.oConn.execute(sSQL, Values)
        data = [x[0] for x in data.fetchall()]

        if len(data) == 0:
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[SP-Failure]-SP_Arm_GetBoardData-NoDataLoaded')
            self.Conn.commit()
            return (data)

        data = data[0]

        self.Conn.commit()
        return (data)

    def MGETSudut(self, type, mode, sudutid, **kwargs):
        sSQL = "EXEC SP_Arm_GetSudutData  ?, ?, ?, ?"
        if kwargs.get('name') == None:
            name = ''
        else:
            name = kwargs['name']
        Values = [type, mode, str(sudutid), name]

        ##print sSQL, Values

        data = self.oConn.execute(sSQL, Values)
        data = data.fetchall()
        ##print data
        data = [x for x in data]

        if len(data) == 0:
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[SP-Failure]-SP_Arm_GetSudutData-NoDataLoaded')
            self.Conn.commit()
            return (data)

        hasil = []
        for item in data:
            change = [x for x in item]
            if len(change) == 1:
                change = change[0]
            hasil.append(change)

        # IF THE DATA WAS NOT ONE
        if kwargs.get('trial') == None:
            if len(hasil) == 1:
                hasil = hasil[0]
                ##print hasil
                if len(str(hasil)) == 1:
                    hasil = str(hasil[0])
                    ##print hasil

        self.Conn.commit()
        return (hasil)


    def MGETKoordinat(self, mode, koordinatid):
        sSQL = "EXEC SP_Arm_GetKoorData ? , ?"
        Values = [mode, str(koordinatid)]

        ##print sSQL, Values

        data = self.oConn.execute(sSQL, Values)
        data = [x[0] for x in data.fetchall()]

        if len(data) == 0:
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[SP-Failure]-SP_Arm_GetKoorData-NoDataLoaded')
            self.Conn.commit()
            return (data)

        ##print data
        ##print "-----------------"
        ##print len(data)
        ##print "-----------------"

        data = data[0]

        self.Conn.commit()
        return (data)

    def MGETConfig(self, types, mode, configid, **kwargs):
        #GET DATA FROM HEADER
        # ATTR = TYPE MODE AT1 AT2
        sSQL = "EXEC SP_Arm_GetConfigData ?, ?, ?, ?"
        if kwargs.get('configname') != None:
            name = kwargs['configname']
        else:
            name = ''

        try:
            configid = int(configid)
        except Exception as e:
            configid = 0

        Values = [types, mode, configid, name]

        ##print sSQL, Values

        data = self.oConn.execute(sSQL, Values)
        data = [x for x in data.fetchall()]

        if len(data) == 0:
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[SP-Failure]-SP_Arm_GetConfigData-NoDataLoaded')
            self.Conn.commit()
            return (data)

        # FILTER DATA
        hasil = []
        ##print data[0]
        for item in data:
            contain = []
            for i in range(len(data[0])):
                contain.append(item[i])
            hasil.append(contain)

        self.Conn.commit()
        return (data)
        
    def MGETConfigDetailSet(self,mode,headerid):
        sSQL = "EXEC SP_Arm_GetConfigDetailSet ? , ?"
        Values = [mode, int(headerid)]

        ##print sSQL, Values

        data = self.oConn.execute(sSQL, Values)
        data = [x[0] for x in data.fetchall()]

        if len(data) == 0:
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[SP-Failure]-SP_Arm_GetConfigDetailSet-NoDataLoaded')
            self.Conn.commit()
            return (data)

        ##print data
        ##print "-----------------"
        ##print len(data)
        ##print "-----------------"
        ##print data

        data = data[0]

        self.Conn.commit()
        return (data)


    def MGetZeroAttribute(self, mode, **kwargs):

        try:
            headid = int(kwargs['headerid'])
        except Exception as e:
            print e
            return


        sSQL = "EXEC SP_Arm_GetZeroAttribute  ?, ?"
        Values = [mode, headid]

        try:
            data = self.oConn.execute(sSQL, Values)
        except Exception as e:
            print e
            return
        else:
            data = data.fetchall()
            data = [x for x in data]

        if len(data) == 0:
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[SP-Failure]-SP_Arm_GetZeroAttribute-NoDataLoaded')
            self.Conn.commit()
            return (data)

        #Wrapping Result data Per Row
        hasil = []
        for item in data:
            contain = []
            for i in range(len(data[0])):
                contain.append(item[i])
            hasil.append(contain)

        self.Conn.commit()
        return (hasil)

    def MGETSudutDetailSet(self,mode,headerid):
        sSQL = "EXEC SP_Arm_GetSudutDetailSet  ?, ?"
        Values = [mode, headerid]

        ##print sSQL, Values

        data = self.oConn.execute(sSQL, Values)
        data = data.fetchall()
        ##print data
        data = [x for x in data]

        if len(data) == 0:
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[SP-Failure]-SP_Arm_GetSudutDetailSet-NoDataLoaded')
            self.Conn.commit()
            return (data)


        #FILTER DATA
        hasil = []
        ##print data[0]
        for item in data:
            contain = []
            for i in range(len(data[0])):
                contain.append(item[i])
            hasil.append(contain)

        ##print hasil
        ##print "-----------------"
        ##print len(hasil)
        ##print "-----------------"

        self.Conn.commit()
        return (hasil)




    def MRecordSudut(self,type, mode,**kwargs):
        if type == 'DETAIL':
            sSQL = "EXEC SP_Arm_InsertSudutDetail ? , ? , ? , ? , ? ,? , ? "



            Values = [mode, int(kwargs['headerid']), int(kwargs['list']), int(kwargs['motorid'])]

            if kwargs.get('val') == None or kwargs['val'] == '-':
                Values.append('')
            else:
                Values.append(float(kwargs['val']))

            if kwargs['speed'] != None and kwargs['speed'] != '-':
                Values.append(float(kwargs['speed']))
            else:
                Values.append('')

            if kwargs['dirc'] != None and kwargs['dirc'] != '-':
                Values.append(int(kwargs['dirc']))
            else:
                Values.append('')


            ##print sSQL, Values

            try:
                self.oConn.execute(sSQL, Values)
                self.Conn.commit()
            except Exception as e:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[SP-Failure]-SP_Arm_InsertSudutDetail-' + str(e))
                return (False)
            else:
                return (True)
            
        elif type == 'HEADER':
            sSQL = "EXEC SP_Arm_InsertSudutHeader ? , ? "
            Values = [mode, str(kwargs['name'])]

            ##print sSQL, Values

            try:
                self.oConn.execute(sSQL, Values)
                self.Conn.commit()
            except Exception as e:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[SP-Failure]-SP_Arm_InsertSudutHeader-' + str(e))
                return (False)
            else:
                return (True)


    def MDeleteSudut(self,type, mode,**kwargs):
        if type == 'DETAIL':
            sSQL = "EXEC SP_Arm_DeleteSudutDetail ? , ?  "
            Values = [mode,int(kwargs['headerid'])]

            ##print sSQL, Values

            try:
                self.oConn.execute(sSQL, Values)
                self.Conn.commit()
            except Exception as e:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[SP-Failure]-SP_Arm_DeleteSudutDetail-' + str(e))
                return (False)
            else:
                return (True)

        elif type == 'HEADER':
            sSQL = "EXEC SP_Arm_DeleteSudutHeader ? , ? "
            Values = [mode, str(kwargs['headerid'])]

            ##print sSQL, Values

            try:
                self.oConn.execute(sSQL, Values)
                self.Conn.commit()
            except Exception as e:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[SP-Failure]-SP_Arm_DeleteSudutHeader-' + str(e))
                return (False)
            else:
                return (True)


    def MUpdateSudut(self, type, mode, **kwargs):
        if type == 'DETAIL':
            headid = kwargs['headerid']
            self.MDeleteSudut('DETAIL',mode,headerid=headid)

            if len(kwargs['arraydata']) != 0:
                for item in kwargs['arraydata']:
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


                        #Save Data
                        try:
                            self.MRecordSudut('DETAIL', 1,headerid=headid , list=lists, motorid=motorid,
                                              val=val,speed=spd, dirc=dirc)
                        except Exception as e:
                            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                             message='[SP-Failure]-SP_Arm_InsertSudutDetail/ON/MUpdateSudut-' + str(e))

                        else:
                            print 'SAVE SUCCESS'

        elif type == 'HEADER':
            sSQL = "EXEC SP_Arm_UpdateSudutData ? , ? , ?"
            Values = [mode, int(kwargs['headerid']), str(kwargs['name'])]

            ##print sSQL, Values

            try:
                self.oConn.execute(sSQL, Values)
                self.Conn.commit()
            except Exception as e:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[SP-Failure]-SP_Arm_UpdateSudutData-' + str(e))
                return (False)
            else:
                return (True)



    def MRecordTransaction(self, type, mode, **kwargs):
        #HEADER INSERT
        if type == 'HEADER':
            sSQL = "EXEC SP_Arm_RecordTransactionH ? , ?  , ? , ?"
            Values = [mode, str(kwargs['name']), str(kwargs['start']), int(kwargs['config'])]

            # #print sSQL, Values
            try:
                data = self.oConn.execute(sSQL, Values)
                self.Conn.commit()
            except Exception as e:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[SP-Failure]-SP_Arm_RecordTransactionH-' + str(e))
                return ('FAIL')
            else:
                #GET HEADER ID
                sSQL = "EXEC SP_Arm_RecordTransactionH ? , ?  , ? , ?"
                Values = [3, str(kwargs['name']), str(kwargs['start']), int(kwargs['config'])]
                data = self.oConn.execute(sSQL, Values)
                data = [x[0] for x in data.fetchall()]
                data = data[0]
                return (data)

        elif type == 'DETAIL':

            sSQL = "EXEC SP_Arm_RecordTransactionD ? , ? , ? , ? , ? , ? , ? , ?"
            Values = [mode, int(kwargs['headerid']), int(kwargs['list']), int(kwargs['motorid']),
                      str(kwargs['start']), str(kwargs['end']), int(kwargs['orientasi']), int(kwargs['value'])]

            # #print sSQL, Values
            try:
                self.oConn.execute(sSQL, Values)
                self.Conn.commit()
            except Exception as e:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[SP-Failure]-SP_Arm_RecordTransactionD-' + str(e))
                return (False)
            else:
                self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                                 message='[SP-Failure]-SP_Arm_RecordTransactionD-' + str('SUCCESS'))
                return (True)

    def MGETConstantCommand(self, type):
        if type == 'SCROLL':
            self.Scroll_Cmd = self.MLoadDataScroll(1)
            self.Scroll_Reset = self.MLoadDataScroll(2)
        elif type == 'NORMAL':
            self.Normal_Cmd = self.MLoadDataScroll(3)
        elif type == 'ACTIVATION':
            self.Activation_Cmd = self.MLoadConstantCommands(1)

    def MGETConstantData(self, mode, **kwargs):
        if mode == 'MOTOR':
            #Place this on init
            data = self.MLoadConstantData(mode,colwanted=kwargs['colwanted'])
            print data
            #Wrapping data
            self.Motor_Data = data


    def MLoadConstantCommands(self, mode):

        #Activation Command
        if mode == 1:
            container = {}
            gripper_activation = self.MGenerateCommands(1, 6, groupcommand='COMMAND_MOTOR', typecommand='ACTIVATION')

            container.update({6: gripper_activation})
            # print container
            return (container)

    def MLoadConstantData(self, mode, **kwargs):

        if mode == 'MOTOR':
            if kwargs['colwanted'] == 'ALL':
                data = self.MGETAllMotorData(2,None)
                container = data
                print container
            return (container)


    def MLoadDataScroll(self, mode):
        #Load Scroll Command Starter & Feedback
        if mode == 1:
            #LoadCommands to Dict
            container = {}
            axis_1 = self.MGenerateCommands(1,1,groupcommand='MANUAL',typecommand='SCROLL')
            axis_2 = self.MGenerateCommands(1, 2, groupcommand='MANUAL', typecommand='SCROLL')
            axis_3 = self.MGenerateCommands(1, 3, groupcommand='MANUAL', typecommand='SCROLL')
            axis_4 = self.MGenerateCommands(1, 4, groupcommand='MANUAL', typecommand='SCROLL')
            axis_5 = self.MGenerateCommands(1, 5, groupcommand='MANUAL', typecommand='SCROLL')

            container.update({1: axis_1})
            container.update({2: axis_2})
            container.update({3: axis_3})
            container.update({4: axis_4})
            container.update({5: axis_5})

            #print container

            return (container)

        #Load Reset Command
        elif mode == 2:
            container = {}
            NormalReset = self.MGenerateCommands(1, 8, groupcommand='COMMAND_MOTOR', typecommand='RESET')
            ScrollReset = self.MGenerateCommands(1, 8, groupcommand='MANUAL', typecommand='RESET')

            container.update({'NORMAL': NormalReset})
            container.update({'SCROLL': ScrollReset})

            #print container

            return (container)

        elif mode == 3:
            container = {}
            axis_1 = self.MGenerateCommands(1, 1, groupcommand='COMMAND_MOTOR', typecommand='COMMAND')
            axis_2 = self.MGenerateCommands(1, 2, groupcommand='COMMAND_MOTOR', typecommand='COMMAND')
            axis_3 = self.MGenerateCommands(1, 3, groupcommand='COMMAND_MOTOR', typecommand='COMMAND')
            axis_4 = self.MGenerateCommands(1, 4, groupcommand='COMMAND_MOTOR', typecommand='COMMAND')
            servo  = self.MGenerateCommands(1, 5, groupcommand='COMMAND_MOTOR', typecommand='COMMAND')
            gripper = self.MGenerateCommands(1, 6, groupcommand='COMMAND_MOTOR', typecommand='COMMAND')

            container.update({1: axis_1})
            container.update({2: axis_2})
            container.update({3: axis_3})
            container.update({4: axis_4})
            container.update({5: servo})
            container.update({6: gripper})

            print container

            return (container)

    def MSaveConfigH(self, mode, headerid, **kwargs):
        sSQL = "EXEC SP_Arm_SP_Arm_SaveConfigH   ?, ?"
        Values = [mode, headerid]

        try:
            data = self.oConn.execute(sSQL, Values)
        except Exception as e:
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[SP-Failure]-SP_Arm_SaveConfigH-' + str(e))
            print e

        self.Conn.commit()

    def MSaveConfigD(self, mode, headerid, lists, sudut, **kwargs):
        sSQL = "EXEC SP_Arm_SP_Arm_SaveConfigD   ?, ?, ?, ?"
        Values = [int(mode), int(headerid), int(lists), sudut]

        try:
            data = self.oConn.execute(sSQL, Values)
        except Exception as e:
            self.CPrintDebug(2, object=self.Logger_List['Main-Log'],
                             message='[SP-Failure]-SP_Arm_SaveConfigH-' + str(e))
            print e

        self.Conn.commit()












