import Eyes
import ArduinoControl

import pygame
from pygame.locals import *
import sys
from nanpy import (ArduinoApi, SerialManager)
import time

''' COLORS '''
colGreen = pygame.Color(0,255,0)
colBlack = pygame.Color(0,0,0)

''' GAME DISPLAY '''
pygame.init()
pygame.mixer.pre_init()

# (width, height)
dispWH = (1600,900)

gameDisplay = pygame.display.set_mode(dispWH,pygame.FULLSCREEN, 32)
pygame.display.set_caption("Treadwell")

# Start both utilities
screen = Eyes.Eyes(gameDisplay)
bot = ArduinoControl.ArduinoControl()

def main()
    while True:
    
        # Moves the bot at the given speed
        bot.makeAMove()
        
        
        # Just for effect
        screen.idle(colGreen)
    
        for event in pygame.event.get():
        
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            elif event.type == KEYDOWN:
                if event.key == K_q:
                    pygame.quit()
                    sys.exit()
                    
                elif event.key == K_UP:
                    bot.incSpeed()
                elif event.key == K_DOWN:
                    bot.decSpeed()
                elif event.key == K_SPACE:
                    bot.stop()
        
        
        
        
        # Last thing to be called
        pygame.display.update()
    