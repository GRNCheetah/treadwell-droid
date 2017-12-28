from nanpy import (ArduinoApi, SerialManager)
from time import sleep

# Arduino pin outs
fL = 10
fR = 5
# Gets the motors moving in the right directions
fL_mod = 1
fR_mod = 1

try:

    connection = SerialManager()
    a = ArduinoApi(connection = connection)

except:
    print("Failed to connect to arduino")


# Setup the pinModes
# Might want to put this before the while loop
# in the try statement to keep from crashing if
# the above doesn't connect
a.pinMode(fL, a.OUTPUT)
a.pinMode(fR, a.OUTPUT)
# Initial speed of the bot
speed = 0
try:
    # This is where the magic happens
    while True:
        a.analogWrite(fL, (fL_mod * speed))
        a.analogWrite(fR, (fR_mod * speed))
        print(fL_mod * int(speed))
        
        inP = input("Command: ")
        if (inP == "u"):
            speed += 10
        elif (inP == "d"):
            speed -= 10
        elif (inP == "s"):
            speed = 0


except:
    print("What the fuck bruh")
    a.analogWrite(fL, a.LOW)
