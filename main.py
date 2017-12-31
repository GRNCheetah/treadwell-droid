import Eyes

import pygame

pygame.init()
pygame.mixer.pre_init()

''' COLORS '''
colGreen = pygame.Color(0,255,0)
colBlack = pygame.Color(0,0,0)

''' GAME DISPLAY '''
# (width, height)
dispWH = (1600,900)

gameDisplay = pygame.display.set_mode(dispWH,pygame.FULLSCREEN, 32)
pygame.display.set_caption("Treadwell")

screen = Eyes.Eyes(gameDisplay)


while True:
    # Reset for the screen, I want this in the Eyes.py file
    gameDisplay.fill(colBlack)

    screen.blink(colGreen)

    
    pygame.display.update()
    