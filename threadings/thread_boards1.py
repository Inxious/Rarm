
import time

#Threads For Board 1

class ThreadsB1():
    def  __init__(self):
        start = 0
        while True:
            if self.Board_Connection.get(1) in ("",None,'OFF'):
                pass
            else:
                if start == 0:
                    print "Thread BOARD 1 STARTED"
                    start += 1
                else:
                    pass
                if self.Board_Reading.get(1) != None:
                    if self.Board_Connection[1] == "ON":

                        if self.Board_Reading[1] == "ON":
                            self.Board1_Reading_Data = ""
                            self.Board1_Reading_Result = "STARTED"

                            time_pass  = 0
                            FLAG = self.Board_Reading_Flag[1].encode()

                            doneread = False
                            while doneread != True:
                                while FLAG  not in self.Board1_Reading_Data:
                                    if int(time_pass) > 120:
                                        print("PROSES TIMEOUT")
                                        self.Board1_Reading_Result = "FAILED"
                                        break

                                    data = str(self.Serial_List[1].readline())

                                    if data:
                                        if self.CurrForm == 'Process':
                                            self.Dv_Table2.AppendItem([1,data])

                                    self.Board1_Reading_Data += (data)

                                    time.sleep(0.0001)
                                    time_pass += float(0.0001)


                                data = str(self.Serial_List[1].readline())

                                if data != FLAG:
                                    data = str(self.Serial_List[1].readline())

                                while data == FLAG:
                                    data = str(self.Serial_List[1].readline())
                                    if data:
                                        if self.CurrForm == 'Process':
                                            self.Dv_Table2.AppendItem([1, data])
                                    pass

                                print 'DONE READ >' + str(data)
                                doneread = True

                            #RESET
                            self.Serial_List[1].flushInput()
                            self.Serial_List[1].flushOutput()

                            if (FLAG in self.Board1_Reading_Data) == True:
                                self.Board1_Reading_Result = "SUCCESS"
                            else:
                                self.Board1_Reading_Result = "FAILED"

                            print self.Board1_Reading_Result

                            if self.Board1_Reading_Result == "FAILED":
                                self.Board1_Reading_Result = "FAILED"
                                self.Proces_Step = "Unfinished"
                                self.timedone = self.CCurTime()
                                self.Board_Reading[1] = "OFF"
                                print 'READ TIMEOUT'

                            elif self.Board1_Reading_Result == "SUCCESS":
                                self.Board1_Reading_Result = "SUCCESS"
                                self.timedone = self.CCurTime()
                                self.Proces_Step = "Finished"
                                self.Board_Reading[1] = "OFF"
                                print 'READ DONE'










