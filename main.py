# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import constants
from constants import *
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def main():
    pygame.init()
    #print("Starting Asteroids!")
    #print("Screen width:", constants.SCREEN_WIDTH,)
    #print("Screen height:", constants.SCREEN_HEIGHT,)
    while True != False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        pygame.display.flip()

if __name__ == "__main__":
    main()
