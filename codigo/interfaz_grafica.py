import sys
import pygame
from acomodador_automatico import all
from cara_xy import cara_xy
from cara_yz import cara_yz
#
# INICIALIZACIÓN

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
fuente3 = pygame.font.SysFont('Times New Roman', 15)




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
    screen.fill((250, 250, 250))

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
def level_easy_screen_1() -> pygame.Rect:
    """NUMBER ONE LEVEL OF THE CROSSWORDS PRE CREATED

    Returns:
        buttons
    """
    screen.fill((250, 250, 250))
    
    level_title = pygame.Rect(60, 10, 300, 45)
    face_button_xy = pygame.Rect(450, 10, 45, 35)
    back_button_1 = pygame.Rect(350, 240, 150, 35)
    word1_puzzle = pygame.Rect(15, 85, 250, 50)
    word2_puzzle = pygame.Rect(15, 130, 250, 50)
    word3_puzzle = pygame.Rect(15, 175, 250, 50)
    word4_puzzle = pygame.Rect(285, 85, 250, 50)
    word5_puzzle = pygame.Rect(285, 130, 250, 50)
    word6_puzzle  = pygame.Rect(285, 175, 250, 50)
    
    

    pygame.draw.rect(screen, (131, 240, 70 ), level_title)
    pygame.draw.rect(screen, (242, 75, 112), face_button_xy)
    pygame.draw.rect(screen, (242, 75, 112), back_button_1)
    pygame.draw.rect(screen, (214, 134, 250), word1_puzzle)
    pygame.draw.rect(screen, (214, 134, 250), word2_puzzle)
    pygame.draw.rect(screen, (214, 134, 250), word3_puzzle)
    pygame.draw.rect(screen, (214, 134, 250), word4_puzzle)
    pygame.draw.rect(screen, (214, 134, 250), word5_puzzle)
    pygame.draw.rect(screen, (214, 134, 250), word6_puzzle)
    

    pygame.draw.rect(screen, (0, 0, 0), level_title, 2)
    pygame.draw.rect(screen, (0, 0, 0), back_button_1, 2)
    pygame.draw.rect(screen, (0, 0, 0), face_button_xy, 2)

    pygame.draw.rect(screen, (0, 0, 0), word1_puzzle, 2)
    pygame.draw.rect(screen, (0, 0, 0), word2_puzzle, 2)
    pygame.draw.rect(screen, (0, 0, 0), word3_puzzle, 2)
    pygame.draw.rect(screen, (0, 0, 0), word4_puzzle, 2)
    pygame.draw.rect(screen, (0, 0, 0), word5_puzzle, 2)
    pygame.draw.rect(screen, (0, 0, 0), word6_puzzle, 2)
    

    level_title_text = fuente.render(" C O U N T R I E S", True, (0, 0, 0))
    screen.blit(level_title_text, (level_title.x + (level_title.width - level_title_text.get_width()) / 2,
        level_title.y + (level_title.height - level_title_text.get_height()) / 2 - 10))
    

    face_button_xy_text = fuente2.render("CRW", True, (0, 0, 0))
    screen.blit(face_button_xy_text, (face_button_xy.x + (face_button_xy.width - face_button_xy_text.get_width()) / 2,
        face_button_xy.y + (face_button_xy.height - face_button_xy_text.get_height()) / 2))


    screen_options_button_text = fuente2.render("B A C K ", True, (0, 0, 0))
    screen.blit(screen_options_button_text, (back_button_1.x + (back_button_1.width - screen_options_button_text.get_width()) / 2,
        back_button_1.y + (back_button_1.height - screen_options_button_text.get_height()) / 2))    
    
    word1_puzzle_text = fuente3.render("1. Citys of love country", True, (0, 0, 0))
    screen.blit(word1_puzzle_text, (word1_puzzle.x + (word1_puzzle.width - word1_puzzle_text.get_width()) / 2,
        word1_puzzle.y + (word1_puzzle.height - word1_puzzle_text.get_height()) / 2))
    
    word2_puzzle_text = fuente3.render("2. The country the Taj Mahal ", True, (0, 0, 0))
    screen.blit(word2_puzzle_text, (word2_puzzle.x + (word2_puzzle.width - word2_puzzle_text.get_width()) / 2,
        word2_puzzle.y + (word2_puzzle.height - word2_puzzle_text.get_height()) / 2))   
    
    word3_puzzle_text = fuente3.render("3. Country of the rising sun", True, (0, 0, 0))
    screen.blit(word3_puzzle_text, (word3_puzzle.x + (word3_puzzle.width - word3_puzzle_text.get_width()) / 2,
       word3_puzzle.y + (word3_puzzle.height - word3_puzzle_text.get_height()) / 2))
    
    word4_puzzle_text = fuente3.render("4. The country of the sphinx", True, (0, 0, 0))
    screen.blit(word4_puzzle_text, (word4_puzzle.x + (word4_puzzle.width - word4_puzzle_text.get_width()) / 2,
        word4_puzzle.y + (word4_puzzle.height - word4_puzzle_text.get_height()) / 2))       
    
    word5_puzzle_text = fuente3.render("5. The country of the kangaroos", True, (0, 0, 0))
    screen.blit(word5_puzzle_text, (word5_puzzle.x + (word5_puzzle.width - word5_puzzle_text.get_width()) / 2,
        word5_puzzle.y + (word5_puzzle.height - word5_puzzle_text.get_height()) / 2))
    
    word6_puzzle_text = fuente3.render("6. The country of the carnivals", True, (0, 0, 0))
    screen.blit(word6_puzzle_text, (word6_puzzle.x + (word6_puzzle.width - word6_puzzle_text.get_width()) / 2,
        word6_puzzle.y + (word6_puzzle.height - word6_puzzle_text.get_height()) / 2))
    
    

    return back_button_1, face_button_xy

