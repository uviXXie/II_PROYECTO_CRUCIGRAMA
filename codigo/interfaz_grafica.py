import sys
import pygame


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
fuente = pygame.font.SysFont('Times New Roman', 27)
fuente2 = pygame.font.SysFont('Times New Roman', 20)

# FUNCIONES DE PANTALLA
def initial_screen():
    """FUNTIONS THTAT SHOW THE INITIAL SCREEN

    Returns:
        buttons: pygame.Rect: Buttons of the screen
    """
    screen.fill((255, 255, 255))  # Fondo blanco

    # RECTÁNGULOS
    title = pygame.Rect(100, 75, 400, 45)
    start_button = pygame.Rect(274, 75, 45, 179)
    exit_button = pygame.Rect(210, 220, 109, 35)

    pygame.draw.rect(screen, (58, 188, 252), title)
    pygame.draw.rect(screen, (131, 240, 70), start_button)
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

    exit_message = [fuente.render("  E ", True, (0, 0, 0)),
                    fuente.render("  X ", True, (0, 0, 0)),
                    fuente.render("  I ", True, (0, 0, 0)),
                    fuente.render("   T", True, (0, 0, 0))]

    for i, letter in enumerate(exit_message):
        screen.blit(letter, (exit_button.x + (i * 20), exit_button.y + (exit_button.height - letter.get_height()) / 2))

    return start_button, exit_button

def screen_options():
    """FUNTIONS THTAT SHOW THE OPTIONS SCREEN
    """
    screen.fill((250, 250, 250))

    options_title = pygame.Rect(85, 20, 400, 45)
    predeterminate_crosswords = pygame.Rect(115, 85, 250, 35)
    create_crosswords = pygame.Rect(115, 130, 250, 35)
    back_button = pygame.Rect(350, 220, 150, 35)

    pygame.draw.rect(screen, (131, 240, 70 ), options_title)
    pygame.draw.rect(screen, (214, 134, 250), predeterminate_crosswords)
    pygame.draw.rect(screen, (214, 134, 250), create_crosswords)
    pygame.draw.rect(screen, (242, 75, 112), back_button)

    options_title_text = fuente.render(" G A M E    O P T I O N S", True, (0, 0, 0))
    screen.blit(options_title_text, (options_title.x + (options_title.width - options_title_text.get_width()) / 2,
                                     options_title.y + (options_title.height - options_title_text.get_height()) / 2))

    predeterminate_crosswords_button = fuente2.render("Predeterminated  crosswords", True, (0, 0, 0))
    screen.blit(predeterminate_crosswords_button, (predeterminate_crosswords.x + (predeterminate_crosswords.width - predeterminate_crosswords_button.get_width()) / 2,
                            predeterminate_crosswords.y + (predeterminate_crosswords.height - predeterminate_crosswords_button.get_height()) / 2))

    create_crosswords_button = fuente2.render("Create your own crosswords", True, (0, 0, 0))
    screen.blit(create_crosswords_button, (create_crosswords.x + (create_crosswords.width - create_crosswords_button.get_width()) / 2,
                            create_crosswords.y + (create_crosswords.height - create_crosswords_button.get_height()) / 2))
    
    back_button_text = fuente2.render("Initial screen", True, (0, 0, 0))
    screen.blit(back_button_text, (back_button.x + (back_button.width - back_button_text.get_width()) / 2,
                            back_button.y + (back_button.height - back_button_text.get_height()) / 2))
    pygame.display.update()
    return predeterminate_crosswords, create_crosswords, back_button
def create_crosswords():
    """FUNTIONS THTAT SHOW THE OPTIONS SCREEN
    """
    screen.fill((250, 250, 250))


# Bucle principal del juego
current_screen = "initial"
running = True
start_button = None
exit_button = None
########
#pasar los botones necesarios = screen_options()
########
predeterminate_crosswords_button = None
create_crosswords_button = None
back_button = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if current_screen == "initial" and start_button and exit_button:
                if exit_button.collidepoint(event.pos):
                    running = False
                elif start_button.collidepoint(event.pos):
                    current_screen = "options"
            elif current_screen == "options" and predeterminate_crosswords_button and create_crosswords_button and back_button:
                if back_button.collidepoint(event.pos):
                    current_screen = "initial"
                elif predeterminate_crosswords_button.collidepoint(event.pos):
                    current_screen = "initial"
                elif create_crosswords_button.collidepoint(event.pos):
                    current_screen = "create_crosswords"
    if current_screen == "initial":
        start_button, exit_button = initial_screen()
    elif current_screen == "options":
        screen_options()
        predeterminate_crosswords_button, create_crosswords_button, back_button = screen_options()
       #pasar los botones necesarios = screen_options()
    elif current_screen == "create_crosswords":
        create_crosswords()


    pygame.display.flip()

pygame.quit()
sys.exit()
