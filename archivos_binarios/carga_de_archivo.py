# crucigrama3d/interfaz.py

import tkinter as tk
from tkinter import filedialog, messagebox
from .modelos import Crucigrama3D, Palabra # type: ignore
from ..serializacion import guardar_crucigrama, cargar_crucigrama

class AplicacionCrucigrama3D:
    def __init__(self, master):
        self.master = master
        master.title("Crucigrama 3D")
        
        # Botón para crear un nuevo crucigrama
        self.btn_nuevo = tk.Button(master, text="Nuevo Crucigrama", command=self.nuevo_crucigrama)
        self.btn_nuevo.pack()
        
        # Botón para cargar un crucigrama existente
        self.btn_cargar = tk.Button(master, text="Cargar Crucigrama", command=self.cargar_crucigrama)
        self.btn_cargar.pack()
        
        # Botón para guardar el crucigrama actual
        self.btn_guardar = tk.Button(master, text="Guardar Crucigrama", command=self.guardar_crucigrama)
        self.btn_guardar.pack()
        
        # Área de texto para mostrar información
        self.texto = tk.Text(master, height=10, width=50)
        self.texto.pack()
        
        # Crucigrama actual
        self.crucigrama = None
    
    def nuevo_crucigrama(self):
        # Implementa una interfaz para crear un nuevo crucigrama
        # Por simplicidad, crearemos uno de ejemplo
        self.crucigrama = Crucigrama3D(
            version=1,
            dimension_x=10,
            dimension_y=10,
            dimension_z=5,
            palabras=[
                Palabra(
                    palabra="PYTHON",
                    definicion="Lenguaje de programación",
                    posicion_x=0,
                    posicion_y=1,
                    posicion_z=0,
                    direccion=0  # X
                ),
                Palabra(
                    palabra="CODE",
                    definicion="Escribir programas",
                    posicion_x=4,
                    posicion_y=0,
                    posicion_z=0,
                    direccion=1  # Y
                )
            ]
        )
        self.texto.insert(tk.END, "Nuevo crucigrama creado.\n")
    
    def cargar_crucigrama(self):
        archivo = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=(("Binario", "*.bin"),))
        if archivo:
            try:
                self.crucigrama = cargar_crucigrama(archivo)
                self.texto.insert(tk.END, f"Crucigrama cargado desde '{archivo}'.\n")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo cargar el crucigrama: {e}")
    
    def guardar_crucigrama(self):
        if self.crucigrama is None:
            messagebox.showwarning("Advertencia", "No hay un crucigrama para guardar.")
            return
        archivo = filedialog.asksaveasfilename(defaultextension=".bin", filetypes=(("Binario", "*.bin"),))
        if archivo:
            try:
                guardar_crucigrama(self.crucigrama, archivo)
                self.texto.insert(tk.END, f"Crucigrama guardado en '{archivo}'.\n")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el crucigrama: {e}")

def iniciar_aplicacion():
    root = tk.Tk()
    app = AplicacionCrucigrama3D(root)
    root.mainloop()
