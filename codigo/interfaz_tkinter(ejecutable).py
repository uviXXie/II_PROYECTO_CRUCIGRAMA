import tkinter as tk
from tkinter import font
from tkinter import ttk
import acomodador_automatico
import cara_xy
import cara_yz

# Inicializar la ventana principal
root = tk.Tk()
root.title("3D Crossword Game")
root.geometry("1000x500")
root.configure(bg="#4A90E2")

# Variables
current_screen = "initial"

# Datos de crucigramas
words_countries = ['france', 'india', 'japan', 'egypt', 'australia', 'brazil']
words_planets = ['saturn', 'mars', 'venus', 'neptune', 'jupiter', 'sun', 'earth', 'uranus', 'mercury', 'orbit']
words_animals = ['whale', 'octopus', 'shark', 'giraffe', 'elephant', 'panda', 'butterfly', 'hippopotamus', 'tiger', 'cheetah', 'monkey', 'ladybug', 'bat', 'buffalo', 'frog', 'dolphin']
pre_size_easy = 6
pre_size_medium = 10
pre_size_hard = 12
countries_crosswords = acomodador_automatico.all(pre_size_easy, words_countries)
planets_crosswords = acomodador_automatico.all(pre_size_medium, words_planets)
animals_crosswords = acomodador_automatico.all(pre_size_hard, words_animals)


""" FIJARSE EN LAS FUNCIONES:
    - create_easy_hint_input
    - create_easy_word_input
    - create_medium_hint_input
    - create_medium_word_input
    - create_hard_hint_input
    - create_hard_word_input
    HAY COMENTARIOS CON LO QUE HACE FALTA HACER
    ADEMAS HACE FALTA CREAR UNA PANTALLA NUEVA PARA JUGAR CON EL CRUCIGRAMA CREADO
"""

def clear_screen():
    """Clear the screen by destroying all widgets."""
    for widget in root.winfo_children():
        widget.destroy()

def create_button(text, command, x, y, bg="#50E3C2", fg="white", font_size=14):
    """Create a button widget.

    Args:
        text (str): text to display on the button
        command (function): function to execute when the button is clicked
        x (int): x-coordinate of the button
        y (int): y-coordinate of the button
        bg (str, optional):  Defaults to "#50E3C2".
        fg (str, optional):  Defaults to "white".
        font_size (int, optional):  Defaults to 14.

    Returns:
        tk.Button: the button widget
    """
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
    create_button("Back", show_options_screen, 350, 200, bg="#D0021B")
    create_button("Create Hard Crossword", create_hard_hint_input, 350, 150)
    create_button("Create Medium Crossword", create_medium_hint_input, 350, 100)
    create_button("Create Easy Crossword", create_easy_hint_input, 350, 50)

    
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
    create_button("Play Medium Crossword", lambda: xy_screen_medium(pre_size_medium, planets_crosswords), 350, 350)

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

    create_button("Back", show_created_crosswords, 355,500, bg="#D0021B")
    create_button("Play Hard Crossword", lambda: xy_screen_hard(pre_size_hard, animals_crosswords), 350, 450)


    current_screen = "hard_mode"