def easy_mode_xy(size:int, matrix: list) -> pygame.Rect:
    """SHOWS THE CROSSWORDS IN XY

    Args:
        matrix (list): matrix to show

    Returns:
        xy_hints: pygame.Rect: Button of the screen
    """
    
    face_xy = cara_xy(size, matrix)

    screen.fill((250, 250, 250))

    xy_hints = pygame.Rect(450, 10, 60, 40)
    to_yz = pygame.Rect(450, 60, 60, 40)


    pygame.draw.rect(screen, (226, 130, 255), xy_hints, 2)
    pygame.draw.rect(screen, (226, 130, 255), to_yz, 2)

    pygame.draw.rect(screen, (0, 0, 0), xy_hints, 2)
    pygame.draw.rect(screen, (0, 0, 0), to_yz, 2)



    xy_hints_text = fuente2.render("HINTS", True, (0, 0, 0))
    screen.blit(xy_hints_text, (xy_hints.x + (xy_hints.width - xy_hints_text.get_width()) / 2,
        xy_hints.y + (xy_hints.height - xy_hints_text.get_height()) / 2))

    to_yz_text = fuente2.render("YZ", True, (0, 0, 0))
    screen.blit(to_yz_text, (to_yz.x + (to_yz.width - to_yz_text.get_width()) / 2,
        to_yz.y + (to_yz.height - to_yz_text.get_height()) / 2))

    return xy_hints, to_yz
def easy_mode_yz(size: int, matrix: list) -> pygame.Rect:
    """SHOWS THE CROSSWORDS IN YZ

    Args:
        matrix (list): matrix to show

    Returns:
        yz_hints: pygame.Rect: Button of the screen
    """
    
    face_yz = cara_yz(size, matrix)

    screen.fill((250, 250, 250))

    yz_hints = pygame.Rect(450, 10, 60, 40)
    to_xy = pygame.Rect(450, 60, 60, 40)



    pygame.draw.rect(screen, (226, 130, 255), yz_hints, 2)
    pygame.draw.rect(screen, (226, 130, 255), to_xy, 2)

    pygame.draw.rect(screen, (0, 0, 0), yz_hints, 2)
    pygame.draw.rect(screen, (0, 0, 0), to_xy, 2)


    yz_hints_text = fuente2.render("HINTS", True, (0, 0, 0))
    screen.blit(yz_hints_text, (yz_hints.x + (yz_hints.width - yz_hints_text.get_width()) / 2,
        yz_hints.y + (yz_hints.height - yz_hints_text.get_height()) / 2))
    
    to_xy_text = fuente2.render("XY", True, (0, 0, 0))
    screen.blit(to_xy_text, (to_xy.x + (to_xy.width - to_xy_text.get_width()) / 2,
        to_xy.y + (to_xy.height - to_xy_text.get_height()) / 2))
    
    return yz_hints, to_xy
