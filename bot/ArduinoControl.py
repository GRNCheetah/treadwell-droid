from nanpy import (ArduinoApi, SerialManager)
from time import sleep

class ArduinoControl:

    def __init__(self):

        # PWM outs on the Arduino
        self.lF = 10 #a
        self.rF = 5  #b
        self.lR = 11 #c
        self.rR = 3  #d

        # Should be between 0-255, speed of the motors
        self.speed = 0

        # Sets connections to arduino
        try:
            print("[+] Init conn to Arduino...")
            self.connection = SerialManager()
            self.a = ArduinoApi(connection = self.connection)
            self.a.pinMode(self.lF, self.a.OUTPUT)
            self.a.pinMode(self.rF, self.a.OUTPUT)
            self.a.pinMode(self.lR, self.a.OUTPUT)
            self.a.pinMode(self.rR, self.a.OUTPUT)
            print("[+] Connected to Arduino.")
        except:
            print("[x] Failed to connect to Arduino")

    def forward(self):
	self.makeAMove(1,1,1,1)

    def backward(self):
        self.makeAMove(-1,-1,-1,-1)

    def rot_left(self):
	self.makeAMove(-1,1,-1,1)

    def rot_right(self):
	self.makeAMove(1,-1,1,-1)

    ## a,b,c,d represent the directions each motor should go for a
    ## given maneuver
    def makeAMove(self,a,b,c,d):

        # Will try to move at the given speed
        try:
            self.a.analogWrite(self.lF, self.speed * a * 1)
            self.a.analogWrite(self.rF, self.speed * b * 1)
            self.a.analogWrite(self.lR, self.speed * c * 1)
            self.a.analogWrite(self.rR, self.speed * d * 1)
        except:
            print("[x] System Error")
            print("[x] stopping...")
            self.a.analogWrite(self.lF, self.a.LOW)
            self.a.analogWrite(self.rF, self.a.LOW)
            self.a.analogWrite(self.lR, self.a.LOW)
            self.a.analogWrite(self.rR, self.a.LOW)

    def incSpeed(self):
	if self.speed < 245:
            self.speed += 10
	else:
	    self.speed = 255
        print("INC SPEEEEED")

    def decSpeed(self):
        if self.speed > 5:
            self.speed -= 10
	else:
	    self.speed = 0

    def stop(self):
        self.a.analogWrite(self.lF, self.a.LOW)
        self.a.analogWrite(self.rF, self.a.LOW)
        self.a.analogWrite(self.lR, self.a.LOW)
        self.a.analogWrite(self.rR, self.a.LOW)
