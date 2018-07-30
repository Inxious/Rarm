import time

class Th_DetectPos():
    def __init__(self):
        self.CPrintDebug(2, object=self.Logger_List['Thread-Log'],
                         message='Starting Thread DetectPos')
        self.DetectingPos = False

        while True:

            if self.DetectingPos == True and self.Controller_Mode == False:

                #DIFFER WHICH FORM IT WAS
                if self.CurrForm in (None,""):
                    self.DetectingPos = False
                elif self.CurrForm != 'Manual':
                    self.DetectingPos = False

                #ONLY GO WHEN THE SLIDE IS FOCUSED
                if self.CurrentFocus not in (None,""):
                    #FUNC TO GET WIDGET USED BY FORM AND FOCUS FILTER

                    if self.NowFocus != self.CurrentFocus:
                        self.NowFocus = self.CurrentFocus
                        self.PositionNow = self.CNows(2, need=self.NowFocus)

                    # Update Position Must ( 2 times )
                    self.CGETCurrValue(1, self.NowFocus)
                    #self.CGETCurrValue(2, self.NowFocus)

                    #Update Position Now
                    self.PositionNow = self.CNows(2, need=self.NowFocus)

                    try:
                        int(self.PositionNow)
                    except Exception as e:
                        pass
                    else:
                        #ONLY GO WHEN THE VALUE IS DIFFERENT
                        if  int(self.PositionNow) != int(self.PositionMust[self.NowFocus]):

                            self.CScrollDelay(self.Limit_Detect)

                            times = 0
                            while int(self.PositionNow) != int(self.PositionMust[self.NowFocus]):

                                #FILTER DIREKSI MOTOR
                                if (int(self.PositionNow) - int(self.PositionMust[self.NowFocus])) < 1:
                                    direksi = int(1)
                                else:
                                    direksi = int(0)

                                #EXECUTING COMMAND
                                self.CRoboMoveStep(2,motorid=int(self.NowFocus),sudut=self.PositionMust[self.NowFocus],dir=direksi)

                                #PRINT DEBUG
                                print 'SETTING ['+ str(self.NowFocus) +'] >> FROM ' +str(self.PositionNow) + ' TO ' +str(self.PositionMust[self.NowFocus])

                                self.CNows(5, type='value', motor=int(self.NowFocus), value=int(self.PositionMust[self.NowFocus]))

                                # Update Position Now
                                self.PositionNow = self.CNows(2, need=self.NowFocus)

                                # Update Position Must
                                self.CGETCurrValue(1, self.NowFocus)

                                #In Case Not Waiting
                                time.sleep(0.0001)
                                times += float(0.0001)

                                if times >= 60:
                                    print 'Positioning Time Out'
                                    break

                            print 'Positioning Done'

                # PASS / ERROR WHEN THE SLIDE NOT FOCUSED
                else:
                    print 'not focused'
                    pass
                    #ToDo : Raise Error






