"15. Crear un programa que pida al usuario ingresar una cadena de texto y determine si es un palíndromo o no"
def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas para ignorar diferencias de mayúsculas y minúsculas
    cadena = cadena.replace(" ", "").lower()
    # Verificar si la cadena es igual a su inversa
    return cadena == cadena[::-1]

# Solicitar al usuario que ingrese una cadena de texto
cadena = input("Ingresa una cadena de texto: ")

# Determinar si la cadena es un palíndromo o no e imprimir el resultado
if es_palindromo(cadena):
    print("La cadena '{}' es un palíndromo.".format(cadena))
else:
    print("La cadena '{}' no es un palíndromo.".format(cadena))
