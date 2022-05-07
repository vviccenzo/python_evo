import pygame
import math
pygame.init()

#Putting the width and height of the screen
WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Inserting the main title of the game
pygame.display.set_caption("Planet Simulation")



def main():
    run = True
    
    while run:
        for event in pygame.event.get():
            #If the user clicks the X button, the game will close
            if event.type == pygame.QUIT:
                run = False
    
    #Closing the game
    pygame.quit()

main()