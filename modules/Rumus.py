
import matplotlib
import numpy
import math


class Rumus():
    @classmethod
    def __init__(self):
        pass

    @classmethod
    def RumusSudutAxis(self, mode, **kwargs):
        if mode == 'wSudutAxis':
            try:
                SudutMotor = float(kwargs['SudutMotor'])
                PerbadinganGear = float(kwargs['PerbandinganGear'])
            except Exception as e:
                print (e)
                return (None)
            else:
                SudutAxis = float(SudutMotor / PerbadinganGear)
                return (SudutAxis)
        elif mode == 'wPerbandingan':
            try:
                SudutMotor = float(kwargs['SudutMotor'])
                SudutAxis = float(kwargs['SudutAxis'])
            except Exception as e:
                print (e)
                return (None)
            else:
                PerbadinganGear = float(SudutAxis * SudutMotor)
                return (PerbadinganGear)
        elif mode == 'wSudutMotor':
            try:
                PerbadinganGear = float(kwargs['PerbandinganGear'])
                SudutAxis = float(kwargs['SudutAxis'])
            except Exception as e:
                print (e)
                return (None)
            else:
                SudutMotor = float(SudutAxis * PerbadinganGear)
                return (SudutMotor)

    @classmethod
    def RumusSudutMotor(self, mode, **kwargs):
        if mode == 'wSudutMotor':
            try:
                PulseStepMotor = float(kwargs['PulseStepMotor'])
                MicroStepDriver = float(kwargs['MicroStepDriver'])
            except Exception as e:
                print (e)
                return (None)
            else:
                SudutMotor = float((float(PulseStepMotor) * float(1.8)) / float(MicroStepDriver))
                return (SudutMotor)
        if mode == 'wPulseStepMotor':
            try:
                SudutMotor = float(kwargs['SudutMotor'])
                MicroStepDriver = float(kwargs['MicroStepDriver'])
            except Exception as e:
                print (e)
                return (None)
            else:
                PulseStepMotor = int((float(SudutMotor)  * float(MicroStepDriver)) / float(1.8))
                return (PulseStepMotor)
        if mode == 'wMicroStepDriver':
            try:
                PulseStepMotor = float(kwargs['PerbandinganGear'])
                SudutMotor = float(kwargs['SudutMotor'])
            except Exception as e:
                print (e)
                return (None)
            else:
                MicroStepDriver = int(float(SudutMotor) * (float(PulseStepMotor) / float(1.8)))
                return (MicroStepDriver)

    @classmethod
    def RumusMenghitungWaktu(self, pulsestep, speed, microstepdriver):
        hitung = float(0)
        accel = float(float(speed) / float(100000))
        steps = int(pulsestep) / int(2)
        steps = steps * int(microstepdriver)
        delays = [x for x in range(steps)]
        angle = int(1)
        c0 = float(float(2000) * math.sqrt(2 * angle / accel) * float(0.67703))
        lastDelay = float(0)

        i = int(0)
        while i < steps:
            d = float(c0)
            if i > 0:
                d = float(lastDelay - (2 * lastDelay) / (4 * i + 1))
            if d < 100:
                d = float(100)
            delays[i] = int(d)
            lastDelay = float(d)
            i += 1

        i1 = int(0)
        while i1 < steps:
            hitung = float(float(hitung) + delays[i1] + 2)
            i1 += 1
        i2 = int(0)
        while i2 < steps:
            hitung = float(float(hitung) + delays[steps - i2 - 1] + 2)
            i2 += 1
        hitung = float(hitung / 1000000)
        return (hitung)

    @classmethod
    def RumusMenghitungAccel(self, pulsestep, microstepdriver, waktu):
        # ToDo ======================
        # pulsestep = step tujuan
        # microstep = microstep driver motor
        # waktu = waktu yang digunakan
        # ToDo ======================
        print 'GO'
        speed1 = int(1)
        hitung = float(0)
        accel = float(speed1) / float(100000)
        steps = int(pulsestep) / int(2)
        steps = int(int(steps) * int(microstepdriver))
        delays = [x for x in range(steps)]
        angle = int(1)
        c0 = float(float(2000) * float(math.sqrt(angle / accel)) * float(0.67703))
        lastDelay = float(0)
        i = int(0)
        while i < steps:
            print '1'
            d = float(c0)
            if i > 0:
                d = float(float(lastDelay) - float(2 * float(lastDelay)) / float(4 * i + 1))
            if d < 100:
                d = 100
            delays[i] = int(d)
            lastDelay = float(d)
            i += 1
        i1 = int(0)
        while i1 < steps:
            print '2'
            hitung = float(float(hitung) + delays[i1] + 2)
            i1 += 1
        i2 = int(0)
        while i2 < steps:
            print '3'
            hitung = float(float(hitung) + delays[steps - i2 - 1] + 2)
            i2 += 1
        hitung = float(hitung) / float(1000000)

        while hitung > waktu:
            print str(hitung) + ' // ' + str(waktu)
            speed1 += 1
            hitung1 = float(0)
            accel = float(float(speed1) / float(100000))
            #waktu = waktu
            steps = pulsestep / 2
            steps = steps * int(microstepdriver)
            angle = 1
            c0 = float(float(2000) * float(math.sqrt(2 * angle / accel)) * float(0.6770))
            lastDelay = 0
            i = int(0)
            while i < steps:
                #print '4'
                d = float(c0)
                if i > 0:
                    d = float(float(lastDelay) - float(2 * float(lastDelay)) / float(4 * i + 1))
                if d < 100:
                    d = 100
                delays[i] = int(d)
                lastDelay = float(d)
                i += 1
            i1 = int(0)
            while i1 < steps:
                #print '5'
                hitung1 = float(float(hitung1) + delays[i1] + 2)
                i1 += 1
            i2 = int(0)
            while i2 < steps:
                #print '6'
                hitung1 = float(float(hitung1) + delays[steps - i2 - 1] + 2)
                i2 += 1
            hitung1 = float(hitung1) / float(1000000)
            hitung = hitung1
            i += 1
        return (speed1)




