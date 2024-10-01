import struct

def save_crossword(file_path, crossword_data):
    with open(file_path, 'wb') as file:
        # Write header: version, dimensions, number of words
        version = 1
        file.write(struct.pack('B', version))  # Write version (1 byte)
        
        x, y, z = crossword_data['dimensions']
        file.write(struct.pack('3I', x, y, z))  # Write X, Y, Z dimensions (3 integers)
        
        num_words = len(crossword_data['words'])
        file.write(struct.pack('I', num_words))  # Write number of words (1 integer)
        
        # Write each word's details
        for word_info in crossword_data['words']:
            word = word_info['word']
            definition = word_info['definition']
            position = word_info['position']
            direction = word_info['direction']

            # Write word and its definition
            file.write(struct.pack('B', len(word)))  # Word length (1 byte)
            file.write(word.encode())  # Word (n bytes)
            file.write(struct.pack('H', len(definition)))  # Definition length (2 bytes)
            file.write(definition.encode())  # Definition (n bytes)

            # Write position (X, Y, Z) and direction
            file.write(struct.pack('3I', *position))  # Position (3 integers)
            file.write(struct.pack('B', direction))  # Direction (1 byte)

def load_crossword(file_path):
    crossword_data = {}
    with open(file_path, 'rb') as file:
        # Read header: version, dimensions, number of words
        version = struct.unpack('B', file.read(1))[0]
        
        x, y, z = struct.unpack('3I', file.read(12))  # Read X, Y, Z dimensions
        crossword_data['dimensions'] = (x, y, z)
        
        num_words = struct.unpack('I', file.read(4))[0]  # Read number of words
        
        words = []
        for _ in range(num_words):
            word_length = struct.unpack('B', file.read(1))[0]
            word = file.read(word_length).decode()  # Read word
            
            def_length = struct.unpack('H', file.read(2))[0]
            definition = file.read(def_length).decode()  # Read definition
            
            position = struct.unpack('3I', file.read(12))  # Read position (X, Y, Z)
            direction = struct.unpack('B', file.read(1))[0]  # Read direction
            
            words.append({'word': word, 'definition': definition, 'position': position, 'direction': direction})
        
        crossword_data['words'] = words
    
    return crossword_data
