import numpy as np

def get_crosswrod_size(side: int) -> tuple[int, int]:
    """CREATES THE CROSSWORD SIZE BY N * M, M = (N * 2 - 1)
    
    Args:
        side (int): CROSSWORD SIDE

    Returns:
        tuple[int,int]: RETURNS CROSSWORD (X,Y)
    """
    return side, side * 2 - 1

def create_matrix(side: int) -> np.ndarray:
    """CREATES THE MATRIX BASED ON THE SIDE N*M
    
    Args:
        side (int): MATRIX SIDES

    Returns:
        np.ndarray: MATRIX RETURNED
    """
    x_y = get_crosswrod_size(side)
    x = x_y[0]
    y = x_y[1]
    matrix = np.zeros((x, y), dtype=int)
    return matrix

def cambiar_cara(side: int) -> tuple[np.ndarray, np.ndarray]:
    """
    Extrae las dos caras de la matriz.
    La primera cara es [x, y] y la segunda cara es [y, z].

    Args:
        side (int): Tamaño del lado de la matriz.

    Returns:
        tuple[np.ndarray, np.ndarray]: Dos matrices representando las caras del cubo.
    """
    matriz = create_matrix(side)
    N, M = matriz.shape
    if M != (N * 2 - 1):
        raise ValueError("La matriz debe tener dimensiones N x M, donde M = N * 2 - 1.")

    # Primera cara [x, y]
    cara_x_y = matriz[:, :N]
    
    # Segunda cara [y, z]
    cara_y_z = matriz[:, N-1:]

    return cara_x_y, cara_y_z

# Ejemplo de uso
cara_x_y, cara_y_z = cambiar_cara(3)
print("Cara [x, y]:")
print(cara_x_y)
print("\nCara [y, z]:")
print(cara_y_z)
