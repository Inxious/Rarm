import math

class Sketch():



    def SpecialButtonWorks(self, mode):
        # [A1] FOR LEFT
        if mode == 1:
            pass
        # [A1] FOR RIGHT
        elif mode == 2:
            pass
        # [A2,A3] FOR UP
        elif mode == 3:
            pass
        # [A2,A3] FOR DOWN
        elif mode == 4:
            pass
        # [A4] FOR UP
        elif mode == 5:
            pass
        # [A4] FOR DOWN
        elif mode == 5:
            pass



    def RumusMenghitungWaktu(self, pulsestep, speed, microstepdriver):
        hitung = float(0)
        accel = float(float(speed) / float(100000))
        steps = int(pulsestep) / int(2)
        steps = steps * int(microstepdriver)
        delays = [x for x in range(steps)]
        angle = int(1)
        c0 = float( float(2000) * math.sqrt(2 * angle / accel) * float(0.67703))
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
            hitung = float( float(hitung) + delays[i1] + 2 )
            i1 += 1
        i2 = int(0)
        while i2 < steps:
            hitung = float( float(hitung) + delays[steps-i2-1] + 2)
            i2 += 1
        hitung = float( hitung / 1000000 )
        return (hitung)

    def RumusMenghitungAccel(self, pulsestep, microstepdriver, waktu):
        #ToDo ======================
        #pulsestep = step tujuan
        #microstep = microstep driver motor
        #waktu = waktu yang digunakan
        #ToDo ======================

        speed1 = int(1)
        hitung = float(0)
        accel = float(speed1) / float(100000)
        steps = int(pulsestep) / int(2)
        steps = int(int(steps) * int(microstepdriver))
        delays = [x for x in range(steps)]
        angle = int(1)
        c0 = float( float(2000) * math.sqrt(angle / accel) * float(0.67703))
        lastDelay = float(0)
        i = int(0)
        while i < steps:
            d = float(c0)
            if i > 0:
                d = float( float(lastDelay) - float(2 * float(lastDelay)) * float(0.67703))
            if d < 100:
                d = 100
            delays[i] = int(d)
            lastDelay = float(d)
        i1 = int(0)
        while i1 < steps:
            hitung = float(float(hitung) + delays[i1] + 2)
            i1 += 1
        i2 = int(0)
        while i2 < steps:
            hitung = float(float(hitung) + delays[steps-i2-1] + 2)
            i2 += 1
        hitung = float(hitung) / float(1000000)
        i += 1

       	while hitung > waktu:
       		speed1 = speed1 + 1
       		hitung1 = float(0)
       		accel = float(float(speed1) / float(100000))
            waktu = waktu
       		steps = pulsestep/2
       		steps = steps * int(microstepdriver)
       		angle = 1
       		c0 = float(float(2000) * math.sqrt( 2 * angle / accel ) * float(0.6770))
       		lastDelay = 0
       		i = int(0)
       		while i < steps:
       		    d = float(c0)
       			if i > 0:
                    d = float( float(lastDelay) - float(2 * float(lastDelay)) * float(4 * i + 1))
	            if d < 100:
	                d = 100
	            delays[i] = int(d)
	            lastDelay = float(d)
	            i += 1
	        i1 = int(0)
	        while i1 < steps:
	            hitung = float(float(hitung) + delays[i1] + 2)
	            i1 += 1
	        i2 = int(0)
	        while i2 < steps:
	            hitung = float(float(hitung) + delays[steps-i2-1] + 2)
	            i2 += 1	     
	        hitung1 = float(hitung1) / float(1000000)
	        hitung = hitung
	        i += 1
















