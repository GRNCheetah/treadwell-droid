from nanpy import (ArduinoApi, SerialManager)
from time import sleep

class ArduinoControl:

    def __init__(self):
    
        # PWM outs on the Arduino
        self.lF = 10
        self.rF = 5
        self.lR = 11
        self.rR = 3
        
        # Should be between 0-255, speed of the motors
        self.speed = 0
        
        # Sets connections to arduino
        try:
            self.connection = SerialManager()
            aelf.a = ArduinoApi(connection = self.connection)
            self.a.pinMode(self.lF, self.a.OUTPUT)
            self.a.pinMode(self.rF, self.a.OUTPUT)
            self.a.pinMode(self.lR, self.a.OUTPUT)
            self.a.pinMode(self.rR, self.a.OUTPUT)
            print("[+] Connected")
        except:
            print("[x] Failed to connect to Arduino")    
    
    def makeAMove(self):

        # Will try to move at the given speed
        try:
            self.a.analogWrite(self.lF, self.speed)
            self.a.analogWrite(self.rF, self.speed)
            self.a.analogWrite(self.lR, self.speed)
            self.a.analogWrite(self.rR, self.speed)
        except:
            print("[x] System Error")
            print("[x] stopping...")
            self.a.analogWrite(self.lF, self.a.LOW)
            self.a.analogWrite(self.rF, self.a.LOW)
            self.a.analogWrite(self.lR, self.a.LOW)
            self.a.analogWrite(self.rR, self.a.LOW)
    
    def incSpeed(self):
        self.speed += 10
        
    def decSpeed(self):
        self.speed -= 10
        
    def stop(self):
        self.a.analogWrite(self.lF, self.a.LOW)
        self.a.analogWrite(self.rF, self.a.LOW)
        self.a.analogWrite(self.lR, self.a.LOW)
        self.a.analogWrite(self.rR, self.a.LOW)
            