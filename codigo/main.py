# como primero crear la matriz para la cara x,y - y,z y hacer el juego en si
# en conjunto con las opciones de cara n*n y quemar opciones y tematicas de juego
import numpy as np

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
    matrix = np.full((x, y), ' ', dtype=object) 
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
    N, M = matrix.shape
    if M != (N * 2 - 1):
        raise ValueError("La matriz debe tener dimensiones N x M, donde M = N * 2 - 1.")

    cara_x_y = matrix[:, :N]
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
    N, M = matrix.shape
    if M != (N * 2 - 1):
        raise ValueError("La matriz debe tener dimensiones N x M, donde M = N * 2 - 1.")
    cara_y_z = matrix[:, N-1:]
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


