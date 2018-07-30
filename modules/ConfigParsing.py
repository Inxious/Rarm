

import configparser

class ConfigPasser():
    def __init__(self):

        self.Magnets = bool(int(self.config.get('Magnet Configuration', 'ISOn')))
        Need_Activation = str(self.config.get('Motor Configuration', 'Need_Activation'))
        Need_Activation = self.CFilterString(1, Need_Activation, remove=['[', ']'])
        self.Need_Activation = list(int(x) for x in Need_Activation.split(','))
        Need_ConvertValue = str(self.config.get('Motor Configuration', 'Need_ConvertValue'))
        Need_ConvertValue = self.CFilterString(1, Need_ConvertValue, remove=['[', ']'])
        self.Need_ConvertValue = list(int(x) for x in Need_ConvertValue.split(','))

        # DigitMotor
        Motor1_Digit_Used = str(self.config.get('Command Configuration', 'Motor_1_Digit'))
        Motor1_Digit_Used = self.CFilterString(1, Motor1_Digit_Used, remove=['[', ']'])
        Motor1_Digit_Used = list(int(x) for x in Motor1_Digit_Used.split(','))

        Motor2_Digit_Used = str(self.config.get('Command Configuration', 'Motor_2_Digit'))
        Motor2_Digit_Used = self.CFilterString(1, Motor2_Digit_Used, remove=['[', ']'])
        Motor2_Digit_Used = list(int(x) for x in Motor2_Digit_Used.split(','))

        Motor3_Digit_Used = str(self.config.get('Command Configuration', 'Motor_3_Digit'))
        Motor3_Digit_Used = self.CFilterString(1, Motor3_Digit_Used, remove=['[', ']'])
        Motor3_Digit_Used = list(int(x) for x in Motor3_Digit_Used.split(','))

        Motor4_Digit_Used = str(self.config.get('Command Configuration', 'Motor_4_Digit'))
        Motor4_Digit_Used = self.CFilterString(1, Motor4_Digit_Used, remove=['[', ']'])
        Motor4_Digit_Used = list(int(x) for x in Motor4_Digit_Used.split(','))

        Motor5_Digit_Used = str(self.config.get('Command Configuration', 'Motor_5_Digit'))
        Motor5_Digit_Used = self.CFilterString(1, Motor5_Digit_Used, remove=['[', ']'])
        Motor5_Digit_Used = list(int(x) for x in Motor5_Digit_Used.split(','))

        Motor6_Digit_Used = str(self.config.get('Command Configuration', 'Motor_6_Digit'))
        Motor6_Digit_Used = self.CFilterString(1, Motor6_Digit_Used, remove=['[', ']'])
        Motor6_Digit_Used = list(int(x) for x in Motor6_Digit_Used.split(','))

        self.Digit_Command = {1: Motor1_Digit_Used, 2: Motor2_Digit_Used,
                              3: Motor3_Digit_Used, 4: Motor4_Digit_Used,
                              5: Motor5_Digit_Used, 6: Motor6_Digit_Used}

        # Perbandingan Gear
        M1 = float(self.config.get('Perbandingan Gear', 'M1'))
        M2 = float(self.config.get('Perbandingan Gear', 'M2'))
        M3 = float(self.config.get('Perbandingan Gear', 'M3'))
        M4 = float(self.config.get('Perbandingan Gear', 'M4'))

        self.Perbandingan_Gear = {1: M1, 2: M2,
                                  3: M3, 4: M4}

        # TESTING SETTINGS

        # Scroll Constant Command Mode
        self.Constant_ScrollCmd = bool(self.config.get('Scroll Mode Configuration', 'LoadDBonStart'))
        if self.Constant_ScrollCmd:
            self.CConstantCommand('ACTIVATION')
            self.CConstantCommand('SCROLL')
            self.CConstantCommand('NORMAL')

        # Motor Microstep constant Data
        self.Constant_MotorData = bool(self.config.get('Constant Data Configuration', 'MotorData'))
        if self.Constant_MotorData:
            self.CConstantData('MOTOR', colwanted='ALL')