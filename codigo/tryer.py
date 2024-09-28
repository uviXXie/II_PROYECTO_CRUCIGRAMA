# import random

# def puede_insertar_horizontal(matriz, palabra, fila, columna):
#     if columna + len(palabra) > len(matriz[0]):
#         return False
#     for i in range(len(palabra)):
#         if matriz[fila][columna + i] not in (' ', palabra[i]):
#             return False
#     return True

# def puede_insertar_vertical(matriz, palabra, fila, columna):
#     if fila + len(palabra) > len(matriz):
#         return False
#     for i in range(len(palabra)):
#         if matriz[fila + i][columna] not in (' ', palabra[i]):
#             return False
#     return True

# def insertar_palabra(matriz, palabra, fila, columna, direccion):
#     if direccion == 'horizontal':
#         for i in range(len(palabra)):
#             matriz[fila][columna + i] = palabra[i]
#     elif direccion == 'vertical':
#         for i in range(len(palabra)):
#             matriz[fila + i][columna] = palabra[i]

# def buscar_interseccion(matriz, palabra):
#     n = len(matriz)
#     posiciones = []
#     for fila in range(n):
#         for columna in range(n):
#             for i in range(len(palabra)):
#                 if matriz[fila][columna] == palabra[i]:
#                     if puede_insertar_horizontal(matriz, palabra, fila, columna - i):
#                         posiciones.append((fila, columna - i, 'horizontal'))
#                     if puede_insertar_vertical(matriz, palabra, fila - i, columna):
#                         posiciones.append((fila - i, columna, 'vertical'))
#     return posiciones

# def agregar_palabra_crucigrama(matriz, palabras, indice=0):
#     if indice >= len(palabras):
#         return matriz
    
#     palabra = palabras[indice]
#     posiciones = buscar_interseccion(matriz, palabra)
#     if not posiciones:
#         n = len(matriz)
#         for fila in range(n):
#             for columna in range(n):
#                 if puede_insertar_horizontal(matriz, palabra, fila, columna):
#                     posiciones.append((fila, columna, 'horizontal'))
#                 if puede_insertar_vertical(matriz, palabra, fila, columna):
#                     posiciones.append((fila, columna, 'vertical'))
    
#     if posiciones:
#         fila, columna, direccion = random.choice(posiciones)
#         insertar_palabra(matriz, palabra, fila, columna, direccion)
#         return agregar_palabra_crucigrama(matriz, palabras, indice + 1)
#     else:
#         raise ValueError("No se puede insertar la palabra en la matriz.")

# Ejemplo de uso
n = 10
matriz = [[' ' for _ in range(n)] for _ in range(n)]
print(matriz)
palabras = ["hola", "roble", "luz"]

# matriz_actualizada = agregar_palabra_crucigrama(matriz, palabras)

# for fila in matriz_actualizada:
#     print(' '.join(fila))
