import Eyes
import ArduinoControl

import socket
import pygame
from pygame.locals import *
import sys
from nanpy import (ArduinoApi, SerialManager)
import time

''' COLORS '''
colGreen = pygame.Color(0,255,0)
colBlack = pygame.Color(0,0,0)

''' GAME DISPLAY '''
#pygame.init()
#pygame.mixer.pre_init()

## (width, height)
dispWH = (1280, 720)

#gameDisplay = pygame.display.set_mode(dispWH)
#pygame.display.set_caption("Treadwell")

## Start both utilities
#screen = Eyes.Eyes(gameDisplay)
bot = ArduinoControl.ArduinoControl()


def server():
    host =  "192.168.4.1"
    port = 8080

    sock = socket.socket()
    sock.bind((host,port))

    print("[+] Awaiting client connection.")

    sock.listen(1)
    conn, addr = sock.accept()

    print("[+] Connection from: " + str(addr))

    return conn, addr


## Main loop
def main():

    ## Setup connection to controller
    conn, addr = server()

    reset = False
    prev_choice = "idle"
    while True:
        data = conn.recv(1024).decode('utf-8'))
        
        ## Check for new choice
        if prev_choice != data: # If data is new
        
            ## Speed control
            if data == "speed_up":
                bot.incSpeed()
            elif data == "speed_down":
                bot.decSpeed()
            
            ## Stop movement
            elif data == "stop" or data == "idle":
                bot.stop()
                
            ## Movement control
            elif data == "forward":
                bot.forward()
            elif data == "backward":
                bot.backward()
            elif data == "rot_left":
                bot.rot_left()
            elif data == "rot_right":
                bot.rot_right()
                
        prev_choice = data
        message = bot.speed
        conn.send(message.decode('utf-8'))


        # Just for effect
        #screen.idle(colGreen)

        """for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                    sys.exit()
                    bot.stop()

                elif event.key == K_UP:
                    bot.incSpeed()
                    print("INCREASING")
                elif event.key == K_DOWN:
                    bot.decSpeed()
                elif event.key == K_SPACE:
                    bot.stop()"""

        # Last thing to be called
        #pygame.display.update()

    return True

if __name__ == "__main__":
    open = True
    while open:
        open = main()
