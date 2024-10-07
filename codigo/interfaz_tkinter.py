from tkinter import ttk
import tkinter

def on_start():
    print("¡Comenzando el crucigrama!")

first_screen = tkinter.Tk()
first_screen.geometry("750x500")
first_screen.title("Crucigrama 3D")

message = tkinter.Label(first_screen, text="Bienvenido al crucigrama 3D", font=("Helvetica", 16), fg="blue")
message.pack(padx=20, pady=20)

button_to_start = ttk.Button(first_screen, text="Comenzar", command=on_start)
button_to_start.pack(padx=50, pady=10)

button_to_exit = ttk.Button(first_screen, text="Salir", command=first_screen.quit)
button_to_exit.pack(padx=50, pady=10)

first_screen.mainloop()
