from main import switch_face_xy
def cara_xy(side: int, matrix: list) -> list:
    """
    Creates a matrix of size side x side.
    
    Args:
        side (int): MATRIX SIDES

    Returns:
        list: MATRIX RETURNED
    """
    matrix = switch_face_xy(side, matrix)
    return matrix
   