def xy_screen_easy(size, crossword):
    """
    Show the xy screen of the easy crossword.

    Args:
        size (int): size of the crossword
        crossword (list): list of lists with the crossword

    """
    global current_screen
    clear_screen()
    face_xy = cara_xy.cara_xy(size, crossword)
    tk.Label(root, text="Easy Crossword", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    create_button("Back to Easy Hints", show_easy_mode, 300, 400)
    to_yz = create_button("Switch to YZ", lambda: yz_screen_easy(size, crossword), 300, 450, bg="#50E3C2")

    current_screen = "xy_screen_easy"

def xy_screen_medium(size, crossword):
    """
    Show the xy screen of the medium crossword.

    Args:
        size (int): size of the crossword
        crossword (list): list of lists with the crossword
    """
    global current_screen
    clear_screen()
    face_xy = cara_xy.cara_xy(size, crossword)
    tk.Label(root, text="Medium Crossword", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    create_button("Back to Medium Hints", show_medium_mode, 300, 400)
    to_yz = create_button("Switch to YZ", lambda: yz_screen_medium(size, crossword), 300, 450, bg="#50E3C2")

    current_screen = "xy_screen_medium"

def xy_screen_hard(size, crossword):
    """Show the xy screen of the hard crossword.
    
    Args:
        
        size (int): size of the crossword
        crossword (list): list of lists with the crossword
        
        """
    global current_screen
    clear_screen()
    face_xy = cara_xy.cara_xy(size, crossword)
    tk.Label(root, text="Hard Crossword", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    create_button("Back to Hard Hints", show_hard_mode, 300, 400)
    to_yz = create_button("Switch to YZ", lambda: yz_screen_hard(size, crossword), 300, 450, bg="#50E3C2")

    current_screen = "xy_screen_hard"

def yz_screen_easy(size, crossword):
    """Show the yz screen of the easy crossword.
    
    Args:
            size (int): size of the crossword
            crossword (list): list of lists with the crossword
            
            """
    global current_screen
    clear_screen()
    face_yz = cara_yz.cara_yz(size, crossword)
    tk.Label(root, text="Easy Crossword", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    create_button("Back to Easy Hints", show_easy_mode, 300, 400)
    to_xy = create_button("Switch to XY", lambda: xy_screen_easy(size, crossword), 300, 450, bg="#50E3C2")

    current_screen = "yz_screen_easy"

def yz_screen_medium(size, crossword):
    """Show the yz screen of the medium crossword.
    
    Args:
        
        size (int): size of the crossword
        crossword (list): list of lists with the crossword
        
        """

    global current_screen
    clear_screen()
    face_yz = cara_yz.cara_yz(size, crossword)
    tk.Label(root, text="Medium Crossword", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    create_button("Back to Medium Hints", show_medium_mode, 300, 400)
    to_xy = create_button("Switch to XY", lambda: xy_screen_medium(size, crossword), 300, 450, bg="#50E3C2")

    current_screen = "yz_screen_medium"

def yz_screen_hard(size, crossword):    
    """Show the yz screen of the hard crossword.
    
    Args:
    
        size (int): size of the crossword
        crossword (list): list of lists with the crossword
        
        """
    global current_screen
    clear_screen()
    face_yz = cara_yz.cara_yz(size, crossword)
    tk.Label(root, text="Hard Crossword", font=("Helvetica", 24, "bold"), fg="white", bg="#4A90E2").pack(pady=20)
    create_button("Back to Hard Hints", show_hard_mode, 300, 400)
    to_xy = create_button("Switch to XY", lambda: xy_screen_hard(size, crossword), 300, 450, bg="#50E3C2")

    current_screen = "yz_screen_hard"

def submit_easy_hints(hints):
    """Function to handle the submission of hints.
    
    Args:
        
        hints (list): list of StringVar objects with the hints
        
        Returns:
        
        list: list of hints submitted
        
        """
    easy_hints = [hint.get() for hint in hints if hint.get()]
    print("Hints submitted:", easy_hints)
    return easy_hints

def submit_easy_words(words):
    """Function to handle the submission of words.
    
    Args:
        
        words (list): list of StringVar objects with the words
        
        Returns:
        
        list: list of words submitted
        
        """
    easy_words = [word.get() for word in words if word.get()]
    print("Words submitted:", easy_words)
    return easy_words

def save_hints_easy(hints):
    """    Function to handle the submission of hints.
    
    Args:
        
        hints (list): list of StringVar objects with the hints
        
        """
    global easy_hints_created
    easy_hints_created = submit_easy_hints(hints)
    print("Hints saved:", easy_hints_created)  # Verifica que las pistas se guardaron correctamente

def save_words_easy(words):
    """Function to handle the submission of words.

    Args:
        words (list): list of StringVar objects with the words
    """
    global easy_words_created
    easy_words_created = submit_easy_words(words)
    print("Words saved:", easy_words_created)  # Verifica que las palabras se guardaron correctamente

def create_easy_hint_input():
    """Show the input screen for the easy mode."""
    clear_screen()
    easy_hints_create = []

    indicator = tk.Label(root, text="Enter the hints for the easy mode (enter fitting words)", font=("Helvetica", 12), bg="#4A90E2", fg="white")
    indicator.place(x=200, y=50)

    for i in range(1, 7):  
        lb_hint = tk.Label(root, text=f"Hint {i}: ", foreground="white", bg="#4A90E2")
        sv_hint = tk.StringVar()
        tb_hint = ttk.Entry(root, textvariable=sv_hint, width=40)

        lb_hint.place(x=200, y=50 + i * 40)  
        tb_hint.place(x=250, y=50 + i * 40)

        easy_hints_create.append(sv_hint)  

    submit_button = tk.Button(root, text="Submit", command=lambda: save_hints_easy(easy_hints_create), font=("Helvetica", 14), bg="#50E3C2", fg="white")
    submit_button.place(x=450, y=400)

    words_button = tk.Button(root, text="Enter the words", command=create_easy_word_input, font=("Helvetica", 14), bg="#50E3C2", fg="white")
    words_button.place(x=450, y=450)
    #Crear boton de guardar pistas
    back_button = tk.Button(root, text="Back", command=show_create_crosswords, font=("Helvetica", 14), bg="#50E3C2", fg="white")
    back_button.place(x=450, y=500)

    current_screen = "easy_hint_input"

    return easy_hints_create

def create_easy_word_input():
    """Show the input screen for the easy mode."""
    clear_screen()

    easy_words_create = []

    indicator = tk.Label(root, text="Enter the words for the easy mode (enter fitting words)", font=("Helvetica", 12), bg="#4A90E2", fg="white")
    indicator.place(x=200, y=50)

    for i in range(1, 7):  
        lb_word = tk.Label(root, text=f"Word {i}: ", foreground="white", bg="#4A90E2")
        sv_word = tk.StringVar()
        tb_word = ttk.Entry(root, textvariable=sv_word, width=40)

        lb_word.place(x=200, y=50 + i * 40)  
        tb_word.place(x=250, y=50 + i * 40)

        easy_words_create.append(sv_word)  

    submit_button = tk.Button(root, text="Submit", command=lambda: save_words_easy(easy_words_create), font=("Helvetica", 14), bg="#50E3C2", fg="white")
    submit_button.place(x=450, y=400)

    hints_button = tk.Button(root, text="Enter the hints", command=create_easy_hint_input, font=("Helvetica", 14), bg="#50E3C2", fg="white")
    hints_button.place(x=450, y=450)
    #crear boton de guardar palabras
    #crear boton para visuarlizar el crucigrama
    #en la pantalla del crucigrama crear boton que regenere el crucigrama

    current_screen = "easy_word_input"

    return easy_words_create

def submit_medium_hints(hints):
    """Function to handle the submission of hints.
    
    Args:
        
        hints (list): list of StringVar objects with the hints
        
        Returns:
        
        list: list of hints submitted
        
        """
    medium_hints = [hint.get() for hint in hints if hint.get()]
    print("Hints submitted:", medium_hints)
    return medium_hints

def submit_medium_words(words):
    """Function to handle the submission of words.
    
    Args:
        
        words (list): list of StringVar objects with the words
        
        Returns:
        
        list: list of words submitted
        
        """
    medium_words = [word.get() for word in words if word.get()]
    print("Words submitted:", medium_words)
    return medium_words

def save_hints_medium(hints):
    """Function to handle the submission of hints.

    Args:

        hints (list): list of StringVar objects with the hints

    """
    global medium_hints_created
    medium_hints_created = submit_medium_hints(hints)
    print("Hints saved:", medium_hints_created)  # Verifica que las pistas se guardaron correctamente

def save_words_medium(words):
    """Function to handle the submission of words.

    Args:

        words (list): list of StringVar objects with the words
    """
    global medium_words_created
    medium_words_created = submit_medium_words(words)
    print("Words saved:", medium_words_created)  # Verifica que las palabras se guardaron correctamente

def create_medium_hint_input():
    """Show the input screen for the medium mode."""
    clear_screen()
    medium_hints_create = []

    indicator = tk.Label(root, text="Enter the hints for the medium mode (enter fitting words)", font=("Helvetica", 12), bg="#4A90E2", fg="white")
    indicator.place(x=200, y=50)

    for i in range(1, 11):  
        lb_hint = tk.Label(root, text=f"Hint {i}: ", foreground="white", bg="#4A90E2")
        sv_hint = tk.StringVar()
        tb_hint = ttk.Entry(root, textvariable=sv_hint, width=40)

        if i <= 5:  
            lb_hint.place(x=200, y=50 + i * 40)  
            tb_hint.place(x=250, y=50 + i * 40)
        else: 
            lb_hint.place(x=600, y=50 + (i - 5) * 40)  
            tb_hint.place(x=650, y=50 + (i - 5) * 40)

        medium_hints_create.append(sv_hint)  

    submit_button = tk.Button(root, text="Submit", command=lambda: save_hints_medium(medium_hints_create), font=("Helvetica", 14), bg="#50E3C2", fg="white")
    submit_button.place(x=450, y=400)

    words_button = tk.Button(root, text="Enter the words", command=create_medium_word_input, font=("Helvetica", 14), bg="#50E3C2", fg="white")
    words_button.place(x=450, y=450)
    #Crear boton de guardar pistas
    back_button = tk.Button(root, text="Back", command=show_create_crosswords, font=("Helvetica", 14), bg="#50E3C2", fg="white")
    back_button.place(x=450, y=500)

    current_screen = "medium_hint_input"

    return medium_hints_create

def create_medium_word_input():
    """Show the input screen for the medium mode."""
    clear_screen()

    medium_words_create = []

    indicator = tk.Label(root, text="Enter the words for the medium mode (enter fitting words)", font=("Helvetica", 12), bg="#4A90E2", fg="white")
    indicator.place(x=200, y=50)

    for i in range(1, 11):  
        lb_word = tk.Label(root, text=f"Word {i}: ", foreground="white", bg="#4A90E2")
        sv_word = tk.StringVar()
        tb_word = ttk.Entry(root, textvariable=sv_word, width=40)

        if i <= 5:  
            lb_word.place(x=200, y=50 + i * 40)  
            tb_word.place(x=250, y=50 + i * 40)
        else: 
            lb_word.place(x=600, y=50 + (i - 5) * 40)  
            tb_word.place(x=650, y=50 + (i - 5) * 40)

        medium_words_create.append(sv_word)  

    submit_button = tk.Button(root, text="Submit", command=lambda: save_words_medium(medium_words_create), font=("Helvetica", 14), bg="#50E3C2", fg="white")
    submit_button.place(x=450, y=400)

    hints_button = tk.Button(root, text="Enter the hints", command=create_medium_hint_input, font=("Helvetica", 14), bg="#50E3C2", fg="white")
    hints_button.place(x=450, y=450)
    #crear boton de guardar palabras
    #crear boton para visuarlizar el crucigrama
    #en la pantalla del crucigrama crear boton que regenere el crucigrama


    current_screen = "medium_word_input"

    return medium_words_create

def submit_hard_hints(hints):
    """Function to handle the submission of hints.
    
    Args:
        
        hints (list): list of StringVar objects with the hints
        
        Returns:
        
        list: list of hints submitted
        
        """ 
    hard_hints = [hint.get() for hint in hints if hint.get()]
    print("Hints submitted:", hard_hints)
    return hard_hints

def submit_hard_words(words):
    """Function to handle the submission of words.
    
    Args:
        
        words (list): list of StringVar objects with the words
        
        Returns:
        
        list: list of words submitted
        
        """ 
    hard_words = [word.get() for word in words if word.get()]
    print("Words submitted:", hard_words)
    return hard_words

def save_hints_hard(hints):
    """Function to handle the submission of hints.

    Args:
    
        hints (list): list of StringVar objects with the hints

    """
    global hard_hints_created
    hard_hints_created = submit_hard_hints(hints)
    print("Hints saved:", hard_hints_created)  # Verifica que las pistas se guardaron correctamente

def save_words_hard(words):
    """Function to handle the submission of words.

    Args:
        
            words (list): list of StringVar objects with the words
    
        """
    global hard_words_created
    hard_words_created = submit_hard_words(words)
    print("Words saved:", hard_words_created)  # Verifica que las palabras se guardaron correctamente

def create_hard_hint_input():
    """Show the input screen for the hard mode."""
    clear_screen()
    hard_hints_create = []

    indicator = tk.Label(root, text="Enter the hints for the hard mode (enter fitting words)", font=("Helvetica", 12), bg="#4A90E2", fg="white")
    indicator.place(x=200, y=50)

    for i in range(1, 17):  
        lb_hint = tk.Label(root, text=f"Hint {i}: ", foreground="white", bg="#4A90E2")
        sv_hint = tk.StringVar()
        tb_hint = ttk.Entry(root, textvariable=sv_hint, width=40)

        if i <= 8:  
            lb_hint.place(x=200, y=50 + i * 40)  
            tb_hint.place(x=250, y=50 + i * 40)
        else: 
            lb_hint.place(x=600, y=50 + (i - 8) * 40)  
            tb_hint.place(x=650, y=50 + (i - 8) * 40)

        hard_hints_create.append(sv_hint)  

    submit_button = tk.Button(root, text="Submit", command=lambda: save_hints_hard(hard_hints_create), font=("Helvetica", 14), bg="#50E3C2", fg="white")
    submit_button.place(x=450, y=400)

    words_button = tk.Button(root, text="Enter the words", command=create_hard_word_input, font=("Helvetica", 14), bg="#50E3C2", fg="white")
    words_button.place(x=450, y=450)
    #crear boton de guardar pistas

    back_button = tk.Button(root, text="Back", command=show_create_crosswords, font=("Helvetica", 14), bg="#50E3C2", fg="white")
    back_button.place(x=450, y=500)

    current_screen = "hard_hint_input"

    return hard_hints_create

def create_hard_word_input():
    """Show the input screen for the hard mode."""
    clear_screen()

    hard_words_create = []

    indicator = tk.Label(root, text="Enter the words for the hard mode (enter fitting words)", font=("Helvetica", 12), bg="#4A90E2", fg="white")
    indicator.place(x=200, y=50)

    for i in range(1, 17):  
        lb_word = tk.Label(root, text=f"Word {i}: ", foreground="white", bg="#4A90E2")
        sv_word = tk.StringVar()
        tb_word = ttk.Entry(root, textvariable=sv_word, width=40)

        if i <= 8:  # Primera columna
            lb_word.place(x=200, y=50 + i * 40)  
            tb_word.place(x=250, y=50 + i * 40)
        else:  # Segunda columna
            lb_word.place(x=600, y=50 + (i - 8) * 40)  
            tb_word.place(x=650, y=50 + (i - 8) * 40)

        hard_words_create.append(sv_word)  

    submit_button = tk.Button(root, text="Submit", command=lambda: save_words_hard(hard_words_create), font=("Helvetica", 14), bg="#50E3C2", fg="white")
    submit_button.place(x=450, y=400)

    hints_button = tk.Button(root, text="Enter the hints", command=create_hard_hint_input, font=("Helvetica", 14), bg="#50E3C2", fg="white")
    hints_button.place(x=450, y=450)
    #crear boton de guardar palabras
    #crear boton para visuarlizar el crucigrama
    #en la pantalla del crucigrama crear boton que regenere el crucigrama

    current_screen = "hard_word_input"

    return hard_words_create



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
    elif current_screen == "easy_hint_input":
        create_easy_hint_input()
    elif current_screen == "easy_word_input":
        create_easy_word_input()
    elif current_screen == "medium_hint_input":
        create_medium_hint_input()
    elif current_screen == "medium_word_input":
        create_medium_word_input()
    elif current_screen == "hard_hint_input":
        create_hard_hint_input()
    elif current_screen == "hard_word_input":
        create_hard_word_input()


    


update_screen()


root.mainloop()

