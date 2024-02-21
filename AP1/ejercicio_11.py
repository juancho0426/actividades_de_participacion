"11. Crear un programa que genere una lista de números pares entre 1 y 100."
def generar_pares():
    pares = []
    for numero in range(2, 101, 2):
        pares.append(numero)
    return pares

# Ejemplo de uso del programa
lista_pares = generar_pares()
print("Lista de números pares entre 1 y 100:")
print(lista_pares)
