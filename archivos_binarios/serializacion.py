# crucigrama3d/serializacion.py

import struct
from .modelos import Crucigrama3D, Palabra

def guardar_crucigrama(crucigrama: Crucigrama3D, archivo: str):
    try:
        with open(archivo, 'wb') as f:
            # Encabezado
            f.write(struct.pack('B', crucigrama.version))  # 1 byte
            f.write(struct.pack('III', crucigrama.dimension_x, crucigrama.dimension_y, crucigrama.dimension_z))  # 3 * 4 bytes
            f.write(struct.pack('I', len(crucigrama.palabras)))  # 4 bytes
            
            # Palabras
            for palabra in crucigrama.palabras:
                # Longitud de la palabra
                longitud_palabra = len(palabra.palabra)
                if longitud_palabra > 255:
                    raise ValueError("La longitud de la palabra excede el límite de 255 caracteres.")
                f.write(struct.pack('B', longitud_palabra))  # 1 byte
                
                # Palabra en bytes
                f.write(palabra.palabra.encode('utf-8'))  # n bytes
                
                # Longitud de la definición
                longitud_definicion = len(palabra.definicion)
                if longitud_definicion > 65535:
                    raise ValueError("La longitud de la definición excede el límite de 65535 caracteres.")
                f.write(struct.pack('H', longitud_definicion))  # 2 bytes
                
                # Definición en bytes
                f.write(palabra.definicion.encode('utf-8'))  # n bytes
                
                # Posición inicial
                f.write(struct.pack('III', palabra.posicion_x, palabra.posicion_y, palabra.posicion_z))  # 3 * 4 bytes
                
                # Dirección
                if palabra.direccion not in (0, 1, 2):
                    raise ValueError("Dirección inválida. Debe ser 0 (X), 1 (Y) o 2 (Z).")
                f.write(struct.pack('B', palabra.direccion))  # 1 byte
        print(f"Crucigrama guardado exitosamente en '{archivo}'.")
    except Exception as e:
        print(f"Error al guardar el crucigrama: {e}")

def cargar_crucigrama(archivo: str) -> Crucigrama3D:
    try:
        with open(archivo, 'rb') as f:
            # Encabezado
            version = struct.unpack('B', f.read(1))[0]
            dimension_x, dimension_y, dimension_z = struct.unpack('III', f.read(12))
            numero_palabras = struct.unpack('I', f.read(4))[0]
            
            palabras = []
            for _ in range(numero_palabras):
                # Longitud de la palabra
                longitud_palabra = struct.unpack('B', f.read(1))[0]
                
                # Palabra
                palabra = f.read(longitud_palabra).decode('utf-8')
                
                # Longitud de la definición
                longitud_definicion = struct.unpack('H', f.read(2))[0]
                
                # Definición
                definicion = f.read(longitud_definicion).decode('utf-8')
                
                # Posición inicial
                posicion_x, posicion_y, posicion_z = struct.unpack('III', f.read(12))
                
                # Dirección
                direccion = struct.unpack('B', f.read(1))[0]
                
                palabras.append(Palabra(
                    palabra=palabra,
                    definicion=definicion,
                    posicion_x=posicion_x,
                    posicion_y=posicion_y,
                    posicion_z=posicion_z,
                    direccion=direccion
                ))
        
        print(f"Crucigrama cargado exitosamente desde '{archivo}'.")
        return Crucigrama3D(
            version=version,
            dimension_x=dimension_x,
            dimension_y=dimension_y,
            dimension_z=dimension_z,
            palabras=palabras
        )
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no existe.")
        raise
    except Exception as e:
        print(f"Error al cargar el crucigrama: {e}")
        raise
