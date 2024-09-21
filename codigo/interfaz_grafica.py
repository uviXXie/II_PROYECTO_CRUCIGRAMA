import sys
import pygame 
import os
print(os.getcwd())

pygame.init()
#PANTALLA
width = 550
height = 300
screen = pygame.display.set_mode((width, height))  
pygame.display.set_caption("CRUCIGRAMA3D")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
##########dibujos#######
title = pygame.Rect(100,75, 400,45)
##########BOTONES###########
start_button = pygame.Rect(270,74,45,175)
exit_button = pygame.Rect(170,204,146,45)
#LOOP DE LA PANTALLA

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #3 valores rgb
    screen.fill((255, 199, 188))
    pygame.draw.rect(screen,(58, 188, 252 ), title)
    pygame.draw.rect(screen,(52, 148, 252 ), start_button)
    pygame.draw.rect(screen,(252, 52, 75 ), exit_button)
    exit_message = fuente.render("EXIT",True,(0, 0, 0 ))
    start_message = fuente.render("START",True,(0, 0, 0  ))
    screen.blit

    pygame.display.update()


pygame.quit()

