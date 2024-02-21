"7. Escribir un programa que encuentre el número más grande y el más pequeño en una lista dada."
def encontrar_maximo_minimo(lista):
    if len(lista) == 0:
        return None, None  # Si la lista está vacía, devolvemos None para ambos casos
    
    maximo = minimo = lista[0]  # Suponemos que el primer elemento es tanto el máximo como el mínimo
    
    for numero in lista:
        if numero > maximo:
            maximo = numero
        elif numero < minimo:
            minimo = numero
    
    return maximo, minimo

# Ejemplo de uso del programa
numeros = [10, 5, 23, 8, 14, 3]
maximo, minimo = encontrar_maximo_minimo(numeros)

if maximo is not None and minimo is not None:
    print("El número más grande en la lista es:", maximo)
    print("El número más pequeño en la lista es:", minimo)
else:
    print("La lista está vacía.")
