import sys
import pygame
import random
import numpy as np
from acomodador_automatico import all  # Aquí importamos el acomodador automático

#
# INICIALIZACIÓN

pygame.init()

# PANTALLA
width = 550
height = 300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CRUCIGRAMA3D")
icon = pygame.image.load('II_PROYECTO_CRUCIGRAMA-main/icon.png')
pygame.display.set_icon(icon)

# FUENTES
fuente = pygame.font.SysFont('Times New Roman', 27)
fuente2 = pygame.font.SysFont('Times New Roman', 20)

# Función para crear la matriz y llamar al acomodador automático
def create_crossword_matrix(mode):
    words = ["python", "code", "pip", "world", "thing", "frontend", "back", "server"]  # Palabras de ejemplo
    if mode == "easy":
        matrix_size = (6, 6, 6)  # Fácil: 6x6x6
    elif mode == "medium":
        matrix_size = (12, 12, 12)  # Medio: 12x12x12
    elif mode == "hard":
        matrix_size = (24, 24, 24)  # Difícil: 24x24x24

    matrix = all(matrix_size[0], words)  # Llamar al acomodador automático
    return matrix

def draw_crossword_3d(matrix):
    cell_size = 30
    offset_x, offset_y = 100, 100  # Ajustar offset para dar más espacio a los ejes

    rows = len(matrix)  # Eje Y (número de filas)
    cols = len(matrix[0])  # Eje X (número de columnas)
    depth = len(matrix[0][0])  # Eje Z (número de capas)

    # Definir los colores
    colors_by_axis = {
        'x': (255, 165, 0),  # Naranja para palabras en el eje X
        'z': (144, 238, 144),  # Verde claro para palabras en el eje Z
        'y': (173, 216, 230),  # Azul claro para el eje Y
        'intersection': (255, 0, 0)  # Rojo para el punto de intersección
    }

    mid_point = cols // 2  # Punto medio para la separación entre X y Z

    fuente_ejes = pygame.font.SysFont('Arial', 20)

    # Dibujar fondo para los ejes X, Z y Y, y marcar el punto de intersección
    for x in range(cols):
        # Del 0 hasta el punto medio, corresponde al eje X (naranja)
        if x < mid_point:
            pygame.draw.rect(screen, colors_by_axis['x'], pygame.Rect(offset_x + x * cell_size, offset_y - 50, cell_size, 50))
        # Del punto medio hasta el final, corresponde al eje Z (verde claro)
        else:
            pygame.draw.rect(screen, colors_by_axis['z'], pygame.Rect(offset_x + x * cell_size, offset_y - 50, cell_size, 50))

    # Dibujar el punto de intersección en rojo (donde X y Z se separan)
    pygame.draw.rect(screen, colors_by_axis['intersection'], pygame.Rect(offset_x + mid_point * cell_size, offset_y - 50, cell_size, 50))

    # Dibujar fondo para el eje Y (azul claro)
    for y in range(rows):
        pygame.draw.rect(screen, colors_by_axis['y'], pygame.Rect(offset_x - 50, offset_y + y * cell_size, 50, cell_size))

    # Etiquetas del eje X (naranja)
    for x in range(mid_point):
        text = fuente_ejes.render(str(x), True, (0, 0, 0))
        screen.blit(text, (offset_x + x * cell_size + 10, offset_y - 30))
    
    # Etiquetas del eje Z (verde claro)
    for z in range(mid_point, cols):
        text = fuente_ejes.render(str(z), True, (0, 0, 0))
        screen.blit(text, (offset_x + z * cell_size + 10, offset_y - 30))

    # Etiquetas del eje Y (azul claro)
    for y in range(rows):
        text = fuente_ejes.render(str(y), True, (0, 0, 0))
        screen.blit(text, (offset_x - 30, offset_y + y * cell_size + 10))

    # Dibujar las celdas de la matriz
    for x in range(rows):  # Eje Y
        for y in range(cols):  # Eje X
            for z in range(depth):  # Eje Z
                char = matrix[x][y][z]  # Obtener el carácter en la celda (x, y, z)

                # Determinar el color de las celdas en función de si están en el eje X o Z
                if y < mid_point:  # Eje X
                    color = colors_by_axis['x']
                elif y >= mid_point:  # Eje Z
                    color = colors_by_axis['z']
                else:
                    color = (255, 255, 255)  # Fondo blanco para celdas vacías

                # Dibujar un rectángulo para cada celda, incluso si está vacía
                rect = pygame.Rect(offset_x + y * cell_size, offset_y + x * cell_size, cell_size, cell_size)
                pygame.draw.rect(screen, color, rect, 0 if char != ' ' else 1)  # Relleno solo si hay una letra

                # Dibujar el borde de la celda
                pygame.draw.rect(screen, (0, 0, 0), rect, 2)

                # Si hay una letra, dibujarla
                if char != ' ':
                    text = fuente.render(char, True, (0, 0, 0))
                    text_rect = text.get_rect(center=rect.center)
                    screen.blit(text, text_rect)

    pygame.display.update()


