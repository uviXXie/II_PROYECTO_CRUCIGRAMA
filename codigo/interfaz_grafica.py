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


def initial_screen():

# FUENTES
    fuente = pygame.font.SysFont('Arial', 30)

    # RECTÁNGULOS
    title = pygame.Rect(100, 75, 400, 45)
    start_button = pygame.Rect(274, 75, 45, 179)  
    exit_button = pygame.Rect(210, 220, 109, 35)  

    pygame.draw.rect(screen, (58, 188, 252), title)
    pygame.draw.rect(screen, (52, 148, 252), start_button)
    pygame.draw.rect(screen, (252, 52, 75), exit_button)


    pygame.draw.rect(screen, (0, 0, 0), start_button, 2) 
    pygame.draw.rect(screen, (0, 0, 0), exit_button, 2)  
    pygame.draw.rect(screen, (0, 0, 0), title, 2) 

    title_text = fuente.render("3  D  C  R  O  S  S  W  O  R  D", True, (0, 0, 0))
    screen.blit(title_text, (title.x + (title.width - title_text.get_width()) / 2,
                            title.y + (title.height - title_text.get_height()) / 2))

    tar_message = [fuente.render("T", True, (0, 0, 0)),
                fuente.render("A", True, (0, 0, 0)),
                fuente.render("R", True, (0, 0, 0))]

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
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        if start_button.collidepoint(pygame.mouse.get_pos()):
            print("START")
        if exit_button.collidepoint(pygame.mouse.get_pos()):
            print("EXIT")
            pygame.quit()
            sys.exit()
def screen_options():
    fuente = pygame.font.SysFont('Arial', 30)

    
    options_title = pygame.Rect(75, 20, 400, 45)
    predeterminate_crosswords = pygame.Rect(100, 65, 300, 45)  
    create_crosswords = pygame.Rect(100,110 , 100, 35)  
    back_button = pygame.Rect(100, 220, 100, 35)

    pygame.draw.rect(screen, (58, 188, 252), options_title)
    pygame.draw.rect(screen, (52, 148, 252), predeterminate_crosswords)
    pygame.draw.rect(screen, (252, 52, 75), create_crosswords)
    pygame.draw.rect(screen, (252, 52, 75), back_button)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # 3 valores rgb
    screen.fill((255, 199, 188))
    initial_screen()
    pygame.display.update()

pygame.quit()
