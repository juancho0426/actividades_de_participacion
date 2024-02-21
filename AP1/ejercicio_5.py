"5. Crear una función que convierta grados Fahrenheit a grados Celsius."
def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Ejemplo de uso de la función
fahrenheit = float(input("Ingresa la temperatura en grados Fahrenheit: "))
celsius = fahrenheit_a_celsius(fahrenheit)
print("La temperatura de {:.2f} grados Fahrenheit equivale a {:.2f} grados Celsius.".format(fahrenheit, celsius))