def level_med_screen() -> pygame.Rect :

    """SHOWS THE SECOND LEVEL OF THE CROSSWORDS

    Returns:
        
    """
    screen.fill((250, 250, 250))
    
    level_title = pygame.Rect(60, 10, 300, 45)
    button_xy_med_pre = pygame.Rect(450, 10, 45, 35)
    next_button = pygame.Rect(25, 240, 35, 35)
    back_button_2 = pygame.Rect(350, 240, 150, 35)
    word1_puzzle = pygame.Rect(15, 85, 250, 50)
    word2_puzzle = pygame.Rect(15, 130, 250, 50)
    word3_puzzle = pygame.Rect(15, 175, 250, 50)
    word4_puzzle = pygame.Rect(285, 85, 250, 50)
    word5_puzzle = pygame.Rect(285, 130, 250, 50)
    word6_puzzle  = pygame.Rect(285, 175, 250, 50)
    

    pygame.draw.rect(screen, (131, 240, 70 ), level_title)
    pygame.draw.rect(screen, (242, 75, 112), button_xy_med_pre)
    pygame.draw.rect(screen, (242, 75, 112), back_button_2)
    pygame.draw.rect(screen, (242, 75, 112), next_button)
    pygame.draw.rect(screen, (214, 134, 250), word1_puzzle)
    pygame.draw.rect(screen, (214, 134, 250), word2_puzzle)
    pygame.draw.rect(screen, (214, 134, 250), word3_puzzle)
    pygame.draw.rect(screen, (214, 134, 250), word4_puzzle)
    pygame.draw.rect(screen, (214, 134, 250), word5_puzzle)
    pygame.draw.rect(screen, (214, 134, 250), word6_puzzle)
    

    pygame.draw.rect(screen, (0, 0, 0), level_title, 2)
    pygame.draw.rect(screen, (0, 0, 0), back_button_2, 2)
    pygame.draw.rect(screen, (0, 0, 0), button_xy_med_pre, 2)
    pygame.draw.rect(screen, (0, 0, 0), next_button, 2)
    pygame.draw.rect(screen, (0, 0, 0), word1_puzzle, 2)
    pygame.draw.rect(screen, (0, 0, 0), word2_puzzle, 2)
    pygame.draw.rect(screen, (0, 0, 0), word3_puzzle, 2)
    pygame.draw.rect(screen, (0, 0, 0), word4_puzzle, 2)
    pygame.draw.rect(screen, (0, 0, 0), word5_puzzle, 2)
    pygame.draw.rect(screen, (0, 0, 0), word6_puzzle, 2)

    level_title_text = fuente.render("SOLAR SISTEM", True, (0, 0, 0))
    screen.blit(level_title_text, (level_title.x + (level_title.width - level_title_text.get_width()) / 2,
        level_title.y + (level_title.height - level_title_text.get_height()) / 2 - 10))
    
    button_xy_med_pre_text = fuente2.render("CRW", True, (0, 0, 0))
    screen.blit(button_xy_med_pre_text, (button_xy_med_pre.x + (button_xy_med_pre.width - button_xy_med_pre_text.get_width()) / 2,
        button_xy_med_pre.y + (button_xy_med_pre.height - button_xy_med_pre_text.get_height()) / 2))

    next_button_text = fuente2.render("->", True, (0, 0, 0))
    screen.blit(next_button_text, (next_button.x + (next_button.width - next_button_text.get_width()) / 2,
        next_button.y + (next_button.height - next_button_text.get_height()) / 2))

    back_button_2_text = fuente2.render("B A C K ", True, (0, 0, 0))
    screen.blit(back_button_2_text, (back_button_2.x + (back_button_2.width - back_button_2_text.get_width()) / 2,
        back_button_2.y + (back_button_2.height - back_button_2_text.get_height()) / 2))

    word1_puzzle_text = fuente3.render("1. The planet of the rings", True, (0, 0, 0))
    screen.blit(word1_puzzle_text, (word1_puzzle.x + (word1_puzzle.width - word1_puzzle_text.get_width()) / 2,  
        word1_puzzle.y + (word1_puzzle.height - word1_puzzle_text.get_height()) / 2))
    
    word2_puzzle_text = fuente3.render("2. The red planet", True, (0, 0, 0))
    screen.blit(word2_puzzle_text, (word2_puzzle.x + (word2_puzzle.width - word2_puzzle_text.get_width()) / 2,
        word2_puzzle.y + (word2_puzzle.height - word2_puzzle_text.get_height()) / 2))
    
    word3_puzzle_text = fuente3.render("3. The planet of love", True, (0, 0, 0))
    screen.blit(word3_puzzle_text, (word3_puzzle.x + (word3_puzzle.width - word3_puzzle_text.get_width()) / 2,
        word3_puzzle.y + (word3_puzzle.height - word3_puzzle_text.get_height()) / 2))
    
    word4_puzzle_text = fuente3.render("4. The planet of the blue color", True, (0, 0, 0))
    screen.blit(word4_puzzle_text, (word4_puzzle.x + (word4_puzzle.width - word4_puzzle_text.get_width()) / 2,
        word4_puzzle.y + (word4_puzzle.height - word4_puzzle_text.get_height()) / 2))

    word5_puzzle_text = fuente3.render("5. The planet of the great red spot", True, (0, 0, 0))
    screen.blit(word5_puzzle_text, (word5_puzzle.x + (word5_puzzle.width - word5_puzzle_text.get_width()) / 2,  
        word5_puzzle.y + (word5_puzzle.height - word5_puzzle_text.get_height()) / 2))

    word6_puzzle_text = fuente3.render("6. The biggest star in the solar sistem", True, (0, 0, 0))
    screen.blit(word6_puzzle_text, (word6_puzzle.x + (word6_puzzle.width - word6_puzzle_text.get_width()) / 2,
        word6_puzzle.y + (word6_puzzle.height - word6_puzzle_text.get_height()) / 2))

    return back_button_2, button_xy_med_pre, next_button
