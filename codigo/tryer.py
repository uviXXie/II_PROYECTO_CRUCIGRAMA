import tkinter as tk
from tkinter import font
from tkinter import ttk
import acomodador_automatico
import cara_xy
import cara_yz

# Inicializar la ventana principal
root = tk.Tk()
root.title("3D Crossword Game")
root.geometry("800x600")
root.configure(bg="#4A90E2")

# Variables
current_screen = "initial"

# Datos de crucigramas
words_countries = ['france', 'india', 'japan', 'egypt', 'australia', 'brazil']
words_planets = ['saturn', 'mars', 'venus', 'neptune', 'jupiter', 'sun', 'earth', 'uranus', 'mercury', 'orbit']
words_animals = ['whale', 'octopus', 'shark', 'giraffe', 'elephant', 'panda', 'butterfly', 'hippopotamus', 'tiger', 'cheetah', 'monkey', 'ladybug', 'bat', 'buffalo', 'frog', 'dolphin']
pre_size_easy = 6
pre_size_medium = 12
pre_size_hard = 24
countries_crosswords = acomodador_automatico.all(pre_size_easy, words_countries)
planets_crosswords = acomodador_automatico.all(pre_size_medium, words_planets)
animals_crosswords = acomodador_automatico.all(pre_size_hard, words_animals)

def clear_screen():
    """Clear the screen by destroying all widgets."""
    for widget in root.winfo_children():
        widget.destroy()

def create_button(text, command, x, y, bg="#50E3C2", fg="white", font_size=14):
    """Utility function to create a button."""
    button = tk.Button(root, text=text, command=command, font=("Helvetica", font_size), bg=bg, fg=fg)
    button.place(x=x, y=y)
    return button

def show_initial_screen():
    """Show the initial screen of the game."""
    global current_screen
    clear_screen()
    tk.Label(root, text="WELCOME TO THE 3D CROSSWORD GAME", font=("Helvetica", 16), fg="blue").place(x=165, y=50)
    create_button("Start", show_options_screen, 350, 150)
    create_button("Exit", root.quit, 352, 200, bg="#D0021B")

    current_screen = "initial"

