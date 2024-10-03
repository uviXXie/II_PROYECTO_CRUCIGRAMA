from main import switch_face_yz
def cara_yz(side: int, matrix: list) -> list:
    """
    Creates a matrix of size side x side.
    
    Args:
        side (int): MATRIX SIDES

    Returns:
        list: MATRIX RETURNED
    """
    matrix = switch_face_yz(side, matrix)
    return matrix