def level_med_screen_2() -> pygame.Rect:
    """SHOWS THE SECOND LEVEL OF THE CROSSWORDS
    """
    screen.fill((250, 250, 250))
    
    level_title = pygame.Rect(60, 10, 300, 45)
    back_button_2 = pygame.Rect(350, 240, 35, 35)
    word1_puzzle = pygame.Rect(15, 85, 250, 50)
    word2_puzzle = pygame.Rect(15, 130, 250, 50)
    word3_puzzle = pygame.Rect(15, 175, 250, 50)
    word4_puzzle = pygame.Rect(285, 85, 250, 50)
    

    pygame.draw.rect(screen, (131, 240, 70 ), level_title)
    pygame.draw.rect(screen, (242, 75, 112), back_button_2)
    pygame.draw.rect(screen, (214, 134, 250), word1_puzzle)
    pygame.draw.rect(screen, (214, 134, 250), word2_puzzle)
    pygame.draw.rect(screen, (214, 134, 250), word3_puzzle)
    pygame.draw.rect(screen, (214, 134, 250), word4_puzzle)
    

    pygame.draw.rect(screen, (0, 0, 0), level_title, 2)
    pygame.draw.rect(screen, (0, 0, 0), back_button_2, 2)
    pygame.draw.rect(screen, (0, 0, 0), word1_puzzle, 2)
    pygame.draw.rect(screen, (0, 0, 0), word2_puzzle, 2)
    pygame.draw.rect(screen, (0, 0, 0), word3_puzzle, 2)
    pygame.draw.rect(screen, (0, 0, 0), word4_puzzle, 2)


    level_title_text = fuente.render("SOLAR SISTEM", True, (0, 0, 0))
    screen.blit(level_title_text, (level_title.x + (level_title.width - level_title_text.get_width()) / 2,
        level_title.y + (level_title.height - level_title_text.get_height()) / 2 - 10))

    back_button_2_text = fuente2.render("<- ", True, (0, 0, 0))
    screen.blit(back_button_2_text, (back_button_2.x + (back_button_2.width - back_button_2_text.get_width()) / 2,
        back_button_2.y + (back_button_2.height - back_button_2_text.get_height()) / 2))
    
    word1_puzzle_text = fuente3.render("7. The only planet with life", True, (0, 0, 0))
    screen.blit(word1_puzzle_text, (word1_puzzle.x + (word1_puzzle.width - word1_puzzle_text.get_width()) / 2,
        word1_puzzle.y + (word1_puzzle.height - word1_puzzle_text.get_height()) / 2))

    word2_puzzle_text = fuente3.render("8. The Ice Giant", True, (0, 0, 0))
    screen.blit(word2_puzzle_text, (word2_puzzle.x + (word2_puzzle.width - word2_puzzle_text.get_width()) / 2,
        word2_puzzle.y + (word2_puzzle.height - word2_puzzle_text.get_height()) / 2))

    word3_puzzle_text = fuente3.render("9. Is the planet nearest to the sun ", True, (0, 0, 0))
    screen.blit(word3_puzzle_text, (word3_puzzle.x + (word3_puzzle.width - word3_puzzle_text.get_width()) / 2,
        word3_puzzle.y + (word3_puzzle.height - word3_puzzle_text.get_height()) / 2))

    word4_puzzle_text = fuente3.render("10. Trajectory of the planets", True, (0, 0, 0))
    screen.blit(word4_puzzle_text, (word4_puzzle.x + (word4_puzzle.width - word4_puzzle_text.get_width()) / 2,
        word4_puzzle.y + (word4_puzzle.height - word4_puzzle_text.get_height()) / 2))

    return back_button_2
