import tkinter as tk
from tkinter import ttk


def create_hint_input():
    """Crea campos de entrada para las pistas."""
    hints_create = []

    indicator = tk.Label(root, text="Enter the hints for the medium mode (enter fitting words)", font=("Helvetica", 12), bg="#4A90E2", fg="white")
    indicator.place(x=200, y=50)

    for i in range(1, 17):  # Cambia el rango según el número de pistas que quieras permitir
        lb_hint = tk.Label(root, text=f"Hint {i}: ", foreground="white", bg="#4A90E2")
        sv_hint = tk.StringVar()
        tb_hint = ttk.Entry(root, textvariable=sv_hint, width=40)

        if i <= 8:  # Primera columna
            lb_hint.place(x=200, y=50 + i * 40)  # Espacio entre las pistas
            tb_hint.place(x=250, y=50 + i * 40)
        else:  # Segunda columna
            lb_hint.place(x=600, y=50 + (i - 8) * 40)  # Ajustar la posición para la segunda columna
            tb_hint.place(x=650, y=50 + (i - 8) * 40)

        hints_create.append(sv_hint)  # Guardar el StringVar en la lista

    submit_button = tk.Button(root, text="Submit", command=lambda: submit_hints(hints_create), font=("Helvetica", 14), bg="#50E3C2", fg="white")
    submit_button.place(x=450, y=400)


def submit_hints(hints):
    """Función para manejar el envío de las pistas."""
    hints = [hint.get() for hint in hints if hint.get()] 
    print("Hints submitted:", hints)



root = tk.Tk()
root.geometry("1000x500")
root.title("Hints for medium mode")
root.configure(bg="#4A90E2")

create_hint_input()

root.mainloop()


