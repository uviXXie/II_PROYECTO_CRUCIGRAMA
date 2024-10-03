import random
import numpy as np
import main
from main import create_matrix
from main import get_crosswrod_size

def all(matrix_size: int, words: list) -> list:
    """ACOMODATES THE WORDS IN THE MATRIX

    Args:
        matrix_size (int): MATRIX SIZE
        words (list): WORDS TO ACOMODATE

    Returns:
        list: MATRIX WITH WORDS ACOMODATED
    """
    def automatic_acomodation(matrix: list, words: list) -> list:
        """ACOMODATES THE WORDS IN THE MATRIX

        Args:
            matrix (list): MATRIX TO ACOMODATE
            words (list): WORDS TO ACOMODATE

        Returns:
            list: MATRIX WITH WORDS ACOMODATED
        """

        def can_insert_horizontal(matrix, word, fila, columna):
            """INSERTS THE WORD HORIZONTALLY

            Args:
                matrix (list): MATRIX TO INSERT THE WORD 
                word (str): WORD TO INSERT
                fila (int): ROW
                columna (int): COLUMN

            Returns:
                bool: IF THE WORD CAN BE INSERTED
            """
            if columna + len(word) > len(matrix[0]):
                return False
            for i in range(len(word)):
                if matrix[fila][columna + i] not in (' ', word[i]):
                    return False
            return True

        def can_insert_vertical(matrix, word, fila, columna):
            """ INSERTS THE WORD VERTICALLY

            Args:
                matrix (int): MATRIX TO INSERT THE WORD
                word (str): WORD TO INSERT
                fila (int): ROW
                columna (int): COLUMN

            Returns:
                bool: IF THE WORD CAN BE INSERTED
            """
            if fila + len(word) > len(matrix):
                return False
            for i in range(len(word)):
                if matrix[fila + i][columna] not in (' ', word[i]):
                    return False
            return True

        def insert_word(matrix, word, fila, columna, direction):
            """ INSERTS THE WORD

            Args:
                matrix (list): MATRIX TO INSERT THE WORD
                word (str): WORD TO INSERT
                fila (int): ROW
                columna (int): COLUMN
                direction (str): DIRECTION
            """
            if direction == 'horizontal':
                for i in range(len(word)):
                    matrix[fila][columna + i] = word[i]
            elif direction == 'vertical':
                for i in range(len(word)):
                    matrix[fila + i][columna] = word[i]

        def find_intersection(matrix, word):
            """ FINDS THE INTERSECTION

            Args:
                matrix (list): MATRIX TO FIND THE INTERSECTION
                word (str): WORD TO FIND THE INTERSECTION

            Returns:
                list: INTERSECTION
            """
            n = len(matrix)
            positions = []
            for fila in range(n):
                for columna in range(n):
                    for i in range(len(word)):
                        if matrix[fila][columna] == word[i]:
                            if columna - i >= 0 and can_insert_horizontal(matrix, word, fila, columna - i):
                                if columna - i + len(word) <= n:
                                    positions.append((fila, columna - i, 'horizontal'))
                            if fila - i >= 0 and can_insert_vertical(matrix, word, fila - i, columna):
                                if fila - i + len(word) <= n:
                                    positions.append((fila - i, columna, 'vertical'))
            return positions

        def add_word_to_crossword(matrix, words, indice=0, intentos=0, max_intentos=1000):
            """ ADDS THE WORD TO THE CROSSWORD

            Args:
                matrix (list): MATRIX TO ADD THE WORD
                words (list): WORDS TO ADD
                indice (int, optional): _description_. Defaults to 0.
                intentos (int, optional): _description_. Defaults to 0.
                max_intentos (int, optional): _description_. Defaults to 1000.

            Raises:
                RecursionError: 
                                ERROR IF THE WORDS CANNOT BE INSERTED
            Returns:
                list: MATRIX WITH WORDS ACOMODATED
            """
            if indice >= len(words):
                return matrix
            
            if intentos >= max_intentos:
                raise RecursionError("No se pudo acomodar todas las palabras en el número máximo de intentos")

            word = words[indice]
            positions = find_intersection(matrix, word)
            if not positions:
                n = len(matrix)
                for fila in range(n):
                    for columna in range(n):
                        if can_insert_horizontal(matrix, word, fila, columna):
                            positions.append((fila, columna, 'horizontal'))
                        if can_insert_vertical(matrix, word, fila, columna):
                            positions.append((fila, columna, 'vertical'))
            
            if positions:
                fila, columna, direction = random.choice(positions)
                insert_word(matrix, word, fila, columna, direction)
                return add_word_to_crossword(matrix, words, indice + 1)
            else:
                # Si no se encuentra una posición, reiniciar el proceso
                return add_word_to_crossword(matrix, words, indice, intentos + 1, max_intentos)

        updated_matrix = add_word_to_crossword(matrix, words)  # Agrega las palabras a la matriz.
        return updated_matrix

    def create_matrix_(matrix_size: int) -> list:
        """ CREATE THE NEW MATRIX

        Args:
            matrix_size (int): MATRIX SIZE

        Returns:
            list: MATRIX CREATED
        """
        matrix = create_matrix(matrix_size)  # Crea la matriz con nuevas dimensiones.
        return matrix  # Devuelve la matriz creada.

    matrix = create_matrix_(matrix_size)  
    updated_matrix = automatic_acomodation(matrix, words)  # Acomoda las palabras en la matriz.
    return updated_matrix
