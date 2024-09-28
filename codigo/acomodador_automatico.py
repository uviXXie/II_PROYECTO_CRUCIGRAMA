import random
import numpy as np
import main
from main import create_matrix
from main import get_crosswrod_size
def automatic_acomodation(matrix_size: int, words: list) -> list:


    def can_insert_horizontal(matrix, word, fila, columna):
        """verificates if the word can be inserted horizontally in the matrix.

        Args:
            matrix (list): matrix to insert the word.
            word (str): word to insert.
            fila (int): row to insert the word.
            columna (int): column to insert the word.

        Returns:
                bool : True if the word can be inserted, False otherwise.
        """
        if columna + len(word) > len(matrix[0]):  # Comprueba si la palabra sale del borde derecho.
            return False  
        for i in range(len(word)):  # Recorre cada letra de la palabra.
            if matrix[fila][columna + i] not in (' ', word[i]):  # Verifica que la posición esté vacía o sea la letra de la palabra.
                return False  # No se puede insertar.
        return True 

    def can_insert_vertical(matrix, word, fila, columna):
        """verificates if the word can be inserted verticaly in the matrix.

        Args:
            matrix (list): matrix to insert the word.
            word (str): word to insert.
            fila (int): row to insert the word.
            columna (int): column to insert the word.

        Returns:
                bool : True if the word can be inserted, False otherwise.
        """
        if fila + len(word) > len(matrix):  # Comprueba si la palabra sale del borde inferior.
            return False  
        for i in range(len(word)):  # Recorre cada letra de la palabra.
            if matrix[fila + i][columna] not in (' ', word[i]):  
                return False  
        return True  

    def insert_word(matrix, word, fila, columna, direccion):
        """Inserts a word in the matrix.

        Args:
            matrix (list): matrix to insert the word.
            word (str): word to insert.
            fila (int): row to insert the word.
            columna (int): column to insert the word.
            direccion (_type_): direction to insert the word.
        """
        if direccion == 'horizontal':  
            for i in range(len(word)):  
                matrix[fila][columna + i] = word[i] 
        elif direccion == 'vertical':  
            for i in range(len(word)):  
                matrix[fila + i][columna] = word[i]  

    def find_intersection(matrix, word):
        """Find the intersections between the matrix and the word.

        Args:
            matrix (list): matrix to insert the word.
            word (str): word to insert.

        Returns:
            _type_: _description_
        """
        n = len(matrix)  
        posiciones = []  # Lista para almacenar las posiciones válidas.
        for fila in range(n):  
            for columna in range(n):  
                for i in range(len(word)): 
                    if matrix[fila][columna] == word[i]:  
                    
                        if can_insert_horizontal(matrix, word, fila, columna - i):
                            posiciones.append((fila, columna - i, 'horizontal'))  # Añade la posición a la lista.
                        # Verifica si se puede insertar verticalmente a partir de esa posición.
                        if can_insert_vertical(matrix, word, fila - i, columna):
                            posiciones.append((fila - i, columna, 'vertical'))  
        return posiciones  # Devuelve las posiciones válidas.

    def add_word_to_crossword(matrix, words, indice=0):
        """Add words to the crossword.

        Args:
            matrix (list): matrix to insert the word.
            words (str): word to insert.
            indice (int, optional): index of the word. Defaults to 0.

        Raises:
            ValueError: if the word cannot be inserted.

        Returns:
            _type_: _description_
        """
        if indice >= len(words):  # Si se han añadido todas las palabras.
            return matrix  # Devuelve la matriz actualizada.
        
        word = words[indice]  # Toma la palabra actual de la lista.
        posiciones = find_intersection(matrix, word)  # Busca posiciones donde se puede insertar la palabra.
        if not posiciones:  # Si no hay posiciones encontradas.
            n = len(matrix)  
            for fila in range(n):  
                for columna in range(n): 
                    
                    if can_insert_horizontal(matrix, word, fila, columna):
                        posiciones.append((fila, columna, 'horizontal'))  # Añade la posición a la lista.
                    # Verifica si se puede insertar verticalmente a partir de esa posición.
                    if can_insert_vertical(matrix, word, fila, columna):
                        posiciones.append((fila, columna, 'vertical'))  # Añade la posición a la lista.
        
        if posiciones:  # Si hay posiciones válidas.
            fila, columna, direccion = random.choice(posiciones)  # Selecciona una posición aleatoria.
            insert_word(matrix, word, fila, columna, direccion)  # Inserta la palabra en la matriz.
            return add_word_to_crossword(matrix, words, indice + 1)  # Continúa con la siguiente palabra.
        else:
            raise ValueError("No se puede insertar la palabra en la matriz.")  # Lanza un error si no se puede insertar.


    matrix = create_matrix(matrix_size)  # Crea la matriz con nuevas dimensiones.
    updated_matrix = add_word_to_crossword(matrix, words)  # Agrega las palabras a la matriz.

    for fila in updated_matrix:  # Recorre cada fila de la matriz actualizada.
        print(' '.join(fila))  
automatic_acomodation(10, ['hola', 'adios', 'casa'])
