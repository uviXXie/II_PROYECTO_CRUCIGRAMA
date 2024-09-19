# como primero crear la matriz para la cara x,y - y,z y hacer el juego en si
# en conjunto con las opciones de cara n*n y quemar opciones y tematicas de juego
def introduction():
    """FIRST MENU THAT SHOWS UP IN THE CONSOLE IF IT IS NECESARY, WITH THE OPTIONS:
        "INICIAR' : SENDS YOU TO THE SECOND MENU
        'SALIR' : EXITS THE PROGRAM
    """
    print("BIENVENIDO A CRUCIGRAMA 3D")
    print("1 > INICIAR")
    print("2 > SALIR")

    while True:
        try:
            choice = int(input("Por favor introduzca su elección: "))
            if choice == 1:
                show_options()
                break  
            elif choice == 2:
                print("Saliendo...")
                exit() 
            else:
                print("INTRODUZCA OPCION VALIDA")
                introduction()
        except ValueError:
            print("Por favor, introduzca una opcion válida '1,2'.")


def show_options():
    print("ESCOGE LA OPCION QUE DESEAS ELEGIR:\n"
      "1 > CRONOGRAMAS PREDETERMINADOS\n"
      "2 > CREAR TU PROPIO CRONOGRAMA 3D\n"
      "3 > VOLVER A PANTALLA PRINCIPAL")
    while True:
        choice = int(input("Introduzca la accion que desea realizar: "))
        while True: 
            try: 
                if choice == 1 :
                    CREATED_CROSSWORDS()
                    break
                elif choice == 2 :
                    CREATE_CROSSWORDS()
                    break
                elif choice == 3:
                    introduction()
                    break
                else: 
                    print("INTRODUZCA OPCION VALIDA")
                    show_options()
                    break
            except ValueError:
                print("Por favor, introduzca una opcion válida '1,2,3'.")

def CREATED_CROSSWORDS():
    """HERE IS WHERE THE DEVELOPER OF THE PROGRAM SAVES SOME CROSSWORDS ALREDY DONE BY SHE
    """
    print("ESCOGE LA OPCION QUE DESEAS ELEGIR:\n"
      "1 > RAZAS DE GATOS POR COLOR \n"
      "2 > PLANETAS DEL SISTEMA SOLAR\n"
      "3 > PAISES\n"
      "4 > VOLVER A OPCIONES")
    while True:
        choice = int(input("Introduzca el crucigrama que desea escoger: "))
        while True: 
            try: 
                if choice == 2 :
                    cats_crosswords()
                    break
                elif choice == 2 :
                    planets_crosswords()
                    break
                elif choice == 3:
                    countrys_crosswords()
                    break
                elif choice == 4:
                    show_options()
                    break
                else: 
                    print("INTRODUZCA OPCION VALIDA")
                    CREATED_CROSSWORDS()
                    break
            except ValueError:
                print("Por favor, introduzca una opcion válida '1,2,3,4'.")
def get_crosswrod_size(side: int) -> tuple[int,int]:
    """CREATES THE CROSSWORD SIZE BY N * M, M = (N * 2 - 1)
    Args:
        side (int): CROSSWORD SIDE

    Returns:
        tuple[int,int]: RETURNS CROSSWORD (X,Y)
    """
    return side, side * 2 - 1 #para hacer una matriz n * n 3d con un y que se comparten x y z debe de haber una celda enmedio funcionando como y

def create_matrix():
    n + 1
    
def get_crossword_cords(side: int , face:int, x: int , y: int) -> tuple[int,int]:
    """OBTAINS THE CORDS FOR THE FIRST OR SECOND FACE OF THE 3D CROSSWORD
    Args:
        side (int): MATRIX SIDES
        FACE (int): USING FACE
        x (int): X CORDS
        y (int): Y CORDS

    Returns:
        tuple: FACE CORDS
    """
    return side - 1 * face + x, y  #le resta una fila a la matriz y la multiplica por el valor de la cara que se use, luego se suma x, esto para hacer el cambio de caras de x,y coordenanda
    
introduction()

