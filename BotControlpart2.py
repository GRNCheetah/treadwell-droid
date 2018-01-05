from nanpy import (ArduinoApi, SerialManager)
from time import sleep

class ArduinoControl:

    def __init__(self):
    
        self.lF = 10
        self.rF = 5
        self.lR = 11
        self.rR = 3

        self.speed = 0
        
    def connect2Arduino(self):
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
        
        try:
            a.analogWrite(self.lF, self.speed)
            a.analogWrite(self.rF, self.speed)
            a.analogWrite(self.lR, self.speed)
            a.analogWrite(self.rR, self.speed)
        except:
            print("[x] System Error")
            print("[x] stopping...")
            a.analogWrite(self.lF, 0)
            a.analogWrite(self.rF, 0)
            a.analogWrite(self.lR, 0)
            a.analogWrite(self.rR, 0)
    
    def incSpeed(self, speed):
        self.speed += 10
            
        
            
            
            
            
meme = ArduinoControl()
meme.connect2Arduino()