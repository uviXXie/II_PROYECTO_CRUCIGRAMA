# como primero crear la matriz para la cara x,y - y,z y hacer el juego en si
# en conjunto con las opciones de cara n*n y quemar opciones y tematicas de juego
import numpy as np
def introduction():
    """FIRST MENU THAT SHOWS UP IN THE CONSOLE IF IT IS NECESARY, WITH THE OPTIONS:
        'INICIAR' : SENDS YOU TO THE SECOND MENU
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
                    created_crosswords()
                    break
                elif choice == 2 :
                    create_crosswords_menu()
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

def created_crosswords():
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
                    created_crosswords()
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

def create_matrix(side: int) -> list:
    """CREATES THE MATRIX BASED IN THE SIDE N*M

    Args:
        side (int): MATRIX SIDES

    Returns:
        list: MATRIX RETURNED
    """
    x_y = get_crosswrod_size(side)
    x = x_y[0]
    y = x_y[1]
    matrix = np.zeros((x,y),dtype = int)
    return matrix

def switch_face_xy(side: int, matrix: list) -> tuple[np.ndarray, np.ndarray]:
    """
    Extracs the first face of the cube.

    Args:
        side (int): MATRIX SIDE HEIGHT.
        matrix (list): MATRIX WE WANT TO PROCESS

    Returns:
        tuple[np.ndarray, np.ndarray]: MATRIX REPRESENTING FACE XY
    """
    matriz = create_matrix(side)
    N, M = matriz.shape
    if M != (N * 2 - 1):
        raise ValueError("La matriz debe tener dimensiones N x M, donde M = N * 2 - 1.")

    cara_x_y = matriz[:, :N]
    return cara_x_y
   
def switch_face_yz(side: int, matrix: list) -> tuple[np.ndarray]:
    """
    Extracs the second face of the cube.

    Args:
        side (int): MATRIX SIDE HEIGHT.
        matrix (list): MATRIX WE WANT TO PROCESS

    Returns:
        tuple[np.ndarray]: MATRIX REPRESENTING FACE YZ
    """
    N, M = matriz.shape
    if M != (N * 2 - 1):
        raise ValueError("La matriz debe tener dimensiones N x M, donde M = N * 2 - 1.")
    cara_y_z = matriz[:, N-1:]
    return cara_y_z 
    
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
def create_crosswords_menu():
    print("TAMAÑO DEL CROSSWORD:\n"
      "1 > 4 x 4 \n"
      "2 > 6 x 6\n"
      "3 > 12 x 12\n"
      "4 > PERSONALIZADOS (N x N)\n"
      "5 > VOLVER A OPCIONES")
    while True:
        choice = int(input("Introduzca el tamano del crucigrama que desea escoger: "))
        while True: 
            try: 
                if choice == 1 :
                    create_crosswords(4)
                    break
                elif choice == 2 :
                    create_crosswords(6)
                    break
                elif choice == 3 :
                    create_crosswords(12)
                    break
                elif choice == 4:
                    side = int(input("INGRESE EL TAMANO DE SU CROSSWORD: "))
                    create_crosswords(side)
                    break
                elif choice == 5:
                    show_options()
                    break
                else: 
                    print("INTRODUZCA OPCION VALIDA")
                    create_crosswords_menu()
                    break
            except ValueError:
                print("Por favor, introduzca una opcion válida '1,2,3,4,5'.")   
            
def automatic_acomodation():
    n=1
introduction()