# FUNCIONES DE PANTALLA
def initial_screen():
    """FUNTIONS THTAT SHOW THE INITIAL SCREEN

    Returns:
        start_button: pygame.Rect: Button of the screen, 
        exit_button: pygame.Rect: Button of the screen
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

    Returns:   back_button: pygame.Rect: Button of the screen, 
    predeterminate_crosswords: pygame.Rect: Button of the screen, 
    create_crosswords: pygame.Rect: Button
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

    pygame.draw.rect(screen, (0, 0, 0), options_title, 2)
    pygame.draw.rect(screen, (0, 0, 0), predeterminate_crosswords, 2)
    pygame.draw.rect(screen, (0, 0, 0), create_crosswords, 2)
    pygame.draw.rect(screen, (0, 0, 0), back_button, 2)

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
def create_crosswords_screen():
    """SHOWS THE MODES TO CREATE NEW CROSSWORDS

    Returns:   screen_options_button: pygame.Rect: Button of the screen, 
    easy_mode_button: pygame.Rect: Button of the screen,
    medium_mode_button: pygame.Rect: Button of the screen,
    hard_mode_button: pygame.Rect: Button of the screen
    """
    screen.fill((250, 250, 250))

    create_crosswords_title = pygame.Rect(85, 20, 420, 45)
    easy_mode_button = pygame.Rect(115, 85, 250, 35)
    medium_mode_button = pygame.Rect(115, 130, 250, 35)
    hard_mode_button = pygame.Rect(115, 175, 250, 35)
    screen_options_button = pygame.Rect(350, 220, 150, 35)

    pygame.draw.rect(screen, (131, 240, 70 ), create_crosswords_title)
    pygame.draw.rect(screen, (242, 75, 112), screen_options_button)
    pygame.draw.rect(screen, (214, 134, 250), easy_mode_button)
    pygame.draw.rect(screen, (214, 134, 250), medium_mode_button)
    pygame.draw.rect(screen, (214, 134, 250), hard_mode_button)

    pygame.draw.rect(screen, (0, 0, 0), create_crosswords_title, 2)
    pygame.draw.rect(screen, (0, 0, 0), screen_options_button, 2)
    pygame.draw.rect(screen, (0, 0, 0), easy_mode_button, 2)
    pygame.draw.rect(screen, (0, 0, 0), medium_mode_button, 2)
    pygame.draw.rect(screen, (0, 0, 0), hard_mode_button, 2)

    create_crosswords_title_text = fuente.render(" C R E A T E   C R O S S W O R D S", True, (0, 0, 0))
    screen.blit(create_crosswords_title_text, (create_crosswords_title.x + (create_crosswords_title.width - create_crosswords_title_text.get_width()) / 2,
            create_crosswords_title.y + (create_crosswords_title.height - create_crosswords_title_text.get_height()) / 2)) 
    screen_options_button_text = fuente2.render("Screen options", True, (0, 0, 0))
    screen.blit(screen_options_button_text, (screen_options_button.x + (screen_options_button.width - screen_options_button_text.get_width()) / 2,
            screen_options_button.y + (screen_options_button.height - screen_options_button_text.get_height()) / 2))    
    easy_mode_button_text = fuente2.render("Easy mode (6 x 6)", True, (0, 0, 0))
    screen.blit(easy_mode_button_text, (easy_mode_button.x + (easy_mode_button.width - easy_mode_button_text.get_width()) / 2,
            easy_mode_button.y + (easy_mode_button.height - easy_mode_button_text.get_height()) / 2))
    medium_mode_button_text = fuente2.render("Medium mode (12 x 12)", True, (0, 0, 0))
    screen.blit(medium_mode_button_text, (medium_mode_button.x + (medium_mode_button.width - medium_mode_button_text.get_width()) / 2,
            medium_mode_button.y + (medium_mode_button.height - medium_mode_button_text.get_height()) / 2))
    hard_mode_button_text = fuente2.render("Hard mode (24 x 24)", True, (0, 0, 0))    
    screen.blit(hard_mode_button_text, (hard_mode_button.x + (hard_mode_button.width - hard_mode_button_text.get_width()) / 2,
            hard_mode_button.y + (hard_mode_button.height - hard_mode_button_text.get_height()) / 2))

    pygame.display.update()

    return screen_options_button, easy_mode_button, medium_mode_button, hard_mode_button
def created_crosswords_screen():
    """SHOW THE MODES OF THE CREATED CROSSWORDS

    Returns:
        _type_: _description_
    """

    create_crosswords_title = pygame.Rect(60, 10, 450, 70)
    easy_mode = pygame.Rect(115, 85, 250, 35)
    medium_mode = pygame.Rect(115, 130, 250, 35)
    hard_mode = pygame.Rect(115, 175, 250, 35)
    screen_options_button = pygame.Rect(350, 220, 150, 35)

    pygame.draw.rect(screen, (131, 240, 70 ), create_crosswords_title)
    pygame.draw.rect(screen, (242, 75, 112), screen_options_button)
    pygame.draw.rect(screen, (214, 134, 250), easy_mode)
    pygame.draw.rect(screen, (214, 134, 250), medium_mode)
    pygame.draw.rect(screen, (214, 134, 250), hard_mode)

    pygame.draw.rect(screen, (0, 0, 0), create_crosswords_title, 2)
    pygame.draw.rect(screen, (0, 0, 0), screen_options_button, 2)
    pygame.draw.rect(screen, (0, 0, 0), easy_mode, 2)
    pygame.draw.rect(screen, (0, 0, 0), medium_mode, 2)
    pygame.draw.rect(screen, (0, 0, 0), hard_mode, 2)

    create_crosswords_title_text = fuente.render(" P R E D E TE R M I N A T E D ", True, (0, 0, 0))
    create_crosswords_title_text2 = fuente.render(" C R O S S W O R D S", True, (0, 0, 0))
    screen.blit(create_crosswords_title_text, (create_crosswords_title.x + (create_crosswords_title.width - create_crosswords_title_text.get_width()) / 2,
            create_crosswords_title.y + (create_crosswords_title.height - create_crosswords_title_text.get_height()) / 2 - 10))
    screen.blit(create_crosswords_title_text2, (create_crosswords_title.x + (create_crosswords_title.width - create_crosswords_title_text2.get_width()) / 2,
            create_crosswords_title.y + (create_crosswords_title.height - create_crosswords_title_text2.get_height()) / 2 + 20))
    screen_options_button_text = fuente2.render("Screen options", True, (0, 0, 0))
    screen.blit(screen_options_button_text, (screen_options_button.x + (screen_options_button.width - screen_options_button_text.get_width()) / 2,
            screen_options_button.y + (screen_options_button.height - screen_options_button_text.get_height()) / 2))
    easy_mode_text = fuente2.render("Easy mode (6 x 6)", True, (0, 0, 0))
    screen.blit(easy_mode_text, (easy_mode.x + (easy_mode.width - easy_mode_text.get_width()) / 2,
            easy_mode.y + (easy_mode.height - easy_mode_text.get_height()) / 2))
    medium_mode_text = fuente2.render("Medium mode (12 x 12)", True, (0, 0, 0))
    screen.blit(medium_mode_text, (medium_mode.x + (medium_mode.width - medium_mode_text.get_width()) / 2,
            medium_mode.y + (medium_mode.height - medium_mode_text.get_height()) / 2))
    hard_mode_text = fuente2.render("Hard mode (24 x 24)", True, (0, 0, 0))
    screen.blit(hard_mode_text, (hard_mode.x + (hard_mode.width - hard_mode_text.get_width()) / 2,
            hard_mode.y + (hard_mode.height - hard_mode_text.get_height()) / 2))


    return screen_options_button, easy_mode, medium_mode, hard_mode
# VARIABLES
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
########
#pasar los botones necesarios = create_crosswords_screen()
########
screen_options_button = None
easy_mode_button = None
medium_mode_button = None
hard_mode_button = None
########
#pasar los botones necesarios = created_crosswords_screen()
########
screen_options_button = None
easy_mode= None
medium_mode = None
hard_mode = None

matrix = None

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
                    current_screen = "created_crosswords"
                elif create_crosswords_button.collidepoint(event.pos):
                    current_screen = "create_crosswords"
            elif current_screen == "create_crosswords" and screen_options_button and easy_mode_button and medium_mode_button and hard_mode_button:
                if screen_options_button.collidepoint(event.pos):
                    current_screen = "options"
                elif easy_mode_button.collidepoint(event.pos):
                    matrix = create_crossword_matrix("easy")  # Genera la matriz fácil
                    current_screen = "show_crossword"  # Cambia de pantalla para mostrar el crucigrama
                elif medium_mode_button.collidepoint(event.pos):
                    matrix = create_crossword_matrix("medium")  # Genera la matriz media
                    current_screen = "show_crossword"
                elif hard_mode_button.collidepoint(event.pos):
                    matrix = create_crossword_matrix("hard")  # Genera la matriz difícil
                    current_screen = "show_crossword"
            elif current_screen == "created_crosswords" and screen_options_button and easy_mode and medium_mode and hard_mode:
                if screen_options_button.collidepoint(event.pos):
                    current_screen = "options"
                elif easy_mode.collidepoint(event.pos):
                    matrix = create_crossword_matrix("easy")
                    current_screen = "show_crossword"
                elif medium_mode.collidepoint(event.pos):
                    matrix = create_crossword_matrix("medium")
                    current_screen = "show_crossword"
                elif hard_mode.collidepoint(event.pos):
                    matrix = create_crossword_matrix("hard")
                    current_screen = "show_crossword"
    if current_screen == "initial":
        start_button, exit_button = initial_screen()
    elif current_screen == "options":
        screen_options()
        predeterminate_crosswords_button, create_crosswords_button, back_button = screen_options()
    elif current_screen == "create_crosswords":
        screen_options_button, easy_mode_button, medium_mode_button, hard_mode_button = create_crosswords_screen()
    elif current_screen == "created_crosswords":
        screen_options_button, easy_mode, medium_mode, hard_mode = created_crosswords_screen()
    elif current_screen == "show_crossword":
        screen.fill((255, 255, 255))  # Limpia la pantalla antes de mostrar el crucigrama
        draw_crossword_3d(matrix)  # Dibujar la capa actual Z

    pygame.display.flip()

pygame.quit()
sys.exit()