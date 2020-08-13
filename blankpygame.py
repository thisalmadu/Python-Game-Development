import pygame, sys
from pygame.locals import * # IMPORTING THE PYGAME MODULE

pygame.init() # always need to be called after importing the pygame module and before calling any other Pygame function
DISPLAYSURF = pygame.display.set_mode((400,300)) # returns the pygame.Surface object for the window.This tuple tells the set_mode() function how wide and how high to make the window in pixels. (400, 300) will make a window with a width of 400 pixels and height of 300 pixels.
pygame.display.set_caption('Welcome to the Game!')
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
