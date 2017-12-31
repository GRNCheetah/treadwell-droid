import pygame
from pygame.locals import *
import sys
import time
import random



''' VARS '''
eye_height = 400
down = True
time2Sleep = 0

DONE = False
ACTION = 'idle'



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
    
    
# Desc: Displays a pair of open eyes
# Pre: Needs a declared display of a certain size
# Post: Displays the eyes in the middle of the screen
def idle(gameDisplay, color):
    pygame.draw.ellipse(gameDisplay, color, (300, 250, 400, 400))
    pygame.draw.ellipse(gameDisplay, color, (900, 250, 400, 400))
    #how long to sit in idle
    return 2
    
#takes down and eye_height
#returns down, eye_height, DONE, time2Sleep
# Desc: Blinks, but has to be in a loop
# Pre: Lots of junk
# Post: Blinks the eyes
def blink(gameDisplay, color, down, eye_height, DONE):
    RATE = 5
    # screen, color, (x,y,w,h), inside
    pygame.draw.ellipse(gameDisplay, color, (300, 650-eye_height, 400, eye_height))
    pygame.draw.ellipse(gameDisplay, color, (900, 650-eye_height, 400, eye_height))
    
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
    
# Desc: Puts the eyes in a squint
# Pre: Needs a game display to have been declared
# Post: Squints the eyes
def squint(gameDisplay, dispWH, color):
    pygame.draw.rect(gameDisplay, color, (300, 400, 400, 100))
    pygame.draw.rect(gameDisplay, color, (900, 400, 400, 100))

    return 2

''' MAIN '''
def main():
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
        
if __name__ == "__main__":
    main()