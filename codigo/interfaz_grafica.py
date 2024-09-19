import sys, pygame 
pygame.init()
ancho , altura = 800, 600


screen = pygame.display.set_mode(ancho,altura)
pygame.display.set_caption("JUEGO CRUCIGRAMA3D")
run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: run = False
pygame.quit()