def medium_mode_xy(size: int, matrix: list):
    """SHOWS THE CROSSWORDS IN XY

    Args:
        matrix (list): matrix to show

    Returns:
        xy_hints: pygame.Rect: Button of the screen
    """
    
    face_xy = cara_xy(size, matrix)

    screen.fill((250, 250, 250))

    xy_hints = pygame.Rect(450, 10, 60, 40)
    to_yz = pygame.Rect(450, 60, 60, 40)


    pygame.draw.rect(screen, (226, 130, 255), xy_hints, 2)
    pygame.draw.rect(screen, (226, 130, 255), to_yz, 2)

    pygame.draw.rect(screen, (0, 0, 0), xy_hints, 2)
    pygame.draw.rect(screen, (0, 0, 0), to_yz, 2)



    xy_hints_text = fuente2.render("HINTS", True, (0, 0, 0))
    screen.blit(xy_hints_text, (xy_hints.x + (xy_hints.width - xy_hints_text.get_width()) / 2,
        xy_hints.y + (xy_hints.height - xy_hints_text.get_height()) / 2))

    to_yz_text = fuente2.render("YZ", True, (0, 0, 0))
    screen.blit(to_yz_text, (to_yz.x + (to_yz.width - to_yz_text.get_width()) / 2,
        to_yz.y + (to_yz.height - to_yz_text.get_height()) / 2))

    return xy_hints, to_yz
