"9. Crear un programa que genere una matriz de números y la imprima en pantalla"
def imprimir_matriz(matriz):
    for fila in matriz:
        for elemento in fila:
            print(elemento, end="\t")
        print()  # Salto de línea después de imprimir cada fila

# Ejemplo de uso del programa
filas = 3
columnas = 3
matriz = []

# Generar la matriz de números
for i in range(filas):
    fila = []
    for j in range(columnas):
        fila.append(i * columnas + j + 1)  # Se pueden cambiar estos valores para generar la matriz deseada
    matriz.append(fila)

# Imprimir la matriz
print("Matriz generada:")
imprimir_matriz(matriz)

