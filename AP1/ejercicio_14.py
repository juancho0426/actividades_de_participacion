"14. Escribir una función que calcule la media aritmética de una lista de números."
def calcular_media(lista):
    if len(lista) == 0:
        return 0  # Si la lista está vacía, la media es 0
    else:
        return sum(lista) / len(lista)

# Ejemplo de uso del programa
numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print("La media aritmética de la lista", numeros, "es:", media)

