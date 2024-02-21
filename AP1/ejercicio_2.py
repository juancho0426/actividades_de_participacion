"Escribir una función que calcule el área de un círculo dado su radio "
from ejercicio_3 import suma


def area(radio):
    A=(3.14)*(radio**2)
    return A

dato=int(input("ingrese el radio: "))
resultado = area(dato)
print(resultado)
print(area(dato))

print(suma(dato,3))