import pygame
from pygame.locals import *
import random


class Eyes:

    def __init__(self, gameDisplay):
        self.gD = gameDisplay
        
        self.intEyeHt = 400
        self.blnDown = True
        self.intTime2Sleep = 0
        self.blnDone = False
        self.blnAction = 'idle'
   
        
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
    def idle(self, color):
        pygame.draw.ellipse(self.gD, color, (300, 250, 400, 400))
        pygame.draw.ellipse(self.gD, color, (900, 250, 400, 400))
        self.blnDone = False
        #how long to sit in idle
        return 2
        
    # Desc: Blinks in while looping
    # Pre: self.blnDone must be false, reset before hand. (Is reset in idle)
    # Post: Blinks the eyes
    def blink(self, color):
        RATE = 5
        # screen, color, (x,y,w,h), inside
        pygame.draw.ellipse(self.gD, color, (300, 650-self.intEyeHt, 400, self.intEyeHt))
        pygame.draw.ellipse(self.gD, color, (900, 650-self.intEyeHt, 400, self.intEyeHt))
        
        if not(self.blnDone):
            if self.intEyeHt > RATE and self.blnDown:
                self.intEyeHt -= RATE
            elif self.intEyeHt < 400 and not(self.blnDown):
                self.intEyeHt += RATE
            elif self.intEyeHt == RATE and self.blnDown:
                self.blnDown = False
                self.intEyeHt += RATE
            elif self.intEyeHt == 400 and not(self.blnDown):
                self.blnDown = True
                self.blnDone = True
    
        
    # Desc: Puts the eyes in a squint
    # Pre: Needs a game display to have been declared
    # Post: Squints the eyes
    def squint(self, color):
        pygame.draw.rect(self.gD, color, (300, 400, 400, 100))
        pygame.draw.rect(self.gD, color, (900, 400, 400, 100))
    
        return 2

        
# used for testing, keeping for a little bit longer cause im lazy
#''' MAIN '''
#def main():
#    while True:
#        gameDisplay.fill(colBlack)
#        
#        ''' PERFORM ACTION '''
#        if ACTION == 'idle' or DONE:
#            time2Sleep = idle()
#            DONE = False
#            ACTION = randAction()
#        elif ACTION == 'blink':
#            down, intEyeHt, DONE, time2Sleep = blink(down, intEyeHt, DONE)
#        elif ACTION == 'squint':
#            time2Sleep = squint()
#            DONE = True
#    
#        for event in pygame.event.get():
#            if event.type == QUIT:
#                pygame.quit()
#                sys.exit()
#                
#            elif event.type == KEYDOWN:
#                if event.key == K_a:
#                    pygame.quit()
#                    sys.exit()
#                
#        pygame.display.update()
#        time.sleep(time2Sleep)
#        
#if __name__ == "__main__":
#    main()