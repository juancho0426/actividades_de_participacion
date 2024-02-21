" 4.Escribir un programa que determine si un número dado es par o impar."
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "El número {} es par.".format(numero)
    else:
        return "El número {} es impar.".format(numero)

# Pedir al usuario que ingrese un número
numero = int(input("Ingresa un número entero: "))

# Llamar a la función para determinar si es par o impar
resultado = es_par_o_impar(numero)
print(resultado)