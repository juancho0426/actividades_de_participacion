"6. Crear un programa que calcule la suma de los números en una lista dada."
def suma_lista(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

# Ejemplo de uso del programa
lista = [10, 20, 30, 40, 50]
resultado = suma_lista(lista)
print("La suma de los números en la lista {} es: {}".format(lista, resultado))