def medium_mode_yz(size: int, matrix: list):
    """SHOWS THE CROSSWORDS IN YZ

    Args:
        matrix (list): matrix to show

    Returns:
        yz_hints: pygame.Rect: Button of the screen
    """
    
    face_yz = cara_yz(size, matrix)

    screen.fill((250, 250, 250))

    yz_hints = pygame.Rect(450, 10, 60, 40)
    to_xy = pygame.Rect(450, 60, 60, 40)



    pygame.draw.rect(screen, (226, 130, 255), yz_hints, 2)
    pygame.draw.rect(screen, (226, 130, 255), to_xy, 2)

    pygame.draw.rect(screen, (0, 0, 0), yz_hints, 2)
    pygame.draw.rect(screen, (0, 0, 0), to_xy, 2)


    yz_hints_text = fuente2.render("HINTS", True, (0, 0, 0))
    screen.blit(yz_hints_text, (yz_hints.x + (yz_hints.width - yz_hints_text.get_width()) / 2,
        yz_hints.y + (yz_hints.height - yz_hints_text.get_height()) / 2))
    
    to_xy_text = fuente2.render("XY", True, (0, 0, 0))
    screen.blit(to_xy_text, (to_xy.x + (to_xy.width - to_xy_text.get_width()) / 2,
        to_xy.y + (to_xy.height - to_xy_text.get_height()) / 2))
    
    return yz_hints, to_xy



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
########    
#pasar los botones necesarios = level_easy_screen_1()
########
back_button_1 = None
next_button = None
face_button_xy = None
########
#pasar los botones necesarios = level_easy_screen_2()
########
back_button_2 = None
face_button_yz = None
########
#pasar los botones necesarios = easy_mode_xy()
########
xy_hints = None
to_yz = None
easy_pre_size = 6
words = ['france', 'india', 'japan', 'egypt', 'australia', 'brazil']
countries_matrix = all(easy_pre_size , words) 
########
#pasar los botones necesarios = easy_mode_yz()
########
yz_hints = None
to_xy = None
########
#pasar los botones necesarios = level_med_screen()
########
words = ['saturn', 'mars', 'venus', 'neptune', 'jupiter', 'sun', 'earth', 'uranus', 'mercury', 'orbit']
med_pre_size = 12
solar_matrix = all(med_pre_size, words)
back_button_2 = None
button_xy_med_pre = None
next_button = None
########
#pasar los botones necesarios = level_med_screen_2()
########
back_button_2 = None



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
                    print("easy mode")
                elif medium_mode_button.collidepoint(event.pos):
                    print("medium mode")
                elif hard_mode_button.collidepoint(event.pos):
                    print("hard mode")
            elif current_screen == "created_crosswords" and screen_options_button and easy_mode and medium_mode and hard_mode:
                if screen_options_button.collidepoint(event.pos):
                    current_screen = "options"
                elif easy_mode.collidepoint(event.pos):
                    current_screen = "level_easy_screen_1"
                elif medium_mode.collidepoint(event.pos):
                    current_screen = "level_med_screen"
                elif hard_mode.collidepoint(event.pos):
                    print("hard mode")
            elif current_screen == "level_easy_screen_1" and back_button_1  and face_button_xy:
                if back_button_1.collidepoint(event.pos):
                    current_screen = "created_crosswords"
                elif face_button_xy.collidepoint(event.pos):
                    current_screen = "easy_mode_xy"   
            elif current_screen == "easy_mode_xy" and xy_hints and to_yz:
                if xy_hints.collidepoint(event.pos):
                    current_screen = "level_easy_screen_1"
                if to_yz.collidepoint(event.pos):
                    current_screen = "easy_mode_yz"
            elif current_screen == "easy_mode_yz" and yz_hints and to_xy:
                if yz_hints.collidepoint(event.pos):
                    current_screen = "level_easy_screen_1"
                if to_xy.collidepoint(event.pos):
                    current_screen = "easy_mode_xy"
            elif current_screen == "level_med_screen" and back_button_2 and button_xy_med_pre and next_button:
                if back_button_2.collidepoint(event.pos):
                    current_screen = "created_crosswords"
                elif button_xy_med_pre.collidepoint(event.pos):
                    current_screen = "medium_mode_xy"
                elif next_button.collidepoint(event.pos):
                    current_screen = "level_med_screen_2"
            elif current_screen == "level_med_screen_2" and back_button_2:
                if back_button_2.collidepoint(event.pos):
                    current_screen = "level_med_screen"
            elif current_screen == "medium_mode_xy" and xy_hints and to_yz:
                if xy_hints.collidepoint(event.pos):
                    current_screen = "level_med_screen"
                if to_yz.collidepoint(event.pos):
                    current_screen = "medium_mode_yz"
            elif current_screen == "medium_mode_yz" and yz_hints and to_xy:
                if yz_hints.collidepoint(event.pos):
                    current_screen = "level_med_screen"
                if to_xy.collidepoint(event.pos):
                    current_screen = "medium_mode_xy"
    if current_screen == "initial":
        start_button, exit_button = initial_screen()
    elif current_screen == "options":
        screen_options()
        predeterminate_crosswords_button, create_crosswords_button, back_button = screen_options()
    elif current_screen == "create_crosswords":
        screen_options_button, easy_mode_button, medium_mode_button, hard_mode_button = create_crosswords_screen()
    elif current_screen == "created_crosswords":
        screen_options_button, easy_mode, medium_mode, hard_mode = created_crosswords_screen()
    elif current_screen == "level_easy_screen_1":
        back_button_1, face_button_xy = level_easy_screen_1()
    elif current_screen == "easy_mode_xy":
        xy_hints, to_yz = easy_mode_xy(easy_pre_size,countries_matrix)
    elif current_screen == "easy_mode_yz":
        yz_hints, to_xy = easy_mode_yz(easy_pre_size,countries_matrix)
    elif current_screen == "level_med_screen":
        back_button_2, button_xy_med_pre, next_button = level_med_screen()
    elif current_screen == "level_med_screen_2":
        back_button_2 = level_med_screen_2()
    elif current_screen == "medium_mode_xy":
        xy_hints, to_yz = medium_mode_xy(med_pre_size,solar_matrix)
    elif current_screen == "medium_mode_yz":
        yz_hints, to_xy = medium_mode_yz(med_pre_size,solar_matrix)



    pygame.display.flip()

pygame.quit()
sys.exit()
