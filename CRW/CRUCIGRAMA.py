import tkinter as tk
from tkinter import messagebox
from word_placer import place_words_in_grid

class CrosswordApp:
    def __init__(self, root):
        self.root = root
        self.root.title("3D Crossword")
        self.root.geometry("600x400")  # Adjusted window size for better display

        # Fonts and styles
        self.title_font = ("Arial", 16, "bold")
        self.button_font = ("Arial", 12)
        self.label_font = ("Arial", 10)

        # Variables for game state
        self.words_easy = ['Peru', 'Iraq', 'Chile', 'Cuba', 'Mali', 'Laos']
        self.words_medium = ['saturn', 'mars', 'venus', 'neptune', 'jupiter', 'sun']
        self.words_hard = ['whale', 'octopus', 'shark', 'giraffe', 'elephant', 'panda']
        
        # Diccionario que contiene las celdas numeradas de cada nivel
        self.numbered_cells = {
            "easy": {
                (0, 0): 1,  # South American country (starts at row 0, column 0)
                (1, 0): 2,  # Middle Eastern country
                (2, 0): 3,  # Long, thin country
                (3, 0): 4,  # Famous for cigars
                (4, 0): 5,  # African country
                (5, 0): 6   # Country in Southeast Asia
            },
            "medium": {
                (0, 0): 1,  # Planet with rings (saturn)
                (1, 0): 2,  # The red planet (mars)
                (2, 0): 3,  # Planet of love (venus)
                (3, 0): 4,  # Farthest planet (neptune)
                (4, 0): 5,  # Has a Great Red Spot (jupiter)
                (5, 0): 6   # Star of the solar system (sun)
            },
            "hard": {
                (0, 0): 1,  # Largest animal (whale)
                (1, 0): 2,  # Eight-armed creature (octopus)
                (2, 0): 3,  # Predator of the sea (shark)
                (3, 0): 4,  # Tallest land animal (giraffe)
                (4, 0): 5,  # Biggest ears (elephant)
                (5, 0): 6   # Black and white bear (panda)
            }
        }

        self.matrices = {
        "easy": self.generate_matrix(6, self.words_easy),
        "medium": self.generate_matrix(10, self.words_medium),
        "hard": self.generate_matrix(12, self.words_hard)
    }

        # Additional variables for crossword game state
        self.hints_shown = False
        self.answers_shown = False
        self.current_level = None
        self.current_view = 'XY'  # Initially, the view is XY
        self.current_screen = None
        self.show_initial_screen()

    def show_initial_screen(self):
        """Display the initial screen with start and exit buttons."""
        self.clear_screen()

        title_label = tk.Label(self.current_screen, text="3D Crossword", font=self.title_font)
        title_label.pack(pady=20)

        start_button = tk.Button(self.current_screen, text="Start Game", font=self.button_font,
                                 command=self.show_options_screen)
        start_button.pack(pady=10)

        settings_button = tk.Button(self.current_screen, text="Settings", font=self.button_font,
                                    command=self.show_settings_screen)
        settings_button.pack(pady=10)

        exit_button = tk.Button(self.current_screen, text="Exit", font=self.button_font, command=self.root.quit)
        exit_button.pack(pady=10)

    def show_options_screen(self):
        """Show the options for pre-made or create-your-own crosswords."""
        self.clear_screen()

        title_label = tk.Label(self.current_screen, text="Game Options", font=self.title_font)
        title_label.pack(pady=20)

        pre_crosswords_button = tk.Button(self.current_screen, text="Pre-Made Crosswords", font=self.button_font,
                                          command=self.show_pre_made_screen)
        pre_crosswords_button.pack(pady=10)

        create_crosswords_button = tk.Button(self.current_screen, text="Create Your Own", font=self.button_font,
                                             command=self.show_create_crosswords_screen)
        create_crosswords_button.pack(pady=10)

        back_button = tk.Button(self.current_screen, text="Back", font=self.button_font, command=self.show_initial_screen)
        back_button.pack(pady=10)

    def show_pre_made_screen(self):
        """Show screen for pre-made crosswords (easy, medium, hard)."""
        self.clear_screen()

        title_label = tk.Label(self.current_screen, text="Select Difficulty", font=self.title_font)
        title_label.pack(pady=20)

        easy_button = tk.Button(self.current_screen, text="Easy", font=self.button_font,
                                command=lambda: self.show_crossword_screen('easy'))
        easy_button.pack(pady=10)

        medium_button = tk.Button(self.current_screen, text="Medium", font=self.button_font,
                                  command=lambda: self.show_crossword_screen('medium'))
        medium_button.pack(pady=10)

        hard_button = tk.Button(self.current_screen, text="Hard", font=self.button_font,
                                command=lambda: self.show_crossword_screen('hard'))
        hard_button.pack(pady=10)

        back_button = tk.Button(self.current_screen, text="Back", font=self.button_font, command=self.show_options_screen)
        back_button.pack(pady=10)

    def show_create_crosswords_screen(self):
        """Screen for creating new crosswords (user-defined mode)."""
        self.clear_screen()

        title_label = tk.Label(self.current_screen, text="Create Your Own Crossword", font=self.title_font)
        title_label.pack(pady=20)

        # Inform user of current status
        tk.Label(self.current_screen, text="This feature is under development.", font=self.label_font).pack(pady=10)

        back_button = tk.Button(self.current_screen, text="Back", font=self.button_font, command=self.show_options_screen)
        back_button.pack(pady=10)

    def show_crossword_screen(self, level):
        """Show the crossword for the selected difficulty level."""
        self.clear_screen()

        self.current_level = level
        self.answers_shown = False  
        self.hints_shown = False  # Asegurarse de que las pistas no se muestran al inicio

        self.entries = []  # Limpiar entradas anteriores
        title_label = tk.Label(self.current_screen, text=f"{level.capitalize()} Mode", font=self.title_font)
        title_label.pack(pady=20)

        # Buttons for changing views (XY and YZ)
        view_frame = tk.Frame(self.current_screen)
        view_frame.pack(pady=10)
        
        answers_button = tk.Button(self.current_screen, text="Show Answers", font=self.button_font,
                            command=self.show_answers)
        answers_button.pack(pady=10)

        xy_button = tk.Button(view_frame, text="XY", font=self.button_font, command=self.display_xy_view)
        xy_button.pack(side=tk.LEFT, padx=5)

        yz_button = tk.Button(view_frame, text="YZ", font=self.button_font, command=self.display_yz_view)
        yz_button.pack(side=tk.LEFT, padx=5)

        matrix = self.matrices[level]

        # Display the initial view (XY)
        self.display_matrix(matrix, self.current_view)

        # Botón para mostrar pistas cuando sea presionado
        hints_button = tk.Button(self.current_screen, text="Show Hints", font=self.button_font,
                                command=lambda: self.toggle_hints(level))
        hints_button.pack(pady=10)

        # Botón para verificar la solución
        check_button = tk.Button(self.current_screen, text="Check Solution", font=self.button_font,
                                command=self.check_solution)
        check_button.pack(pady=10)

        back_button = tk.Button(self.current_screen, text="Back", font=self.button_font,
                                command=lambda: self.show_pre_made_screen())
        back_button.pack(pady=10)

    def display_xy_view(self):
        """Change the view to XY and update the display."""
        self.current_view = "XY"
        self.answers_shown = False
        self.clear_screen()
        self.show_crossword_screen(self.current_level)

    def display_yz_view(self):
        """Change the view to YZ and update the display."""
        self.current_view = "YZ"
        self.answers_shown = False
        self.clear_screen()
        self.show_crossword_screen(self.current_level)

    def toggle_hints(self, level):
        """Toggle the display of hints on/off."""
        if self.hints_shown:
            self.clear_hints()
        else:
            self.show_hints_only(level)  # Asegúrate de que este es el nombre correcto
        self.hints_shown = not self.hints_shown

    def show_hints_only(self, level):
        """Display only the hints without the answers."""
        hints = {
            "easy": ["1. South American country", "2. Middle Eastern country", "3. Long, thin country", 
                    "4. Famous for cigars", "5. African country", "6. Country in Southeast Asia"],
            "medium": ["1. Planet with rings", "2. The red planet", "3. Planet of love", 
                    "4. Farthest planet", "5. Has a Great Red Spot", "6. Star of the solar system"],
            "hard": ["1. Largest animal", "2. Eight-armed creature", "3. Predator of the sea", 
                    "4. Tallest land animal", "5. Biggest ears", "6. Black and white bear"]
        }
        
        matrix = self.matrices[level]
        self.display_hints(matrix, hints[level])  # Display hints with numbers


    def show_answers(self):
        """Mostrar las respuestas correctas en la cuadrícula."""
        if not self.answers_shown:  # Solo generar una vez las respuestas
            matrix = self.matrices[self.current_level]  # Matriz de respuestas correctas

            # Mostrar las respuestas en las casillas donde corresponde
            for i, row_entries in enumerate(self.entries):
                for j, letter_entry in enumerate(row_entries):
                    correct_letter = matrix[i][j].upper()  # Obtener la letra correcta
                    if correct_letter != ' ':
                        letter_entry.delete(0, tk.END)  # Limpiar la entrada actual
                        letter_entry.insert(0, correct_letter)  # Mostrar la respuesta correcta
                        letter_entry.config(state='disabled', bg='lightblue')  # Deshabilitar para no modificarla

            self.answers_shown = True  # Marcar que las respuestas ya se han mostrado
    
    def check_solution(self):
        """Verificar si las respuestas del usuario son correctas, incluyendo los espacios en blanco."""
        if self.current_level:
            correct_matrix = self.matrices[self.current_level]  # Matriz de respuestas correctas
            errors = []  # Lista para almacenar las posiciones incorrectas

            # Recorrer las filas de la matriz y verificar las entradas del usuario
            for i, row_entries in enumerate(self.entries):
                for j, letter_entry in enumerate(row_entries):
                    user_letter = letter_entry.get().upper().strip()  # Obtener la entrada del usuario y quitar espacios en blanco
                    correct_letter = correct_matrix[i][j].upper()  # Obtener la letra correcta

                    if correct_letter == ' ':  # Si la respuesta correcta es un espacio en blanco
                        if user_letter == '':  # Si el campo está vacío, es correcto
                            letter_entry.config(bg='lightgreen')
                        else:  # El campo no está vacío pero debería estarlo
                            letter_entry.config(bg='lightcoral')
                            errors.append((i + 1, j + 1))  # Almacenar la posición del error
                    else:
                        if user_letter == correct_letter:  # Si la letra ingresada es correcta
                            letter_entry.config(bg='lightgreen')
                        else:  # Si la letra ingresada es incorrecta
                            letter_entry.config(bg='lightcoral')
                            errors.append((i + 1, j + 1))  # Almacenar la posición del error

            # Mostrar los errores o indicar que la solución es correcta
            if errors:
                error_positions = ", ".join([f"({row}, {col})" for row, col in errors])
                messagebox.showerror("Errores", f"Letras incorrectas en posiciones: {error_positions}")
            else:
                messagebox.showinfo("¡Correcto!", "¡Felicidades! ¡Todas las respuestas son correctas!")
        else:
            messagebox.showerror("Error", "No se ha seleccionado ningún nivel.")

    def clear_hints(self):
        """Ocultar las pistas cuando se presiona nuevamente el botón de Show Hints."""
        if self.hint_frame:
            self.hint_frame.destroy()

    def display_matrix(self, matrix, view, show_answers=False):
        """Display a crossword matrix with numbers and blank spaces."""
        self.entries = []  # Limpiar entradas anteriores

        if view == 'YZ':
            matrix = self.transform_matrix_yz(matrix)

        for i, row in enumerate(matrix):
            row_frame = tk.Frame(self.current_screen)
            row_frame.pack()
            row_entries = []
            for j, letter in enumerate(row):
                # Crear un marco para la celda
                cell_frame = tk.Frame(row_frame, width=40, height=40, bd=1, relief="solid")
                cell_frame.pack_propagate(False)  # Evitar que el tamaño cambie con el contenido
                cell_frame.pack(side=tk.LEFT, padx=2, pady=2)

                if (i, j) in self.numbered_cells[self.current_level]:
                    # Si la celda tiene un número, mostrarlo en la esquina superior izquierda
                    number = self.numbered_cells[self.current_level][(i, j)]
                    number_label = tk.Label(cell_frame, text=str(number), font=("Arial", 8), anchor="nw")
                    number_label.pack(anchor="nw")

                if letter == ' ':
                    # Celda vacía (como los espacios negros en el crucigrama)
                    empty_label = tk.Label(cell_frame, bg="black", width=2, height=1)
                    empty_label.pack(fill=tk.BOTH, expand=True)
                else:
                    # Celda donde el usuario puede escribir
                    letter_entry = tk.Entry(cell_frame, width=2, font=self.button_font, justify='center')

                    if show_answers:
                        # Si se muestran respuestas, introducir la letra correcta
                        letter_entry.insert(0, letter)
                        letter_entry.config(state='disabled', bg='lightblue')

                    letter_entry.pack(fill=tk.BOTH, expand=True)
                    row_entries.append(letter_entry)

            self.entries.append(row_entries)

    def transform_matrix_yz(self, matrix):
        """Transform the matrix for YZ view."""
        size = len(matrix)
        transformed_matrix = [[' ' for _ in range(size)] for _ in range(size)]

        # Example transformation: rotate 90 degrees (or any other transformation for YZ view)
        for i in range(size):
            for j in range(size):
                transformed_matrix[i][j] = matrix[j][i]  # Simple transpose

        return transformed_matrix

    def display_hints(self, matrix, hints):
        """Display the crossword hints on the side of the matrix."""
        for i, row in enumerate(matrix):
            row_frame = tk.Frame(self.current_screen)
            row_frame.pack()
            row_entries = []
            for j, letter in enumerate(row):
                # Crear las celdas de la matriz
                letter_label = tk.Label(row_frame, text=letter, width=5, height=2, relief="solid", font=self.button_font)
                letter_label.pack(side=tk.LEFT, padx=2, pady=2)
            
            # Verificar que existan pistas suficientes
            if i < len(hints):
                hint_label = tk.Label(row_frame, text=hints[i], font=self.label_font)
                hint_label.pack(side=tk.LEFT, padx=5)
            else:
                # Si no hay más pistas, muestra un espacio vacío
                hint_label = tk.Label(row_frame, text="", font=self.label_font)
                hint_label.pack(side=tk.LEFT, padx=5)


    def generate_matrix(self, size, words):
        """Generate a matrix and automatically place the words."""
        try:
            return place_words_in_grid(size, words)
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            return None

    def clear_screen(self):
        """Clear the current screen's content."""
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = tk.Frame(self.root)
        self.current_screen.pack(fill=tk.BOTH, expand=True)

    def show_settings_screen(self):
        """Display the settings screen."""
        self.clear_screen()

        title_label = tk.Label(self.current_screen, text="Settings", font=self.title_font)
        title_label.pack(pady=20)

        # Placeholder for volume control
        tk.Label(self.current_screen, text="Volume (Coming Soon)", font=self.label_font).pack(pady=5)

        # Placeholder for color scheme control
        tk.Label(self.current_screen, text="Color Scheme (Coming Soon)", font=self.label_font).pack(pady=5)

        back_button = tk.Button(self.current_screen, text="Back", font=self.button_font, command=self.show_initial_screen)
        back_button.pack(pady=10)

    def validate_crossword(self):
        """Function to validate crossword input."""
        messagebox.showinfo("Validate", "Crossword validation feature coming soon!")

    def show_leaderboard(self):
        """Function to display leaderboard (placeholder)."""
        messagebox.showinfo("Leaderboard", "Leaderboard feature coming soon!")


# Main game loop
if __name__ == "__main__":
    root = tk.Tk()
    app = CrosswordApp(root)
    root.mainloop()
