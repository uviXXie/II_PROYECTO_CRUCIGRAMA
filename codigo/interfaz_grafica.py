import sys
import pygame 
pygame.init()
#PANTALLA
width = 800
height = 600
screen = pygame.display.set_mode((width, height))  
pygame.display.set_caption("JUEGO CRUCIGRAMA3D")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#LOOP DE LA PANTALLA

run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()

