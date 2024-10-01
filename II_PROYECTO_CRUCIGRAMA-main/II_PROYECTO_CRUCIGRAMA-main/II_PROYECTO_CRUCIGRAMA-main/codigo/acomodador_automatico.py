import random
import numpy as np
import main
from main import create_matrix
from main import get_crosswrod_size

def all(matrix_size: int, words: list) -> list:
    def automatic_accomodation(matrix: list, words: list) -> list:
        """Accommodates words in the matrix (3D) automatically."""
        
        def can_insert_horizontal(matrix, word, row, col):
            """Verifies if the word can be inserted horizontally in the matrix."""
            if col + len(word) > len(matrix[0]):  # Check if the word exceeds matrix width.
                return False
            for i in range(len(word)):
                if matrix[row][col + i] not in (' ', word[i]):
                    return False
            return True

        def can_insert_vertical(matrix, word, row, col):
            """Verifies if the word can be inserted vertically in the matrix."""
            if row + len(word) > len(matrix):  # Check if the word exceeds matrix height.
                return False
            for i in range(len(word)):
                if matrix[row + i][col] not in (' ', word[i]):
                    return False
            return True

        def can_insert_depth(matrix, word, row, col, depth):
            """Checks if the word can be inserted along the Z axis (depth)."""
            if depth + len(word) > len(matrix[0][0]):  # Check if the word exceeds matrix depth.
                return False
            for i in range(len(word)):
                if matrix[row][col][depth + i] not in (' ', word[i]):
                    return False
            return True

        def insert_word(matrix, word, row, col, depth, direction):
            """Inserts a word in the matrix."""
            if direction == 'horizontal':
                for i in range(len(word)):
                    matrix[row][col + i] = word[i]
            elif direction == 'vertical':
                for i in range(len(word)):
                    matrix[row + i][col] = word[i]
            elif direction == 'depth':
                for i in range(len(word)):
                    matrix[row][col][depth + i] = word[i]

        def find_intersection(matrix, word):
            """Finds the intersections between the matrix and the word."""
            n = len(matrix)
            valid_positions = []
            for row in range(n):
                for col in range(n):
                    for depth in range(len(matrix[0][0])):  # Traverse through the Z axis.
                        for i in range(len(word)):
                            if matrix[row][col][depth] == word[i]:
                                # Ensure that intersection doesn't exceed boundaries.
                                if col - i >= 0 and can_insert_horizontal(matrix, word, row, col - i):
                                    valid_positions.append((row, col - i, depth, 'horizontal'))
                                if row - i >= 0 and can_insert_vertical(matrix, word, row - i, col):
                                    valid_positions.append((row - i, col, depth, 'vertical'))
                                if depth - i >= 0 and can_insert_depth(matrix, word, row, col, depth - i):
                                    valid_positions.append((row, col, depth - i, 'depth'))
            return valid_positions

        def add_word_to_crossword(matrix, words, index=0):
            """Adds words to the crossword."""
            if index >= len(words):
                return matrix
            
            word = words[index]
            valid_positions = find_intersection(matrix, word)
            if not valid_positions:
                n = len(matrix)
                for row in range(n):
                    for col in range(n):
                        for depth in range(len(matrix[0][0])):
                            if can_insert_horizontal(matrix, word, row, col):
                                valid_positions.append((row, col, depth, 'horizontal'))
                            if can_insert_vertical(matrix, word, row, col):
                                valid_positions.append((row, col, depth, 'vertical'))
                            if can_insert_depth(matrix, word, row, col, depth):
                                valid_positions.append((row, col, depth, 'depth'))
            
            if valid_positions:
                row, col, depth, direction = random.choice(valid_positions)
                insert_word(matrix, word, row, col, depth, direction)
                return add_word_to_crossword(matrix, words, index + 1)
            else:
                raise ValueError(f"Cannot insert the word '{word}' in the matrix.")

        updated_matrix = add_word_to_crossword(matrix, words)
        return updated_matrix

    def print_matrix_3d(matrix):
        """Prints the 3D matrix layer by layer."""
        depth = len(matrix[0][0])  # Z-axis depth
        for z in range(depth):
            print(f"Layer {z + 1} (Z={z}):")
            for row in matrix:  # row will be a 2D slice of the matrix for each z
                print(' '.join([row[col][z] for col in range(len(row))]))  # Correct way to access each (x, y, z) value
            print()  # Add a newline between layers for better readability


    def create_matrix_(matrix_size: int) -> list:
        """Create a matrix based on the given size."""
        matrix = create_matrix(matrix_size)
        return matrix

    # Create the matrix and accommodate words
    matrix = create_matrix_(matrix_size)
    updated_matrix = automatic_accomodation(matrix, words)

    # Print the matrix after words have been accommodated
    print_matrix_3d(updated_matrix)

    return updated_matrix  # Return the updated matrix
