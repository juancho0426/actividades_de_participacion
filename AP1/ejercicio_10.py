"10. Escribir una función que calcule el factorial de un número dado."
def factorial(numero):
    if numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

# Ejemplo de uso del programa
numero = int(input("Ingresa un número entero para calcular su factorial: "))
resultado_factorial = factorial(numero)
print("El factorial de", numero, "es:", resultado_factorial)

