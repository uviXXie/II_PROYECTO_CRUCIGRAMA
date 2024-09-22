import sys
import pygame
import os

print(os.getcwd())

pygame.init()

# PANTALLA
width = 550
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CRUCIGRAMA3D")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# FUENTES
fuente = pygame.font.SysFont('Arial', 30)

# RECTÁNGULOS
title = pygame.Rect(100, 75, 400, 45)
start_button = pygame.Rect(274, 75, 45, 179)  # Botón de START
exit_button = pygame.Rect(210, 220, 109, 35)  # Botón de EXIT

# LOOP DE LA PANTALLA
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 3 valores rgb
    screen.fill((255, 199, 188))
    pygame.draw.rect(screen, (58, 188, 252), title)
    pygame.draw.rect(screen, (52, 148, 252), start_button)
    pygame.draw.rect(screen, (252, 52, 75), exit_button)

    # DIBUJAR RECTÁNGULOS NEGROS ALREDEDOR DE LOS BOTONES
    pygame.draw.rect(screen, (0, 0, 0), start_button, 2)  # Borde negro alrededor del botón START
    pygame.draw.rect(screen, (0, 0, 0), exit_button, 2)   # Borde negro alrededor del botón EXIT
    pygame.draw.rect(screen, (0, 0, 0), title, 2) 
    # TÍTULO "3D CROSSWORD"
    title_text = fuente.render("3  D  C  R  O  S  S  W  O  R  D", True, (0, 0, 0))
    screen.blit(title_text, (title.x + (title.width - title_text.get_width()) / 2,
                              title.y + (title.height - title_text.get_height()) / 2))

    # MENSAJES CON FORMATO DE CRUCIGRAMA
    # "TAR" en forma vertical, centrado en el botón
    tar_message = [fuente.render("T", True, (0, 0, 0)),
                   fuente.render("A", True, (0, 0, 0)),
                   fuente.render("R", True, (0, 0, 0))]

    # DIBUJAR LETRAS EN FORMATO DE CRUCIGRAMA
    # "TAR" en forma vertical
    for i, letter in enumerate(tar_message):
        screen.blit(letter, (start_button.x + (start_button.width - letter.get_width()) / 2,
                             start_button.y + (start_button.height - letter.get_height()) / 2 - 30 + i * 35))

    # "EXIT" en forma horizontal
    exit_message = [fuente.render("  E ", True, (0, 0, 0)),
                    fuente.render("  X ", True, (0, 0, 0)),
                    fuente.render("  I ", True, (0, 0, 0)),
                    fuente.render("   T", True, (0, 0, 0))]

    for i, letter in enumerate(exit_message):
        screen.blit(letter, (exit_button.x + (i * 20), exit_button.y + (exit_button.height - letter.get_height()) / 2))

    pygame.display.update()

pygame.quit()
