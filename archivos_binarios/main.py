# main.py

from crucigrama3d.modelos import crucigrama3D, Palabra
from crucigrama3d.serializacion import guardar_crucigrama, cargar_crucigrama

def main():
    # Crear un crucigrama de ejemplo
    crucigrama = crucigrama3D(
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
    
    archivo = 'crucigrama3d.bin'
    
    # Guardar el crucigrama en un archivo binario
    guardar_crucigrama(crucigrama, archivo)
    
    # Cargar el crucigrama desde el archivo binario
    crucigrama_cargado = cargar_crucigrama(archivo)
    print("\nCrucigrama Cargado:")
    print(crucigrama_cargado)

if __name__ == "__main__":
    main()
