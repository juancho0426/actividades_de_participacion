"""13. Crear un programa que pida al usuario ingresar dos números y calcule su suma, resta, multiplicación y 
división."""
def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero."
    else:
        return num1 / num2

# Solicitar al usuario que ingrese dos números
numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

# Calcular suma, resta, multiplicación y división
resultado_suma = suma(numero1, numero2)
resultado_resta = resta(numero1, numero2)
resultado_multiplicacion = multiplicacion(numero1, numero2)
resultado_division = division(numero1, numero2)

# Imprimir resultados
print("Suma:", resultado_suma)
print("Resta:", resultado_resta)
print("Multiplicación:", resultado_multiplicacion)
print("División:", resultado_division)
