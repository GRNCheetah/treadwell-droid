import pygame
from pygame.locals import *
import sys
import time
import random

pygame.init()
pygame.mixer.pre_init()

''' COLORS '''
colGreen = pygame.Color(0,255,0)
colBlack = pygame.Color(0,0,0)

''' GAME DISPLAY '''
dispWidth = 1600
dispHeight = 900

gameDisplay = pygame.display.set_mode((dispWidth, dispHeight),pygame.FULLSCREEN, 32)
pygame.display.set_caption("Hello, I'm Darren")

''' CONSTANTS '''
ACTION = "" # keeps track of current action

''' FUNCTIONS '''
def randAction():
    randNum = random.randrange(1, 1000)
    print(randNum)
    act = ""
    if randNum >= 1 and randNum <= 800:
        act = 'idle'
    elif randNum > 800 and randNum <= 900:
        act = 'blink'
    elif randNum > 900 and randNum <= 1000:
        act = 'squint'
    return act
    
def idle():
    pygame.draw.ellipse(gameDisplay, colGreen, (300, 250, 400, 400))
    pygame.draw.ellipse(gameDisplay, colGreen, (900, 250, 400, 400))
    #how long to sit in idle
    return 2
    
#takes down and eye_height
#returns down, eye_height, DONE, time2Sleep
def blink(down, eye_height, DONE):
    RATE = 5
    # screen, color, (x,y,w,h), inside
    pygame.draw.ellipse(gameDisplay, colGreen, (300, 650-eye_height, 400, eye_height))
    pygame.draw.ellipse(gameDisplay, colGreen, (900, 650-eye_height, 400, eye_height))
    
    if eye_height > RATE and down:
        eye_height -= RATE
    elif eye_height < 400 and not(down):
        eye_height += RATE
    elif eye_height == RATE and down:
        down = False
        eye_height += RATE
    elif eye_height == 400 and not(down):
        down = True
        DONE = True

    return down, eye_height, DONE, .00001
    
def squint():
    pygame.draw.rect(gameDisplay, colGreen, (300, 400, 400, 100))
    pygame.draw.rect(gameDisplay, colGreen, (900, 400, 400, 100))

    return 2

''' MAIN '''
eye_height = 400
down = True
time2Sleep = 0

DONE = False
ACTION = 'idle'
while True:
    gameDisplay.fill(colBlack)
    
    ''' PERFORM ACTION '''
    if ACTION == 'idle' or DONE:
        time2Sleep = idle()
        DONE = False
        ACTION = randAction()
    elif ACTION == 'blink':
        down, eye_height, DONE, time2Sleep = blink(down, eye_height, DONE)
    elif ACTION == 'squint':
        time2Sleep = squint()
        DONE = True

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == KEYDOWN:
            if event.key == K_a:
                pygame.quit()
                sys.exit()
            
    pygame.display.update()
    time.sleep(time2Sleep)