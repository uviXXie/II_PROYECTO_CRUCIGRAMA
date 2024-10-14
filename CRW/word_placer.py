import random

def create_empty_grid(size):
    """Create an empty grid of the given size filled with spaces."""
    return [[' ' for _ in range(size)] for _ in range(size)]

def can_place_word(grid, word, row, col, direction):
    """Check if a word can be placed at a certain position in a certain direction."""
    if direction == 'horizontal':
        if col + len(word) > len(grid):
            return False
        for i in range(len(word)):
            if grid[row][col + i] != ' ' and grid[row][col + i] != word[i]:
                return False
    elif direction == 'vertical':
        if row + len(word) > len(grid):
            return False
        for i in range(len(word)):
            if grid[row + i][col] != ' ' and grid[row + i][col] != word[i]:
                return False
    return True

def place_word(grid, word, row, col, direction):
    """Place a word on the grid in a certain direction."""
    if direction == 'horizontal':
        for i in range(len(word)):
            grid[row][col + i] = word[i]
    elif direction == 'vertical':
        for i in range(len(word)):
            grid[row + i][col] = word[i]

def place_words_in_grid(size, words):
    """Try to place all words in a grid of a given size."""
    grid = create_empty_grid(size)
    directions = ['horizontal', 'vertical']

    for word in words:
        placed = False
        attempts = 0
        while not placed and attempts < 100:
            direction = random.choice(directions)
            if direction == 'horizontal':
                row = random.randint(0, size - 1)
                col = random.randint(0, size - len(word))
            elif direction == 'vertical':
                row = random.randint(0, size - len(word))
                col = random.randint(0, size - 1)

            if can_place_word(grid, word, row, col, direction):
                place_word(grid, word, row, col, direction)
                placed = True
            attempts += 1

        if not placed:
            raise ValueError(f"Could not place word: {word}")

    return grid
