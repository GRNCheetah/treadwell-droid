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

while True:

    Eyes.squint(gameDisplay, dispWH, colGreen)
    
    print(dispWH[0])
    
    pygame.display.update()
    