def show_options_screen():
    """Show the options screen of the game."""
    global current_screen
    clear_screen()
    tk.Label(root, text="Options", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    
    create_button("Predetermined Crosswords", show_created_crosswords, 350, 100)
    create_button("Create Crosswords", show_create_crosswords, 350, 150)
    create_button("Back", show_initial_screen, 350, 200, bg="#D0021B")

    current_screen = "options"

def show_created_crosswords():
    """Show the created crosswords screen of the game."""
    global current_screen
    clear_screen()
    tk.Label(root, text="Created Crosswords", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    
    create_button("Easy Mode", show_easy_mode, 350, 100)
    create_button("Medium Mode", show_medium_mode, 350, 150)
    create_button("Hard Mode", show_hard_mode, 350, 200)
    create_button("Back", show_options_screen, 350, 250, bg="#D0021B")

    current_screen = "created_crosswords"

def show_create_crosswords():
    """Show the create crosswords screen of the game."""
    global current_screen
    clear_screen()
    tk.Label(root, text="Create Crosswords", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    create_button("Easy Mode (6*6)", show_easy_mode_input, 350, 100)
    create_button("Medium Mode (12*12)", show_medium_mode_input, 350, 150)
    create_button("Hard Mode (24*24)" , show_hard_mode_input, 350, 200)
    create_button("Back", show_options_screen, 350, 250, bg="#D0021B")
    
    current_screen = "create_crosswords"

def show_easy_mode():
    """Show the easy mode screen of the game."""
    global current_screen
    clear_screen()
    tk.Label(root, text="Easy Mode", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)

    hints = [
        "1. A country known for the Eiffel Tower.",
        "2. Home to the Taj Mahal.",
        "3. An island nation in Asia.",
        "4. Known for pyramids and the Nile.",
        "5. A continent down under.",
        "6. The land of Carnival."
    ]
    
    for hint in hints:
        tk.Label(root, text=hint, font=("Helvetica", 12), bg="#4A90E2", fg="white").pack()

    create_button("Play Easy Crossword", lambda: xy_screen_easy(pre_size_easy, countries_crosswords), 350, 300)
    create_button("Back", show_created_crosswords, 355, 400, bg="#D0021B")
    
    current_screen = "easy_mode"

def show_medium_mode():
    """Show the medium mode screen of the game."""
    global current_screen
    clear_screen()
    tk.Label(root, text="Medium Mode", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)

    hints = [
        "1. A planet with rings.",
        "2. The red planet.",
        "3. The second planet from the sun.",
        "4. The eighth planet from the sun.",
        "5. The largest planet in the solar system.",
        "6. The star at the center of the solar system.",
        "7. The third planet from the sun.",
        "8. The seventh planet from the sun.",
        "9. The closest planet to the sun.",
        "10. The path a planet takes around the sun."
    ]
    
    for hint in hints:
        tk.Label(root, text=hint, font=("Helvetica", 12), bg="#4A90E2", fg="white").pack()

    create_button("Back", show_created_crosswords, 355, 400, bg="#D0021B")

    current_screen = "medium_mode"

def show_hard_mode():
    """Show the hard mode screen of the game."""
    global current_screen
    clear_screen()
    tk.Label(root, text="Hard Mode", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)

    hints = [
        "1. The largest animal on Earth.",
        "2. An animal with eight tentacles.",
        "3. The king of the jungle.",
        "4. The tallest animal in the world.",
        "5. The largest land animal.",
        "6. A bear native to China.",
        "7. An insect with colorful wings.",
        "8. A large mammal that loves water.",
        "9. A big cat with stripes.",
        "10. A big cat that can run very fast.",
        "11. A primate that loves bananas.",
        "12. A small insect with red wings.",
        "13. A flying mammal.",
        "14. A large mammal with horns.",
        "15. An amphibian that loves water.",
        "16. A marine mammal that loves to jump."
    ]
    
    for hint in hints:
        tk.Label(root, text=hint, font=("Helvetica", 12), bg="#4A90E2", fg="white").pack()

    create_button("Back", show_created_crosswords, 355, 400, bg="#D0021B")

    current_screen = "hard_mode"

def xy_screen_easy(size, crossword):
    """Show the xy screen of the easy crossword."""
    global current_screen
    clear_screen()
    face_xy = cara_xy.cara_xy(size, crossword)
    tk.Label(root, text="Easy Crossword", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    create_button("Back to Easy Hints", show_easy_mode, 300, 400)
    to_yz = create_button("Switch to YZ", lambda: yz_screen_easy(size, crossword), 300, 450, bg="#50E3C2")

    current_screen = "xy_screen_easy"

def xy_screen_medium(size, crossword):
    """Show the xy screen of the medium crossword."""
    global current_screen
    clear_screen()
    face_xy = cara_xy.cara_xy(size, crossword)
    tk.Label(root, text="Medium Crossword", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    create_button("Back to Medium Hints", show_medium_mode, 300, 400)
    to_yz = create_button("Switch to YZ", lambda: yz_screen_medium(size, crossword), 300, 450, bg="#50E3C2")

    current_screen = "xy_screen_medium"

def xy_screen_hard(size, crossword):
    """Show the xy screen of the hard crossword."""
    global current_screen
    clear_screen()
    face_xy = cara_xy.cara_xy(size, crossword)
    tk.Label(root, text="Hard Crossword", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    create_button("Back to Hard Hints", show_hard_mode, 300, 400)
    to_yz = create_button("Switch to YZ", lambda: yz_screen_hard(size, crossword), 300, 450, bg="#50E3C2")

    current_screen = "xy_screen_hard"

def yz_screen_easy(size, crossword):
    """Show the yz screen of the easy crossword."""
    global current_screen
    clear_screen()
    face_yz = cara_yz.cara_yz(size, crossword)
    tk.Label(root, text="Easy Crossword", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    create_button("Back to Easy Hints", show_easy_mode, 300, 400)
    to_xy = create_button("Switch to XY", lambda: xy_screen_easy(size, crossword), 300, 450, bg="#50E3C2")

    current_screen = "yz_screen_easy"

def yz_screen_medium(size, crossword):
    """Show the yz screen of the medium crossword."""
    global current_screen
    clear_screen()
    face_yz = cara_yz.cara_yz(size, crossword)
    tk.Label(root, text="Medium Crossword", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    create_button("Back to Medium Hints", show_medium_mode, 300, 400)
    to_xy = create_button("Switch to XY", lambda: xy_screen_medium(size, crossword), 300, 450, bg="#50E3C2")

    current_screen = "yz_screen_medium"

def yz_screen_hard(size, crossword):    
    """Show the yz screen of the hard crossword."""
    global current_screen
    clear_screen()
    face_yz = cara_yz.cara_yz(size, crossword)
    tk.Label(root, text="Hard Crossword", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    create_button("Back to Hard Hints", show_hard_mode, 300, 400)
    to_xy = create_button("Switch to XY", lambda: xy_screen_hard(size, crossword), 300, 450, bg="#50E3C2")

    current_screen = "yz_screen_hard"

def show_easy_mode_input():
    """Show the input screen for the easy mode."""
    global current_screen
    clear_screen()
    

    current_screen = "easy_mode_input"
# def show_medium_mode_input():
#     """Show the input screen for the medium mode."""
#     global current_screen
#     clear_screen()
#     hints = create_hint_input()

#     for hint in hints:
#         tk.Label(root, text=hint, font=("Helvetica", 12), bg="#4A90E2", fg="white").pack()

#     create_button("Back", show_created_crosswords, 355, 400, bg="#D0021B")


#     current_screen = "medium_mode_input"

    
    


# def create_hint_input():
#     """Crea campos de entrada para las pistas."""
#     hints_create = []

#     indicator = tk.Label(root, text="Enter the hints for the medium mode (enter fitting words)", font=("Helvetica", 12), bg="#4A90E2", fg="white")
#     indicator.place(x=200, y=50)

#     for i in range(1, 6):  # Cambia el rango según el número de pistas que quieras permitir
#         lb_hint = tk.Label(root, text=f"Hint {i}: ", foreground="white", bg="#4A90E2")
#         lb_hint.place(x=200, y=50 + i * 40)  # Espacio entre las pistas

#         sv_hint = tk.StringVar()
#         tb_hint = ttk.Entry(root, textvariable=sv_hint, width=40)
#         tb_hint.place(x=250, y=50 + i * 40)

#         hints_create.append(sv_hint)  # Guardar el StringVar en la lista

#     submit_button = tk.Button(root, text="Submit", command=lambda: submit_hints(hints_create), font=("Helvetica", 14), bg="#50E3C2", fg="white")
#     submit_button.place(x=350, y=300)

# def submit_hints(hinst):
#     """Función para manejar el envío de las pistas."""
#     hints = [hint.get() for hint in hints if hint.get()] 
#     print("Hints submitted:", hints)  



# current_screen = "medium_mode_input"

def show_hard_mode_input():
    """Show the input screen for the hard mode."""

    global current_screen
    clear_screen()
    

    current_screen = "hard_mode_input"







def update_screen():
    """Update the current screen based on the current_screen variable."""
    if current_screen == "initial":
        show_initial_screen()
    elif current_screen == "options":
        show_options_screen()
    elif current_screen == "created_crosswords":
        show_created_crosswords()
    elif current_screen == "create_crosswords":
        show_create_crosswords()
    elif current_screen == "easy_mode":
        show_easy_mode()
    elif current_screen == "medium_mode":
        show_medium_mode()
    elif current_screen == "hard_mode":
        show_hard_mode()
    elif current_screen == "xy_screen_easy":
        xy_screen_easy(pre_size_easy, countries_crosswords)
    elif current_screen == "xy_screen_medium":
        xy_screen_medium(pre_size_medium, planets_crosswords)
    elif current_screen == "xy_screen_hard":
        xy_screen_hard(pre_size_hard, animals_crosswords)
    elif current_screen == "yz_screen_easy":
        yz_screen_easy(pre_size_easy, countries_crosswords)
    elif current_screen == "yz_screen_medium":
        yz_screen_medium(pre_size_medium, planets_crosswords)
    elif current_screen == "yz_screen_hard":
        yz_screen_hard(pre_size_hard, animals_crosswords)
    elif current_screen == "easy_mode_input":
        show_easy_mode_input()
    elif current_screen == "medium_mode_input":
        pass
    elif current_screen == "hard_mode_input":
        show_hard_mode_input()

# Mostrar la pantalla inicial
update_screen()

# Ejecutar la aplicación
root.mainloop()
